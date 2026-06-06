# Contributing to DecisionMap

DecisionMap is a protocol and prompt toolkit. Keep contributions narrow, concrete, and reviewable.

## High-Value Contributions

- stronger real-world examples
- protocol clarity improvements
- prompt alignment fixes
- schema/example consistency improvements
- operator guidance improvements in `README.md`, `USAGE.md`, or `RUNBOOK.md`

## Before You Open a PR

1. Read:
   - [README.md](README.md)
   - [USAGE.md](USAGE.md)
   - [protocol.md](protocol.md)
2. If your change affects semantics, sync the relevant public artifacts:
   - `README.md`
   - `USAGE.md`
   - `protocol.md`
   - `prompts/`
   - `examples/`
   - `schemas/`
3. Run the public validation checks:

```bash
python3 -m pip install jsonschema
python3 scripts/validate_examples.py
rg -n "Low-Medium|Medium-Low|confidence\\s*:\\s*[0-9]" README.md USAGE.md protocol.md prompts schemas examples
```

## Example Contributions

When proposing a new example:
- use a concrete vertical and realistic constraints
- state the decision owner, objective, constraints, and counterparties
- keep facts, assumptions, and interpretations separated
- include measurable signals and breakpoints
- if you add a JSON fixture, it must validate against the relevant schema

## Prompt / Protocol Changes

When changing prompts or protocol language:
- preserve stage order and public artifact names unless there is a strong reason not to
- keep confidence language as `Low / Medium / High`
- avoid turning the protocol into a generic advice chatbot
- update any examples that would become misaligned

## Schema and Fixture Changes

If you update a schema:
- update the matching JSON fixtures in `examples/json/`
- run `scripts/validate_examples.py`
- mention the schema change in [CHANGELOG.md](CHANGELOG.md)

## Expected PR Shape

Keep PRs small and explicit:
- one main intent per PR
- include docs updates when public behavior changes
- include validation evidence in the PR description

Useful PR description format:
- what changed
- why it changed
- how it was validated
- any remaining assumptions or trade-offs
