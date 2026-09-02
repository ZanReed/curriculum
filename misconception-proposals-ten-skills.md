# Misconception proposals — the ten uninstrumented skills

**Date:** 2026-08-26 · **Status:** RATIFIED and merged at graph v0.12.0. Kept as the reasoning record.

**Thirteen** new ids and **two** new attachments of existing ids, across the ten skills that
carried `misconceptions: []`. (This document's original header said twelve and five; it had
counted attachments of *new* ids to second skills as though they were attachments of existing
ones. The merged graph is right; the header was wrong.)

**Merged at v0.12.0**, with three changes made after ratification — recorded in §4 below
rather than edited silently into the entries, so the reasoning and the outcome stay
distinguishable.

Two things every proposal below has to earn, per §7:

1. **A carrier.** *"Bindings that can never fire are worse than none"* — the data then reads
   *students didn't make this mistake*. Each entry names a distractor that can actually hold
   it, and each is on an auto-scored per-item type, since a map on a teacher-graded item
   yields no aggregate signal until a human marks it.
2. **Attachment to every skill that can elicit it** (§7, as generalised in v0.11.4), not
   merely the skill it was noticed on.

Labels name **the error, not one of its notations** — the defect found in
`mis.transform.horizontal-direction` last week, where a label naming `f(x-h)` sat on a
point-slope skill nine chains earlier and read as a mistake.

---

## Chain 3 — `linear.form.standard`

**`mis.form.intercept-wrong-variable`**
*Sets the wrong variable to zero when finding an intercept*
→ `linear.form.standard`

The x-intercept requires y = 0, and students reliably substitute the variable they are
solving *for* rather than the other one. It is a procedural slip with a conceptual root:
the intercept is understood as "where the graph meets the axis" without the axis being
characterised by the *other* coordinate being zero.
**Carrier:** numeric fill-in on 3x + 4y = 12. Correct x-intercept 4; the binding catches 3.

**`mis.form.standard-slope-sign`**
*Reads the slope of Ax + By = C as A/B, dropping the negative*
→ `linear.form.standard`, `linear.form.convert`

Pattern-matching `m` out of a form where it is not literally present. Worth attaching to
`convert` as well: converting standard to slope-intercept is exactly where the sign is lost,
and an author writing conversion distractors should be anticipating it.
**Carrier:** mc on the slope of 2x + 3y = 6. Correct −2/3, distractor 2/3.

---

## Chain 5 — `function.definition`

**`mis.function.one-to-one-required`**
*Requires each output to have exactly one input — rejects y = x² as a function, or applies
the test horizontally*
→ **`function.definition.mapping` and `function.definition.vlt`**

The definitional misconception of the whole function arc: "each input has exactly one
output" read as a bijection. Its graphical manifestation is reaching for a horizontal line,
which is why it belongs on **both** skills rather than appearing as two ids — the same error
in two notations, which is exactly the case the relabelling rule was written for.
**Carrier:** mc, "which of these is a function?" with y = x² among the options; and a graph
item where the correct answer is a function failing a horizontal line test.

**`mis.function.needs-a-formula`**
*Rejects a correspondence as a function because no equation defines it*
→ `function.definition.mapping`, `function.repr.correspondence`

The student's working definition of "function" is *thing with an equation*. Given a table
where each input appears once, or a set like {(1,3), (2,5), (4,9)}, they answer **not a
function — there's no rule.** Same for an unlabelled curve on a graph.

**The carrier has to ask for the reason, not the verdict.** A bare yes/no cannot distinguish
this student from one who said no for the one-to-one reason, or who miscounted:

> *Is this table a function?*
> - Yes — each input has exactly one output ✓
> - No — there is no equation → `needs-a-formula`
> - No — two different inputs give the same output → `one-to-one-required`
> - Yes, but only once we find its rule → `needs-a-formula`

Auto-scorable, and it discriminates between the two ids that a verdict-only item would leave
indistinguishable — which is the argument for keeping both rather than collapsing them.

**The stronger case is the second attachment.** `function.repr.correspondence` asks students
to see a table, a graph and an equation as *the same object*. A student holding this believes
the equation **is** the function and the table merely describes it. That is not a definitional
quibble; it is the thing that stops chain 7 working.

**Known risk:** "there is no equation" may read as transparently wrong to a test-wise student,
so the id may under-fire. If the data shows that, the fix is an error-analysis item (§16) —
*a student said this isn't a function because you can't write a formula for it; is she right?*
— which is harder to answer by elimination.

---

## Chain 8 — `function.domain-range`

**`mis.function.domain-range-swapped`**
*Reports the range when asked for the domain, or the reverse*
→ **`function.domain-range.graph` and `function.domain-range.context`**

The most common error on both skills. See §2 below — the shared attachment is deliberate
and it does **not** change the chain's consolidation ruling.
**Carrier:** mc on a graph with clearly different domain and range intervals.

**`mis.function.endpoint-open-closed`**
*Includes an open endpoint, or excludes a closed one, when reading an interval*
→ `function.domain-range.graph`

The circle convention is a notation students read as decoration. Worth its own id rather
than folding into the swap, because the remediation is different: one is a vocabulary
problem, this is a convention problem.
**Carrier:** mc over four interval notations differing only in bracket type.

**`mis.function.context-restriction-ignored`**
*Gives the mathematical domain of the formula, ignoring what the context permits*
→ `function.domain-range.context`, `linear.model.contextual`

Negative time, fractional people, more items sold than exist. The formula's domain is ℝ and
the student reports ℝ. Attached to `linear.model.contextual` as well, where building and
*critiquing* a model is exactly where this surfaces.
**Carrier:** mc on the domain of a cost model with a stated quantity limit.

---

## Chain 9 — `function.families`

**`mis.family.any-line-is-parent`** → merged as **`mis.family.any-member-is-parent`**, see §4
*Treats any linear function as the parent rather than y = x specifically*
→ `function.family.parent-linear`

"Parent" is heard as "kind of" rather than "the untransformed one," which breaks the entire
transformation arc that follows immediately in chains 10–12.
**Carrier:** mc over four linear equations, only one of which is the parent.

**`mis.family.negative-squares-negative`** → merged as **`mis.arith.negative-squared`**, see §4
*Believes squaring a negative input gives a negative output, so plots the left branch below
the axis*
→ `function.family.parent-quadratic`

Students describe y = x² as symmetric and then plot (−2, −4). The verbal description and the
plotted points come from different places and neither corrects the other.
**Carrier:** graph item or a table-completion fill-in at x = −2. Correct 4, binding catches −4.

---

## Chain 13 — `roc.average.secant`

**`mis.roc.secant-vs-tangent`**
*Treats the average rate of change over an interval as the rate at a point*
→ `roc.average.secant`, `limit.secant-to-tangent`, `deriv.interpret.slope-tangent`

The confusion the entire limit chain exists to resolve, and it must be instrumented on all
three skills that touch it — it is first anticipatable at chain 13, is the explicit subject
of chain 15, and remains available as a wrong answer at chain 16. A pair-confusion whose
halves sit in different chains, which the per-chain structural check cannot see.
**Carrier:** mc, "the slope of this secant tells you…", with *the speed at x = 2* among the
options.

Also attaching the existing **`mis.roc.uses-endpoint-value`** → `roc.average.secant`.
Reporting f(b) rather than the change in f is available on this skill too, and it is already
instrumented on the two neighbours.

---

## Chain 14 — `limit.notation`

**`mis.limit.one-sided-superscript-ignored`**
*Reads x → a⁻ and x → a⁺ as x → a, and reports the two-sided limit*
→ `limit.notation`, `limit.graphical.estimate`

Superscripts are the smallest carrier of meaning in the notation and the first thing skipped.
It matters most at a jump discontinuity, which is where `limit.graphical.estimate` lives.
**Carrier:** mc on a piecewise graph where the one-sided and two-sided answers differ.

Also attaching the existing **`mis.limit.equals-substitution`** → `limit.notation`. A student
who believes the limit *is* the substitution will write `lim f(x) = f(a)` as a matter of
notation, not just of evaluation — the notation skill can elicit it and should anticipate it.

---

## Chain 17 — `deriv.f-prime-as-function`

**`mis.deriv.f-prime-is-a-number`**
*Treats f′ as a single value rather than a function that varies with x*
→ `deriv.f-prime-as-function`

The residue of meeting f′(a) at a point first (chain 16) and generalising late. Students who
hold it cannot make sense of the power rule producing an expression rather than a number.
**Carrier:** mc, "what kind of object is f′?", or a fill-in asking for f′(1) and f′(3) from
one derivative.

**`mis.deriv.reads-f-graph-as-f-prime`**
*Reads the graph of f as if it were the graph of f′ — says f′ is positive where f is positive
rather than where f is increasing*
→ `deriv.f-prime-as-function`, `deriv.interpret.slope-tangent`

Arguably the single most documented misconception in introductory calculus, and the skill it
belongs to is currently uninstrumented. Height and slope are both read off the same picture,
and nothing in the graph distinguishes which one the question is about.
**Carrier:** mc on a graph of f, "on which interval is f′ negative?", with the interval where
f is negative among the distractors.

---

## 0. A correction to an existing deferral: `mis.rate.units-dropped`

Not one of the twelve, but it surfaced while checking their carriers and it changes a
standing decision.

`mis.rate.units-dropped` has been deferred on the grounds that **numeric blanks cannot carry
units** — the platform reported three tokenizer collisions, one of which scored the literal
word "kph" as correct. That is true, and the deferral was recorded as *waiting on a capability*.

**The reasoning was wrong.** Even if units-bearing blanks shipped tomorrow, binding
units-dropped to a blank that does not *require* units would still be invalid: the binding
would fire on every correct answer, because omitting units was never a choice the student
made. A misconception about the form of a response is only detectable where the format admits
that form **and** the item demands it.

So the id is not blocked — it is **mis-scoped**. The carrier available today is an mc with the
unitless distractor:

> *A car travels 36 km in 3 hours. What is its speed?*
> - 12 km/h ✓
> - 12 → `mis.rate.units-dropped`

The capability wish keeps its value — a units-bearing blank would catch the error on free
response rather than only where an author anticipated it — but it stops being a blocker.

**This is now a rule, not a note**, because `mis.slope.units-dropped` and
`mis.deriv.units-dropped` are already registered and attached across four skills, so the same
trap is waiting in chains 2, 4, 13 and 16. Written into §7:

> A misconception about the FORM of a response binds only where the response format admits
> that form and the item requires it.

Same family as the existing rule that distractor maps go only on auto-scored per-item types.
Both are about a binding that cannot fire meaning something other than what it appears to.

---

## 1. What this does to the four judgement rulings

The point of authoring these was partly to re-test the four consolidation rulings that rest
on my judgement rather than on evidence. Result:

| chain | ruling | before | after |
|---|---|---|---|
| `function.definition` | earns 1C | judgement | **confirmed** — `one-to-one-required` on both skills |
| `function.families` | no C | judgement | **confirmed** — no shared id; the two errors are unrelated |
| `function.domain-range` | no C | judgement | **flags, ruling held** — see §2 |
| `deriv.definition` | earns 1C | judgement | **still judgement** — no new ids on its skills |

Two of four resolved, one held against its own flag with a reason, one still open. That is
roughly what "revisit when instrumented" should look like, and `deriv.definition` stays on
the list.

## 2. ⚠ A limitation of the shared-misconception proxy, found by using it

`mis.function.domain-range-swapped` attaches to both skills of
`chain.function.domain-range`, so the chain now flags — and my ruling was that it earns **no**
consolidation. I am holding the ruling, and the reason is a real limitation rather than an
excuse:

> **The proxy detects the same error appearing in two skills. The criterion requires the two
> skills to be confusable with each other.** Those are different claims.

Reading domain from a graph and restricting domain in a context are not confusable *tasks* —
a student never has to decide which one applies. They are the same task in two settings, and
the shared error is a mistake made *within* each rather than a confusion *between* them.

`mis.function.one-to-one-required` in chain 5 is the contrasting case: a student genuinely
must decide whether the mapping definition or its graphical test is the tool for the question
in front of them, and the error is choosing wrongly between them.

**So the proxy is necessary, not sufficient.** A shared id is grounds to ask the §14 question,
not to answer it. That is the same posture the FD check and the structural check both landed
on, arrived at independently for a third time — worth noticing as a pattern about this
project rather than about any one checker.

---

## 3. If ratified

Registry 22 → 34 ids. Skills with no anticipated misconceptions: **10 → 0.**

Merge order, per the standing step: **ratify → merge into the graph → regenerate
`misconception-registry.txt` → then author bindings.** None of these ids should appear in a
`.md` before the registry carries them.

Nothing here is authored against a distractor that exists yet — every carrier above is a
sketch of an item that *could* hold the binding, in the activities these chains have not been
written for. That is the correct order (the id has to exist before the item can bind to it),
but it does mean each carrier is a prediction, and the ones that turn out to be unwritable
should send the id back rather than acquire a strained item to justify it.


---

## 4. Changes made after ratification

Three, all from applying the platform's pair-attachment report to the merged graph. Recorded
here rather than edited into the entries above, so what was proposed and what shipped stay
distinguishable.

**Prefix split — `mis.family.*` was carving by skill domain, not error kind.** It held both
*misunderstands what "parent" means* and *believes (−2)² = −4*, which are unrelated error
types, and D21 says prefixes carve by kind. So the squaring error became
**`mis.arith.negative-squared`** — a new prefix with precedent, since `ext.arith.fractions`
already exists as an external prereq. Accepted cost: a prefix holding one id. The alternative
buried an error that recurs wherever a quadratic is evaluated at a negative input under a
chain-9 label.

**`mis.family.any-line-is-parent` → `mis.family.any-member-is-parent`**, relabelled *"treats
any member of a family as the parent rather than the untransformed one — any line for y = x,
any parabola for y = x²"*, and attached to **both** family skills. The error generalises; the
label named only lines. §7's second clause: attachment defensible on both sides, label too
narrow, so reword. Free to rename because nothing bound to it yet.

**Two attachments added.** `mis.function.needs-a-formula` → `function.definition.vlt`, because
an unlabelled curve has no equation either — the case argued for in the entry above and then
not attached. And `mis.function.endpoint-open-closed` → `function.domain-range.context`:
*can t = 0? can you buy zero items?* is boundary inclusion in a setting where the open-circle
convention never appears. That second one would not have been found by reading.

**Labels were later renormalised** (v0.12.1–v0.12.4) after six carried flattened math notation
— `x2` for `x²`, `->` for `→`, `f'` for `f′`. Registries are now generated through a notation
gate rather than hand-edited. Any label quoted in this document is the proposal wording; the
graph is authoritative.
