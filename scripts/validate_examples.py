#!/usr/bin/env python3
"""Validate public JSON fixtures against the published DecisionMap schemas."""

from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    import jsonschema
except ImportError as exc:  # pragma: no cover - import guard
    raise SystemExit("Missing dependency: install jsonschema with `python3 -m pip install jsonschema`.") from exc


REPO_ROOT = Path(__file__).resolve().parents[1]
VALIDATIONS = [
    (
        REPO_ROOT / "schemas" / "strategy_map.schema.json",
        REPO_ROOT / "examples" / "json" / "strategy_map.agri_market_entry.json",
    ),
    (
        REPO_ROOT / "schemas" / "cascade_log.schema.json",
        REPO_ROOT / "examples" / "json" / "cascade_log.agri_market_entry.json",
    ),
]


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def main() -> int:
    failures: list[str] = []
    for schema_path, example_path in VALIDATIONS:
        schema = load_json(schema_path)
        example = load_json(example_path)
        validator_class = jsonschema.validators.validator_for(schema)
        validator_class.check_schema(schema)
        validator = validator_class(schema)
        errors = sorted(validator.iter_errors(example), key=lambda error: list(error.absolute_path))
        if errors:
            for error in errors:
                location = ".".join(str(part) for part in error.absolute_path) or "<root>"
                failures.append(f"{example_path.name}: {location}: {error.message}")
        else:
            print(f"OK  {example_path.relative_to(REPO_ROOT)}")

    if failures:
        print("Validation failed:", file=sys.stderr)
        for failure in failures:
            print(f" - {failure}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
