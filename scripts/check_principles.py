#!/usr/bin/env python3
"""Check 1: the graph's `authoring_principles` field is byte-identical to
authoring-principles.md.

Single-source rule (author-ruled 2026-09-02): the .md is the ONLY edit
surface for the pedagogy prose. The field stays in the graph so a drafting
session still loads exactly one file, but it is machine-written — run this
script with --fix after editing the .md. CI runs it without --fix, so a
hand-edited field and a forgotten sync both land red, and a red build has
one fix (re-run with --fix), never a which-copy-is-right adjudication.

Usage:
    check_principles.py <graph.json> <principles.md>          # verify (CI)
    check_principles.py <graph.json> <principles.md> --fix    # sync .md -> graph

--fix rewrites the graph with json.dumps(indent=2, ensure_ascii=False) plus
a trailing newline, which round-trips the builder's output byte-identically
(verified against the graph file 2026-09-02). If a future graph fails the
round-trip, --fix refuses rather than reformat the whole file.
"""

import json
import sys
from pathlib import Path

FIELD = "authoring_principles"


def main() -> int:
    args = [a for a in sys.argv[1:] if a != "--fix"]
    fix = "--fix" in sys.argv[1:]
    if len(args) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    graph_path, md_path = Path(args[0]), Path(args[1])
    for p in (graph_path, md_path):
        if not p.exists():
            print(f"check 1 FAIL: missing input {p}", file=sys.stderr)
            return 1

    raw = graph_path.read_bytes()
    doc = json.loads(raw)
    if FIELD not in doc:
        print(f"check 1 FAIL: graph has no `{FIELD}` field — the shape "
              "changed; update this script deliberately.", file=sys.stderr)
        return 1

    prose = md_path.read_text(encoding="utf-8")
    if doc[FIELD] == prose:
        print("check 1 OK: authoring_principles is byte-identical to "
              f"{md_path.name}")
        return 0

    if not fix:
        print(f"check 1 FAIL: `{FIELD}` in {graph_path.name} differs from "
              f"{md_path.name}.\n  The .md is the source; run\n"
              f"    python3 scripts/check_principles.py {graph_path.name} "
              f"{md_path.name} --fix\n"
              "  and commit the result. Never edit the JSON field by hand.",
              file=sys.stderr)
        return 1

    # Formatting-safety gate: only rewrite a file our serializer round-trips.
    if (json.dumps(doc, indent=2, ensure_ascii=False) + "\n").encode("utf-8") != raw:
        print("check 1 FAIL: --fix refused — this serializer does not "
              "round-trip the graph byte-identically, so rewriting would "
              "produce formatting noise. Sync the field another way or "
              "update this script.", file=sys.stderr)
        return 1

    doc[FIELD] = prose
    graph_path.write_text(json.dumps(doc, indent=2, ensure_ascii=False) + "\n",
                          encoding="utf-8")
    print(f"check 1: rewrote `{FIELD}` in {graph_path.name} from {md_path.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
