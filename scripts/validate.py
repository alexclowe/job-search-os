#!/usr/bin/env python3
"""Validate this repository's plugin, marketplace manifest, and archetype registry.

Standalone: no dependencies beyond the Python 3 standard library. Run from the
repo root (or pass the root as the first argument):

    python3 scripts/validate.py

Checks
  1. Every */skills/*/SKILL.md has YAML frontmatter with a `name` that matches
     its folder and a one-line `description` containing no `<` or `>`.
  2. .claude-plugin/marketplace.json parses, every plugin `source` points at a
     folder in this repo that carries .claude-plugin/plugin.json, and the
     manifest's plugin name matches plugin.json.
  3. Every archetypes/*.md (except _template.md, README.md, index.md and
     NOTICE.md) carries the required sections, a Slug line that matches its
     filename, and the three generated-block markers (facts, canada, sources).
     Dollar figures, percentages and thousands-separated numbers may appear
     only inside those generated blocks, which the maintainers fill from
     public BLS and O*NET data; contributors leave them empty. A filled Sources
     block must carry the CC BY 4.0 line, and the verbatim O*NET credit when
     the file is marked "uses: onet".
  4. archetypes/ carries LICENSE (CC BY 4.0) and NOTICE.md, and every
     archetype file is listed in archetypes/index.md.
Exit status is non-zero on any failure; every problem is printed.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent

REQUIRED_ARCHETYPE_SECTIONS = [
    "## Target titles",
    "## Where the postings live",
    "## What a recruiter screens for first",
    "## Story types that land",
    "## Resume conventions",
    "## How interviews usually run",
    "## How pay is usually structured",
    "## What's usually negotiable",
    "## Red flags in postings",
    "## Verify before relying on this",
    "## In Canada",
    "## Sources",
]
NOT_ARCHETYPES = {"_template.md", "README.md", "index.md", "NOTICE.md"}
BLOCKS = {name: re.compile(rf"<!-- {name}:start[^>]*-->\n(.*?)<!-- {name}:end -->", re.S)
          for name in ("facts", "canada", "sources")}
NUMBERS = re.compile(r"\$\s?\d|\d\s?%|\b\d{1,3},\d{3}\b")
ONET_CREDIT = (
    "This page includes information from the O*NET 31.0 Database by the U.S. Department of "
    "Labor, Employment and Training Administration (USDOL/ETA). Used under the CC BY 4.0 "
    "license. O*NET® is a trademark of USDOL/ETA."
)

SLUG_RE = re.compile(r"^\*\*Slug:\*\* `([a-z0-9-]+)`", re.M)

problems: list[str] = []


def fail(msg: str) -> None:
    problems.append(msg)


def parse_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    block = text[4:end]
    fm: dict[str, str] = {}
    current: str | None = None
    for line in block.splitlines():
        m = re.match(r"^([A-Za-z_][\w-]*):\s*(.*)$", line)
        if m:
            current = m.group(1)
            fm[current] = m.group(2)
        elif current and (line.startswith(" ") or line.startswith("\t")):
            fm[current] = (fm[current] + "\n" + line.strip()).strip()
    return fm


def check_skills() -> int:
    count = 0
    for skill_md in sorted(ROOT.glob("*/skills/*/SKILL.md")):
        count += 1
        rel = skill_md.relative_to(ROOT)
        fm = parse_frontmatter(skill_md.read_text(encoding="utf-8"))
        if fm is None:
            fail(f"{rel}: missing YAML frontmatter")
            continue
        name = fm.get("name", "").strip().strip('"').strip("'")
        if not name:
            fail(f"{rel}: frontmatter has no `name`")
        elif name != skill_md.parent.name:
            fail(f"{rel}: name `{name}` does not match folder `{skill_md.parent.name}`")
        desc = fm.get("description", "")
        if not desc.strip():
            fail(f"{rel}: frontmatter has no `description`")
        else:
            if "\n" in desc:
                fail(f"{rel}: description spans more than one line")
            if "<" in desc or ">" in desc:
                fail(f"{rel}: description contains `<` or `>`")
    if count == 0:
        fail("no SKILL.md files found under */skills/*/")
    return count


def check_marketplace() -> None:
    mp = ROOT / ".claude-plugin" / "marketplace.json"
    if not mp.exists():
        fail(".claude-plugin/marketplace.json is missing")
        return
    try:
        doc = json.loads(mp.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        fail(f"marketplace.json does not parse: {e}")
        return
    plugins = doc.get("plugins") or []
    if not plugins:
        fail("marketplace.json lists no plugins")
    for p in plugins:
        src = p.get("source", "")
        if not src.startswith("./"):
            fail(f"marketplace.json: plugin source `{src}` must be a relative path starting with ./")
            continue
        folder = ROOT / src[2:]
        manifest = folder / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            fail(f"marketplace.json: source `{src}` has no .claude-plugin/plugin.json")
            continue
        try:
            pj = json.loads(manifest.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            fail(f"{manifest.relative_to(ROOT)} does not parse: {e}")
            continue
        if pj.get("name") != p.get("name"):
            fail(f"marketplace.json plugin `{p.get('name')}` != plugin.json name `{pj.get('name')}`")
        if not pj.get("version"):
            fail(f"{manifest.relative_to(ROOT)}: no version")


def check_archetypes() -> int:
    folder = ROOT / "archetypes"
    if not folder.exists():
        fail("archetypes/ folder is missing")
        return 0
    for name in ("LICENSE", "NOTICE.md", "index.md"):
        if not (folder / name).exists():
            fail(f"archetypes/{name} is missing")
    index = (folder / "index.md").read_text(encoding="utf-8") if (folder / "index.md").exists() else ""
    listed = set(re.findall(r"^\| `([a-z0-9-]+)\.md` \|", index, re.M))
    count = 0
    for md in sorted(folder.glob("*.md")):
        if md.name in NOT_ARCHETYPES:
            continue
        count += 1
        rel = md.relative_to(ROOT)
        text = md.read_text(encoding="utf-8")
        m = SLUG_RE.search(text)
        if not m:
            fail(f"{rel}: missing `**Slug:** `<slug>`` line")
        elif m.group(1) != md.stem:
            fail(f"{rel}: slug `{m.group(1)}` does not match filename")
        for section in REQUIRED_ARCHETYPE_SECTIONS:
            if not any(line.startswith(section) for line in text.splitlines()):
                fail(f"{rel}: missing section `{section}`")
        outside = text
        for name, rx in BLOCKS.items():
            if not rx.search(text):
                fail(f"{rel}: missing the generated `{name}` block markers (copy them from _template.md)")
            outside = rx.sub("", outside)
        for n in sorted(set(NUMBERS.findall(outside))):
            fail(f"{rel}: figure `{n}` outside the generated blocks (the maintainers add numbers from public data)")
        src = BLOCKS["sources"].search(text)
        if src and src.group(1).strip():
            if "licensed CC BY 4.0" not in src.group(1):
                fail(f"{rel}: Sources block lacks the CC BY 4.0 licence line")
            if "<!-- uses: onet -->" in text and ONET_CREDIT not in src.group(1):
                fail(f"{rel}: marked `uses: onet` but the Sources block lacks the O*NET credit")
        also = re.search(r"^\*\*Also read:\*\*\s*(.*)$", text, re.M)
        if not also:
            fail(f"{rel}: missing `**Also read:**` line")
        elif also.group(1).strip() != "none" and not re.fullmatch(r"`[a-z0-9-]+`(, `[a-z0-9-]+`)*", also.group(1).strip()):
            fail(f"{rel}: Also read must be `slug` references separated by commas (or none), no other text")
        canada = BLOCKS["canada"].search(text)
        if canada and canada.group(1).strip() and "no clear match" not in canada.group(1):
            m = re.search(r"\*\*NOC 2021:\*\* (?:possibly )?(.+?)(?:\.|,) ", canada.group(1))
            codes = re.split(r" or |; ", m.group(1)) if m else []
            if not codes or not all(re.fullmatch(r"\d{5}", c) for c in codes):
                fail(f"{rel}: the NOC line must list only 5-digit unit groups")
        if listed and md.stem not in listed:
            fail(f"{rel}: not listed in archetypes/index.md")
    return count


def main() -> int:
    skills = check_skills()
    check_marketplace()
    archetypes = check_archetypes()
    if problems:
        print(f"x {len(problems)} problem(s):")
        for p in problems:
            print(f"  - {p}")
        return 1
    print(f"ok: {skills} skills, marketplace manifest, and {archetypes} archetypes validated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
