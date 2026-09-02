#!/usr/bin/env python3
"""Check 4: referential integrity of the graph and its registries.

Graph-internal assertions:
  A. every skill prereq resolves to a skill id or an external-prereq id
  B. every misconception reference on a skill resolves to the taxonomy
  C. no misconception in the taxonomy is attached to zero skills
  D. the chunking plan's skill set equals the graph's skill set (both ways)
  E. `parts`, where declared, is an integer >= 1 (absent means 1 — only
     multi-part skills declare it; generate-registries.py reads it the same way)

Registry cross-assertions (bound to the seeded v0.13.0 format):
  F. every id in skill-registry.txt / misconception-registry.txt /
     external-prereq-registry.txt exists in the graph, every `= n` in the
     skill registry matches the graph's declared parts, and every
     chain-registry folder name resolves to a chain in the chunking plan
  G. the parts total declared in skill-registry.txt's header equals
     sum(parts) over the graph's skills — the burndown denominator (51 at seed)

Non-vacuity guard: an extraction that yields zero ids from a present registry
is itself a failure — an extractor that silently matches nothing would pass
while checking nothing.

Usage: check_integrity.py <graph.json>
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REGISTRIES = ("skill-registry.txt", "misconception-registry.txt",
              "external-prereq-registry.txt")


def registry_rows(path: Path) -> list[tuple[str, int | None]]:
    """Parse `id` / `id = n` rows, comments stripped. Returns (id, n|None)."""
    rows = []
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        m = re.fullmatch(r"(\S+)(?:\s*=\s*(\d+))?", line)
        if m:
            rows.append((m.group(1), int(m.group(2)) if m.group(2) else None))
    return rows


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

    # E — parts, where declared, is a sane integer (absent means 1)
    for s in skills:
        if "parts" in s and not (isinstance(s["parts"], int) and s["parts"] >= 1):
            failures.append(f"E skill has non-integer or < 1 parts: "
                            f"{s.get('id', '<no id>')} = {s['parts']!r}")

    # F — every registry id exists in the graph; `= n` matches declared parts
    here = graph_path.resolve().parent
    graph_parts = {s.get("id"): s.get("parts", 1) for s in skills}
    for reg, ids in ((REGISTRIES[0], skill_ids), (REGISTRIES[1], mis_ids),
                     (REGISTRIES[2], ext_ids)):
        path = here / reg
        if not path.exists():
            failures.append(f"F missing registry file: {reg}")
            continue
        rows = registry_rows(path)
        if not rows:
            failures.append(f"F extracted zero ids from {reg} — format "
                            "changed; rebind registry_rows() deliberately")
            continue
        for rid, n in rows:
            if rid not in ids:
                failures.append(f"F registry id not in graph: {reg}: {rid}")
            elif reg == REGISTRIES[0] and n is not None and graph_parts.get(rid, 1) != n:
                failures.append(f"F parts mismatch: {reg} declares {rid} = {n}, "
                                f"graph says {graph_parts.get(rid, 1)}")

    # F (chain registry, hand-maintained) — folder names resolve to chains
    chain_ids = {c.get("chain_id") for c in plan.get("chains", [])}
    chain_reg = here / "chain-registry.txt"
    if chain_reg.exists():
        # Rows are `NN-chain.x.y = Display Title`; the folder name is the LHS.
        folders = []
        for raw in chain_reg.read_text(encoding="utf-8").splitlines():
            line = raw.split("#", 1)[0].strip()
            if line and "=" in line:
                folders.append(line.split("=", 1)[0].strip())
        if not folders:
            failures.append("F extracted zero entries from chain-registry.txt")
        for folder in folders:
            if re.sub(r"^\d+-", "", folder) not in chain_ids:
                failures.append(f"F chain-registry folder names unknown chain: {folder}")
    else:
        failures.append("F missing registry file: chain-registry.txt")

    # G — the skill registry's declared parts total equals the graph's sum
    total = sum(s.get("parts", 1) for s in skills)
    if (here / REGISTRIES[0]).exists():
        header = (here / REGISTRIES[0]).read_text(encoding="utf-8")
        m = re.search(r"(\d+)\s+parts", header)
        if not m:
            failures.append(f"G no 'N parts' declaration found in "
                            f"{REGISTRIES[0]}'s header")
        elif int(m.group(1)) != total:
            failures.append(f"G parts total: {REGISTRIES[0]} declares "
                            f"{m.group(1)}, graph sums to {total}")

    if failures:
        print(f"check 4 FAIL — {len(failures)} finding(s):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"check 4 OK: {len(skill_ids)} skills, {len(mis_ids)} "
          f"misconceptions, {len(ext_ids)} external prereqs, "
          f"{total} parts")
    return 0


if __name__ == "__main__":
    sys.exit(main())
