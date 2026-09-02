#!/usr/bin/env python3
"""
Partition check — fails if the authoring prose restates a threshold that
activity_defaults declares.

The partition (D25): activity_defaults holds every fact a validator reads;
the prose holds reasoning and cites KEYS, never values. This check is the
enforcement, because a partition nobody checks is two copies within weeks.

Both halves live in one file, so this is a single-file self-consistency test.
Exit 1 on any violation.
"""
import json, re, sys

NOISE = [
    (r'§\s*\d+', ' '),                      # section refs: "see §8"
    # Key citations only — dotted identifier, no digits, no operators. Anything
    # else inside backticks stays visible, because the partition rule tells authors
    # to cite keys, so backticks are exactly where a value will eventually be typed.
    (r'`[A-Za-z_][A-Za-z0-9_.]*`', ' '),
    (r'\$[^$]*\$', ' '),                    # inline math
    (r'\(\s*-?\d+\s*,\s*-?\d+\s*\)', ' '),  # coordinate pairs (2,1)
    (r'\b\w\(\s*[\dxh][^)]{0,8}\)', ' '),   # f(3), f(x)=3, f(a+h)
    (r'\b[Pp]art \d+\+?', ' '),             # chain position labels
    (r'\b[Pp]osition \d+\+?', ' '),
    (r'\bD\d+\b', ' '),                     # decision refs
]

# Each probe: (label, json path, regex the prose must NOT contain).
# Anchored on the unit or operator, not the bare digit — a bare-digit grep
# false-positives on section refs and worked examples at ~60%, and a check
# that cries wolf gets switched off.
PROBES = [
    ('hook_contract.minimum',        r'ceil\s*\('),
    ('activity_defaults.duration_min', r'\b\d+\s*(?:–|-|to )\s*\d+\s*min'),
    ('chain_rules.position_gt_1',    r'\b\d+\s*-?\s*second\b'),
    ('phase_budget_min',             r'\b(?:review|worked|faded|independent|DoL)\s+\d+\b'),
    ('review_selection.constraint',  r'(?:distance|rows?|edges?)\s*(?:>=|≥|of at least)\s*\d+'),
]

# Advisory only. Word-spelled thresholds ("one hook per two activities") are
# invisible to the probes above, and probing for number-words directly
# false-positives on ordinary prose ("exactly one primary skill", "two ideas in
# one activity"). The fix is upstream, not a smarter regex: THRESHOLDS ARE
# WRITTEN AS DIGITS (D25). These are listed for a human, never failed on.
WORDNUM = re.compile(r'\b(one|two|three|four|five|six|seven|eight|nine|ten)\b', re.I)
UNITWORD = re.compile(r'(hook|activit|minute|second|item|row|edge)', re.I)

def main(path):
    d = json.load(open(path))
    prose = d['authoring_principles']
    violations = []
    for lineno, raw in enumerate(prose.splitlines(), 1):
        if raw.lstrip().startswith('#'):
            continue
        line = raw
        for pat, sub in NOISE:
            line = re.sub(pat, sub, line)
        for key, probe in PROBES:
            if re.search(probe, line, re.I):
                violations.append((lineno, key, raw.strip()))
    for ln, key, txt in violations:
        print(f'PARTITION VIOLATION  L{ln}  restates {key}\n    {txt[:100]}')
    advisory = [
        (n, l.strip()) for n, l in enumerate(prose.splitlines(), 1)
        if not l.lstrip().startswith('#') and WORDNUM.search(l) and UNITWORD.search(l)
    ]
    if advisory:
        print(f'\nadvisory — {len(advisory)} line(s) pair a spelled-out number with a unit.')
        print('Not failed on. Review by hand; if any is a threshold, write it as a digit')
        print('or move it to activity_defaults. See D25.')
        for n, t in advisory:
            print(f'    L{n}: {t[:88]}')
    if violations:
        print(f'\n{len(violations)} violation(s). Prose must cite the key, not the value.')
        return 1
    print('\npartition clean (hard probes)')
    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else 'thread-01-rate-of-change.v0.11.0.json'))
