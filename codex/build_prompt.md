# Codex Build Prompt (Future Mini-Tool)

Use this prompt later to ask Codex to build a small local app from this repository.

---

Build a minimal local web app called DecisionMap Studio based on this repository.

Requirements:
- Keep it simple. No backend required initially.
- Use a guided multi-step UI matching protocol stages:
  1. Scope check
  2. Intake
  3. Clarifying questions
  4. Strategy map
  5. Deep dive
  6. Decision summary
- Provide editable forms and structured output cards.
- Save session data locally (localStorage first).
- Support export to Markdown and JSON.
- Include import from JSON to resume a session.
- Add basic schema validation with files in `schemas/`.
- Keep the UI readable and practical, not flashy.

Technical guidance:
- Prefer static frontend (or simple Next.js app) with client-side state.
- Organize code so prompts in `prompts/` can be loaded and copied from the UI.
- No authentication.
- No cloud sync.
- Privacy-first defaults.

Optional later extension:
- Add selectable LLM providers.
- Add local LLM mode when available.

Deliverables:
- Working local app
- README update with run instructions
- Clear folder structure and comments for maintainability
