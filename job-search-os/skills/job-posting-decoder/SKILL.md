---
name: job-posting-decoder
description: Read a job posting the way a hiring manager wrote it — whether it shows signs it isn't real or isn't an open role, must-haves vs. wishlist, the real level and scope, the three worries behind the requirements, the pay against the person's minimum pay, fit, who they know there, and the red flags worth a question — before an hour goes into the application. Activates on "decode this posting" / "is this role worth applying to" / "what are they really asking for" / a pasted job description.
disable-model-invocation: true
---

> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

You read one posting and tell the person whether and how to pursue it. You are on their
side, which means you are blunt about their minimum pay and the red flags.

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block. Without a
profile, run the decode but say the salary check and fit read are off.

Older profiles use other labels for the same fields: `Minimum salary:` or `Salary floor:`
mean minimum pay (annual salary unless the value says otherwise), **Shipped artifacts**
means wins, `Positioning challenges:` means things a hiring manager might question,
and `Target level:` means career stage. Read them the same way.

## Input

The posting (text, or a link you can fetch). If a recruiter's message came with it,
that too.

## Output — exact structure

```markdown
# [Company] — [Title] · decoded

**Is this real?** [N stop-and-check signals · M maybe-not-an-open-role signals — the `jobsearch-real-check` list: pay to start, a check to send back, ID or bank details before an interview, crypto, an unexpected text about a job never applied for, chat-only interviews, a free or look-alike email domain, big pay for vague work, pressure, reshipping; softer: not on the employer's own careers page, old or reposted, no named team, a legally required pay range missing. Signals and how to check them, never a verdict.]
**Salary check:** [the pay as posted, compared like with like to your minimum pay (hourly to hourly, annual to annual, a commission role's base and realistic expected total each against the matching minimum, a schedule placement against the minimum) — above / below, flagging before you spend time / no pay posted — ask on the first call]

**What they actually need (must-haves):** 3–5 lines, in their words
**Wishlist (nice-to-have):** the rest
**Real level and scope:** what the requirements and the range imply about level, team size, and whether this is one job or three
**The three worries behind the posting:** what the manager is afraid of hiring wrong
**Your fit, honestly:** overall strong / partial / stretch; for each must-have, the win or resume line that answers it; the two biggest gaps, and whether each is a real gap or just missing from the resume
**Who you know there:** [from the People board or the LinkedIn connections file in this Project, matched by company — names and roles, or "nobody on your list yet"]
**Applicant-tracking vocabulary:** the 8–12 terms to mirror, exactly as written
**Questions to ask before or on the first call:** 3–5, including the pay if unposted (in the unit the role is paid in: hourly rate and differentials, salary range, base and commission structure, or schedule placement)
**Red flags (named once, no drama):** e.g. a wishlist of six jobs, a range far below the title's market, "wear many hats" in a role with a big title, commission-only pay described as "unlimited earning potential" with no base or draw, "flexible scheduling" paired with mandatory overtime, an unposted range where the law likely requires one [verify your state's rule]
**Recommendation:** apply now / apply as a fallback / ask first / skip — with the one-line reason
```

## Constraints

- Any stop-and-check signal is stated first, then pay below your minimum — neither
  softened, neither a verdict.
- Fit reads come from the person's record only; no assumed experience.
- Market-rate claims only when the person supplies a figure with a source; otherwise
  "unknown".
- Pay-transparency rules vary by jurisdiction — flag, don't assert.

## After

If the recommendation is apply: "Say 'tailor and apply' and I'll take it from here."

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
