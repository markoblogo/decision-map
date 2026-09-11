# RUNBOOK.md

## Quickstart

<!-- AGENTSGEN:START section=quickstart -->
- Read the entrypoint and supporting docs first:
  - `README.md`
  - `USAGE.md`
  - `protocol.md`
- Review prompts flow in order:
  - `prompts/system_prompt.md`
  - `prompts/01_intake.md` -> `prompts/05_decision_summary.md`
- Install validation dependencies once: `python3 -m pip install -r requirements-dev.txt`
- Run the release gate: `python3 scripts/check_repo.py`
<!-- AGENTSGEN:END section=quickstart -->

## Common Tasks

<!-- AGENTSGEN:START section=common_tasks -->
- Agent Skill validation: `python3 /path/to/skill-creator/scripts/quick_validate.py skills/decision-map`
- Schema quick inspection:
  - `sed -n '1,260p' schemas/strategy_map.schema.json`
  - `sed -n '1,320p' schemas/cascade_log.schema.json`
- Fixture validation:
  - `python3 scripts/validate_examples.py`
<!-- AGENTSGEN:END section=common_tasks -->

## Troubleshooting

<!-- AGENTSGEN:START section=troubleshooting -->
- If `jsonschema` is missing, install `requirements-dev.txt` in a virtual environment.
- If a user file cannot be inferred from its filename, pass `--schema strategy-map` or `--schema cascade-log`.
- If a skill check fails, fix its YAML frontmatter or remove unresolved scaffold text.
<!-- AGENTSGEN:END section=troubleshooting -->
