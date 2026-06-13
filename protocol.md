# DecisionMap Protocol

DecisionMap is a structured facilitation protocol for complex business, product, market, and marketing decisions under uncertainty.

This file is the normative specification for:
- scope boundaries
- stage sequence
- required output shapes
- confidence language
- Stage 6 cascade-log semantics

For repository overview and examples, use [README.md](README.md).  
For manual execution, use [USAGE.md](USAGE.md).

## Scope

### In scope

- business strategy
- product strategy
- market positioning
- competitive response
- go-to-market decisions
- marketing strategy under uncertainty

### Out of scope

- military conflict
- political conflict
- legal advice
- medical advice
- financial investment advice
- mergers and acquisitions
- layoffs or HR restructuring

If a request is out of scope, the facilitator must stop and state the boundary clearly.

## Operating Principles

### 1. Options before answers

DecisionMap must not collapse the situation into one polished recommendation too early.

The first major output is a map of realistic options.

### 2. Facts, assumptions, interpretations, unknowns

Important claims must be separated into:
- **Fact**
- **Assumption**
- **Interpretation**
- **Unknown**

The facilitator must not hide assumptions inside confident language.

### 3. Reality before elegance

An option is only useful if it survives contact with:
- available resources
- time pressure
- market conditions
- customer behavior
- competitor reactions
- internal constraints

### 4. Human decision ownership

DecisionMap structures judgment. It does not replace judgment.

### 5. Confidence language

All strategy confidence must use:
- `Low`
- `Medium`
- `High`

Numeric confidence scoring is out of spec.

### 6. Optional human-context bootstrap

DecisionMap may accept optional external human-context artifacts, including `ID` profile files.

If such artifacts are provided, the preferred order is:
- `soul.md`
- `profile.core.md`
- `handshake.md`

These artifacts may shape:
- tone and formatting
- decision-style preferences
- stable user constraints
- misalignment prevention

They must not be treated as evidence about the market, product, customer, competitor, or external environment.

## Stage Sequence

Follow this sequence unless the user already provides an artifact from a later stage:

1. Scope check
2. Intake
3. Clarifying questions
4. First strategy map
5. Strategy selection and deep dive
6. Decision summary
7. Cascade log update loop

## Stage 0: Scope Check

### Purpose

Confirm that the problem belongs inside the protocol and is concrete enough to begin.

### Required output

- scope result: `in scope`, `partially in scope`, or `out of scope`
- rewritten decision statement
- decision owner
- primary objective
- obvious constraints
- unresolved blockers

### Gate

Proceed only if:
- the decision is in scope
- there is a real choice between plausible paths
- the owner and objective are identifiable

## Stage 1: Intake

### Purpose

Create the first usable map of the decision context.

### Required intake areas

- business, product, or market context
- decision pressure
- target customers or market segment
- relevant competitors or other parties
- available resources
- hard constraints
- evidence already available

### Required output

- structured situation summary
- known facts
- assumptions
- interpretations
- major unknowns
- initial framing confidence: `Low`, `Medium`, or `High`

### Gate

Do not generate strategy recommendations during intake.

## Stage 2: Clarifying Questions

### Purpose

Reduce ambiguity before generating the first option map.

### Question rule

Ask only questions that can materially change:
- which strategies are realistic
- which strategies are too risky
- which strategies fit the real objective
- which assumptions are unsafe

### Required output

- answered-question summary
- unresolved unknowns
- confirmed assumptions
- unconfirmed assumptions
- framing confidence

### Gate

Proceed only when the context is sufficient to create several distinct options.  
If not, stop and request the missing inputs.

## Stage 3: First Strategy Map

### Purpose

Generate the first comparable set of realistic strategies.

### Option count

The map must include `3-7` strategically distinct options.

### Required pre-map restatement

- decision statement
- known facts
- key assumptions
- major unknowns
- framing confidence

### Required fields for each option

- name
- short summary
- expected upside
- price/cost:
  - money
  - time
  - reputation
  - opportunity cost
  - operational complexity
  - customer trust
  - strategic flexibility lost
- required resources
- key risks
- likely reactions:
  - competitors
  - customers
  - partners
  - internal stakeholders
- time effects:
  - short-term
  - medium-term
  - long-term
- core assumptions
- breakpoints
- signals to monitor
- confidence with rationale

### Required map-level output

- key trade-offs
- dominant uncertainties
- suggested shortlist
- best current working hypothesis
- what would change this view

### Canonical machine-readable form

If rendered as JSON, the output must satisfy [schemas/strategy_map.schema.json](schemas/strategy_map.schema.json).

## Stage 4: Strategy Selection and Deep Dive

### Purpose

Pressure-test the shortlisted options instead of accepting them at face value.

### Required analysis for each selected option

- strategic logic
- what must be true
- execution path
- resource fit
- main risks
- invalidators
- first tests or experiments
- updated confidence

### Required comparative dimensions when multiple options remain

- upside
- downside risk
- resource fit
- speed
- reversibility
- learning value
- strategic flexibility

## Stage 5: Decision Summary

### Purpose

Produce the best current working strategy while keeping trade-offs visible.

### Required output

- chosen working strategy
- why it was chosen
- rejected or deferred options and why
- accepted trade-offs
- required resources
- active assumptions
- unresolved uncertainties
- immediate next actions
- signals to monitor
- revisit trigger or review date
- a `what would change this view` section

## Stage 6: Cascade Log Update Loop

Stage 6 is part of the DecisionMap protocol for long-running decisions.

### Purpose

Keep strategic memory alive when reality changes after the initial decision.

### Use when

- a competitor move changes the landscape
- customer feedback invalidates a prior assumption
- market or channel conditions shift
- internal constraints change
- the team revisits the same strategic choice on a regular cadence

### Required update inputs

- latest decision version or decision summary
- what happened since the last version
- new facts
- assumptions confirmed or invalidated
- signal movement
- outcomes observed
- whether the current working strategy remains valid

### Required update questions

At each update the facilitator must ask:
- what happened since the last decision?
- which assumptions held?
- which assumptions broke?
- which signals moved?
- did other parties react as expected?
- are the shortlisted options still valid?
- should the team continue, adapt, or pivot?

### Required update outputs

Each update must produce:
- updated facts
- updated assumptions
- updated strategy confidence
- updated breakpoints or revisit triggers
- next working hypothesis version
- cascade log entry

### Cascade log minimum sections

- project metadata
- parties
- decision versions
- assumptions
- signals
- actions
- outcomes
- update entries

### Canonical machine-readable form

If rendered as JSON, the output must satisfy [schemas/cascade_log.schema.json](schemas/cascade_log.schema.json).

## Reference Artifacts

- Cascade template: [examples/templates/cascade_log_template.md](examples/templates/cascade_log_template.md)
- Worked cascade example: [examples/cascade_log_agri_commodity_market_entry.md](examples/cascade_log_agri_commodity_market_entry.md)
- JSON fixtures:
  - [examples/json/strategy_map.agri_market_entry.json](examples/json/strategy_map.agri_market_entry.json)
  - [examples/json/cascade_log.agri_market_entry.json](examples/json/cascade_log.agri_market_entry.json)
