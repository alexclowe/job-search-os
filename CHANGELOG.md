# Changelog

All notable changes to the Job Search AI Operating System are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the plugin's `version` in `job-search-os/.claude-plugin/plugin.json`, and each version is also a [GitHub Release](https://github.com/alexclowe/job-search-os/releases) with the plugin zip and the documentation zip attached.

## [1.4.0] — 2026-09-28

Views you can see at a glance. Still five jobs.

### Added
- **An Application Board you can move.** The board is now a column per stage with a card per application, the stage written on every card (not just shown by colour), and a "Due this week" strip. Each card has a **Stage** menu: a move you make is saved on the board, and the next job you run (tailor & apply, work my inbox, follow up & negotiate, the weekly review, the command center, or the funnel report) applies it first, fills in that stage's date if it's blank, and tells you in one line.
- **The Search Funnel view**, read-only, rebuilt from the board by the funnel report and the weekly review.
- **The Offer Comparison view** (Follow up & negotiate): open offers side by side from the Offer Tracker, labelled for each pay type (differentials and overtime, bonus, commission and draw with the ramp, step and stipends), with schedule, benefits, and the salary check. Figures only as stated; "not stated" where you need to ask.
- **Your Search This Week**, a read-only home view the command center keeps current: active applications, interviews this week, offers in play, follow-ups due, and the week's three moves.
- **The Practice Round view** (mock interview, and "practice it with me" in Prep for an interview): the current question, an answer timer, how many answers used a Story Bank story, and each answer's rating (strong, solid, needs a story, needs a shorter version) with its one-line feedback. It never stores your answers.
- The views ship as fixed templates inside the plugin (`skills/*/templates/`). Jobs change only the data in them, so they look the same every time.
- A template check (`scripts/job-search-os/lint-artifact-templates.py`, with tests): no network calls or outside scripts, no browser storage as the record, the stage shown in words as well as colour, readable at phone width.

### Changed
- **Tailor & apply always shows the three choices** after the check card (tailor it, skip it, get the intro first), as buttons where the app supports them and as a numbered list where it doesn't.
- The Offer Tracker gains **Schedule** and **Benefits** columns (added blank to an existing tracker).
- A board that saves moves is private to your organization (no public link), and people you share it with as viewers can see it but can't move cards. Where the board can't save moves, the jobs fall back to a table and you say the move instead ("move Northwind to Interviewing"). The spreadsheet copy of the board is kept either way.

## [1.3.1] — 2026-09-28

Fixes found in the full claude.ai smoke test, and a new video set.

### Fixed
- **Tailor & apply now stops on the check card.** When the check came back clean, it used to go straight into tailoring. It now ends its turn on the card and waits for you to choose: tailor it, skip it, or get the intro first.
- **Setup only uses what you give it.** A fresh-start rule in the setup wizard and a profile rule in the command center stop them from pulling pay figures or roles from anywhere other than your paste, your answers, or your saved profile.
- **Plain pay wording everywhere.** The words rule (the lowest pay you'll accept is your **minimum pay**; the comparison is the **salary check**) now appears in every job and every skill that talks about pay.

### Added
- Ten narrated clips recorded on claude.ai with fictional sample data: first run, setup, the check card, the people tracker, tailor & apply, interview prep, a mock interview, negotiation, the funnel report, and the weekly review.

## [1.3.0] — 2026-09-28

Profession archetypes for 108 jobs.

### Added
- **108 profession archetypes** (up from 8), from nurses, teachers, and bookkeepers to electricians, cooks, truck drivers, security guards, physicians, and software developers. Each covers target titles, where postings live, what a recruiter screens for first, story types that land, resume conventions, how interviews usually run, how pay is usually structured, what's usually negotiable, red flags in postings, where to verify licensing, and what differs in Canada.
- **Pay-type-aware archetypes:** each one is written for how that work is actually paid (hourly with overtime and differentials, salary, commission and draws, day rates, per-mile, per-visit, salary schedules, tips), so the minimum-pay check and the negotiation asks compare like with like.
- **US facts from public data:** pay ranges, projected openings, and typical entry education from BLS Occupational Employment and Wage Statistics (May 2025) and Employment Projections 2025–35; titles and tasks from the O\*NET® 31.0 Database. Numbers appear only in generated blocks, never in hand-written text.
- **Canada notes:** the NOC 2021 unit group where one fits (or a plain "no clear match"), Job Bank for outlook and wages, and the provincial regulator, college, or certification body to check, named only after it was checked on its official site.
- **Index lookup:** `archetypes/index.md` lists every archetype with the names and aliases it covers; every job reads it first and opens only the matching file.
- **"Also read"** links between related archetypes (for example paralegal and lawyer).
- `archetypes/NOTICE.md` and `archetypes/LICENSE`.

### Changed
- The archetypes are licensed **CC BY 4.0**; the plugin and code stay MIT.
- Every archetype was reviewed against official sources before release: two pilot reviews, then a review of each of the two batches, with each factual fix checked on the source the review cited.

## [1.2.0] — 2026-09-28

The work before you apply and after you interview.

### Added
- **One check card before every application** (Tailor & apply): is this real, the pay against your minimum, your fit (strong, partial, or stretch, with the two biggest gaps), and who you know there — then one choice: tailor it, skip it, or get the intro first.
- **Is this real?** (`jobsearch-real-check`): the caution signals official consumer-protection guidance names for job scams, plus softer signs a posting isn't an open role, and how to check. Signals, never verdicts.
- **Posting terms after tailoring**: the posting's terms your resume now uses, and the ones your record can't support yet — asked as questions ("Did you do X?"), never added.
- **Nothing undersold** (`jobsearch-undersell-guard`): the mirror of the oversell check, against the same record.
- **Application-form answers** (`jobsearch-application-questions`): why us, why this job, desired pay in your pay unit, how you heard, licenses. Never the voluntary self-identification questions.
- **People tracker** (`jobsearch-people-tracker`) and a **People** board: reads your LinkedIn connections export (finds the header row, matches by company because email is usually blank), keeps only people at companies you're applying to, drafts the intro request.
- **Company brief** (`jobsearch-company-brief`): one page, every fact with a source and a date; runs before recruiter-screen prep and carries into later rounds.
- **Mock interviews** (`jobsearch-mock-interview`) and a practice round inside Prep for an interview: one question at a time, feedback after each answer, profession formats (clinical scenarios, demo lessons, sell-me-this role-plays, technical plus behavioral), new stories added to the Story Bank.
- **Build a resume from scratch** (`jobsearch-master-resume`): a short interview and a master resume in current US and Canadian conventions, including the two-page federal limit and licenses near the top for nurses and teachers.
- **Funnel report** (`jobsearch-funnel-report`) inside the weekly review: reply rate by source and where applications stall, with one fix; "too few to tell yet" under 10 applications.

### Changed
- The Application Board gains Real check, Fit, Referral, and stage dates (Reply on, Screen on, Interview on, Final on, Offer on, Closed on, Closed why). Older boards keep working; missing columns are added blank and read as unknown.
- The Weekly Search Log gains a "Where it stops" column.
- Scam signals, resume conventions, and pay-transparency notes follow official sources (FTC and FBI IC3 job-scam guidance, state attorney general alerts, USAJOBS and OPM, Canada's Job Bank, university career centers, state and provincial labour pages), with anything unsettled worded as "check your state's current rule".

## [1.1.0] — 2026-09-28

Built for every profession, not just senior tech roles.

### Added
- **Pay type** in setup and the profile: annual salary, hourly, commission or commission plus base, or a salary schedule. Your minimum pay is saved in that unit (for example `$44/hour`, `$68,000/year`, `$55,000 base or $120,000 expected total`, `step 6 or $58,000`).
- The salary check compares like with like: hourly to hourly, salary to salary, a commission role's base and realistic expected total each against the matching minimum, and salary-schedule placement against the step you need. Differentials and "up to" commission figures are never counted as base.
- Offer worksheet, Offer Tracker, counter scripts, recruiter-screen scripts, and pay research all handle hourly (differentials, overtime, guaranteed hours), commission (split, draw, ramp, clawbacks, lead source), and salary schedules (step placement, years credited, stipends, pension). Equity appears only when an offer includes it.
- A second sample: **Maria Delgado (SAMPLE)**, a nurse paid hourly moving to a clinic job, alongside the data-engineer sample.
- Archetypes gained three sections, **How interviews usually run**, **How pay is usually structured**, and **What's usually negotiable**, filled in for all eight professions. Interview prep, follow up and negotiate, and the weekly review now read them too, not just tailor and apply.

### Changed
- Career stage replaces the senior-only level picker: early career or entry level, experienced, lead or supervisor, manager or director, executive, changing careers, returning to work.
- Plain wording in the profile: **Wins** (three to five things you did and what came of them) replaces "shipped artifacts", and **Things a hiring manager might question** replaces "positioning challenges". Profiles saved with the old labels keep working.

## [1.0.0] — 2026-09-28

First public release.

### Added
- Command center (`/jobsearch-os`) with a "Try it on a sample" first run.
- Five end-to-end jobs: Tailor & apply, Work my inbox, Prep for an interview, Follow up & negotiate, Run my weekly review.
- Living trackers: Application Board, Story Bank, Offer Tracker, Weekly Search Log.
- Three always-on guardrails: minimum salary, every claim holds up, no invention.
- Connect-tools flow for Gmail, Google Calendar, and Google Drive (personal accounts only; every send behind approval).
- 18 standalone skills: posting decoder, comp research, resume tailor, cover letter, LinkedIn rewrite, AI-use positioning, story bank, STAR answers, recruiter-screen, hiring-manager, panel and final-round, and reference-call prep, negotiation script, counter-offer handler, decline letter, 30-60-90 plan, outbound networking, severance-leverage script.
- Profession archetype registry with eight seeded archetypes and a template.
- One-plugin marketplace manifest so the repository installs with "Add from a repository".
- Repository validation workflow (`scripts/validate.py`, `scripts/check-readme-links.py`).
