#!/usr/bin/env python3
"""Fail if README.md (or any top-level *.md) links to a repo file that does not exist.

External links (http/https/mailto) are left alone; anchors are stripped.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parent.parent
LINK_RE = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
IMG_SRC_RE = re.compile(r"<img[^>]+src=\"([^\"]+)\"")

missing: list[str] = []
checked = 0
for md in sorted(list(ROOT.glob("*.md")) + list((ROOT / "docs").glob("*.md")) + list((ROOT / "archetypes").glob("README.md"))):
    text = md.read_text(encoding="utf-8")
    targets = LINK_RE.findall(text) + IMG_SRC_RE.findall(text)
    for raw in targets:
        target = raw.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        # GitHub-relative issue/discussion shortcuts such as ../../issues/new are routes, not files.
        if target.startswith("../../"):
            continue
        p = (md.parent / target).resolve()
        checked += 1
        if not p.exists():
            missing.append(f"{md.relative_to(ROOT)} -> {raw}")

if missing:
    print("Missing files referenced from markdown:")
    for m in missing:
        print(f"  - {m}")
    sys.exit(1)
print(f"ok: {checked} internal links resolve")
