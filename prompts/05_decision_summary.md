# Prompt 05: Decision Summary

Use this prompt to produce the final structured decision summary after the Strategy Deep Dive.

This stage does not produce final truth.

It produces a decision-ready record: the current working strategy, the trade-offs accepted, the assumptions behind the choice, and the signals that should trigger a revisit.

---

You are running **DecisionMap Stage 5: Decision Summary**.

Create a structured summary of the current working decision.

The goal is to help the user leave the session with:
- a clear working strategy
- visible trade-offs
- explicit assumptions
- next actions
- monitoring signals
- conditions for revisiting the decision

---

## Before writing the summary

Briefly restate:

1. **Decision statement**
   - the decision being made

2. **Shortlisted options**
   - options that were seriously considered

3. **Selected working strategy**
   - the current choice, if one has been selected

4. **Confidence level**
   - Low / Medium / High
   - explain why

If no strategy is ready to select, say so clearly and produce a “not ready to decide” summary instead.

---

## Decision summary structure

### 1. Executive summary

Write a short summary in 3–6 sentences.

Include:
- what is being decided
- what strategy is currently selected
- why it fits better than alternatives
- the biggest remaining uncertainty

Do not oversell the decision.

---

### 2. Chosen working strategy

Include:

- strategy name
- short explanation
- intended outcome
- time horizon
- confidence level
- uncertainty note

Make clear that this is a working hypothesis based on current information.

---

### 3. Why this strategy was chosen

Explain the key reasons.

Cover:
- fit with stated goal
- fit with available resources
- risk profile
- timing
- competitive or market logic
- why this path is preferable now

Avoid generic statements. Tie the reasoning to the case.

---

### 4. Rejected or deferred options

List the meaningful alternatives that were not chosen.

For each include:

- option name
- status: rejected / deferred / possible later
- reason
  - resource mismatch
  - risk too high
  - timing not right
  - weak evidence
  - lower strategic fit
  - unacceptable trade-off

This section is important: it prevents the decision from looking obvious in hindsight.

---

### 5. Trade-offs accepted

State what the user is choosing to optimize for and what they are accepting as the price.

Include relevant trade-offs such as:

- speed vs quality
- upside vs downside protection
- growth vs margin
- control vs distribution
- focus vs optionality
- short-term result vs long-term positioning
- learning vs immediate execution
- reputation vs aggression
- simplicity vs sophistication

Make the cost of the choice visible.

---

### 6. Assumptions behind the decision

Separate assumptions into:

- user-side assumptions
- market/customer assumptions
- competitor/partner/channel assumptions
- execution assumptions

For each important assumption include:

- assumption
- why it matters
- confidence: Low / Medium / High
- how it could be tested or monitored

Do not hide weak assumptions.

---

### 7. Unresolved uncertainties

List the main things that are still unknown.

For each uncertainty include:

- why it matters
- which part of the strategy it affects
- whether it blocks execution or can be monitored while moving

---

### 8. Immediate next actions

List concrete next actions.

For each action include:

- action
- purpose
- owner/function if known
- timeframe if possible
- expected signal or output

Prefer practical next moves over broad advice.

If the best next action is “collect more data”, specify exactly what data and why.

---

### 9. Signals to monitor

Define what should be watched after the decision.

Include:

- leading indicators
- risk signals
- competitor/customer/partner reactions
- internal execution signals
- thresholds or triggers where possible

Signals should be observable, not vague.

---

### 10. Revisit conditions

Define when the decision should be revisited.

Use one or more:

- date
- event
- metric threshold
- competitor action
- customer signal
- resource change
- failed assumption
- new evidence

This is what turns the decision from a one-time answer into a living strategy.

---

### 11. Cascade log entry

If the user is working in project mode, produce a compact cascade log entry.

Include:

- decision version
- date
- decision statement
- chosen strategy
- rejected/deferred options
- core assumptions
- accepted trade-offs
- next actions
- signals to monitor
- revisit trigger
- confidence level

If the user is not using project mode, label this section as optional/exportable.

---

## Output format

Return:

1. **Executive summary**
2. **Full structured decision record**
3. **Open questions and unresolved uncertainties**
4. **Immediate next actions**
5. **Monitoring and revisit plan**
6. **Optional cascade log entry**

End with:

> This is a working hypothesis, not a final truth.

---

## Rules

Do not present the chosen strategy as objectively correct.

Do not erase rejected options from the record.

Do not hide trade-offs.

Do not convert uncertainty into confident language.

Do not create action items that depend on unavailable resources without saying so.

If the decision is not ready, produce a clear “not ready to decide” summary and explain what must be resolved first.
