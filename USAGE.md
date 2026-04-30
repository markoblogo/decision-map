# Using DecisionMap Manually

DecisionMap can be used without any app. Copy the system prompt, then run the stage prompts in order.

## Before you start

- Choose a business, product, market, or marketing decision.
- Anonymize sensitive information if you are using a hosted LLM.
- Prepare relevant notes, docs, links, metrics, or context.
- Do not use DecisionMap for out-of-scope domains listed in `README.md` and `protocol.md`.

## Step-by-step copy-paste workflow

### Step 0

- Start a new chat with an LLM.
- Paste `prompts/system_prompt.md` as the system/developer instruction if the tool supports it.
- If the tool does not support system prompts, paste it as the first message and tell the model to follow it.

### Step 1

- Paste `prompts/01_intake.md`.
- Add your situation/context.
- Answer the intake questions.

### Step 2

- Paste `prompts/02_clarifying_questions.md`.
- Ask the model to generate only decision-critical questions.
- Answer them.

### Step 3

- Paste `prompts/03_strategy_map.md`.
- Generate the first strategy map.
- Review the 3-7 options.

### Step 4

- Select 1-3 options.
- Paste `prompts/04_deep_dive.md`.
- Ask the model to pressure-test selected options.

### Step 5

- Paste `prompts/05_decision_summary.md`.
- Generate the final decision record and working hypothesis.

### Optional

- Use `schemas/cascade_log.schema.json` if you are continuing the decision over time.
- Use project mode manually by copying the decision summary into a new update session.

## Privacy note

- Hosted models may process your data externally.
- Anonymize names, companies, exact financials, customer data, and internal documents.
- For sensitive work, use a local model or an approved internal environment.

## What good output looks like

A good DecisionMap run should produce:

- a clear decision statement
- separated facts, assumptions, interpretations, and unknowns
- a strategy map with multiple options
- visible trade-offs
- pressure-tested shortlisted options
- a working hypothesis
- monitoring and revisit triggers

## Common mistakes

- asking for final advice too early
- giving too little context
- treating the first map as truth
- ignoring resource constraints
- choosing the most attractive option without testing assumptions

## Related files

- [README.md](/Users/antonbiletskiy-volokh/Downloads/Projects/DecisionMap/README.md)
- [protocol.md](/Users/antonbiletskiy-volokh/Downloads/Projects/DecisionMap/protocol.md)
- [prompts/](/Users/antonbiletskiy-volokh/Downloads/Projects/DecisionMap/prompts)
- [examples/](/Users/antonbiletskiy-volokh/Downloads/Projects/DecisionMap/examples)
