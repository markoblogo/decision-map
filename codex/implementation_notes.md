# DecisionMap MVP Implementation Notes

## Goal

Create a privacy-first MVP that guides users through the DecisionMap protocol without requiring backend infrastructure.

## MVP shape

Two valid starting approaches:
- Static web app (HTML/CSS/JS + lightweight state)
- Simple Next.js app (App Router) running fully client-side for v1

## Core features

1. Guided form flow
- Stage-by-stage wizard aligned to `protocol.md`
- Required fields and context hints per stage
- Explicit labels for facts, assumptions, unknowns

2. Strategy cards
- Render 3-7 options in comparable cards/table
- Show cost, upside, risks, reactions, horizons, breakpoints, confidence

3. Local persistence
- Save current session to localStorage automatically
- Allow manual save snapshots in JSON
- Support restore/import from JSON

4. Export
- Export final decision packet as:
  - Markdown summary
  - Structured JSON matching schemas

## Data and validation

- Use `schemas/strategy_map.schema.json` for stage 3 validation.
- Use `schemas/cascade_log.schema.json` for optional update loop records.
- Validate before export and show human-readable validation errors.

## Privacy-first defaults

- No server calls in MVP mode.
- No telemetry by default.
- Clear warning before copying sensitive text into external LLM tools.
- Keep all data in-browser unless user explicitly exports.

## Suggested component blocks

- `StageNavigator`
- `IntakeForm`
- `ClarifyingQuestionsPanel`
- `StrategyOptionCard`
- `StrategyComparisonTable`
- `DecisionSummaryBuilder`
- `ExportPanel`

## Later integrations (optional)

1. LLM API integration
- User-supplied API key stored only in session memory
- Provider abstraction (OpenAI/Anthropic/local endpoint)

2. Local model integration
- Support local endpoint adapters
- Keep UI protocol stable regardless of model source

3. Collaboration
- Deferred to later versions (out of MVP scope)

## Non-goals for MVP

- Multi-user accounts
- Cloud database
- Real-time collaboration
- Advanced analytics dashboard
