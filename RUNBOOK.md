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
- Validate public JSON fixtures when touching schemas/examples:
  - `python3 -m pip install jsonschema`
  - `python3 scripts/validate_examples.py`
<!-- AGENTSGEN:END section=quickstart -->

## Common Tasks

<!-- AGENTSGEN:START section=common_tasks -->
- Consistency scan:
  - `rg -n "Low-Medium|Medium-Low|confidence\\s*:\\s*[0-9]" README.md USAGE.md protocol.md prompts schemas examples`
- Link scan:
  - `rg -n "\\]\\(/Users/" README.md USAGE.md`
- Schema quick inspection:
  - `sed -n '1,260p' schemas/strategy_map.schema.json`
  - `sed -n '1,320p' schemas/cascade_log.schema.json`
- Fixture validation:
  - `python3 scripts/validate_examples.py`
<!-- AGENTSGEN:END section=common_tasks -->

## Troubleshooting

<!-- AGENTSGEN:START section=troubleshooting -->
- If dependencies fail: verify the expected Node/Python version for this repo.
- If tests are flaky: re-run once, then isolate and fix the root cause.
- If environment is unclear: ask for the expected OS/tooling versions.
<!-- AGENTSGEN:END section=troubleshooting -->
