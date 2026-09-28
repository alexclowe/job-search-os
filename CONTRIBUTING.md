# Contributing

Thanks for looking. Two kinds of contribution land here.

## 1. Profession archetypes (the most useful thing you can send)

An archetype is a short markdown brief for one profession. The **Tailor & apply** job reads it when someone names that profession, to sharpen how it decodes a posting and orders a resume. It never adds a claim to anyone's resume.

**To add one**

1. Copy [`archetypes/_template.md`](./archetypes/_template.md) to `archetypes/<profession-slug>.md` (lowercase, hyphens: `dental-hygienist.md`).
2. Fill every section. Keep lines short and hedged: "tend to", "often", "where the employer expects it". You are describing a market, not promising one.
3. **No statistics, no salary figures, no named employers.** If a number matters, point to the official body where it can be verified instead of quoting it.
4. Licensing and credential claims must name the official body (a state board, a certifying organisation), not a blog.
5. Open a pull request titled `archetype: <profession>`. Say in one line what your connection to the profession is (you do it, you hire for it, you recruit for it).

We fold accepted archetypes into the plugin's source so they ship inside the plugin as well as in `archetypes/`.

**Don't know the profession well enough to write it?** Open an [archetype request](https://github.com/alexclowe/job-search-os/issues/new?template=profession-archetype.yml) with what you do know.

**Before you open the pull request,** run `python3 scripts/validate.py` from the repo root. It checks the slug line, the required sections, and that no dollar figures slipped in; the same check runs in CI on every pull request.

## 2. Skill improvements

The plugin folder is mirrored from a private build repository, so a pull request that edits `job-search-os/` directly cannot be merged as-is. Instead:

- Open a [skill idea issue](https://github.com/alexclowe/job-search-os/issues/new?template=skill-idea.yml) describing the change and, if you can, paste the edited `SKILL.md` section. We fold accepted changes upstream and they arrive with the next mirror.
- Or fork this repo (it is a template), make the change in your copy, and install your fork. If it works better, tell us in an issue.

## Ground rules

- Plain language. No marketing adjectives in skills or archetypes.
- Nothing that sends, submits, accepts, or declines on a user's behalf. Drafts only, behind approval.
- Nothing that fabricates. Every figure a skill produces must trace to the user's own record or be marked `[confirm]`.
- Be kind in issues. Everyone here is either job hunting or helping someone who is.
