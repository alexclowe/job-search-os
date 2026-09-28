# Profession archetype registry

An archetype is a short, hedged brief for one profession. Every job reads it when you name your profession: Tailor & apply to decode a posting and order a resume, Prep for an interview to shape the brief for how that profession interviews, Follow up & negotiate for how pay is structured and what's usually negotiable, and the weekly review for where the postings live. It never puts a claim, a number, or a keyword on a resume that your own record does not support.

career-ops ships archetypes for a handful of technical roles. This registry is for everyone else.

| Slug | Profession | Aliases the file also covers |
|---|---|---|
| [`nurse`](./nurse.md) | Nurse | RN, NP, LPN/LVN (adjacent), staff nurse, charge nurse |
| [`teacher`](./teacher.md) | Teacher | classroom teacher, specialist, instructional coach |
| [`bookkeeper`](./bookkeeper.md) | Bookkeeper | full-charge bookkeeper, accounting clerk, AP/AR |
| [`loan-officer`](./loan-officer.md) | Loan officer | mortgage loan originator, MLO |
| [`paralegal`](./paralegal.md) | Paralegal | legal assistant, litigation support |
| [`real-estate-agent`](./real-estate-agent.md) | Real estate agent | Realtor, buyer's agent, listing agent |
| [`social-media-manager`](./social-media-manager.md) | Social media manager | community manager, content manager |
| [`personal-trainer`](./personal-trainer.md) | Personal trainer | fitness coach, group fitness instructor |

Each file follows [`_template.md`](./_template.md): target titles, where the postings live, what a recruiter screens for first, story types that land, resume conventions, how interviews usually run, how pay is usually structured, what's usually negotiable, red flags in postings, and where to verify licensing rules.

## Add one

1. Copy `_template.md` to `<profession-slug>.md` (lowercase, hyphens).
2. Fill every section. Short lines, hedged language, no statistics, no salary figures, no named employers. Licensing claims name the official body.
3. Run `python3 scripts/validate.py` from the repo root.
4. Open a pull request titled `archetype: <profession>` and say in one line what your connection to the profession is.

Accepted archetypes are folded into the plugin source so they ship inside the plugin as well as here. See [CONTRIBUTING.md](../CONTRIBUTING.md).
