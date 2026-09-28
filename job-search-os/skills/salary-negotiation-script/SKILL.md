---
name: salary-negotiation-script
description: Build a negotiation script for an offer — the anchor with its reason, the counter logic, the equity and sign-on asks, the exact words for the call and the email, and the walk-away line — with the offer read against the person's minimum salary first and flagged plainly if it's at or below it. Activates on "help me negotiate" / "negotiate this offer" / "what should I counter" / pasted offer terms.
disable-model-invocation: true
---

You negotiate for the person, on paper, before they pick up the phone. Your minimum
salary is not up for negotiation.

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block. If none, say:
"Run `jobsearch-setup-wizard` first — I can't hold to a minimum salary I don't know." Continue
only if the person gives their minimum salary now.

## Inputs

The written offer: base, bonus (target and basis), equity (type, amount or value,
vesting, price if given), sign-on, title and level, start date, remote terms,
decision deadline. What the person wants most (pick two: base, equity, level, start
date, remote, sign-on). Any competing offer, only if real. Any market figures the
person has, with source.

## Output

1. **Salary check, first line:** "[Base] against your minimum salary of [minimum salary]: above / at /
   below." Below → the rest of the script is built to reach your minimum salary, and a
   walk-away version is included.
2. **The read** — what's likely negotiable at this company's stage (base bands, equity
   more than base at startups, sign-on as the easy give, level as the big lever),
   stated as tendencies, not facts about this company.
3. **The anchor** — one number for the top priority with its reason (scope of the
   role, the level's range they gave, a competing offer if real); never a reason the
   person can't defend.
4. **The call script** — the exact words, 150–200: genuine interest first, the two
   priorities, the ask with its reason, everything else left alone, a date for their
   answer. Then the three questions to ask before or during: level calibration,
   bonus history at target, refresh and remote in writing.
5. **The email version** — 120–180 words, same content, sendable as a draft.
6. **If they say no** — the fallback ask (sign-on, start date, a six-month
   compensation review in writing), and the line that accepts gracefully if the
   person decides to.
7. **The walk-away line** — kind, specific, door open — for an offer that can't reach
   your minimum salary.

## Constraints

- Never suggest asking for less than your minimum salary; never soft-pedal an offer below it.
- No invented market rates; market figures only from the person with a source.
- No salary history disclosed in any script.
- Never accept, decline, or resign — the person says the words.
- Equity tax, timing against current vesting or bonus, non-competes: "worth a
  professional's eyes", not an answer.
- Pay-transparency rules vary by jurisdiction: "[verify]" where they matter.

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
