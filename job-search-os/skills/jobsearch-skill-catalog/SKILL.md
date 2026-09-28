---
name: jobsearch-skill-catalog
description: List every skill in the Job Search AI Operating System, grouped by category. Invoke when a job seeker says "browse all skills", "show me every skill", "what can this do", "skill list", or "what's in the Job Search Operating System". Run this anytime to see what's available.
---

# Job Search AI Operating System — Skill Catalog

**Render instruction (for Claude — read first):** when this skill runs, your reply to the user MUST contain the full catalog below — every category heading and every skill line, reproduced in full. The contents of this file are **not** visible to the user; nothing is "already rendered above." Never summarize the list, trim categories, or point to the catalog without printing it. After the full list you may add one short line suggesting a good next skill.

Every skill in the pack, grouped by category. Run any of them by typing `/<skill-name>` in a conversation inside the Project where this pack is installed.

This catalog skill is safe to run even before `/jobsearch-setup-wizard` — it doesn't require a profile.

## Jobs — the Operating System (start here)

Say **"open my command center"** (or type `/jobsearch-os`) to see these as cards. Each job runs a whole piece of work end to end, drops drafts into your connected Gmail, Calendar, and Drive (or hands you paste-ready output), and keeps a living tracker.

- `/jobsearch-os` — Command center — your jobs as cards, with active applications, interviews this week, offers in play, and follow-ups due
- `/jobsearch-workflow-tailor-apply` — Tailor & apply — one check card first (is it real, the pay, your fit, who you know there), then a tailored resume and cover letter from what you did and what came of it, the posting terms that made it in, the form answers, filed on your Application Board
- `/jobsearch-workflow-inbox` — Work my inbox — recruiter messages, scheduling, and rejections → replies in your voice, interviews on your calendar, the board updated (can run on a schedule)
- `/jobsearch-workflow-interview-prep` — Prep for an interview — a sourced company brief first, then a stage-specific brief: their worries, your stories mapped to them, answers, questions to ask back — and a practice round
- `/jobsearch-workflow-follow-up-negotiate` — Follow up & negotiate — thank-you notes, a follow-up cadence, an offer worksheet, and a counter built on your minimum pay
- `/jobsearch-workflow-weekly-review` — Run my weekly review — what moved, what's stale, where your search stalls (reply rate by source), exactly three moves, outreach drafted, focus blocks, Weekly Search Log (can run on a schedule)
- `/jobsearch-connect-tools` — Connect my tools — Gmail, Google Calendar, Google Drive (personal accounts only)

Every skill below still runs on its own, any time.

## Setup & navigation

- `/jobsearch-setup-wizard` — Capture your career story once (role, targets, minimum pay, what a hiring manager might question, wins, voice) so every skill reads it
- `/jobsearch-skill-catalog` — This list — every skill, grouped by category
- `/jobsearch-master-resume` — No resume, or an old one? A short interview → a master resume in current US and Canadian conventions, the base every tailored resume starts from

## Guards (always-on — they flag, never block)

- `/jobsearch-salary-guard` — Flags a role, message, or offer at or below your minimum pay before you spend time on it
- `/jobsearch-oversell-guard` — Checks that every claim holds up on every resume, letter, and answer; strips the AI-register words that get applications flagged
- `/jobsearch-fabrication-guard` — Source check — any metric, title, or date with no source in your record becomes [confirm]
- `/jobsearch-undersell-guard` — The other direction — real wins from your record that a draft buried, understated, or left out
- `/jobsearch-real-check` — Is this real? — caution signals that a posting or recruiter message is a scam, or not an open role, and how to check (signals, never verdicts)

## Read the posting

- `/job-posting-decoder` — Must-haves vs. wishlist, the real level, the three worries behind the requirements, the salary check, red flags, and a recommendation
- `/comp-research` — Compensation evidence for your target roles, every figure with a source, your minimum pay against it
- `/jobsearch-company-brief` — A one-page company brief, every fact with a source and a date — the raw material for "why us" and the questions you ask

## Apply

- `/resume-tailor` — Your real resume, reordered and rewritten for one posting — what you did and what came of it, ahead of titles, every claim traceable
- `/cover-letter-draft` — A 250–350 word letter that couldn't be sent to any other company, in your voice
- `/linkedin-rewrite` — Headline and About section for your target roles, what a hiring manager might question handled, visibility set so your current employer doesn't see it
- `/ai-use-positioning` — The honest answer to "how do you use AI in your work", plus the resume and LinkedIn lines that say the same thing
- `/jobsearch-application-questions` — The online-application questions — why us, why this job, desired pay in your pay unit, how you heard — in your voice; never the voluntary self-ID questions

## Interview

- `/story-bank-builder` — Your wins turned into reusable interview stories, kept as a live Story Bank
- `/star-answer-builder` — One behavioral question → a spoken answer from a named story, or an honest "no story yet"
- `/recruiter-screen-prep` — The six questions, the compensation script that holds to your minimum pay, the red flags to listen for
- `/hiring-manager-prep` — Their three worries, twelve likely questions with your answers, the story to lead with, questions to ask back
- `/panel-and-final-round-prep` — Per-interviewer plan for a loop, strategic framing for a final round, the close, an energy plan
- `/reference-call-prep` — A brief and a heads-up note for each reference
- `/jobsearch-mock-interview` — Practice out loud, one question at a time, feedback after each answer, new stories added to your Story Bank

## Offers & exits

- `/salary-negotiation-script` — Salary check first, the anchor with its reason, the exact words for the call and the email, the walk-away line
- `/counter-offer-handler` — A counter from your current employer or a revised offer, tested against why you started looking
- `/decline-offer-letter` — A gracious, specific no that keeps the door open
- `/thirty-sixty-ninety-plan` — The plan a final round asks for, and the one you actually run after saying yes

## Network & pipeline

- `/outbound-networking` — Warm intro, former colleague, cold hiring manager, alum, or inbound-recruiter reply — short, specific, one small ask
- `/jobsearch-people-tracker` — Who you know at the companies you're applying to — from your LinkedIn connections export, kept on a live People board, with the intro request drafted
- `/jobsearch-funnel-report` — Reply rate by source and where applications stall, with one fix for the stall point ("too few to tell yet" below 10 applications)

## Just laid off

- `/severance-leverage-script` — Read the separation offer, get a written copy and time, ask for what's commonly negotiable, every legal point flagged for a professional

---

**Need help getting started?**

- Run `/jobsearch-setup-wizard` first if you haven't yet — it captures your career story so every skill reads it.
- Good first picks:
  - `/jobsearch-os` — your command center
  - `/jobsearch-workflow-tailor-apply` — on a posting you're looking at right now
  - `/story-bank-builder` — before your first interview
