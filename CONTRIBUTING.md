# Contributing

Thanks for looking. Two kinds of contribution land here.

## 1. Profession archetypes (the most useful thing you can send)

An archetype is a short markdown brief for one profession. Every job reads it when someone names that profession: to decode postings and order a resume, to shape interview prep, to know how pay is usually structured and what's usually negotiable, and to know where the postings live. It never adds a claim or a number to anyone's resume.

**To add one**

1. Copy [`archetypes/_template.md`](./archetypes/_template.md) to `archetypes/<profession-slug>.md` (lowercase, hyphens: `dental-hygienist.md`).
2. Fill every section. Keep lines short and hedged: "tend to", "often", "where the employer expects it". You are describing a market, not promising one.
3. **Write no numbers and name no employers.** Leave the three generated blocks from the template (facts, canada, sources) empty; the maintainers fill pay, openings, and entry education from public BLS and O\*NET data when your archetype is folded in. Archetypes are published under CC BY 4.0 (see `archetypes/NOTICE.md`), and by contributing you agree to that.
4. Licensing and credential claims must name the official body (a state board, a certifying organisation), not a blog.
5. Open a pull request titled `archetype: <profession>`. Say in one line what your connection to the profession is (you do it, you hire for it, you recruit for it).

We fold accepted archetypes into the plugin's source so they ship inside the plugin as well as in `archetypes/`.

**Don't know the profession well enough to write it?** Open an [archetype request](https://github.com/alexclowe/job-search-os/issues/new?template=profession-archetype.yml) with what you do know.

**Before you open the pull request,** run `python3 scripts/validate.py` from the repo root. It checks the slug line, the required sections, the generated-block markers, and that no figures slipped in outside them; the same check runs in CI on every pull request.

## 2. Skill improvements

The plugin folder is mirrored from a private build repository, so a pull request that edits `job-search-os/` directly cannot be merged as-is. Instead:

- Open a [skill idea issue](https://github.com/alexclowe/job-search-os/issues/new?template=skill-idea.yml) describing the change and, if you can, paste the edited `SKILL.md` section. We fold accepted changes upstream and they arrive with the next mirror.
- Or fork this repo (it is a template), make the change in your copy, and install your fork. If it works better, tell us in an issue.

## Ground rules

- Plain language. No marketing adjectives in skills or archetypes.
- Nothing that sends, submits, accepts, or declines on a user's behalf. Drafts only, behind approval.
- Nothing that fabricates. Every figure a skill produces must trace to the user's own record or be marked `[confirm]`.
- Be kind in issues. Everyone here is either job hunting or helping someone who is.
