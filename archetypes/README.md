# Profession archetype registry

An archetype is a short, hedged brief for one profession. Every job reads it when you name your profession: Tailor & apply to decode a posting and order a resume, Prep for an interview to shape the brief for how that profession interviews, Follow up & negotiate for how pay is structured and what's usually negotiable, and the weekly review for where the postings live. It never puts a claim, a number, or a keyword on a resume that your own record does not support.

career-ops ships archetypes for a handful of technical roles. This registry is for everyone else.

**Every archetype, with the names and aliases it covers, is listed in [`index.md`](./index.md).** That index is generated from the maintainers' archetype list on every release, so it is always the complete, current set; the plugin's jobs read it first to find the right file.

Each file follows [`_template.md`](./_template.md): target titles, where the postings live, what a recruiter screens for first, story types that land, resume conventions, how interviews usually run, how pay is usually structured (with US pay and openings from public BLS data), what's usually negotiable, red flags in postings, where to verify licensing rules, what differs in Canada, and its sources.

## Add one

1. Copy `_template.md` to `<profession-slug>.md` (lowercase, hyphens).
2. Fill every section. Short lines, hedged language, no named employers, and write no numbers yourself: leave the three generated blocks (facts, canada, sources) empty, and the maintainers fill pay, openings, and entry education from public BLS and O\*NET data when they fold your archetype in. Licensing claims name the official body.
3. Run `python3 scripts/validate.py` from the repo root.
4. Open a pull request titled `archetype: <profession>` and say in one line what your connection to the profession is.

Accepted archetypes are folded into the plugin source so they ship inside the plugin as well as here. See [CONTRIBUTING.md](../CONTRIBUTING.md).

## Licence

The archetypes in this folder are licensed **CC BY 4.0** ([`LICENSE`](./LICENSE)); the rest of the repository is MIT. They use data from the U.S. Bureau of Labor Statistics and the O\*NET® 31.0 Database (CC BY 4.0); the credits and what we changed are in [`NOTICE.md`](./NOTICE.md). By contributing an archetype you agree it is published under CC BY 4.0.
