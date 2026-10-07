#!/usr/bin/env python3
"""Teacher-guide check (D50): every catalogue activity carries a well-formed guide.

Run against the catalogue folder before every batch import (the catalogue has no
CI of its own); this repo's CI runs it against tests/fixtures/guides-catalogue so
the script can't rot.

Activities are found the way the platform's importer finds them: every .md file
(case-insensitive) under the catalogue root, skipping any file or folder whose
name starts with '.'. A file is an activity when its ```meta fence has a `key:`.
The guide is the activity's ```teacher-guide fence (D50 amendment 2026-10-07;
`teacher_guide.home`). The platform checks only that the fence parses; the
rules below are this side's.

Assertions:
  A. every activity has exactly one ```teacher-guide fence, and it comes last
     in the file; no .guides/ folder is left in the catalogue (the interim home
     is retired)
  C. the guide's `## ` headings are the sections `teacher_guide.sections` names,
     in that order and only those; `marking` is present exactly when the
     activity carries a rubric (`teacher_guide.conditional_sections`). An
     assessment file (```meta `type:` in `teacher_guide.assessment_types`, D51)
     takes `assessment_sections` instead, with `practice link` on quizzes only
  D. the guide's body is at most `teacher_guide.max_words` words
     (`assessment_max_words` for an assessment file)
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

META_KEY = re.compile(r"^key:\s*(\S+)\s*$", re.M)
META_TYPE = re.compile(r"^type:\s*(\S+)\s*$", re.M)
META_FENCE = re.compile(r"^```meta\n(.*?)^```", re.M | re.S)
GUIDE_FENCE = re.compile(r"^```teacher-guide[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)
RUBRIC = re.compile(r"^rubric:", re.M)
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
    assessment_types = set(tg["assessment_types"])
    assessment_sections = [s.lower() for s in tg["assessment_sections"]]
    assessment_max_words = tg["assessment_max_words"]
    quiz_only = {s.lower() for s in tg.get("assessment_conditional_sections", {})}

    root = args.catalogue
    errors: list[str] = []
    if (root / ".guides").exists():
        errors.append("A: .guides/ still exists; guides live in each activity's ```teacher-guide fence")

    keys: dict[str, Path] = {}
    for path in walk(root):
        text = path.read_text()
        meta = META_FENCE.search(text)
        key = META_KEY.search(meta.group(1)) if meta else None
        if not key:
            continue  # not an activity file (no meta key)
        rel = path.relative_to(root)
        if key.group(1) in keys:
            errors.append(f"{rel}: duplicate activity key {key.group(1)} (also {keys[key.group(1)]})")
        keys[key.group(1)] = rel

        fences = list(GUIDE_FENCE.finditer(text))
        if not fences:
            errors.append(f"A: {rel}: no ```teacher-guide fence")
            continue
        if len(fences) > 1:
            errors.append(f"A: {rel}: {len(fences)} ```teacher-guide fences; exactly one")
        guide = fences[0]
        if text[guide.end():].strip():
            errors.append(f"A: {rel}: the ```teacher-guide fence must be last in the file")

        body = guide.group(1)
        without_guide = text[: guide.start()] + text[guide.end():]
        has_rubric = bool(RUBRIC.search(without_guide))

        kind = META_TYPE.search(meta.group(1))
        kind = kind.group(1) if kind else None
        if kind in assessment_types:
            want = [s for s in assessment_sections if s not in quiz_only or kind == "quiz"]
            cap = assessment_max_words
        else:
            want = [s for s in sections if s not in conditional or has_rubric]
            cap = max_words
        got = [h.lower() for h in HEADING.findall(body)]
        if got != want:
            errors.append(f"C: {rel}: sections {got}, expected {want}")

        words = len(body.split())
        if words > cap:
            errors.append(f"D: {rel}: guide is {words} words, cap is {cap} (teacher_guide)")

        if CITATION.search(body):
            errors.append(f"E: {rel}: rule citation (§ or D-number) in a guide")
        if "[[" in body:
            errors.append(f"E: {rel}: [[term]] markup in a guide")

    if not keys:
        print(f"FAIL: no activities found under {root} (vacuity guard)")
        return 1

    for e in errors:
        print("FAIL:", e)
    if errors:
        return 1
    print(f"OK: {len(keys)} activities, each with its teacher guide")
    return 0


if __name__ == "__main__":
    sys.exit(main())
