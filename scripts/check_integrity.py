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

Thread structure (D39):
  H. a top-level `threads` registry exists, each entry has an id and a label, ids
     are unique, every chunking-plan chain carries a `thread` that resolves to it,
     and the retired top-level `thread_id` is absent

Retired external prereqs (D45):
  I. no id in external-prereq-retired.txt appears as an external prereq or as a
     skill prereq; the ledger must exist and yield at least one id

Retired skills (D48 note, 2026-10-06):
  J. no id in skill-ids-retired.txt appears as a skill, a prereq or a chunking-plan
     entry; the ledger must exist and yield at least one id

Reporting strands (D51):
  K. every thread's `strand` is null or one of `assessment.reporting.strands`, as is
     any skill's own `strand`; every Y7–Y10 skill resolves a strand (its own, else its
     thread's); where a skill has NZC phase statements, the resolved strand is one of
     theirs

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

    # H — thread structure (D39). Skills carry no thread: it is derived from the chain.
    threads = need("threads", list)
    thread_ids = [t.get("id") for t in threads if isinstance(t, dict)]
    for t in threads:
        if not (isinstance(t, dict) and t.get("id") and t.get("label")):
            failures.append(f"H thread entry needs an id and a label: {t!r}")
    for tid in {t for t in thread_ids if thread_ids.count(t) > 1}:
        failures.append(f"H duplicate thread id: {tid}")
    if threads and not thread_ids:
        failures.append("H extracted zero thread ids from a present `threads` registry")
    for c in plan.get("chains", []):
        th = c.get("thread")
        if not th:
            failures.append(f"H chain has no `thread`: {c.get('chain_id')}")
        elif th not in thread_ids:
            failures.append(f"H chain {c.get('chain_id')} names unknown thread: {th}")
    if "thread_id" in doc:
        failures.append("H retired top-level `thread_id` is present (D39); "
                        "the `threads` registry replaces it")

    # I — retired external-prereq ids are never reused (D45; append-only ledger)
    retired_path = here / "external-prereq-retired.txt"
    if retired_path.exists():
        retired = {ln.split("#", 1)[0].strip() for ln in retired_path.read_text().splitlines()}
        retired.discard("")
        if not retired:
            failures.append("I extracted zero ids from external-prereq-retired.txt")
        for rid in sorted(retired & ext_ids):
            failures.append(f"I retired external prereq is back in external_prereqs: {rid}")
        for s in skills:
            for p in s.get("prereqs", []):
                if p in retired:
                    failures.append(f"I skill uses a retired external prereq: {s.get('id')} -> {p}")
    else:
        failures.append("I missing ledger: external-prereq-retired.txt")

    # J — retired skill ids are never reused (D48 note; append-only ledger)
    rs_path = here / "skill-ids-retired.txt"
    if rs_path.exists():
        rs = {ln.split("#", 1)[0].strip() for ln in rs_path.read_text().splitlines()}
        rs.discard("")
        if not rs:
            failures.append("J extracted zero ids from skill-ids-retired.txt")
        for rid in sorted(rs & skill_ids):
            failures.append(f"J retired skill is back in skills: {rid}")
        for s in skills:
            for p in s.get("prereqs", []):
                if p in rs:
                    failures.append(f"J skill uses a retired skill as a prereq: {s.get('id')} -> {p}")
        for c in doc.get("chunking_plan", {}).get("chains", []):
            for sid in c.get("skills", []):
                if sid in rs:
                    failures.append(f"J chain {c.get('chain_id')} lists a retired skill: {sid}")
    else:
        failures.append("J missing ledger: skill-ids-retired.txt")

    # K — every Y7–Y10 skill reports into one strand (D51)
    strands = set(doc.get("activity_defaults", {}).get("assessment", {})
                  .get("reporting", {}).get("strands", []))
    if not strands:
        failures.append("K extracted zero strands from activity_defaults.assessment.reporting.strands")
    thread_strand = {t.get("id"): t.get("strand") for t in threads if isinstance(t, dict)}
    for tid, st in thread_strand.items():
        if st is not None and st not in strands:
            failures.append(f"K thread {tid} names unknown strand: {st}")
    skill_thread = {sid: c.get("thread") for c in plan.get("chains", [])
                    for sid in c.get("skills", [])}
    reported = 0
    for s in skills:
        sid, own = s.get("id"), s.get("strand")
        if own is not None and own not in strands:
            failures.append(f"K skill {sid} names unknown strand: {own}")
        resolved = own or thread_strand.get(skill_thread.get(sid))
        if s.get("band_nz") in ("Y7", "Y8", "Y9", "Y10"):
            if not resolved:
                failures.append(f"K Y7–Y10 skill resolves no strand: {sid}")
                continue
            reported += 1
        phases = (s.get("alignment") or {}).get("nzc_phase") or []
        nzc = {re.sub(r"^P\d\.Y\d+\.", "", p).split(":")[0].lower() for p in phases}
        if resolved and nzc and resolved not in nzc:
            failures.append(f"K skill {sid} reports into {resolved}, but its NZC phase "
                            f"statements are {sorted(nzc)}")
    if skills and not reported:
        failures.append("K resolved a strand for zero Y7–Y10 skills")

    if failures:
        print(f"check 4 FAIL — {len(failures)} finding(s):", file=sys.stderr)
        for f in failures:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"check 4 OK: {len(skill_ids)} skills, {len(mis_ids)} "
          f"misconceptions, {len(ext_ids)} external prereqs, "
          f"{total} parts, {len(thread_ids)} threads")
    return 0


if __name__ == "__main__":
    sys.exit(main())
