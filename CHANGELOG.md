# Changelog

All notable changes to the Job Search AI Operating System are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/); versions follow the plugin's `version` in `job-search-os/.claude-plugin/plugin.json`, and each version is also a [GitHub Release](https://github.com/alexclowe/job-search-os/releases) with the plugin zip and the documentation zip attached.

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
