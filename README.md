# DecisionMap

**A practical protocol for using AI to map complex business and product decisions.**

DecisionMap is not another “AI tool”.  
It is a structured way to think through decisions where there is no single correct answer — only trade-offs.

---

## What it is

DecisionMap helps you turn messy, high-stakes situations into a **map of strategic options**.

It is especially useful when the problem is not lack of intelligence, but a fragmented or distorted picture of reality.

Instead of asking:
> “What should we do?”

it reframes the problem as:
> “What are our real options — and what does each of them cost?”

Each option is broken down into:
- expected upside
- cost (money, time, reputation, risk)
- required resources
- likely reactions from competitors, customers, or partners
- short / mid / long-term effects
- assumptions
- breakpoints (where it fails)
- signals to monitor

The output is not “the answer”.

It is a **working strategic hypothesis**, with visible trade-offs.

---

## What it is not

DecisionMap is not:
- a chatbot that gives advice
- a prediction engine
- a replacement for decision-makers
- a “smart agent” that thinks for you

It does not:
- guarantee outcomes
- remove uncertainty
- make decisions on your behalf

And it is intentionally **out of scope** for:
- military or political conflict
- legal or medical advice
- financial investment decisions
- M&A, layoffs, or HR restructuring

---

## When to use it

Use DecisionMap when:
- you have multiple plausible strategies and no clear winner
- the decision involves trade-offs, not right vs wrong
- competitors or external reactions matter
- you feel “stuck” — not because the problem is impossible, but because the picture is unclear

---

## Why not just use ChatGPT?

Because most AI chats do this:

→ you describe a situation  
→ it gives you a clean, confident answer  

The problem is:
- it skips clarification
- it hides assumptions
- it collapses multiple options into one narrative
- it creates an illusion of certainty

DecisionMap does the opposite.

It forces a process:
1. clarify the problem
2. separate facts, assumptions, interpretations, and unknowns
3. ask only questions that can change the strategy map
4. build multiple realistic strategies
5. compare trade-offs, resources, risks, and breakpoints
6. pressure-test shortlisted options
7. produce a decision record and working hypothesis

This is slower — but real decisions require that.

---

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
````

---

## **Quick start (manual)**

You don’t need any app. You can run this with any LLM.

1. Set the system prompt from `prompts/system_prompt.md`
2. Run `01_intake.md` with your situation
3. Answer `02_clarifying_questions.md`
4. Generate options via `03_strategy_map.md`
5. Deep dive into selected ones with `04_deep_dive.md`
6. Finalize with `05_decision_summary.md`

Optional: track updates using the cascade log schema.

---

## **Privacy**

DecisionMap does not require storing data.

However:

- most LLM APIs are external
- your input may be processed by third-party providers

So:  
→ anonymize sensitive information  
→ or run this locally if needed

---

## **Future direction (optional)**

This can be turned into a lightweight tool:

- guided session (instead of free chat)
- strategy cards instead of text blobs
- local-first storage
- export to Markdown / JSON

Future versions may include:
- project mode
- cascade logs for long-running decisions
- structured memory of decisions, assumptions, signals, outcomes, and revisions

But the core value is already here:  
→ the protocol

---

## **Status**

Early version.

The goal is not to build another AI product.

The goal is to define a **clear, usable way to think with AI under uncertainty**.
