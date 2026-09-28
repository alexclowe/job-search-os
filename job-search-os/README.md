# Job Search AI Operating System

**The AI operating system for a senior job search.** 30 skills: a command center and five end-to-end jobs — tailor and apply, work my inbox, prep for an interview, follow up and negotiate, run my weekly review — plus every individual skill a search needs: posting decoder, resume and cover letter, LinkedIn, story bank, stage-by-stage interview prep, negotiation, counter-offers, references, outreach, and a severance script, with three guardrails built in (minimum salary, every claim holds up, no invention).

Built by The AI Career Lab. https://clowealex.gumroad.com/l/job-search-ai-os

---

## What's inside

**The Operating System (8 skills):**
- `jobsearch-os` — the command center: your five jobs as cards, a one-line summary from your trackers, and "Try it on a sample" on first run
- `jobsearch-workflow-tailor-apply` — Tailor & apply: salary check, posting decoded, tailored resume and cover letter, Application Board row
- `jobsearch-workflow-inbox` — Work my inbox: recruiter replies, scheduling, rejections read, interviews on the calendar, board updated
- `jobsearch-workflow-interview-prep` — Prep for an interview: a brief for the round that's actually next, from your Story Bank
- `jobsearch-workflow-follow-up-negotiate` — Follow up & negotiate: thank-you notes, follow-up cadence, offer worksheet, counter script, Offer Tracker
- `jobsearch-workflow-weekly-review` — Run my weekly review: what moved, what's stale, three moves, outreach, focus blocks, Weekly Search Log
- `jobsearch-connect-tools` — connect Gmail, Google Calendar, and Google Drive (personal accounts; drafts only — nothing sends without your click)
- `jobsearch-skill-catalog` — browse every skill in the plugin

**1 setup wizard:**
- `jobsearch-setup-wizard` — captures your career story once (current role, target roles, minimum salary, positioning challenges, shipped artifacts, voice); every other skill reads from it

**18 individual skills:**

*Read the posting:* `job-posting-decoder` · `comp-research`

*Apply:* `resume-tailor` · `cover-letter-draft` · `linkedin-rewrite` · `ai-use-positioning`

*Interview:* `story-bank-builder` · `star-answer-builder` · `recruiter-screen-prep` · `hiring-manager-prep` · `panel-and-final-round-prep` · `reference-call-prep`

*Offers & exits:* `salary-negotiation-script` · `counter-offer-handler` · `decline-offer-letter` · `thirty-sixty-ninety-plan`

*Network:* `outbound-networking`

*Just laid off:* `severance-leverage-script`

**3 passive guards:**
- `jobsearch-salary-guard` — flags any role, message, or offer at or below your minimum salary before you spend time on it
- `jobsearch-oversell-guard` — checks that every claim holds up on every resume, letter, and answer; strips AI-register tells
- `jobsearch-fabrication-guard` — any figure, title, or date with no source in your record becomes `[confirm]`

---

## Install

### Claude desktop app (recommended)
1. **Create a Project first.** Open **Projects** in the left sidebar and create one (suggested name: `My Job Search`). Your profile and trackers are saved there.
2. **Install the plugin.** Click **Customize → Plugins → Add ▾ → Upload plugin** and choose the `job-search-os-claude-plugin…zip` file as-is (don't unzip it).
3. **Start a conversation inside the Project and say "set me up".** Paste your resume — it fills in most of your profile — confirm one card (your minimum salary is the one thing it will insist on), and your command center opens. About two minutes.

### Claude Code — CLI (advanced / optional)
From the unzipped plugin folder, run `claude plugin install ./job-search-os`, then `/job-search-os:jobsearch-setup-wizard`.

### Claude.ai web — manual fallback (no plugin support)
1. Open `skills/jobsearch-setup-wizard/SKILL.md` and follow it to produce your profile block.
2. Paste the profile block into a Claude Project's Custom Instructions.
3. Reference individual skills by pasting their SKILL.md content as needed.

---

## How the tools fit

**Works out of the box, no setup required.** Every skill accepts pasted postings, messages, resumes, and offer terms. You get the full plugin value with zero connector wiring.

**With Gmail, Google Calendar, and Google Drive connected** (a short sign-in under **Customize → Connectors**, using a personal account — never an employer's): jobs put replies and notes in your Drafts folder, interview holds and focus blocks on your calendar, and tailored files in a per-company Drive folder. Reading your inbox means: it looks for recruiter and hiring-team messages, shows you what it found, and you confirm before anything is used.

---

## Recommended cadence

| Frequency | Run |
|---|---|
| Monday | **Run my weekly review** (`jobsearch-workflow-weekly-review`) |
| Twice a week | **Work my inbox** (`jobsearch-workflow-inbox`) |
| Per posting | **Tailor & apply** — or `job-posting-decoder` first if you're unsure it's worth the hour |
| Before every interview | **Prep for an interview** |
| The day after | **Follow up & negotiate** |
| Once, early | `story-bank-builder` — every interview prep reads it |
| When an offer lands | **Follow up & negotiate** → `salary-negotiation-script` → `thirty-sixty-ninety-plan` |

Guards fire automatically based on what's being produced. You don't run them manually.

---

## License

See `LICENSE.md`. Single-person license — install on as many of your own devices as you want; don't redistribute or resell.

## Questions

alex@theaicareerlab.com
