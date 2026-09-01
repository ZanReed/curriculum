#!/usr/bin/env python3
"""Check 4: referential integrity of the graph and its registries.

Graph-internal assertions (implemented, run everywhere):
  A. every skill prereq resolves to a skill id or an external-prereq id
  B. every misconception reference on a skill resolves to the taxonomy
  C. no misconception in the taxonomy is attached to zero skills
  D. the chunking plan's skill set equals the graph's skill set (both ways)
  E. every skill declares an integer `parts` >= 1 (the burndown denominator)

Registry cross-assertions (BOUND AFTER SEED — fail red until then):
  F. every id in skill-registry.txt / misconception-registry.txt /
     external-prereq-registry.txt exists in the graph
  G. the declared parts total in skill-registry.txt equals sum(parts)

F and G need the real registry format to parse; guessing a format risks an
extractor that silently matches nothing and passes vacuously. Until they are
bound to the seeded files, they FAIL with NOT-BOUND — a red that names its
own fix, never a skip. When binding them, keep the non-vacuity guard: an
extraction that yields zero ids is itself a failure.

Usage: check_integrity.py <graph.json>
"""

import json
import sys
from pathlib import Path

REGISTRIES = ("skill-registry.txt", "misconception-registry.txt",
              "external-prereq-registry.txt")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__, file=sys.stderr)
        return 2
    graph_path = Path(sys.argv[1])
    if not graph_path.exists():
        print(f"check 4 FAIL: missing graph {graph_path}", file=sys.stderr)
        return 1
    doc = json.loads(graph_path.read_text(encoding="utf-8"))

    failures: list[str] = []

    def need(key: str, kind: type) -> object:
        val = doc.get(key)
        if not isinstance(val, kind):
            failures.append(f"graph shape: `{key}` missing or not "
                            f"{kind.__name__} — shape changed; update this "
                            "script deliberately")
        return val if isinstance(val, kind) else kind()

    skills = need("skills", list)
    misconceptions = need("misconceptions", list)
    external = need("external_prereqs", list)
    plan = need("chunking_plan", dict)

    skill_ids = {s.get("id") for s in skills if isinstance(s, dict)}
    mis_ids = {m.get("id") for m in misconceptions if isinstance(m, dict)}
    ext_ids = {e.get("id") for e in external if isinstance(e, dict)}
    for name, ids in (("skills", skill_ids), ("misconceptions", mis_ids),
                      ("external_prereqs", ext_ids)):
        if None in ids:
            failures.append(f"{name}: an entry has no id")
        ids.discard(None)

    # A + B — dangling references off skills
    referenced_mis: set[str] = set()
    for s in skills:
        sid = s.get("id", "<no id>")
        for p in s.get("prereqs", []):
            if p not in skill_ids and p not in ext_ids:
                failures.append(f"A dangling prereq: {sid} -> {p}")
        for m in s.get("misconceptions", []):
            referenced_mis.add(m)
            if m not in mis_ids:
                failures.append(f"B dangling misconception ref: {sid} -> {m}")

    # C — orphan misconceptions
    for m in sorted(mis_ids - referenced_mis):
        failures.append(f"C orphan misconception (attached to no skill): {m}")

    # D — chunking plan covers exactly the graph's skills
    plan_skills: set[str] = set()
    for chain in plan.get("chains", []):
        plan_skills.update(chain.get("skills", []))
    for sid in sorted(plan_skills - skill_ids):
        failures.append(f"D chunking plan names unknown skill: {sid}")
    for sid in sorted(skill_ids - plan_skills):
        failures.append(f"D skill in graph but in no chain: {sid}")

    # E — parts declared everywhere
    partless = sorted(s.get("id", "<no id>") for s in skills
                      if not (isinstance(s.get("parts"), int)
                              and s.get("parts", 0) >= 1))
    for sid in partless:
        failures.append(f"E skill missing integer parts >= 1: {sid}")

    # F + G — registry cross-checks: not bound until the seed lands
    here = graph_path.resolve().parent
    for reg in REGISTRIES:
        if not (here / reg).exists():
            failures.append(f"F missing registry file: {reg}")
    failures.append(
        "F/G NOT-BOUND: registry parsing is not yet implemented — bind it "
        "to the seeded registry format (and keep the zero-ids-extracted "
        "guard) in scripts/check_integrity.py, then delete this line")

    if failures:
        print(f"check 4 FAIL — {len(failures)} finding(s):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"check 4 OK: {len(skill_ids)} skills, {len(mis_ids)} "
          f"misconceptions, {len(ext_ids)} external prereqs, "
          f"{sum(s.get('parts', 0) for s in skills)} parts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
