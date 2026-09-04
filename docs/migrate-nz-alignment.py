#!/usr/bin/env python3
"""Reproducible migration v0.13.0 -> v0.14.0-proposed (D31-D34). Run once from a
clean v0.13.0 graph; kept as a reasoning record, not a tool. Never re-run on main."""
import json, re, sys
from collections import OrderedDict

P = 'thread-01-rate-of-change.json'
d = json.load(open(P), object_pairs_hook=OrderedDict)

# ---------------------------------------------------------------- 1. vocabulary
LABELS = {
 'linear.slope.two-points':        'Compute the gradient from two points',
 'linear.slope.from-graph':        'Read the gradient from a graph, attending to axis scale',
 'linear.slope.interpret-context': 'Interpret the gradient as a rate of change in context, with units',
 'linear.form.slope-intercept-graph': 'Graph a line from y = mx + c',
 'linear.form.slope-intercept-write': 'Write y = mx + c from a graph, a table, or two points',
 'linear.form.point-slope':        'Write and use the point–gradient form y − y₁ = m(x − x₁)',
 'linear.form.standard':           'Use the form Ax + By = C, including intercepts',
 'roc.average.secant':             'Identify average rate of change as the gradient of a secant line',
 'deriv.interpret.slope-tangent':  'Interpret f′(a) as the gradient of the tangent line at x = a',
}
NOTES = {
 'transform.horizontal.translate': ('Prereq edge to point-slope', 'Prereq edge to the point–gradient form'),
 'roc.average.function-notation':  ('this is the slope formula they learned in Year 9', 'this is the gradient formula they learned in Year 9 or 10'),
}
MIS = {
 'mis.slope.units-dropped':     'Reports the gradient as a bare number, no units, in a contextual problem',
 'mis.slope.steeper-is-bigger': 'Treats visual steepness as gradient magnitude without reading the scale',
 'mis.form.m-b-swapped':        'Reads c as the gradient and m as the intercept in y = mx + c',
 'mis.form.standard-slope-sign':'Reads the gradient of Ax + By = C as A/B, dropping the negative',
}
for s in d['skills']:
    if s['id'] in LABELS: s['label'] = LABELS[s['id']]
    if s['id'] in NOTES:
        a, b = NOTES[s['id']]; assert a in s['notes'], s['id']; s['notes'] = s['notes'].replace(a, b)
for m in d['misconceptions']:
    if m['id'] in MIS: m['label'] = MIS[m['id']]

# ---------------------------------------------------------------- 2. alignment arrays + values
# nzc_phase values: <phase>.<year>.<strand>; the quoted statements live in docs/alignment-sources.md.
# ncea values: achievement standard ids. All PROPOSED (D31) — recordable, not checkable.
NZC = {
 'rate.unit-rate':                    ['P3.Y7.Number', 'P4.Y9.Number'],
 'rate.constant-of-proportionality':  ['P3.Y7.Algebra', 'P3.Y8.Number'],
 'rate.proportional-graph':           ['P3.Y7.Algebra', 'P4.Y9.Algebra'],
 'linear.slope.two-points':           ['P4.Y10.Algebra'],
 'linear.slope.from-graph':           ['P4.Y10.Algebra'],
 'linear.slope.interpret-context':    ['P4.Y9.Algebra'],
 'linear.form.slope-intercept-graph': ['P4.Y9.Algebra', 'P4.Y10.Algebra'],
 'linear.form.slope-intercept-write': ['P4.Y10.Algebra'],
 'linear.form.point-slope':           [],
 'linear.form.standard':              [],
 'linear.form.convert':               [],
 'linear.model.contextual':           ['P4.Y9.Algebra'],
 'function.definition.mapping':       [],
 'function.definition.vlt':           [],
 'function.notation.evaluate':        ['P3.Y8.Algebra'],
 'function.notation.solve':           ['P3.Y8.Algebra'],
 'function.repr.correspondence':      ['P4.Y9.Algebra'],
 'function.domain-range.graph':       [],
 'function.domain-range.context':     [],
 'function.family.parent-linear':     ['P4.Y9.Algebra'],
 'function.family.parent-quadratic':  ['P4.Y10.Algebra'],
 'transform.vertical.translate':      ['P4.Y10.Algebra'],
 'transform.horizontal.translate':    [],
 'transform.vertical.stretch':        ['P4.Y10.Algebra'],
 'transform.reflect':                 [],
 'transform.horizontal.stretch':      [],
 'transform.compose-order':           [],
 'transform.quadratic.vertex-form':   ['P4.Y10.Algebra'],
 'transform.write-from-graph':        [],
}
NCEA = {
 'rate.unit-rate':                    ['AS91945'],
 'rate.constant-of-proportionality':  ['AS91945'],
 'rate.proportional-graph':           ['AS91947'],
 'linear.slope.two-points':           ['AS91947'],
 'linear.slope.from-graph':           ['AS91947', 'AS91946'],
 'linear.slope.interpret-context':    ['AS91947', 'AS91946'],
 'linear.form.slope-intercept-graph': ['AS91947'],
 'linear.form.slope-intercept-write': ['AS91947'],
 'linear.form.point-slope':           ['AS91256'],
 'linear.form.standard':              ['AS91256'],
 'linear.form.convert':               ['AS91256'],
 'linear.model.contextual':           ['AS91945', 'AS91946', 'AS91947'],
 'function.definition.mapping':       ['AS91257'],
 'function.definition.vlt':           ['AS91257'],
 'function.notation.evaluate':        ['AS91257'],
 'function.notation.solve':           ['AS91261', 'AS91257'],
 'function.repr.correspondence':      ['AS91947', 'AS91257'],
 'function.domain-range.graph':       ['AS91257'],
 'function.domain-range.context':     ['AS91257'],
 'function.family.parent-linear':     ['AS91947'],
 'function.family.parent-quadratic':  ['AS91947'],
 'transform.vertical.translate':      ['AS91257'],
 'transform.horizontal.translate':    ['AS91257'],
 'transform.vertical.stretch':        ['AS91257'],
 'transform.reflect':                 ['AS91257'],
 'transform.horizontal.stretch':      ['AS91257'],
 'transform.compose-order':           ['AS91257'],
 'transform.quadratic.vertex-form':   ['AS91947', 'AS91257'],
 'transform.write-from-graph':        ['AS91257', 'AS91947'],
 'roc.average.from-table':            ['AS91947', 'AS91946'],
 'roc.average.secant':                ['AS91947', 'AS91262'],
 'roc.average.function-notation':     ['AS91262'],
 'roc.average.varies-nonlinear':      ['AS91947', 'AS91262'],
 'roc.average.interpret-context':     ['AS91947', 'AS91262'],
 'limit.numeric.table':               ['AS91578'],
 'limit.graphical.estimate':          ['AS91578'],
 'limit.notation':                    ['AS91578'],
 'limit.secant-to-tangent':           ['AS91262', 'AS91578'],
 'limit.difference-quotient.setup':   ['AS91262'],
 'limit.difference-quotient.simplify':['AS91262'],
 'deriv.definition.at-a-point':       ['AS91262'],
 'deriv.interpret.slope-tangent':     ['AS91262'],
 'deriv.interpret.context-units':     ['AS91262'],
 'deriv.from-definition.polynomial':  ['AS91262'],
 'deriv.f-prime-as-function':         ['AS91262'],
 'deriv.rule.power':                  ['AS91262'],
 'deriv.justify.constant':            ['AS91262'],
}
for s in d['skills']:
    old = s.get('alignment') or {}
    for k in ('teks', 'ccss', 'nzc_phase'):
        assert old.get(k) is None, (s['id'], k, old.get(k))
    s['alignment'] = OrderedDict([
        ('nzc_phase', NZC.get(s['id'], [])),
        ('ncea',      NCEA.get(s['id'], [])),
        ('ccss',      []),
        ('teks',      []),
    ])

# ---------------------------------------------------------------- 3. re-band the calculus end (D32)
REBAND = {k: 'Y12' for k in (
 'limit.numeric.table','limit.graphical.estimate','limit.notation','limit.secant-to-tangent',
 'limit.difference-quotient.setup','limit.difference-quotient.simplify',
 'deriv.definition.at-a-point','deriv.interpret.slope-tangent','deriv.interpret.context-units',
 'deriv.from-definition.polynomial','deriv.f-prime-as-function','deriv.rule.power','deriv.justify.constant')}
for s in d['skills']:
    if s['id'] in REBAND:
        s['band'] = s['band_nz'] = REBAND[s['id']]

ad = d['activity_defaults']
ad['band_labels'] = OrderedDict([
  ('scheme', 'dual'),
  ('note', 'band_us is an approximate US analogue for authors arriving from TEKS/CCSS material. It is NOT how band_nz is derived: band_nz is set per skill from the NZC teaching sequence and the NCEA standard the skill serves (D32). The Y12/Y13 rows in particular are not equivalences — NZ Y12 (AS91262) already differentiates polynomials, and limits are a Y13 (AS91578) graph property, so the whole limit.* and deriv.* run sits at Y12 here.'),
  ('map', ad['band_labels']['map']),
])

# ---------------------------------------------------------------- 4. locales (D33)
new_locales = []
for loc in ad['locales']:
    if loc['id'] == 'nz-ncea':
        loc = OrderedDict([
          ('id', 'nz-ncea'),
          ('label', loc['label']),
          ('grades', ['N', 'A', 'M', 'E']),
          ('levels', OrderedDict([
            ('A', 'Achieved — uses appropriate methods and communicates accurate mathematical information related to the context. Standard wording: "Apply <methods> in solving problems."'),
            ('M', 'Merit — relational thinking: applies methods using logical connections between them and communicates through appropriate mathematical statements. In an item: explain the reasoning, justify with the mathematics, link two or more processes.'),
            ('E', 'Excellence — extended abstract thinking: extends methods using logical connections to explore or solve a problem by considering limitations, assumptions, generalisations or predictions. In an item: generalise, prove, evaluate the validity of a claim, extend the problem.'),
          ])),
          ('dol_rule', 'Every rubric line on a nz-ncea DoL carries a level tag (A, M or E) in the activity\'s x_dol_rubric_levels meta key, in rubric-line order. The primary-skill item reaches E. Error-analysis items (principles §16) are the auto-scorable route to M.'),
          ('calculator', 'An approved calculator is permitted in the L1–L3 externals (AS91946/91947 and above). A calculator: off setting on an activity is a skill-level authoring choice, never a locale rule.'),
          ('context', 'AS91945 (L1 internal) requires problems that relate to life in Aotearoa New Zealand or the Pacific. At Y11 a local context is a standard requirement, not a tone preference.'),
          ('cohorts', 'Applies to learners who are Y10 or above in 2026: Y11 through 2027, Y12 through 2028, Y13 through 2029. Every learner Y9 or below in 2026 sits nz-nzce instead, so the Y8–Y10 chains are authored against this locale only as the best current guess for its successor.'),
          ('sources', 'NZQA AS91945, AS91257, AS91262, AS91578 achievement criteria and explanatory notes; MoE Mathematics and Statistics NCEA Level 1 Subject Learning Outcomes (2024). Read 2026-09-02; see docs/alignment-sources.md.'),
        ])
    elif loc['id'] == 'nz-nzce':
        loc = OrderedDict([
          ('id', 'nz-nzce'),
          ('label', loc['label']),
          ('status', 'stub — cannot be filled yet'),
          ('confirmed', 'Subject-based; A–E letter grades; at least 5 subjects with 3 or more passed per certificate; no fully internally assessed subjects; Y11 Foundational Award in literacy and numeracy with Mathematics compulsory. Rollout: Foundational Award 2028, NZCE (Y12) 2029, NZACE (Y13) 2030; the 2026 Y9 cohort is the first full cohort through.'),
          ('unconfirmed', 'Grading methodology behind the letters, the internal/external balance, and the Y11–13 mathematics subject content (Phase 5 draft) — deferred by the Ministry to "Tranche 2". Nothing published as of 2026-09-02.'),
          ('revisit', 'When Tranche 2 lands. Until then no DoL is authored against this locale; nz-ncea is the standing proxy.'),
        ])
    new_locales.append(loc)
ad['locales'] = new_locales

# ---------------------------------------------------------------- 5. version + notes
d['version'] = '0.14.0-proposed'
d['notes'] = d['notes'].replace(
  'Alignment codes are deliberately null — fill from source documents rather than trusting anyone\'s memory of them.',
  'Alignment values are PROPOSED (D31, 2026-09-02) from the NZC Phase 3/4 pages and NZQA standards read that day — see docs/alignment-sources.md for the quoted statements. They record a claim; they do not check one. ccss/teks stay empty until someone reads those documents.')
assert 'PROPOSED' in d['notes']

json.dump(d, open(P, 'w'), ensure_ascii=False, indent=2)
pass
print('ok')
