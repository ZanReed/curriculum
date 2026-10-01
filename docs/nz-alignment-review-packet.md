> **Historical record (written 2026-09-03).** This is the packet sent for critical review of the
> D31–D34 proposals. The rulings landed as amended on 2026-09-05 (PR #1); D32's hold was later
> superseded by D36. Read the decision log, not this file, for what stands.

# Four proposed rulings from the NZ alignment pass — review packet

**Status:** PROPOSED — not merged, awaiting this review.
**Sources read:** 2 Sep 2026 (NZC Phase 3/4 teaching sequence, NZQA achievement standards).
**Where:** branch `nz-alignment`, [PR #1](https://github.com/ZanReed/curriculum/pull/1) on `ZanReed/curriculum`.

The curriculum graph (47 skills, Year 8 proportional reasoning through introductory calculus)
was seeded with US vocabulary, US-analogy year bands, and empty alignment fields. On 2 September
the NZ source documents were read and four rulings were drafted. Each is presented below with
its evidence, **its own named weaknesses**, and the questions where critical push-back is most
wanted. Nothing is final: each ruling's hunks stand alone, so a rejected one reverts cleanly
without disturbing the others.

---

## D31 — How an alignment claim is recorded

**The ruling.** Each skill's alignment becomes four arrays — `nzc_phase`, `ncea`, `ccss`,
`teks` — with the NZ pair populated for all 47 skills. An NZC value is
`P<phase>.Y<year>.<Strand>` (e.g. `P4.Y9.Algebra`): a phase alone spans two to three years and
the refreshed curriculum is written year by year, so anything coarser says almost nothing. An
NCEA value is a standard id (e.g. `AS91947`).

Values in the graph are **pointers only**. Every quoted statement backing a value lives in one
dated reference file (`docs/alignment-sources.md`, with URLs and the read date), because the
NZC pages are live and unnumbered — a quote copied into the graph would be a hand-maintained
duplicate of a moving document. If the live page and the reference file ever disagree, the page
wins and the value is declared stale.

**What it does not claim.** Recording an alignment does not make it checkable. Whether an
assessment item actually works at the level its standard asks remains a human read.

**Named weaknesses.** The three linear-forms skills (point–gradient, `Ax + By = C`, converting
between forms) have **no NZC Years 9–10 statement at all** and point only at AS91256, whose
text was not re-read. NZ classrooms rarely name these forms. Their `nzc_phase` is deliberately
left empty rather than filled with an invented category.

**Push back here:**

1. Is phase-year-strand the right grain, or does year-level alignment overclaim precision for
   a curriculum schools will sequence differently?
2. Should the thread keep **three separate skills** for the US linear forms, given no NZ
   document asks for them — or collapse them?
3. Any NZC statement you'd read differently than the pointers imply? The quotes are all in the
   sources file — spot-check a few against your own reading.

---

## D32 — Where the calculus end sits in NZ years

**The ruling.** All thirteen limits-and-derivatives skills move to **Year 12** (previously
split Y12/Y13 by a US analogy: Y12 ↔ Precalculus, Y13 ↔ Calculus). The evidence: AS91262, the
*Year 12* standard, already differentiates polynomials, finds tangents and turning points, and
does kinematics — and lists no limits. Limits, continuity and the chain/product/quotient rules
formally belong to AS91578 at Year 13. The limit skills stay at Y12 anyway because they are
prerequisites of Y12 skills (a band later than its dependents is incoherent), and in practice
first principles is taught in Year 12 as the motivation for AS91262.

The US-analogue map is **kept** for authors arriving from TEKS/CCSS material, but annotated:
it is an analogue, not how the NZ bands are derived, and its top two rows are not equivalences.

**Consequence, stated plainly.** The thread now has **no Year 13 skill**. It ends at the power
rule; AS91578's content (chain rule, optimisation, related rates) was never in it.

**Named weaknesses.** The **middle of the spine was left alone on weaker evidence**: function
notation (Y10) and graph transformations (Y11) have no NZC Y9–10 statement and are first
assessed by AS91257 at Year 12 — each may read one year early for NZ. The Phase 5 draft that
would settle it was not reachable; the question is recorded, not decided.

**Push back here:**

1. Does "no Y13 skill" match your read of where this thread should end — or should it grow
   toward AS91578 content instead of re-banding?
2. From your classroom knowledge: do Year 11 courses teach enough f(x) and transformations
   that the current Y10/Y11 bands are fine, or is the one-year-early worry real?
3. Is keeping the US map worth the risk of someone reading it as an equivalence despite the
   note?

---

## D33 — What a locale entry carries, and the NZCE stub

**The ruling.** The `nz-ncea` locale entry now states what an author needs: the grade set;
what Achieved, Merit and Excellence each require, in the standards' own wording (Merit =
relational thinking, Excellence = extended abstract thinking, each with what that looks like in
an item); a rule that every rubric line is tagged A, M or E and the primary-skill item reaches
E; calculator and context facts (a Level 1 internal *requires* problems grounded in Aotearoa or
the Pacific); which cohorts it applies to; and its sources.

The successor qualification's locale (`nz-nzce`) is an **explicit stub** — confirmed facts,
unconfirmed facts, and a revisit trigger — because the cohort arithmetic is stark: every
learner Year 9 or below in 2026 will never sit an NCEA standard, yet everything about the
replacement's grading is deferred to the Ministry's "Tranche 2," unpublished as of the read
date. Until it lands, `nz-ncea` stands as the named proxy, and the stub says exactly what it is
standing in for and until when.

**Named weaknesses.** The proxy is a bet: that the successor's assessment shape (A–E letters,
no fully-internal subjects) stays compatible with justification-weighted rubric items. If
Tranche 2 lands somewhere else, the Y8–10 chains' assessment layer gets re-cut.

**Push back here:**

1. Are the A/M/E descriptors, as operationalised ("in an item: generalise, prove, evaluate a
   claim…"), faithful to how you'd moderate them?
2. Is "primary-skill item reaches E" the right bar for every rubric-graded lesson close, or
   too strong as a blanket rule?
3. Would you author Y8–10 against anything other than the NCEA proxy in the interim — and if
   so, against what?

---

## D34 — Whose language the curriculum speaks

**The ruling.** Everything a student can see goes NZ: *gradient* (never *slope*), `y = mx + c`
(never `y = mx + b`), *point–gradient form*. *Standard form* is not renamed but demoted to a
description — "the form `Ax + By = C`" — because NZ has no name for it and inventing one would
be an unsourced claim. Machine identifiers are untouched: they are keys other files reference,
and renaming a key is a breaking event with no student-visible benefit.

**Named weaknesses.** One deliberate exception: *parent function* stays, on the grounds that
NZ usage is mixed and the term appears in AS91257 resources — a judgment call, not a sourced
fact.

**Push back here:**

1. Does *parent function* read naturally to NZ students in your experience, or should it
   become something like *basic graph*?
2. Any other US-isms you'd expect students to trip on that this pass missed — *y-intercept*
   conventions, interval language, anything in statistics-adjacent phrasing?

---

Everything above lives on the `nz-alignment` branch
([PR #1](https://github.com/ZanReed/curriculum/pull/1)): the full decision text in
`decision-log-additions.md`, every quoted source statement in `docs/alignment-sources.md`, and
the graph diff itself.

*Prepared 3 Sep 2026 for critical review — the weaknesses above are the rulings' own
declarations, and disagreement with any of them is the feedback being asked for.*
