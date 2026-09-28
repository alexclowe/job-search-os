# Job Search AI Operating System

**The job search that runs in the Claude app. No terminal, no config files, nothing to fork before you can start.**

A free Claude plugin (MIT) for anyone running a real job search: five end-to-end jobs, living trackers, and three guardrails that keep your resume honest and your time off roles below your salary floor. Drafts land in your own Gmail, Calendar, and Drive, and nothing is sent, submitted, accepted, or declined without your click.

Built by [The AI Career Lab](https://theaicareerlab.com) for people who looked at the excellent open-source job-search tools for Claude Code and thought "I don't use a terminal." Same idea. Different door.

## Install in three clicks

In the Claude desktop app (any paid plan: Pro, Max, or Team):

1. **Customize → Plugins → Add ▾ → Add marketplace → Add from a repository**
2. Paste `alexclowe/job-search-os` and click **Sync**
3. Under **Discover**, click **Add** on *Job Search AI Operating System*

Then start a conversation inside a Project and say **"set up my Job Search OS"**. Paste your current resume; setup takes about two minutes and ends on your command center. Pick **"Try it on a sample"** to watch it tailor one application for a made-up job seeker before you paste anything real.

Claude Code users: `/plugin marketplace add alexclowe/job-search-os` then `/plugin install job-search-os@job-search-os`.

Prefer a zip and the PDF guides (Start Here, Jobs Guide, cheat sheet, skill catalog)? The free kit is on Gumroad, pay what you want: **[clowealex.gumroad.com/l/job-search-ai-os](https://clowealex.gumroad.com/l/job-search-ai-os)**. It asks for an email so we can send updates when the skills change.

## What it does

Say **"open my command center"** (or `/jobsearch-os`) and pick a job. Each one runs start to finish and files its results on a living tracker.

| Job | What happens |
|---|---|
| **Tailor & apply** | Salary-floor check on the posting *first*, then a tailored resume and cover letter that lead with what you shipped, every claim traced to your own record, filed on the Application Board |
| **Work my inbox** | Recruiter replies drafted in your voice, interviews put on your calendar, rejections read once and closed |
| **Prep for an interview** | A brief for the round that is actually next, built from your Story Bank |
| **Follow up & negotiate** | Thank-you notes, a follow-up cadence, an offer worksheet, and a counter built on your floor |
| **Run my weekly review** | What moved, what went stale, exactly three moves for the week, focus blocks on your calendar. Can run every Monday on a schedule |

**Living trackers** you edit in place: Application Board, Story Bank, Offer Tracker, Weekly Search Log.

**Three guardrails, always on:** the salary floor (flagged before you spend an hour), defensibility (every claim has to survive "what exactly did you do?"), and no invention (any figure without a source in your record becomes `[confirm]`). They flag; the decisions stay yours.

**Every individual skill is also runnable on its own:** posting decoder, resume tailor, cover letter, LinkedIn rewrite, story bank, STAR answers, recruiter-screen and hiring-manager and panel prep, reference-call prep, comp research, salary-negotiation script, counter-offer handler, decline letter, 30-60-90 plan, outbound networking, a severance-leverage script for the first 24 hours after a layoff, and more. Type `/` in Claude to see all of them.

## How it compares

[ai-job-search](https://github.com/MadsLorentzen/ai-job-search) and [career-ops](https://github.com/career-ops-hq/career-ops) are outstanding, and if you live in a terminal you should look at both. This project exists for everyone else.

| | ai-job-search | career-ops | Job Search AI Operating System |
|---|---|---|---|
| Runs in | Claude Code (fork the repo) | Claude Code, Codex, OpenCode, Antigravity (npm) | The Claude app (desktop or web) via plugin |
| Setup | git, Node, LaTeX, edit config files | npm init, YAML config, markdown CV | Three clicks, then paste your resume |
| Job portal scanning | Yes (scrapers) | Yes (many portals, zero-token triage) | No: you bring the posting |
| CV output | LaTeX / PDF templates | ATS PDF, LaTeX, markdown | .docx and .pdf in your Project or Drive |
| Email, calendar, files | No | No (draft-only, never sends) | Drafts into your own Gmail, Calendar, Drive, behind approval |
| Evaluation rubric | Company research checklist | A to H report, 1 to 5 score | Floor check + posting decode; no numeric score |
| Interview prep | Yes | Yes, with practice and debrief modes | Yes, by round, from your Story Bank |
| Negotiation | Salary benchmarking | Offer prep | Floor-protected script, counter-offer handler, offer worksheet |
| Guardrails | Profile-driven | Story provenance (no invented numbers) | Floor, defensibility, no invention, AI-register tells stripped |
| Profession focus | General, technical-leaning | Tech archetypes (LLMOps, Agentic, PM, SA, FDE, …) | Profession archetype registry (nurses, teachers, bookkeepers, …), see below |
| Cost to run | Free tiers possible | Free tiers possible | Needs a paid Claude plan (plugins are not on Free) |
| Licence | MIT | MIT | MIT |

Honest summary: they scan and score more; this one lives where non-developers already work and drafts into the tools they already use.

## Profession archetypes (contributions wanted)

career-ops ships archetypes for a handful of tech roles. This registry is for everyone else.

An archetype is a short, hedged brief the **Tailor & apply** job reads when you name your profession: the titles hiring teams actually use, where postings tend to live, what a recruiter screens for first, the story types that land, resume conventions, and red flags in postings. It sharpens the posting decode and the resume ordering. It never puts a claim, a number, or a keyword on your resume that your own record does not support.

Shipped so far: `nurse`, `teacher`, `bookkeeper`, `loan-officer`, `paralegal`, `real-estate-agent`, `social-media-manager`, `personal-trainer`. They live in [`archetypes/`](./archetypes) (and inside the plugin, next to the skill that reads them).

Know a profession well? Copy [`archetypes/_template.md`](./archetypes/_template.md), keep every line hedged and short, cite an official body for anything about licensing, and open a pull request or an [archetype request issue](../../issues/new?template=profession-archetype.md). See [CONTRIBUTING.md](./CONTRIBUTING.md).

## Fork and own it

This is a GitHub template repository: **Use this template → Create a new repository** gives you your own copy to edit. Skills are plain markdown (`SKILL.md` files); change the voice, the floor rules, the job steps, or add your own archetype, then install your fork the same three-click way with your own `owner/repo`.

Or don't fork at all: once installed, ask Claude inside your Project to change a skill ("make the cover letter shorter and never mention pay") and it edits the plugin conversationally.

## What it will not do

- Send an email, submit an application, accept or decline an offer, or click anything on your behalf.
- Invent a metric, a title, a date, or an employer. Anything without a source in your record is marked `[confirm]`.
- Give legal, tax, or salary advice. Separation agreements, equity, and non-competes get a "worth a professional's eyes" line, not an answer.
- Touch an employer's mailbox or Drive. Personal accounts only.
- Run without a paid Claude plan. Plugins are not available on Claude Free.

## Repo layout

```
job-search-os/          the plugin (30 skills), installable as-is
.claude-plugin/         marketplace.json so this repo is its own marketplace
archetypes/             the profession archetype registry
CONTRIBUTING.md         how to add an archetype or improve a skill
```

The plugin folder is mirrored from the private build repo on every release, so open issues here and pull requests against `archetypes/`; skill changes are folded upstream and land in the next mirror.

## Acknowledgements

- [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) for showing that a whole job search can live in Claude Code.
- [career-ops-hq/career-ops](https://github.com/career-ops-hq/career-ops) for the A to H rubric, story provenance, and the archetype idea this registry extends.
- Everyone who sends an archetype for a profession the tech world forgets.

## Licence

MIT. See [LICENSE](./LICENSE).

— [The AI Career Lab](https://theaicareerlab.com)
