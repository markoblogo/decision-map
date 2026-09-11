# AGENTS.md

Instructions for coding agents working on DecisionMap.

<!-- AGENTSGEN:START section=overview -->
## Overview

DecisionMap is a documentation-first decision protocol with an installable Agent Skill and validated JSON outputs.
<!-- AGENTSGEN:END section=overview -->

<!-- AGENTSGEN:START section=repo_context -->
## Repository Context

DecisionMap is an installable Agent Skill, open decision protocol, prompt toolkit, and pair of JSON schemas. It is documentation-first; do not turn it into a hosted app unless explicitly requested.

Read these entrypoints before editing semantics:

- `README.md` — user entrypoint
- `protocol.md` — normative behavior and scope
- `USAGE.md` — manual operator flow
- `skills/decision-map/SKILL.md` — portable agent workflow
- `schemas/` and `examples/json/` — machine-readable contract and fixtures
<!-- AGENTSGEN:END section=repo_context -->

<!-- AGENTSGEN:START section=guardrails -->
## Guardrails

- Keep facts, assumptions, interpretations, and unknowns distinct.
- Strategy confidence is only `Low`, `Medium`, or `High`, with a rationale. Do not add numeric or hybrid confidence levels.
- Preserve 3–7 distinct options in the strategy map and 1–3 options in its shortlist.
- Preserve human decision ownership and describe recommendations as working hypotheses.
- Keep military or political conflict, legal or medical advice, investment decisions, M&A, layoffs, and HR restructuring out of scope.
- Treat schema changes as compatibility changes: update matching fixtures, docs, and changelog together.
- Never add private decision data, credentials, or identifying customer information to examples.
<!-- AGENTSGEN:END section=guardrails -->

<!-- AGENTSGEN:START section=rules -->
## Rules

- Keep changes focused and preserve public artifact names.
- Update related protocol, prompt, skill, schema, fixture, and changelog content together when semantics change.
- Do not commit secrets or private decision data.
<!-- AGENTSGEN:END section=rules -->

<!-- AGENTSGEN:START section=workflow -->
## Workflow

1. Read the nearest normative document and related example.
2. Make the smallest change that keeps protocol, prompts, skill, schemas, and examples aligned.
3. Add or update a fixture when machine-readable behavior changes.
4. Run the release gate before finishing.
5. Record public behavior changes in `CHANGELOG.md`.
<!-- AGENTSGEN:END section=workflow -->

<!-- AGENTSGEN:START section=style -->
## Style

- Write compact, concrete Markdown with descriptive headings.
- Avoid generic strategy advice and false precision.
- Prefer realistic constraints, measurable signals, explicit breakpoints, and reversible tests.
- Keep the Agent Skill self-contained; installed clients may copy only `skills/decision-map/`.
- Avoid new dependencies when the standard library or current validator is sufficient.
<!-- AGENTSGEN:END section=style -->

<!-- AGENTSGEN:START section=verification -->
## Verification

Install development requirements in a virtual environment, then run:

```bash
python3 -m pip install -r requirements-dev.txt
python3 scripts/check_repo.py
```

When the skill changes, also run the Skill Creator `quick_validate.py` against `skills/decision-map`.
<!-- AGENTSGEN:END section=verification -->

<!-- AGENTSGEN:START section=commands -->
## Commands

- Full gate: `python3 scripts/check_repo.py`
- JSON only: `python3 scripts/validate_examples.py`
- User output: `python3 scripts/validate_examples.py FILE --schema strategy-map`
<!-- AGENTSGEN:END section=commands -->

<!-- AGENTSGEN:START section=structure -->
## Structure

- `prompts/` staged manual workflow
- `skills/decision-map/` portable Agent Skill
- `schemas/` public JSON contracts
- `examples/` worked and machine-readable examples
- `scripts/` local and CI validation
<!-- AGENTSGEN:END section=structure -->

<!-- AGENTSGEN:START section=output_protocol -->
## Agent Output

Report changed behavior, verification evidence, and any remaining compatibility risk.
<!-- AGENTSGEN:END section=output_protocol -->

<!-- AGENTSGEN:START section=stack -->
## Stack

- Markdown and YAML for documentation and skill metadata
- JSON Schema Draft 2020-12 for structured outputs
- Python 3.12 and `jsonschema` for validation
- GitHub Actions for the release gate
<!-- AGENTSGEN:END section=stack -->

<!-- AGENTSGEN:START section=static -->
## Documentation Notes

Keep local links relative and verify them with the repository gate. Preserve the existing public logo unless a visual redesign is explicitly requested.
<!-- AGENTSGEN:END section=static -->
