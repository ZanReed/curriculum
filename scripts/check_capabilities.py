#!/usr/bin/env python3
"""Capability check (B14): the graph's DERIVED capability fields against the
platform's pinned facts, plus the capability shape check.

Field ownership (D27 amendment, 2026-10-03):
  DERIVED  - status, grading.scoring, grading.captures_response,
             grading.score_shape. The platform derives them from its code and
             publishes docs/capability-facts.json; this repo commits a PINNED
             copy in platform-pins/ and this script gates the graph against it.
  AUTHORED - id, label, medium, affords, constraints, grading.note. Curriculum
             prose. Never compared; prose a fact contradicts is FLAGGED only.

The gate is decidable from this repo's own artifacts: it never fetches. The
scheduled workflow (capability-drift.yml) is what notices the platform's main
moving past the pin; bumping the pin is the act that changes derived fields.

Fails (exit 1) when:
  1. the pinned file's sha256 is not the one recorded in its .pin.json
     (a hand-edited pin is not a pin);
  2. a capability entry has a field outside the known shape, lacks a required
     one, repeats an id, or uses a status/scoring/score_shape outside the
     vocabulary (this SHAPE check replaces the B14 version gate);
  3. a pinned capability is missing from the graph, or its derived fields
     differ from the pin;
  4. a graph capability the pin does not know is marked anything but
     `proposed` (shipped needs code backing);
  5. an authored field still carries the PROSE OWED marker.

Reports, never fails: prose that a pinned fact contradicts.

Usage:
  check_capabilities.py <graph.json> --facts <pinned.json> --pin <pin.json>
  check_capabilities.py --facts <pinned.json> --upstream <fetched.json>
      (drift report for the scheduled workflow: exit 1 if derived fields differ)
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys

ALLOWED = {"id", "label", "medium", "status", "affords", "constraints", "grading"}
REQUIRED = ALLOWED
GRADING_ALLOWED = {"scoring", "captures_response", "score_shape", "note"}
GRADING_REQUIRED = {"scoring", "captures_response", "score_shape"}
STATUSES = {"shipped", "proposed"}
AUTHORED = ("label", "medium", "affords", "constraints")
MARKER = "PROSE OWED"


def derived(entry: dict) -> dict:
    g = entry.get("grading") or {}
    return {
        "status": entry.get("status"),
        "scoring": g.get("scoring"),
        "captures_response": g.get("captures_response"),
        "score_shape": g.get("score_shape"),
    }


def check_graph(graph_path: str, facts_path: str, pin_path: str) -> int:
    errors: list[str] = []
    flags: list[str] = []

    raw = open(facts_path, "rb").read()
    pin = json.load(open(pin_path))
    actual = hashlib.sha256(raw).hexdigest()
    if actual != pin.get("sha256"):
        errors.append(f"{facts_path} sha256 is {actual}, but {pin_path} records {pin.get('sha256')} "
                      "- re-pin from the platform's main; never hand-edit the pinned copy.")
    facts = json.loads(raw)
    vocab = facts["vocabulary"]
    pinned = facts["capabilities"]
    if not pinned:
        errors.append("the pinned facts list no capabilities - an empty pin would check nothing.")

    caps = json.load(open(graph_path)).get("capabilities") or []
    if not caps:
        errors.append("the graph has no capabilities - nothing to check.")
    seen: set[str] = set()
    for c in caps:
        cid = c.get("id", "<no id>")
        if cid in seen:
            errors.append(f"capability '{cid}' appears twice.")
        seen.add(cid)
        extra, missing = set(c) - ALLOWED, REQUIRED - set(c)
        if extra:
            errors.append(f"capability '{cid}' has unknown field(s) {sorted(extra)}.")
        if missing:
            errors.append(f"capability '{cid}' lacks field(s) {sorted(missing)}.")
        g = c.get("grading") or {}
        gx, gm = set(g) - GRADING_ALLOWED, GRADING_REQUIRED - set(g)
        if gx:
            errors.append(f"capability '{cid}' grading has unknown field(s) {sorted(gx)}.")
        if gm:
            errors.append(f"capability '{cid}' grading lacks field(s) {sorted(gm)}.")
        if c.get("status") not in STATUSES:
            errors.append(f"capability '{cid}' status {c.get('status')!r} is not one of {sorted(STATUSES)}.")
        if g.get("scoring") not in vocab["scoring"]:
            errors.append(f"capability '{cid}' scoring {g.get('scoring')!r} is not in {vocab['scoring']}.")
        if g.get("score_shape") not in vocab["score_shape"]:
            errors.append(f"capability '{cid}' score_shape {g.get('score_shape')!r} is not in {vocab['score_shape']}.")
        if not isinstance(g.get("captures_response"), bool):
            errors.append(f"capability '{cid}' captures_response is not a boolean.")
        for field in AUTHORED:
            if MARKER in str(c.get(field, "")):
                errors.append(f"capability '{cid}' {field} still says {MARKER!r} - the curriculum side writes it before merge.")

        fact = pinned.get(cid)
        if fact is None:
            if c.get("status") != "proposed":
                errors.append(f"capability '{cid}' is marked {c.get('status')} but the pinned facts have no code backing for it.")
            continue
        want = {"status": fact["status"], **fact["grading"]}
        have = derived(c)
        diff = {k: (have[k], want[k]) for k in want if have.get(k) != want[k]}
        if diff:
            parts = ", ".join(f"{k}: graph {a!r} vs pin {b!r}" for k, (a, b) in sorted(diff.items()))
            errors.append(f"capability '{cid}' derived fields differ from the pin - {parts}.")

        # Prose flags (report only).
        prose = f"{c.get('affords', '')} {c.get('constraints', '')}"
        fence = (fact.get("reached_by") or {}).get("fence")
        if fence and fence != cid and fence not in prose:
            flags.append(f"'{cid}' is authored via the ```{fence} fence, which its prose never mentions.")
    for cid in pinned:
        if cid not in seen:
            errors.append(f"pinned capability '{cid}' is missing from the graph - add its entry (prose is the curriculum side's).")

    families = (facts.get("prose_facts") or {}).get("graded_curve_families") or []
    for c in caps:
        prose = f"{c.get('affords', '')} {c.get('constraints', '')}"
        if re.search(r"graph grades|up to (linear|quadratic|cubic)", prose, re.I):
            flags.append(f"'{c.get('id')}' prose describes what graph grades; the pinned families are: {', '.join(families)}.")

    for f in flags:
        print(f"FLAG   {f}")
    for e in errors:
        print(f"ERROR  {e}", file=sys.stderr)
    if errors:
        print(f"\n{len(errors)} error(s).", file=sys.stderr)
        return 1
    print(f"capabilities: {len(caps)} entries; {len(pinned)} pinned derived facts agree "
          f"(pin {pin.get('source_commit', '?')[:7]}); {len(flags)} prose flag(s).")
    return 0


def drift_report(facts_path: str, upstream_path: str) -> int:
    pinned = json.load(open(facts_path))["capabilities"]
    upstream = json.load(open(upstream_path))["capabilities"]
    lines = []
    for cid in sorted(set(pinned) | set(upstream)):
        a, b = pinned.get(cid), upstream.get(cid)
        if a is None:
            lines.append(f"NEW      {cid}: {json.dumps(b['grading'])} status {b['status']}")
        elif b is None:
            lines.append(f"REMOVED  {cid}")
        elif {"status": a["status"], **a["grading"]} != {"status": b["status"], **b["grading"]}:
            lines.append(f"CHANGED  {cid}: {json.dumps({'status': a['status'], **a['grading']})} -> "
                         f"{json.dumps({'status': b['status'], **b['grading']})}")
    if not lines:
        print("no derived-field drift: the platform's main agrees with the pin.")
        return 0
    print("the platform's main has moved past the pin (open a pin-bump PR, with pre-merge notice):")
    for line in lines:
        print("  " + line)
    return 1


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("graph", nargs="?")
    p.add_argument("--facts", required=True)
    p.add_argument("--pin")
    p.add_argument("--upstream")
    a = p.parse_args()
    if a.upstream:
        return drift_report(a.facts, a.upstream)
    if not (a.graph and a.pin):
        p.error("graph and --pin are required unless --upstream is given")
    return check_graph(a.graph, a.facts, a.pin)


if __name__ == "__main__":
    sys.exit(main())
