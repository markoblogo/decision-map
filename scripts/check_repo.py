#!/usr/bin/env python3
"""Run the repository's lightweight release checks."""

from __future__ import annotations

import re
import subprocess
import sys
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
TEXT_DIRS = ["prompts", "schemas", "examples", "skills"]
TEXT_FILES = ["README.md", "USAGE.md", "protocol.md", "CONTRIBUTING.md", "RUNBOOK.md"]
FORBIDDEN_CONFIDENCE = re.compile(r"Low-Medium|Medium-Low|confidence\s*:\s*\d", re.IGNORECASE)
MARKDOWN_LINK = re.compile(r"\[[^]]+\]\(([^)]+)\)")


def text_paths() -> list[Path]:
    paths = [ROOT / name for name in TEXT_FILES]
    for directory in TEXT_DIRS:
        paths.extend(path for path in (ROOT / directory).rglob("*") if path.is_file())
    return paths


def check_text() -> list[str]:
    failures: list[str] = []
    for path in text_paths():
        try:
            content = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if "TODO" in content and "skills/decision-map" in path.as_posix():
            failures.append(f"{path.relative_to(ROOT)}: unresolved TODO")
        if FORBIDDEN_CONFIDENCE.search(content):
            failures.append(f"{path.relative_to(ROOT)}: unsupported confidence format")
        if path.suffix == ".md":
            for target in MARKDOWN_LINK.findall(content):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                clean_target = target.split("#", 1)[0]
                if clean_target and not (path.parent / clean_target).resolve().exists():
                    failures.append(f"{path.relative_to(ROOT)}: broken local link {target}")
    return failures


def check_skill() -> list[str]:
    skill_path = ROOT / "skills" / "decision-map" / "SKILL.md"
    content = skill_path.read_text(encoding="utf-8")
    if not content.startswith("---\n") or "\n---\n" not in content[4:]:
        return ["skills/decision-map/SKILL.md: invalid YAML frontmatter"]
    _, frontmatter, _ = content.split("---", 2)
    metadata = yaml.safe_load(frontmatter)
    failures: list[str] = []
    if not isinstance(metadata, dict):
        return ["skills/decision-map/SKILL.md: frontmatter must be a mapping"]
    if metadata.get("name") != "decision-map":
        failures.append("skills/decision-map/SKILL.md: name must be decision-map")
    description = metadata.get("description")
    if not isinstance(description, str) or not description.strip():
        failures.append("skills/decision-map/SKILL.md: description is required")
    unexpected = set(metadata) - {"name", "description"}
    if unexpected:
        failures.append(f"skills/decision-map/SKILL.md: unexpected keys {sorted(unexpected)}")
    return failures


def main() -> int:
    result = subprocess.run(
        [sys.executable, str(ROOT / "scripts" / "validate_examples.py")],
        cwd=ROOT,
        check=False,
    )
    failures = check_text() + check_skill()
    for failure in failures:
        print(f"FAIL  {failure}", file=sys.stderr)
    if result.returncode or failures:
        return 1
    print("OK  repository text checks")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
