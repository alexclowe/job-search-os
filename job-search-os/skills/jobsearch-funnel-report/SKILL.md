---
name: jobsearch-funnel-report
description: Diagnose your job-search funnel for the Job Search AI Operating System — reply rate by source (referral, job board, recruiter reached out, applied direct) and where applications die (no reply, screens that stall, interviews without a final, finals without an offer), from your Application Board, with one fix tied to each stall point. Says "too few to tell yet" instead of guessing from small numbers. Invoke with "where is my search stalling", "funnel report", "diagnose my search", or "why am I not getting replies". Also runs inside the weekly review.
disable-model-invocation: true
---

> **Words rule (never break):** the lowest pay the person will accept is their **minimum pay**
> (in their pay type), in every status line, reply, file, and tracker. The comparison against
> it is the **salary check**. Never call it a "floor", even if an older profile or memory does.

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Never name profile or connection filenames in conversation.

More applications is rarely the fix. This finds the stage where things stop and names
the one change that stage needs.

## Read the board

List this Project's artifacts first, including ones from earlier conversations, and
read the **Application Board** (or its CSV backup). Ignore rows under "Samples" and
anything named "SAMPLE — …".

Columns this report uses (older boards may lack some — treat a missing column or a
blank cell as **unknown**, never as zero, and say how many rows had it):
- **Source** — referral · job board · recruiter reached out · applied direct · other
- **Stage** and the stage dates — Applied on · Reply on · Screen on · Interview on ·
  Final on · Offer on · Closed on · Closed why

If there's no Source on older rows, ask once whether the person wants to fill it in
for the active ones (a quick clickable list per row) — or run the report without the
by-source view.

## Pre-flight — Moves saved on the board

Before you read or change the **Application Board**, apply any moves the person made
on the board itself. A board built from the template saves each move in the board
artifact's storage: one document per row in its `moves` collection, holding the row
id, the new stage, and when it was saved. Read that collection with the artifact
storage tool. For each saved move whose row is still on the board:
- set that row's **Stage** in the board's data block to the saved stage;
- if the date for the new stage is blank, fill it with the date the move was saved
  (Applied → Applied on, Screening → Screen on, Interviewing → Interview on, Onsite →
  Final on, Offer → Offer on, Closed → Closed on);
- a row moved to Closed with no Closed why: ask for the reason once, as clickable
  choices, or leave it blank.
Then republish the board once, delete exactly the saved-move documents you applied
(and any for rows no longer on the board), update the CSV backup, and say it in one
line: "Applied 2 moves you made on the board: Northwind → Interviewing, Harbor →
Closed." If the board has no storage, the storage tool isn't available here, or
nothing is saved, skip this without comment and use the board as it is.

## Count honestly

For each source and in total: applications (rows with Applied on, or stage Applied or
later) · replies (Reply on set, or any stage past Applied, or Closed why "rejected"
with a reply) · screens · interviews · finals · offers.

**Minimum sample:** a source with fewer than 10 applications gets "too few to tell
yet" instead of a rate. Under 10 applications in total, don't diagnose at all — show
the counts and say "Come back after about 10 applications; before that, any pattern is
noise." Never extrapolate, and never compare to "industry averages" — there's no
source for one that fits everyone.

## Where things die

A row has **stalled** at its stage when there's been no stage change and no touch in
14 or more days and it isn't Closed. Group closed-and-stalled rows by the last stage
reached:

| Where it stops | What it usually points to | The fix to try first |
|---|---|---|
| **No reply** (applied, nothing back) | The resume isn't landing for these postings, the source is cold, or the roles are a stretch | Rework the top third of the master resume for the target role; shift effort to referrals (check who you know at your target companies); run the fit check before applying |
| **Screens that stall** (a recruiter call, then nothing) | Pay or level mismatch, or the "why this role" answer | Recruiter-screen prep with a company brief; confirm the pay range on the first call; tighten the why-now line |
| **Interviews without a final** | Stories not landing for their worries | A mock interview on the round that stalls; add stories to the Story Bank for the top worries |
| **Finals without an offer** | The close, references, or fit at the last step | Final-round prep, a 30-60-90 plan, reference prep — and ask for feedback on the next one |

Name the stage with the biggest drop that has enough rows to count, and give **one**
fix for it. Mention a second only if it's close.

## Output

```markdown
**Funnel — [date range], [N] applications (samples excluded)**

| Source | Applied | Replied | Screen | Interview | Final | Offer | Reply rate |
|---|---|---|---|---|---|---|---|
| Referral | … | … | … | … | … | … | …% or "too few to tell yet" |
| … | | | | | | | |
| **All** | … | | | | | | |

**Where it stops:** [stage] — [count] of [count] ([what the rows show]).
**Try first:** [one fix, one line, and the skill or job that does it].
**Unknown:** [N] rows without a source or dates — filling them in sharpens this.
```

Save as "Funnel — [date].md" in this Project when run on its own; inside the weekly
review it goes in the week plan.

## The Search Funnel view (read-only)

When artifacts are available, also publish (or update, never duplicate) the **Search
Funnel** artifact from the fixed template `templates/search-funnel.html` that ships
with this skill (`jobsearch-funnel-report/templates/search-funnel.html`). Copy the
file exactly and change **only the JSON inside `<script type="application/json"
id="funnel-data">`**:
- `rows`: one object per Application Board row after saved moves are applied
  (samples excluded), with `stage`, `source`, `closedWhy`, `appliedOn`, `replyOn`,
  `screenOn`, `interviewOn`, `finalOn`, `offerOn` copied as they are on the board
  (blank as "").
- `whereItStops` and `tryFirst`: the same one-line diagnosis and fix as the report,
  in words. Leave both blank below the minimum sample.
- `asOf`: today's date. Leave `minSample` at 10.
Never type a count or a rate into it: the view computes every number from the rows.
Publish it without storage or any other capability; it is a picture of the board, and
it changes only when a job rebuilds it. If artifacts aren't available, the markdown
report above is the whole output.

## Constraints

- Every number comes from the board; nothing is estimated or rounded to look better.
- No rate below the minimum sample. No outside benchmarks.
- Kind, plain tone — a slow funnel is information, not a verdict on the person.

## About this plugin

Part of the Job Search AI Operating System by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os
