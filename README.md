# DecisionMap

![DecisionMap Logo](DesMaps.png)

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub stars](https://img.shields.io/github/stars/markoblogo/decision-map?style=social)](https://github.com/markoblogo/decision-map/stargazers)
[![Last commit](https://img.shields.io/github/last-commit/markoblogo/decision-map)](https://github.com/markoblogo/decision-map/commits/main)
[![Schema validation](https://github.com/markoblogo/decision-map/actions/workflows/validate-examples.yml/badge.svg)](https://github.com/markoblogo/decision-map/actions/workflows/validate-examples.yml)

**DecisionMap is a practical protocol for turning complex business, product, market, and marketing decisions into visible strategy maps.**

It is a protocol + prompt toolkit, not a hosted service and not a substitute for leadership judgment.

## What It Is

Use DecisionMap when the real problem is not a lack of ideas, but a messy decision with multiple plausible paths, asymmetric risks, and uncertain external reactions.

DecisionMap helps users:
- restate the real decision
- separate facts, assumptions, interpretations, and unknowns
- generate 3-7 distinct strategic options
- compare trade-offs, risks, resources, and breakpoints
- pressure-test shortlisted options
- keep an update loop alive through a cascade log

The main output is a **working strategic hypothesis**, not a final truth.

## Scope

DecisionMap is designed for:
- business strategy
- product strategy
- market positioning
- competitive response
- go-to-market decisions
- marketing strategy under uncertainty

It is intentionally out of scope for:
- military or political conflict
- legal or medical advice
- financial investment decisions
- mergers and acquisitions
- layoffs or HR restructuring

## Quick Start

1. Start with [USAGE.md](USAGE.md) for the manual runbook.
2. Use [prompts/system_prompt.md](prompts/system_prompt.md) as the runtime system/developer prompt.
3. Run the stage prompts in order:
   - `prompts/01_intake.md`
   - `prompts/02_clarifying_questions.md`
   - `prompts/03_strategy_map.md`
   - `prompts/04_deep_dive.md`
   - `prompts/05_decision_summary.md`
4. If the decision continues over time, use the cascade log artifacts in `examples/`.

## Optional ID Bootstrap

DecisionMap stays standalone, but it can optionally consume `ID` as a portable human-context layer for longer-running strategic work.

Recommended bootstrap order:

1. `profiles/<owner>/soul.md`
2. `profiles/<owner>/profile.core.md`
3. `profiles/<owner>/handshake.md`

Use that order when:

- the same decision evolves across multiple sessions
- the user has strong formatting, tone, or decision-style preferences
- you want continuity without re-explaining the same working style every time

Do not treat `ID` as market evidence or decision truth. It is only user-context and operating-constraints input.

## Canonical Examples

These are the flagship examples for v0.2.

- [examples/agri_commodity_market_entry.md](examples/agri_commodity_market_entry.md) - compact agri/commodities strategy map for a Ukrainian sunflower oil exporter evaluating Indian market entry.
- [examples/fmcg_route_to_market_full_run.md](examples/fmcg_route_to_market_full_run.md) - full walkthrough for an FMCG chilled dairy brand redesigning route-to-market expansion.
- [examples/cascade_log_agri_commodity_market_entry.md](examples/cascade_log_agri_commodity_market_entry.md) - worked update loop that continues the agri/commodities case after the first decision.

Starter generic examples are still included, but they are no longer the flagship credibility artifacts:
- [examples/full_run_product_launch.md](examples/full_run_product_launch.md)
- [examples/product_launch.md](examples/product_launch.md)
- [examples/competitive_response.md](examples/competitive_response.md)

## JSON Outputs

DecisionMap ships with normative schemas and real JSON fixtures:

- [schemas/strategy_map.schema.json](schemas/strategy_map.schema.json)
- [schemas/cascade_log.schema.json](schemas/cascade_log.schema.json)
- [examples/json/strategy_map.agri_market_entry.json](examples/json/strategy_map.agri_market_entry.json)
- [examples/json/cascade_log.agri_market_entry.json](examples/json/cascade_log.agri_market_entry.json)

Validate the public examples with:

```bash
python3 -m pip install jsonschema
python3 scripts/validate_examples.py
```

## Cascade Log

Stage 6 is a first-class capability in v0.2, not just a note.

Use it when the decision evolves over weeks or months and you need structured memory for:
- what was decided
- which assumptions were active
- which signals moved
- what happened next
- what changed in the working hypothesis

Artifacts:
- [examples/templates/cascade_log_template.md](examples/templates/cascade_log_template.md)
- [examples/cascade_log_agri_commodity_market_entry.md](examples/cascade_log_agri_commodity_market_entry.md)
- [examples/json/cascade_log.agri_market_entry.json](examples/json/cascade_log.agri_market_entry.json)

## Document Roles

| Artifact | Role |
| --- | --- |
| `README.md` | Canonical entrypoint for new users and contributors |
| `USAGE.md` | Manual operator runbook for chat-based execution |
| `protocol.md` | Normative spec for stages, outputs, confidence language, and cascade semantics |
| `prompts/*` | Executable prompt assets used during a run |
| `schemas/*` | Machine-readable shape for Stage 3 and Stage 6 outputs |

## Repository Structure

```text
decision-map/
├── README.md
├── USAGE.md
├── protocol.md
├── CONTRIBUTING.md
├── CHANGELOG.md
├── prompts/
├── schemas/
├── examples/
│   ├── json/
│   └── templates/
├── scripts/
└── .github/
```

## Contributing

The repo now has a lightweight open-source contribution layer:
- [CONTRIBUTING.md](CONTRIBUTING.md)
- `.github/ISSUE_TEMPLATE/`
- [CHANGELOG.md](CHANGELOG.md)

Contributions are especially useful for:
- stronger real-world examples
- protocol clarity improvements
- schema/example consistency
- better manual operator guidance

## Roadmap

Roadmap is intentionally lightweight in-repo. Use GitHub Issues/Milestones for active work and prioritization.

Current v0.2 direction:
- canonical real-world examples
- validated JSON fixtures
- stronger cascade-log workflow
- clearer contributor ergonomics

## ABVX Ecosystem

DecisionMap remains standalone and usable with any LLM.

Inside the ABVX ecosystem:
- `lab.abvx` can list it as a decision/strategy protocol artifact
- `agentsgen` can maintain repo-local agent docs for contributors
- `SET` can track or audit the repo
- `ID` can optionally provide portable user context for longer-running decision work, with `soul.md` as the preferred first-pass bootstrap

None of these integrations are required for manual use.

Related repos:

- `lab.abvx` is the public hub where DecisionMap is cataloged: https://github.com/markoblogo/lab.abvx
- `AGENTS.md_generator`, `SET`, `ID`, and `abvx-agent-skills` form the adjacent AI coding tools stack, but are optional here.

## Privacy

DecisionMap itself does not require storing data, but hosted LLM APIs may process your input externally.

For sensitive work:
- anonymize names, companies, exact numbers, and internal documents
- remove customer data and personal data
- use a local model or approved internal environment when needed
