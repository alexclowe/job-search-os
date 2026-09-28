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
  3. Every archetypes/*.md (except _template.md and README.md) carries the
     required sections, a Slug line that matches its filename, and no dollar
     figures.
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
    "## Red flags in postings",
    "## Verify before relying on this",
]

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
    count = 0
    for md in sorted(folder.glob("*.md")):
        if md.name in {"_template.md", "README.md"}:
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
        if re.search(r"\$\s?\d", text):
            fail(f"{rel}: contains a dollar figure (archetypes carry no salary numbers)")
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
