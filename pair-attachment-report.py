#!/usr/bin/env python3
"""
Pair-attachment report (B10) — a misconception attached to SOME but not ALL
skills of a chain.

WHY THIS RUNS ON THE CURRICULUM SIDE. It reads the thread graph, and the
platform reads nothing in that file — deliberately, and stated in writing. A
report that lives here keeps that boundary intact; a report that lives on the
platform would make it read the graph for the first time to answer a question
the platform does not own.

WHAT IT IS FOR. It does NOT decide whether a chain is confusable, and it does
not decide whether an attachment is wrong. It narrows §7's authoring question
-- "can the sibling skill exhibit this error?" -- from 47 skills to a handful of
candidates, at the moment someone has the chain in their head.

WHY 2-SKILL CHAINS ARE REPORTED SEPARATELY. In a 2-skill chain a partial
attachment means the misconception is on one of exactly two siblings, which is
the shape both real bugs had (mis.transform.inside-outside,
mis.function.evaluate-vs-solve). Measured on v0.11.1: 6 candidates in 2-skill
chains, both bugs among them. In larger chains the signal is much weaker --
33 candidates -- so those print under a separate heading and should not be
worked through row by row.

NOT A GATE. Precision was 2-in-6 on the only run with known answers. A check
that fails a build at that rate gets switched off, and this one is here to feed
a human question rather than answer it.

KNOWN BLIND SPOT: a confusion whose two skills sit in DIFFERENT chains is
invisible to this -- mis.transform.stretch-vs-shift names one skill in
chain.transform.translate and one in chain.transform.stretch-reflect. Per-chain
completeness cannot see cross-chain pairs.

    python3 pair-attachment-report.py thread-01-rate-of-change.json
"""
import json, sys
from collections import defaultdict

def report(path):
    d = json.load(open(path))
    mis = {m['id']: m['label'] for m in d['misconceptions']}
    skills = {s['id']: set(s['misconceptions']) for s in d['skills']}
    small, large = [], []
    for c in d['chunking_plan']['chains']:
        ids = [i for i in c['skills'] if i in skills]
        if len(ids) < 2:
            continue
        used = set().union(*(skills[i] for i in ids))
        for m in sorted(used):
            on = [i for i in ids if m in skills[i]]
            if 0 < len(on) < len(ids):
                row = (c['chain_id'], m, on, [i for i in ids if i not in on])
                (small if len(ids) == 2 else large).append(row)

    print(f"PAIR-ATTACHMENT REPORT — {path}\n")
    print(f"{len(small)} candidate(s) in 2-skill chains — ask each one:\n")
    for chain, m, on, off in small:
        print(f"  {chain}")
        print(f"    {m}")
        print(f"      \"{mis.get(m,'')}\"")
        print(f"      attached: {on[0]}")
        print(f"      NOT on:   {off[0]}")
        print(f"      -> can {off[0].split('.')[-1]} exhibit this error? "
              f"if yes, attach. if the label only describes the attached side, reword it.\n")
    print(f"{len(large)} further partial attachment(s) in larger chains "
          f"(weaker signal, not a worklist):")
    for chain, m, on, off in large:
        print(f"    {chain:34} {m:44} {len(on)}/{len(on)+len(off)}")
    print("\nReport only. Nothing here is a defect until a human says the sibling can exhibit it.")
    return 0

if __name__ == '__main__':
    sys.exit(report(sys.argv[1] if len(sys.argv) > 1 else 'thread-01-rate-of-change.json'))
