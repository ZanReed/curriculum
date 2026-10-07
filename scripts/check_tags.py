#!/usr/bin/env python3
"""Tag check (D52): every catalogue activity's `tags:` are glossary terms.

Run against the catalogue folder before every batch import, beside check_guides.py
(the catalogue has no CI of its own); this repo's CI runs it against
tests/fixtures/guides-catalogue so the script can't rot.

Activities are found the way the platform's importer finds them (dot entries
skipped, .md matched case-insensitively, `key:` in ```meta). Assessment files
(`type:` in `teacher_guide.assessment_types`) are skipped: the Activity Bank never
lists them (D51 ruling 12), so their tags are never shown.

Assertions:
  A. the activity has a `tags:` line in its ```meta fence
  B. it has between `tags.min` and `tags.max` tags, with no repeats
  C. every tag is a `term:` in glossary.md, written exactly as the glossary writes it

The bounds are read from the graph, never restated (D25).
Non-vacuity guard: a catalogue with no activities, or a glossary with no terms, fails.

Usage: check_tags.py <catalogue> --graph <graph.json> --glossary <glossary.md>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

META_FENCE = re.compile(r"^```meta\n(.*?)^```", re.M | re.S)
META_KEY = re.compile(r"^key:\s*(\S+)\s*$", re.M)
META_TYPE = re.compile(r"^type:\s*(\S+)\s*$", re.M)
META_TAGS = re.compile(r"^tags:\s*(.*?)\s*$", re.M)
TERM = re.compile(r"^term:\s*(.+?)\s*$", re.M)


def walk(root: Path):
    """Yield .md files under root, skipping dot entries at every depth (as the importer does)."""
    for entry in sorted(root.iterdir()):
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            yield from walk(entry)
        elif entry.name.lower().endswith(".md"):
            yield entry


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("catalogue", type=Path)
    ap.add_argument("--graph", type=Path, required=True)
    ap.add_argument("--glossary", type=Path, required=True)
    args = ap.parse_args()

    defaults = json.loads(args.graph.read_text())["activity_defaults"]
    lo, hi = defaults["tags"]["min"], defaults["tags"]["max"]
    skip_types = set(defaults["teacher_guide"]["assessment_types"])
    terms = set(TERM.findall(args.glossary.read_text()))
    if not terms:
        print(f"FAIL: no glossary terms found in {args.glossary} (vacuity guard)")
        return 1

    errors: list[str] = []
    checked = 0
    for path in walk(args.catalogue):
        meta = META_FENCE.search(path.read_text())
        if not meta or not META_KEY.search(meta.group(1)):
            continue
        kind = META_TYPE.search(meta.group(1))
        if kind and kind.group(1) in skip_types:
            continue
        checked += 1
        rel = path.relative_to(args.catalogue)
        line = META_TAGS.search(meta.group(1))
        if not line:
            errors.append(f"A: {rel}: no tags: line")
            continue
        tags = [t.strip() for t in line.group(1).split(",") if t.strip()]
        if not lo <= len(tags) <= hi:
            errors.append(f"B: {rel}: {len(tags)} tags, expected {lo}-{hi} (activity_defaults.tags)")
        if len(set(tags)) != len(tags):
            errors.append(f"B: {rel}: a tag is repeated")
        for t in tags:
            if t not in terms:
                errors.append(f"C: {rel}: tag {t!r} is not a glossary term")

    if not checked:
        print(f"FAIL: no activities found under {args.catalogue} (vacuity guard)")
        return 1
    for e in errors:
        print("FAIL:", e)
    if errors:
        return 1
    print(f"OK: {checked} activities, every tag a glossary term")
    return 0


if __name__ == "__main__":
    sys.exit(main())
