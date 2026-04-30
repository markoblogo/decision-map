# DecisionMap

**A practical AI-assisted protocol for mapping complex business and product decisions.**

DecisionMap is a lightweight protocol and prompt toolkit for using LLMs as structured decision facilitators.

## What it is

DecisionMap helps you turn complex business, product, market, and marketing choices into a visible map of strategic options.

Instead of forcing a single answer, it helps you compare options across:
- expected upside
- cost and resource requirements
- risks and likely responses from other parties
- time horizons
- assumptions and breakpoints
- signals to monitor over time

The final output is a **working strategic hypothesis**, not a claim of certainty.

## What it is not

DecisionMap is not:
- a SaaS product (yet)
- a new AI model
- a guaranteed prediction engine
- a replacement for leadership accountability

It is also **not intended** for:
- military conflict
- political conflict
- legal advice
- medical advice
- financial investment advice
- mergers and acquisitions
- layoffs or HR restructuring

## When to use it

Use DecisionMap when:
- the decision has multiple plausible paths
- uncertainty is high and stakes are meaningful
- competitors, partners, or market reactions matter
- your team is stuck between options and needs clearer trade-offs

## How it differs from a normal AI chat

A normal AI chat often jumps to an answer too quickly.

DecisionMap enforces a sequence:
1. scope check
2. intake
3. clarifying questions
4. multi-option strategy map
5. deep dive on selected options
6. decision summary with assumptions and monitoring signals

It separates facts from assumptions, labels uncertainty, and prevents false precision.

## Repository structure

```text
decision-map/
├── README.md
├── protocol.md
├── prompts/
│   ├── system_prompt.md
│   ├── 01_intake.md
│   ├── 02_clarifying_questions.md
│   ├── 03_strategy_map.md
│   ├── 04_deep_dive.md
│   └── 05_decision_summary.md
├── schemas/
│   ├── strategy_map.schema.json
│   └── cascade_log.schema.json
├── examples/
│   ├── product_launch.md
│   └── competitive_response.md
├── codex/
│   ├── build_prompt.md
│   └── implementation_notes.md
├── LICENSE
└── .gitignore
```

## Quick start (manual, with any LLM)

1. Set the model `system` message from `prompts/system_prompt.md`.
2. Run `prompts/01_intake.md` with your situation.
3. Run `prompts/02_clarifying_questions.md` and answer thoroughly.
4. Run `prompts/03_strategy_map.md` to generate 3-7 options.
5. Run `prompts/04_deep_dive.md` for 1-3 shortlisted options.
6. Run `prompts/05_decision_summary.md` to produce a working strategy and monitoring plan.
7. Optionally log updates using `schemas/cascade_log.schema.json`.

## Privacy note

DecisionMap is designed to work with user-provided data only. You should anonymize sensitive or identifiable information before sharing it with any hosted model.

If privacy requirements are strict, run this protocol with a local model or approved internal environment.

## Future optional mini-tool direction

A lightweight local-first web tool can be built later to:
- guide users through each protocol stage
- save sessions locally in browser storage
- export outputs as Markdown/JSON
- optionally connect to a local LLM or approved API

## Status

**Early protocol draft.**

The structure is stable enough for pilots and internal workshops, and expected to evolve with real usage feedback.
