---
name: star-answer-builder
description: Turn one behavioral interview question into a spoken-register answer built from a named entry in the person's Story Bank — situation, what they did, what changed — and say plainly when no story fits. Activates on "tell me about a time" / "behavioral question" / "how do I answer this" / a pasted interview question.
disable-model-invocation: true
---

One question in, one answer out — from a real story, or an honest "no story yet".

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block; and the
**Story Bank** artifact in this Project if it exists. If neither, say: "Run
`jobsearch-setup-wizard` first — answers come from your wins, not from a
question bank." Continue only with pasted material.

Older profiles use other labels for the same fields: `Minimum salary:` or `Salary floor:`
mean minimum pay (annual salary unless the value says otherwise), **Shipped artifacts**
means wins, `Positioning challenges:` means things a hiring manager might question,
and `Target level:` means career stage. Read them the same way.

## Input

The question, and (optional) the role and round it's for.

## Method

1. Name what the question is really testing (ownership, conflict, judgment under
   ambiguity, influence, learning from failure).
2. Pick the Story Bank entry or resume line that best answers it. If two fit, show both
   and recommend one. If none fits, say so and suggest which three wins could be
   built into a story for it — never invent one.
3. Write the answer.

## Output

```markdown
**Testing for:** [one line]
**Story:** [Story Bank name or resume line]

**Answer (90 seconds, spoken):**
Situation — [2 sentences: the context and the stakes]
What I did — [3–5 sentences: decisions, not activities; "I", not "we", where true]
What changed — [1–2 sentences: the result, in the person's own figures; no figure → what was different after]
[Optional one line: what I'd do differently]

**If they follow up with "what exactly did you do?"** — [2 lines]
```

Then a **15-second version** for a panel that's short on time.

## Constraints

- Figures only from the person's record. No rounding up.
- "I" for what they did, "we" for what the team did — never claim the team's work.
- Nothing confidential about the current employer beyond what the profile allows.
- Spoken register; no AI-register words.

## After

Offer: "Want this saved to your Story Bank as a reusable answer? Say 'save it'."

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
