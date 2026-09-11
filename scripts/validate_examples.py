#!/usr/bin/env python3
"""Validate DecisionMap JSON files against the published schemas."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - import guard
    raise SystemExit(
        "Missing dependency: run `python3 -m pip install -r requirements-dev.txt`."
    ) from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = {
    "strategy-map": REPO_ROOT / "schemas" / "strategy_map.schema.json",
    "cascade-log": REPO_ROOT / "schemas" / "cascade_log.schema.json",
}
PREFIXES = {"strategy_map.": "strategy-map", "cascade_log.": "cascade-log"}


def load_json(path: Path) -> object:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValueError(f"{path}: {exc}") from exc


def infer_schema(path: Path) -> str:
    for prefix, schema_name in PREFIXES.items():
        if path.name.startswith(prefix):
            return schema_name
    raise ValueError(
        f"Cannot infer schema for {path.name}; pass --schema strategy-map or --schema cascade-log."
    )


def bundled_examples() -> list[Path]:
    paths = sorted((REPO_ROOT / "examples" / "json").glob("*.json"))
    if not paths:
        raise ValueError("No bundled JSON examples found.")
    return paths


def validate(path: Path, schema_name: str) -> list[str]:
    schema = load_json(SCHEMAS[schema_name])
    instance = load_json(path)
    validator_class = jsonschema.validators.validator_for(schema)
    validator_class.check_schema(schema)
    validator = validator_class(schema, format_checker=jsonschema.FormatChecker())
    errors = sorted(validator.iter_errors(instance), key=lambda error: list(error.absolute_path))
    return [
        f"{path}: {'.'.join(str(part) for part in error.absolute_path) or '<root>'}: {error.message}"
        for error in errors
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", nargs="*", type=Path, help="JSON files to validate")
    parser.add_argument("--schema", choices=sorted(SCHEMAS), help="schema for supplied files")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        paths = args.files or bundled_examples()
        failures: list[str] = []
        for path in paths:
            schema_name = args.schema or infer_schema(path)
            errors = validate(path, schema_name)
            if errors:
                failures.extend(errors)
            else:
                try:
                    display_path = path.relative_to(REPO_ROOT)
                except ValueError:
                    display_path = path
                print(f"OK  {display_path} ({schema_name})")
    except (KeyError, ValueError) as exc:
        print(f"Validation failed: {exc}", file=sys.stderr)
        return 1

    if failures:
        print("Validation failed:", file=sys.stderr)
        for failure in failures:
            print(f" - {failure}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
