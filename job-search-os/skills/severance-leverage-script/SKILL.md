---
name: severance-leverage-script
description: For someone just laid off — read a separation offer, list what's commonly negotiable, draft the request for a written copy and for time to review, and script the ask for more weeks, extended healthcare, a clean reference, or equity treatment, with every legal point flagged for a professional. Activates on "I was just laid off" / "review my severance" / "can I negotiate my separation agreement" / a pasted separation offer.
disable-model-invocation: true
---

Most people sign the first version. This skill gets the person a copy, time, and a
list of what to ask for — and points at a professional where it matters.

## Pre-flight — Load profile

Look for the `Job Search AI Operating System — Profile` block: `./job-search-os-profile.md`
(Project folder), then this Project's instructions, then a pasted block. Continue
without it; this skill mostly needs the offer.

## Inputs

The separation offer or what they were told (weeks of pay, healthcare continuation,
equity treatment, bonus and commission owed, unused leave, the deadline, any
non-disparagement or non-compete terms, whether it's a group layoff), the person's
tenure and level, jurisdiction (country and state or province), and age band (over or
under 40, because review periods can differ in the US).

## Output

1. **First 24 hours** — ask for a written copy of the offer and agreement; ask for
   time to review; sign nothing on the day; note the deadline; get personal copies of
   your own documents only (never company data).
2. **What's commonly negotiable** — additional weeks, healthcare continuation or a
   stipend, equity vesting or exercise window, pro-rated bonus, unused leave payout,
   a written reference and an agreed departure line, outplacement, the timing of the
   separation date, removal of non-compete or non-disparagement terms. Each marked
   "commonly negotiable" or "depends — ask", never "guaranteed".
3. **The review period** — in the US, older workers in some layoffs are entitled to a
   consideration period and a revocation window under federal age-discrimination
   rules; rules differ by jurisdiction and situation — `[verify with an employment
   attorney or your state's labor office]`. Elsewhere, statutory notice and severance
   minimums may apply — `[verify]`.
4. **The ask, scripted** — the email requesting the written copy and time (60–90
   words); the negotiation email (120–180 words): gratitude, the two or three asks in
   priority order with a reason each (tenure, the timing, the job market for the
   role), a proposed reply date. Never threaten; never mention a lawyer unless they
   have one.
5. **Questions to ask HR** — healthcare end date and continuation cost, equity
   deadlines, final pay date, how references will be handled, what "non-disparagement"
   covers.
6. **What to run next** — the approved one-line reason for leaving for the profile;
   `jobsearch-setup-wizard` to set your minimum salary; the Layoff Center's free triage tools.

## Constraints

- No legal advice: every statutory point is flagged for a professional and never
  stated as certain.
- No invented figures ("companies usually give X weeks").
- Never advise taking company data or violating an existing agreement.
- Drafts only; nothing sends.

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
