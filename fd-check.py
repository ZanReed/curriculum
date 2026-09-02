#!/usr/bin/env python3
"""
Functional-dependency report for the capability registry (D27).

Flags where one field is a total function of another across every record —
D3 applied WITHIN a file, as distinct from partition-check.py, which asks
whether the prose restates a JSON value.

THIS IS A REPORT, NOT A GATE. It exits 0 always. At N=22 its precision is
about 1-in-5: most total dependencies at this scale are coincidence, and no
threshold separates the real one from the rest. The discriminator is printed
beside each hit because only a human can answer it:

    Is there a RULE that makes this true, or is it merely true today?

Definitional dependencies (scoring -> authoritative, which D8 defines) should
be collapsed to a single declaration. Incidental ones must be left alone —
mechanically deleting the dependent field removes information the moment a
new record breaks the coincidence.
"""
import json, sys, itertools
from collections import defaultdict

# A source field whose values are near-unique determines everything trivially.
# `note` is free text: 10 distinct values over 10 records, so it "determines"
# every other field and reports five vacuous dependencies. Guard on it, or the
# report is noise before a human ever reads it.
MAX_SOURCE_CARDINALITY_RATIO = 0.5

def records(path):
    d = json.load(open(path))
    out = []
    for c in d['capabilities']:
        r = {'id': c['id'], 'status': c.get('status')}
        r.update(c.get('grading', {}))
        out.append(r)
    return out

def main(path):
    recs = records(path)
    fields = sorted({k for r in recs for k in r} - {'id'})
    print(f'{len(recs)} records · fields: {", ".join(fields)}\n')
    hits, skipped = [], []
    for a, b in itertools.permutations(fields, 2):
        pres = [r for r in recs if a in r and b in r]
        if not pres:
            continue
        distinct = {str(r[a]) for r in pres}
        m = defaultdict(set)
        for r in pres:
            m[str(r[a])].add(str(r[b]))
        if not all(len(v) == 1 for v in m.values()):
            continue
        ratio = len(distinct) / len(pres)
        (skipped if ratio > MAX_SOURCE_CARDINALITY_RATIO else hits).append((a, b, len(distinct), ratio))
    for a, b, n, _ in hits:
        print(f'  {a} -> {b}   ({n} distinct source values)')
        print(f'      Is there a rule that makes this true, or is it merely true today?')
    if skipped:
        print(f'\n  suppressed as vacuous (source near-unique, ratio > {MAX_SOURCE_CARDINALITY_RATIO}):')
        for a, b, n, ratio in skipped:
            print(f'    {a} -> {b}  (cardinality {ratio:.2f})')
    print(f'\n{len(hits)} candidate(s) for a human. Report only — never a build gate.')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'thread-01-rate-of-change.json'))
