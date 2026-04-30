# DecisionMap Protocol

DecisionMap is a staged protocol for using LLMs as structured facilitators for business, product, market, and marketing strategy decisions under uncertainty.

## Scope and intent

DecisionMap supports strategic reasoning, option comparison, and uncertainty mapping.

It is not designed for military, political, legal, medical, investment, M&A, or HR restructuring decisions.

## Global rules

1. Do not provide a final strategy before enough context is collected.
2. If information is missing, explicitly list what is missing.
3. Separate facts, assumptions, and interpretations.
4. Build several options, not one answer.
5. Every option must include:
   - expected upside
   - price/cost
   - resource requirements
   - risks
   - likely response from other parties
   - short/mid/long-term effects
   - breakpoints
   - signals to monitor
6. End with a working hypothesis, not final truth.
7. The user remains responsible for decisions.

## Stage 0: Scope check

Purpose: ensure the decision is in-scope and defined clearly enough to proceed.

Inputs:
- one-sentence decision statement
- domain and context

Outputs:
- in-scope / out-of-scope result
- rewritten decision statement (if ambiguous)
- explicit constraints on allowed guidance

Gate to proceed:
- decision fits business/product/market/marketing strategy
- decision owner and objective are identifiable

## Stage 1: Intake

Purpose: collect baseline decision context.

Capture:
- business context
- product/service context
- target market and segments
- competitor landscape
- current pressure (time, revenue, churn, launch window, etc.)
- available resources and hard constraints
- known data sources (metrics, research, internal docs)

Output:
- structured intake summary
- list of known facts
- list of obvious unknowns

## Stage 2: Clarifying questions

Purpose: resolve ambiguity before generating strategy options.

Question areas:
- real goal behind the decision
- success criteria and failure criteria
- required time horizon
- budget, team, capabilities
- non-negotiable constraints
- other parties and likely incentives
- market conditions and trend direction
- top risks and unknowns
- what cannot be sacrificed

Output:
- answered question set
- unresolved unknowns list
- confidence in problem framing

Gate to proceed:
- enough information to model multiple realistic options

## Stage 3: First strategy map

Purpose: generate 3-7 strategically distinct options.

For each option include:
- option name
- short summary
- expected upside
- price/cost
- required resources
- key risks
- likely reaction from competitors/customers/partners
- short/mid/long-term effects
- assumptions
- breakpoints (conditions that invalidate the option)
- monitoring signals
- confidence level

Output:
- comparable strategy map (table/cards)
- option ranking by fit to stated goals (not absolute truth)

## Stage 4: Strategy deep dive

Purpose: pressure-test shortlisted options before choosing a working direction.

For selected options analyze:
- logic chain and causal assumptions
- execution steps
- critical dependencies
- key weak points
- first tests/experiments to run
- conditions that would invalidate the strategy

Output:
- deep-dive analysis for each shortlisted option
- updated risk and confidence notes

## Stage 5: Decision summary

Purpose: produce a decision-ready output that is explicit about trade-offs.

Include:
- chosen working strategy
- why it was chosen
- rejected options and why
- accepted trade-offs
- assumptions and uncertainty labels
- next actions (owner + timeframe where possible)
- signals to monitor
- explicit revisit trigger/date

Output:
- working strategic hypothesis
- immediate action plan

## Stage 6: Optional update loop / cascade log

Purpose: keep the decision map current as reality changes.

Cadence:
- event-triggered (major market/competitor change)
- periodic (weekly/monthly/quarterly)

At each update:
- log new facts
- check which assumptions still hold
- update signals and outcomes
- revise option confidence and breakpoints
- decide whether to continue, adapt, or pivot

Output:
- cascade log entry
- updated working hypothesis version

## Recommended facilitator behavior

- Be explicit when confidence is low.
- Prefer transparent reasoning over polished certainty.
- State what data would most improve decision quality.
- Keep outputs structured and comparable.
- Avoid single-path advice when alternatives remain viable.
