#!/usr/bin/env python3
"""Teacher-guide check (D50): every catalogue activity has a well-formed guide.

Run against the catalogue folder before every batch import (the catalogue has no
CI of its own); this repo's CI runs it against tests/fixtures/guides-catalogue so
the script can't rot.

Activities are found the way the platform's importer finds them: every .md file
under the catalogue root, skipping any file or folder whose name starts with '.'.
An activity's key is the `key:` line of its ```meta fence, and its chain folder is
the first segment of its path (the importer's chainFolderOf). Its guide lives at
.guides/<chain folder>/<activity key>.md (`teacher_guide.home_until_platform_field`).

Assertions:
  A. every activity has a guide at its path, and every guide has an activity
  B. a guide opens with front matter whose `activity:` equals its file name
  C. a guide's `## ` headings are the sections `teacher_guide.sections` names,
     in that order and only those; `marking` is present exactly when the
     activity carries a rubric (`teacher_guide.conditional_sections`)
  D. a guide's body (everything after the front matter) is at most
     `teacher_guide.max_words` words
  E. no rule citations (§-numbers, D-numbers) and no [[term]] markup (D50 ruling 5)

The sections and the cap are read from the graph, never restated (D25).
Non-vacuity guard: a catalogue with no activities is a failure.

Usage: check_guides.py <catalogue> --graph <graph.json>
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

GUIDES_DIR = ".guides"
META_KEY = re.compile(r"^key:\s*(\S+)\s*$", re.M)
META_FENCE = re.compile(r"^```meta\n(.*?)^```", re.M | re.S)
RUBRIC = re.compile(r"^rubric:", re.M)
FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)
ACTIVITY = re.compile(r"^activity:\s*(\S+)\s*$", re.M)
HEADING = re.compile(r"^## (.+?)\s*$", re.M)
CITATION = re.compile(r"§\s*\d|\bD\d+\b")


def walk(root: Path):
    """Yield .md files under root, skipping dot entries at every depth (as the importer does)."""
    for entry in sorted(root.iterdir()):
        if entry.name.startswith("."):
            continue
        if entry.is_dir():
            yield from walk(entry)
        elif entry.name.lower().endswith(".md"):  # case-insensitive, as batch-import.mjs
            yield entry


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("catalogue", type=Path)
    ap.add_argument("--graph", type=Path, required=True)
    args = ap.parse_args()

    tg = json.loads(args.graph.read_text())["activity_defaults"]["teacher_guide"]
    sections = [s.lower() for s in tg["sections"]]
    conditional = {s.lower() for s in tg.get("conditional_sections", {})}
    max_words = tg["max_words"]

    root = args.catalogue
    errors: list[str] = []

    # activity key -> (chain folder, has rubric)
    activities: dict[str, tuple[str, bool]] = {}
    for path in walk(root):
        text = path.read_text()
        meta = META_FENCE.search(text)
        key = META_KEY.search(meta.group(1)) if meta else None
        if not key:
            continue  # not an activity file (no meta key)
        chain = path.relative_to(root).parts[0]  # first path segment, as chainFolderOf
        if key.group(1) in activities:
            errors.append(f"{path.relative_to(root)}: duplicate activity key {key.group(1)}")
        activities[key.group(1)] = (chain, bool(RUBRIC.search(text)))

    if not activities:
        print(f"FAIL: no activities found under {root} (vacuity guard)")
        return 1

    expected = {Path(GUIDES_DIR, chain, f"{key}.md"): key for key, (chain, _) in activities.items()}
    guides_root = root / GUIDES_DIR
    found = {p.relative_to(root) for p in guides_root.rglob("*.md")} if guides_root.is_dir() else set()

    for rel in sorted(expected.keys() - found):
        errors.append(f"A: activity {expected[rel]} has no guide at {rel}")
    for rel in sorted(found - expected.keys()):
        errors.append(f"A: guide {rel} has no activity at that chain folder and key")

    for rel in sorted(found & expected.keys()):
        key = expected[rel]
        has_rubric = activities[key][1]
        text = (root / rel).read_text()
        front = FRONT.match(text)
        if not front:
            errors.append(f"B: {rel}: no front matter")
            continue
        act = ACTIVITY.search(front.group(1))
        if not act or act.group(1) != key:
            errors.append(f"B: {rel}: activity: line must be {key}")
        body = text[front.end():]

        want = [s for s in sections if s not in conditional or has_rubric]
        got = [h.lower() for h in HEADING.findall(body)]
        if got != want:
            errors.append(f"C: {rel}: sections {got}, expected {want}")

        words = len(body.split())
        if words > max_words:
            errors.append(f"D: {rel}: {words} words, cap is teacher_guide.max_words ({max_words})")

        if CITATION.search(body):
            errors.append(f"E: {rel}: rule citation (§ or D-number) in a guide")
        if "[[" in body:
            errors.append(f"E: {rel}: [[term]] markup in a guide")

    for e in errors:
        print("FAIL:", e)
    if errors:
        return 1
    print(f"OK: {len(activities)} activities, {len(found)} guides")
    return 0


if __name__ == "__main__":
    sys.exit(main())
