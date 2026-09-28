---
name: jobsearch-os
description: The command center for the Job Search AI Operating System — your home base. Triggers when a job seeker says "what should I work on", "what's next in my search", "open my command center", "job search command center", "show my pipeline", "start over", "go home", or "restart". Also the way out of any stuck flow. Loads the career profile, summarizes active applications, interviews this week, offers in play, and follow-ups owed from the trackers, shows the five search jobs as cards, and runs the one they pick. Also invoke for "try it on a sample".
---

> **Naming rule (never break):** the product is the **Job Search AI Operating System**.
> Use only this product name — never an older one. Profile and connection filenames are technical — never
> name them in conversation.

This is the home screen. It drafts nothing itself: it loads the person's career profile,
shows their jobs as cards, runs the one they pick, and comes back here afterwards.
"Start over", "go home" and "restart" also mean: drop whatever was in progress and
render this screen fresh.

## Pre-flight — Profile

Look for the career profile where every skill in this pack looks, in this order: the
Project file `./job-search-os-profile.md`, then this Project's instructions, then a
profile block pasted in this chat. Accept any block with the profile fields (current
role, target roles, pay type and minimum pay, what a hiring manager might question,
wins, search stage) whatever its heading says. Older profiles use other labels for the
same fields: `Minimum salary:` or `Salary floor:` mean minimum pay (treat the pay type
as annual salary unless the value says otherwise), `Shipped artifacts` means wins,
`Positioning challenges:` means things a hiring manager might question, and
`Target level:` means career stage. Check all three before deciding it's missing.
Read the profile only from those three places — never from account memory or other
conversations; if it's missing, the wizard collects it fresh.
- **Present:** use the person's name and target roles in the header. Note whether the
  minimum pay, wins, and what a hiring manager might question are filled in — the
  guards depend on them.
- **Absent:** don't render the command center. Say: "Let's get your career story set up
  first — about two minutes. Say 'run the setup wizard'." Stop there.

## Step 1 — Gather the summary line

List this Project's artifacts (including ones from earlier conversations). Ignore
anything named "SAMPLE — …". Count:
- rows on the "Application Board" with stage Applied, Screening, Interviewing, or
  Onsite → active applications; rows with a Due date in the next 7 days → follow-ups due
- rows on the Application Board with a date this week in Screen on, Interview on, or
  Final on (or, on an older board, stage Screening, Interviewing, or Onsite with an
  interview date this week) → interviews this week
- rows on the "Offer Tracker" with status Received or Countered → offers in play
- the latest "Weekly Search Log" row → the three moves for this week and how many are done

Never guess a number. If no trackers exist, the summary is: "Nothing tracked yet — run
any job below to start."

## Step 2 — Render the command center (fixed layout, identical every time)

Render the cards with the visual card/widget tool when it is available; otherwise render
the same layout as a clean numbered list. Clicking a card only stages its label — when
the choice arrives (clicked or typed), **run the mapped skill immediately**. Do not
improvise the structure: the "Suggested" tag is the only thing that changes.

**Header:** `Command center — [first name]'s search · [today's date]`, then the summary
line (e.g. "6 active applications · 2 interviews this week · 1 offer in play · 3
follow-ups due · this week: 1 of 3 moves done").

**First run only — "Try it on a sample (2 minutes)":** when no Application Board, Story
Bank, Offer Tracker, or Weekly Search Log exists yet, show this one extra card above the
Jobs list. Hide it once any real tracker exists.

**Jobs** — all five, this order, these labels:
1. **Tailor & apply** — a posting and your resume → one check card first (is it real,
   the pay, your fit, who you know there), then a tailored resume and cover letter
   that lead with what you did and what came of it, the form answers, filed on your
   Application Board.
2. **Work my inbox** — recruiter messages, scheduling requests, and rejections → replies
   drafted in your voice, interviews on your calendar, the board updated.
   *(Can run on a schedule.)*
3. **Prep for an interview** — the company, the round, and your Story Bank → a sourced
   company brief, then a prep brief for that stage: likely questions, your stories
   mapped to their concerns, the questions to ask back — and a practice round, one
   question at a time.
4. **Follow up & negotiate** — after any round or an offer → thank-you notes, a
   follow-up cadence, and a counter built on your minimum pay, logged on the Offer Tracker.
5. **Run my weekly review** — your board and your week → what moved, what's stale,
   where your search stalls (reply rate by source), three moves for the week, outreach
   drafted, focus blocks on your calendar.
   *(Can run on a schedule.)*

**"Suggested" tag** (at most two, cosmetic only — never reorder or hide a card): an
offer with status Received → tag 4; an interview in the next 3 days → tag 3; Monday, or
no Weekly Search Log row for this week → tag 5; follow-ups overdue → tag 2; no trackers
yet → tag 1.

**Setup & more** — always these, in this order:
- **Connect my tools** — Gmail, Google Calendar, and Google Drive.
- **No resume? Build one** — *only when there's no master resume in this Project*.
  A short interview → a master resume in current conventions
  (`jobsearch-master-resume`).
- **Complete your profile** — *only when the profile has no wins, no
  what a hiring manager might question, or no minimum pay*. Adds the three fields every draft and
  guard depends on.
- **Browse all skills** — every individual prompt in the pack still runs on its own.

## Step 3 — Run the pick

**Try it on a sample** → first offer the two samples as clickable options: **A nurse
moving to a clinic job (hourly pay)** · **A data engineer (annual salary)**. Then run
**Tailor & apply** (`jobsearch-workflow-tailor-apply`) on the one they pick, end to end,
without asking intake questions. Show the check card exactly as a real run would (is
it real, pay, fit, people — the sample's People line reads "nobody on your list yet —
samples never import connections"), then choose **Tailor it** automatically and say
"In a real run you pick here." Show the posting-terms list with its "did you do these?"
questions answered by the sample's own record, and skip the form answers unless asked. Label every output **SAMPLE**, prefix saved files and
the tracker with "SAMPLE — ", and make **no connector writes and no inbox reads**: show
what would land in Drive and on the calendar instead ("This is the folder that would
appear in your Drive"). Close with: "That's one application, checked against your
minimum pay and tailored. Now run it on a real posting?"

> **SAMPLE A (fictional) — hourly pay:** Maria Delgado, RN, 7 years on a med-surg unit
> at a community hospital, 12-hour nights, now looking for a daytime outpatient or
> clinic role. Pay type: hourly. Minimum pay: $44/hour base (she earns $41/hour plus a
> night differential now). Things a hiring manager might question: "all inpatient
> experience; no clinic or scheduling-system background." Wins: cut patient falls on
> her unit by redesigning hourly rounding with two other nurses; precepted nine new
> graduate nurses; became the unit's go-to for the new electronic charting rollout and
> trained the night shift on it. Posting: Riverbend Family Health (fictional), RN Care
> Coordinator, weekdays 8–4:30, no weekends, posted pay $42–$48/hour, asks for care
> coordination, patient education, charting-system fluency, and "calm with a full
> phone queue."

> **SAMPLE B (fictional) — annual salary:** Sam Okafor, 11 years in data engineering,
> two of them as an engineering manager leading four people, now returning to a
> hands-on role. Pay type: annual salary. Minimum pay: $185,000/year base, remote in the
> US. Things a hiring manager might question: "reads as a manager on paper; the
> hands-on work of the last two years is invisible on the resume." Wins: cut over a
> nightly batch pipeline to streaming with no customer-visible downtime; cut warehouse
> spend by about a third by re-partitioning the ten largest tables; built the team's
> first on-call rotation and runbooks. Posting: Northwind Labs (fictional), Staff Data
> Engineer, remote US, posted range $175,000–$210,000, asks for streaming experience,
> cost ownership, mentoring, and "comfortable being the most senior engineer in the
> room."

Compare like with like in the sample, exactly as a real run would: Maria's $44/hour
minimum against the posted $42–$48/hour (inside the range, not a flag, but worth
asking about differentials and guaranteed hours on the first call).

- Tailor & apply → `jobsearch-workflow-tailor-apply` (real posting)
- Work my inbox → `jobsearch-workflow-inbox`
- Prep for an interview → `jobsearch-workflow-interview-prep`
- Follow up & negotiate → `jobsearch-workflow-follow-up-negotiate`
- Run my weekly review → `jobsearch-workflow-weekly-review`
- Connect my tools → `jobsearch-connect-tools`
- No resume? Build one → `jobsearch-master-resume`
- Complete your profile → `jobsearch-setup-wizard`
- Browse all skills → `jobsearch-skill-catalog`

Everything a job produces is a draft. Nothing sends, submits, accepts, or declines on
its own.

## Step 4 — Come back

When a job finishes, ask "What's next?" and render this same command center again —
same layout, fresh summary line.

## Samples still show the live board

Publishing or updating an **artifact is not a connector write** — it is allowed, and
expected, during "Try it on a sample". When the sample job reaches its tracker step,
publish the Application Board artifact exactly as a real run would, with the sample
row in its "Samples" section (never counted in totals), so the user sees the board the
product will keep for them. Only Gmail, Calendar, and Drive writes are off during a
sample. In the close, name the board and where to find it (Artifacts in the sidebar).

## Your boards

Right under the summary line, if any live tracker artifacts exist (not "SAMPLE" ones),
add one line naming them so the user can jump to them — e.g. "Your boards: Application
Board · Story Bank · Offer Tracker · People (open them from Artifacts in the sidebar)". Jobs
create and update these boards; the command center only points to them.

## About this skill

Home screen of the **Job Search AI Operating System** by The AI Career Lab.
More at https://clowealex.gumroad.com/l/job-search-ai-os
