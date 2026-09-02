#!/usr/bin/env python3
"""
Generate the registries from the thread graph, with a notation gate on labels.

WHY THIS EXISTS. Five labels were hand-fixed for lost math notation and a sixth
was missed, because the fix chased a cause (an ASCII-safe merge script) that did
not explain all the instances. The true cause is that notation in labels was
never normalised anywhere. Hand-fixing is what produced five and then missed one.

WHY THIS ONE IS A GATE AND NOT A REPORT. By the criterion this project settled
on: a check may gate when what it detects is decidable from the artifact. An
ASCII apostrophe following a letter inside a misconception label is always wrong
here -- there is no legitimate possessive in a label. Whether a correlation has a
reason (fd-check) or whether a sibling can exhibit an error (pair-attachment) is
not decidable from the file, so those report.

WHY A LABEL'S NOTATION IS NOT COSMETIC. The label is what an author reads while
writing distractors, months after the id was minted. A superscript-free label on
a misconception about ignoring superscripts reads as a typo, and the next author
"corrects" it by deleting the distinction the id exists to detect.

DELIBERATELY NOT PROBED: a hyphen between alphanumerics, as a candidate minus
sign. It fires on "two-sided", "y-direction", "one-to-one" -- ordinary language,
at a rate that would get the gate switched off. Same reason the math-blank
detector tests the constructed node instead of scanning for $ delimiters.

    python3 generate-registries.py thread-01-rate-of-change.json
"""
import json, re, sys

# The apostrophe probe is NARROW on purpose. The broad form [A-Za-z]\)?' fires on
# "the student's first step", "doesn't distribute", "Newton's method" -- and then
# tells the author to put a prime in "student's". A misdiagnosing gate is worse
# than a noisy one: a noisy check gets ignored, a wrong-advice check gets obeyed.
# Requiring the apostrophe to end a token or precede "(" is what a prime actually
# looks like. Measured: clean on all three possessives, fires on f'(x) and f'.
BAD = [
    (r"\b[A-Za-z]'(?=\(|\s|$|,|\.)", "ASCII apostrophe — use the prime ′"),
    (r"->|=>",         "ASCII arrow — use →"),
    (r"\^",            "caret exponent — use a superscript"),
    (r"<=|>=",         "ASCII comparison — use ≤ ≥"),
    (r"\b[a-z]\d\b",   "digit beside a variable — lost superscript?"),
]

def check_labels(items, kind):
    bad = []
    for it in items:
        for pat, why in BAD:
            if re.search(pat, it['label']):
                bad.append((it['id'], it['label'], why))
    for i, l, w in bad:
        print(f"NOTATION  {kind} {i}\n    {l}\n    -> {w}", file=sys.stderr)
    return bad

def main(path):
    d = json.load(open(path))
    v = d.get('version', '?')
    # Every collection carrying a label, not just the one that prompted the gate.
    # The gate was built after five hand-fixed misconception labels missed a sixth;
    # it then checked only misconception labels and missed four SKILL labels with
    # the same defect. When a fix moves from hand to machine the scope moves with
    # it -- but only as far as the conversation had reached. Skill labels are the
    # comments in skill-registry.txt, read while choosing a `skill:` line.
    bad = []
    for key, kind in [('skills', 'skill'), ('misconceptions', 'misconception'),
                      ('external_prereqs', 'external-prereq'), ('capabilities', 'capability')]:
        bad += check_labels([x for x in d.get(key, []) if 'label' in x], kind)
    if bad:
        print(f"\n{len(bad)} label(s) with flattened notation. Nothing written.", file=sys.stderr)
        return 1

    def write(name, header, rows):
        with open(name, 'w', encoding='utf-8') as f:
            f.write('\n'.join(header + rows) + '\n')
        print(f"  {name:32} {len(rows)} entries")

    write('misconception-registry.txt',
          ["# Misconception registry — the valid mis.* id set.", "#",
           f"# Generated from {path} v{v}. Do not hand-edit: regenerate.",
           "# An id-shaped token not listed here warns, and fails under --strict.", ""],
          [f"{m['id']:<50}# {m['label']}"
           for m in sorted(d['misconceptions'], key=lambda m: m['id'])])

    # skill-registry.txt is now generated too. Its part counts used to live ONLY in
    # this text file, which is why it could not be -- so a "regeneration" was a hand
    # edit with a stale stamp on it, caught by the platform. D23 always said the part
    # count is a property of the SKILL; it now lives on the skill and this file is a
    # pure projection. chain-registry.txt stays hand-maintained because its display
    # titles are authored prose with no source in the graph, and it carries no stamp.
    pos, rows = {}, []
    for i, c in enumerate(d['chunking_plan']['chains'], 1):
        for sid in c['skills']:
            pos.setdefault(sid, (i, c['chain_id']))
    seen = set()
    for c in d['chunking_plan']['chains']:
        rows.append(f"\n# {c['chain_id']}  ({len(c['skills'])} skills, {c['activities']} activities projected)")
        for sid in c['skills']:
            if sid in seen:
                continue
            seen.add(sid)
            sk = next(x for x in d['skills'] if x['id'] == sid)
            left = f"{sid} = {sk['parts']}" if sk.get('parts', 1) > 1 else sid
            rows.append(f"{left:<42}# {sk['label']}")
    orphans = [x for x in d['skills'] if x['id'] not in seen]
    if orphans:
        rows.append('\n# NOT IN ANY CHAIN:')
        rows += [f"{x['id']:<42}# {x['label']}" for x in orphans]
    total = sum(x.get('parts', 1) for x in d['skills'])
    write('skill-registry.txt',
          ["# Skill registry — the valid skill id set.", "#",
           "# A bare id is a one-part skill; `id = n` declares a skill delivered across n",
           "# activities (D23). External prerequisites are NOT here — valid review and DoL",
           "# targets, never taught, never counted toward coverage.",
           f"# Generated from {path} v{v} — {len(d['skills'])} skills, {total} parts,"
           f" {len(d['chunking_plan']['chains'])} chains. Do not hand-edit: regenerate.", ""],
          rows)

    write('external-prereq-registry.txt',
          ["# External prerequisites — assumed prior knowledge.", "#",
           "# Valid targets for review items, DoL item 2 and prereq edges. NOT skills this",
           "# curriculum teaches: never counted toward coverage, never a primary `skill:`.",
           f"# Generated from {path} v{v}.", ""],
          [f"{e['id']:<30}# {e['label']}" for e in d['external_prereqs']])

    print(f"\ngenerated from v{v}. chain-registry.txt is NOT generated — its display"
          "\ntitles are authored prose with no source in the graph.")
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'thread-01-rate-of-change.json'))
