---
name: story-bank-builder
description: Build or grow the person's Story Bank — each shipped artifact turned into a reusable interview story with situation, what they did, what changed, and the questions it answers — as a live tracker the interview jobs read. Activates on "build my story bank" / "add a story" / "turn my projects into interview stories" / "what stories do I have".
disable-model-invocation: true
---

Every strong interview answer is a story the person already lived. This skill writes
them down once so no round starts from a blank page.

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block. If none, say:
"Run `jobsearch-setup-wizard` first — the shipped artifacts there are the raw
material." Continue only if the person pastes their projects.

## Inputs

The shipped artifacts from the profile and the resume, plus anything the person adds
now. For each, ask for at most one missing detail (usually the result); the rest is
`[confirm]`.

## Method

For each artifact, draft a story card:
- **Story name** — five words, memorable ("the streaming cutover").
- **Artifact** — what was built, shipped, fixed, or run.
- **Situation** — the context and the stakes, two sentences.
- **What I did** — the decisions the person made, in "I" statements; the team's work
  stays "we".
- **What changed** — the result in the person's own figures; no figure → what was
  different after.
- **Answers these questions** — three to six behavioral prompts it fits (ownership,
  conflict, ambiguity, influence, failure, scale, mentoring).
- **Gets ahead of** — which positioning challenge it counters, if any.
- **Used with** — left blank; the interview jobs fill it.

Aim for six to ten stories. Flag gaps: if no story covers conflict, failure, or
influencing without authority, say so and ask for a candidate.

## Output

Publish or update the **"Story Bank"** artifact in this Project (list existing
artifacts first, including from earlier conversations; update if it exists, create
only if absent). Columns: Story · Artifact · Situation · What I did · What changed ·
Answers these questions · Gets ahead of · Used with. Keep a CSV copy in the Project.
Then, in chat, the story names and the gaps.

## Constraints

- Nothing invented — every result figure comes from the person.
- Nothing confidential about the current employer beyond what the profile allows.
- Stories stay in the person's voice; no AI-register words.

## After

"Say 'prep for an interview' and I'll map these to whatever round is next."

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
