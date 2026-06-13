# Using DecisionMap Manually

This document is the operator runbook for running DecisionMap in a chat interface.

For project overview, examples, and repository navigation, start with [README.md](README.md).  
For normative protocol rules, use [protocol.md](protocol.md).

## What You Need

- any LLM chat interface, hosted or local
- access to `prompts/`, `protocol.md`, `examples/`, and `schemas/`
- your decision context: notes, metrics, constraints, evidence, and relevant documents

## Before You Start

- choose a business, product, market, or marketing decision inside DecisionMap scope
- define the current pressure: deadline, competitor move, revenue target, launch window, margin pressure, or similar
- anonymize sensitive information if you use a hosted model
- gather any evidence you already have: metrics, research notes, customer feedback, market signals, or internal constraints

## Manual Chat Flow

### Step 0a: Optional ID bootstrap

If the user already maintains an `ID` profile, load it before the runtime prompt in this order:

1. `profiles/<owner>/soul.md`
2. `profiles/<owner>/profile.core.md`
3. `profiles/<owner>/handshake.md`

Use this only as human-context input:
- formatting and tone preferences
- decision style and escalation preferences
- stable constraints
- known misalignment patterns

Do not treat it as market evidence or substitute for Stage 1 intake.

### Step 0b: Set the runtime prompt

- paste [prompts/system_prompt.md](prompts/system_prompt.md) as the system/developer instruction if the chat tool supports it
- if not, paste it as the first message and tell the model to follow it as the operating protocol

### Step 1: Intake

- paste `prompts/01_intake.md`
- provide the situation, decision pressure, goals, constraints, and relevant evidence
- expect a structured summary of facts, assumptions, interpretations, and unknowns

### Step 2: Clarifying questions

- paste `prompts/02_clarifying_questions.md`
- ask for only decision-critical questions
- answer them directly; if something is unknown, mark it unknown rather than guessing

### Step 3: First strategy map

- paste `prompts/03_strategy_map.md`
- expect 3-7 distinct options with visible trade-offs, risks, required resources, and signals to monitor
- compare the options before choosing a favorite

### Step 4: Deep dive

- select 1-3 options
- paste `prompts/04_deep_dive.md`
- use this stage to pressure-test execution path, invalidators, and first experiments

### Step 5: Decision summary

- paste `prompts/05_decision_summary.md`
- produce the working strategic hypothesis, immediate actions, signals, and revisit triggers

## Stage 6: Cascade Log Workflow

Use Stage 6 when the decision stays alive after the first session.

### Start a new cascade log

- copy [examples/templates/cascade_log_template.md](examples/templates/cascade_log_template.md)
- create the first entry from the Stage 5 decision summary
- if you need machine-readable output, adapt the same state into [schemas/cascade_log.schema.json](schemas/cascade_log.schema.json)

### Reopen a decision later

When you revisit the decision, provide:
- the previous decision summary or latest cascade log
- what changed since last review
- new facts, broken assumptions, or new signals
- whether the chosen strategy is still active, at risk, or invalidated

Then ask the model to:
- compare new facts vs previous assumptions
- update strategy confidence
- decide whether to continue, adapt, or pivot
- append a new update entry

### Append a new update

Each update should include:
- what happened since the last version
- which assumptions were confirmed or invalidated
- signal movement
- outcomes observed
- next actions
- new revisit triggers

Use these artifacts as references:
- [examples/cascade_log_agri_commodity_market_entry.md](examples/cascade_log_agri_commodity_market_entry.md)
- [examples/json/cascade_log.agri_market_entry.json](examples/json/cascade_log.agri_market_entry.json)

## Validation Flow

If you are producing JSON outputs for automation or archival:

```bash
python3 -m pip install jsonschema
python3 scripts/validate_examples.py
```

This validates the public fixtures against the published schemas.

## What Good Output Looks Like

A good DecisionMap run should produce:
- a clear decision statement
- separated facts, assumptions, interpretations, and unknowns
- a realistic strategy map with distinct options
- visible trade-offs and breakpoints
- a pressure-tested shortlist
- a working strategic hypothesis
- concrete signals and revisit triggers

## Common Operator Mistakes

- asking for a final recommendation before enough context exists
- letting the model collapse multiple options into cosmetic variants
- hiding assumptions inside confident language
- treating an early map as final truth
- forgetting to record signals and revisit triggers for ongoing decisions
