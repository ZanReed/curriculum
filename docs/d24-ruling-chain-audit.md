# Curriculum → Platform: D24 ruled, all 17 chains audited, and an attachment bug your catch exposed

**Re:** *the alignment key, two things you did not see, and a read on §5*, 2026-08-26
**Date:** 2026-08-26 · **Status:** D24 ruled; 26 slack activities allocated; plan is wrong by one

---

## 0. Headline

**D24 is ruled** and all 17 chains are audited below. The 26 slack activities allocate as
**12 consolidations and 14 additional skill parts**, plus **one activity the plan is
missing**.

Your `chain.transform.translate` catch is right, and chasing it found something better than
the catch: **a misconception-attachment bug that makes the criterion unmeasurable on
exactly the chains where it matters most.** That is §2, and it is the most useful thing in
this letter.

Activity 04 is closed. §5 of your letter settles it and I am not re-opening it — details in
§6.

---

## 1. The criterion, with a mechanical proxy

> **A chain earns a consolidation when it produces confusability between its own skills.**

§14's own logic: *once two confusable skills both exist, independent practice interleaves
items that force the choice between them.* A chain whose skills cannot be confused has
nothing to interleave, and a consolidation there is padding.

**The measurable proxy: two skills in one chain sharing a misconception id.** A shared id
is not a hunch about confusability — it is a recorded claim that the same wrong move
appears in both places. Ten of 17 chains flag on it:

```
rate.proportional      mis.rate.ratio-inverted            transform.compose   mis.transform.horizontal-direction
linear.slope           mis.slope.rise-run-inverted        roc.average         mis.roc.uses-endpoint-value
linear.forms           mis.form.m-b-swapped               limit.intro         mis.limit.equals-substitution
transform.stretch-reflect  mis.transform.inside-outside   limit.difference-quotient  mis.function.f-of-a-plus-h-distributed
deriv.rules            mis.deriv.constant-rule-confused
```

---

## 2. 🚨 The proxy misses two chains, and the reason is an authoring bug

**`chain.transform.translate` does not flag.** Neither does `chain.function.notation`. Both
obviously earn a consolidation. The proxy fails on both for the same reason, and it is not
a flaw in the proxy:

| misconception | label | attached to | should also be on |
|---|---|---|---|
| `mis.transform.inside-outside` | *applies inside changes to the y-direction and outside changes to the x-direction* | `transform.horizontal.translate` | `transform.vertical.translate` |
| `mis.function.evaluate-vs-solve` | *confuses evaluating f(k) with solving f(x) = k* | `function.notation.solve` | `function.notation.evaluate` |

**Both are pair-confusion misconceptions attached to only one side of the pair.** A student
who applies outside changes to the x-direction gets the *vertical* case wrong too — the
error is symmetric, so the attachment must be. And `evaluate-vs-solve` is §14's own worked
example of a discrimination, attached to one of the two skills it discriminates between.

**This matters beyond the audit.** §7's whole argument is that a binding is a sensor.
A pair-confusion attached one-sidedly is a sensor pointed at half the phenomenon: items on
the unattached skill carry no binding, so the data will under-report the error by roughly
half and will attribute all of it to the skill that happens to hold the attachment.
`mis.transform.inside-outside` is annotated in the graph as *"highest-value misconception
in the thread"*, and it is currently instrumented on one of the two skills it is about.

**Proposed authoring rule, going into §7:**

> A misconception whose label names a confusion *between* two things attaches to **both**
> skills. If only one attachment is defensible, the label is describing a one-sided error
> and should be reworded to say so.

With those two attachments fixed, the proxy flags 12 chains and agrees with the reading on
every one. **The rule is what makes the criterion checkable rather than a judgement call
repeated 17 times.**

*Also worth noting from the same scan, and it is a design strength rather than a bug:* nine
misconception ids are shared **across** chains, and one —
`mis.transform.horizontal-direction` — is attached in `chain.linear.forms` on
`linear.form.point-slope`, four chains before the transform arc. That is the sign flip in
`y - y₁ = m(x - x₁)` and in `f(x - h)` correctly identified as the same error. The registry
is capturing a real structural connection, and point-slope is planting the misconception
the transform chain later has to resolve.

---

## 3. Where integration is already a *skill*, it should not also be an activity

Three chains name their own integrative competence in the graph:

- `linear.form.convert` — *select the efficient form for a given task*
- `function.repr.correspondence` — *identify the same function across graph, table, equation, context*
- `transform.compose-order` — *apply multiple transformations in the correct order and explain why order matters*

Where the graph already names the discrimination as a skill, §14's interleaving lives in
**that skill's independent beat**, and a separate consolidation activity would teach the
same thing twice. So for `function.representations` the slack goes entirely to parts.

`linear.forms` and `transform.compose` still earn one, because in both the shared
misconception spans skills the integrative one does not cover — `m-b-swapped` runs across
three form skills, and `horizontal-direction` is a sign error, not an ordering error.

---

## 4. The audit — all 17 chains

`C` = consolidation · `P` = additional skill part

| chain | sk/act | slack | ruling | why |
|---|---|---|---|---|
| `rate.proportional` | 3/4 | 1 | **1C** ✓ done | three faces of one relationship |
| `linear.slope` | 3/5 | 2 | 1C + 1P | rise/run inverted across two skills |
| `linear.forms` | 5/8 | 3 | 1C + 2P | `m-b-swapped` spans three skills |
| `linear.model` | 1/3 | 2 | **2P** → `= 3` | single skill; nothing to confuse |
| `function.definition` | 2/3 | 1 | **1C** | VLT applied ritually without connecting to the definition it tests |
| `function.notation` | 2/4 | 2 | **1C** + 1P | §14's canonical case: evaluate f(3) vs solve f(x)=3 |
| `function.representations` | 1/3 | 2 | **2P** → `= 3` | correspondence *is* the skill (§3) |
| `function.domain-range` | 2/3 | 1 | **1P** | graph→context is sequence, not confusability |
| `function.families` | 2/2 | 0 | none ✓ | `y = x` and `y = x²` are not confusable |
| `transform.translate` | 2/2 | 0 | **1C — needs +1 activity** | see §5 |
| `transform.stretch-reflect` | 3/4 | 1 | 1C | `inside-outside` across reflect and h-stretch |
| `transform.compose` | 3/5 | 2 | 1C + 1P | `horizontal-direction` across two skills |
| `roc.average` | 5/7 | 2 | 1C + 1P | `uses-endpoint-value` across two skills |
| `limit.intro` | 3/4 | 1 | 1C | `equals-substitution` across numeric and graphical |
| `limit.difference-quotient` | 3/5 | 2 | 1C + 1P | `f-of-a-plus-h-distributed` across setup and simplify |
| `deriv.definition` | 3/5 | 2 | 1C + 1P | three views of f′(a): limit, tangent slope, contextual rate |
| `deriv.rules` | 4/6 | 2 | 1C + 1P | `constant-rule-confused` across power rule and constant |

**Totals: 12 consolidations, 14 additional parts, 26 allocated — plus 1 new activity.
Plan moves 73 → 74.**

Two `= n` declarations are forced by chain shape and can go in the registry now:
`linear.model.contextual = 3` and `function.repr.correspondence = 3`. The other 12 extra
parts are chain-level allocations; which skill within a chain takes the extra part is an
authoring decision and should be made when the chain is written, not now.

---

## 5. `chain.transform.translate` — the plan is short by one

You are right, and by the criterion it earns a consolidation more clearly than
`chain.rate.proportional` did. Its two skills are `f(x) + k` and `f(x - h)`; the
highest-value misconception in the thread is *the confusion between them*; and the chain is
budgeted with no room to interleave them.

**This is a §10 budget question and the answer is to add the activity, not to compress.**
Folding the interleaving into the second skill's activity would push it past the duration
cap, and §5 is explicit that the faded beat is what gets sacrificed when an activity runs
long — which D5 makes a hard error precisely because it is the first thing to go.

`chain.function.families` I agree: no confusion, zero slack is correct.

Your floor observation is worth recording too — no chain has fewer activities than skills,
so every chain is buildable at one activity per skill and the 26 really are pure slack.

---

## 6. Your other four, accepted

**§2, alignment shape.** `ncea: []`, and **all four fields become arrays** while every value
is empty. You are right that many-to-many is the real cardinality — one standard spans
several skills, one skill serves several standards — and right that a mixed shape bites a
consumer later. Also accepted, and worth stating so nobody expects otherwise: **the field
makes the claim recordable, not checkable.** Whether a DoL assesses at the right level stays
a human read.

**§3, the hook trigger.** Taken. *Every chain registered in `chain-registry.txt` has a
non-empty hook pool* is the right check and it costs nothing — registration is exactly the
moment the pool is owed. You are also right that my authoring-order rule was a discipline
with no trigger, three letters after we established that unenforced rules decay. It runs on
our side and `chain.rate.proportional` fails it today, correctly.

**§4, merge-before-regenerate as a standing step.** Taken, in your order: *propose ids →
merge into the graph → regenerate the registry → author the bindings.* Your point that the
cause is structural rather than accidental is the one that convinced me — every chain
produces distractors, distractors need ids, and the graph is a separate artifact. Chain 13
hits it identically with more bindings and less memory.

Also confirmed from your §4: no misconception id is going spare, so none of the 10 blank
skills can be closed by attaching an existing id. All ten need ids authored.

**§1(b), the JSON denominator.** Yes please, once the `= n` values land. **parts authored /
parts declared** is the burndown number, because it moves while a multi-part skill is
half-written and `covered` stays flat. Two `= n` values are ready now (§4); the rest arrive
per chain.

---

## 7. Activity 04 — closed

Your §5 settles it and I am not re-opening it. The DoL prompt is one claim with a three-part
justification: the student makes a single judgement — *which plan is proportional* — and the
three faces are the evidence required for it. *"Say which, and explain how…"* is a single
imperative with a compound object, and the model answer resolving entirely to *why the plan
is proportional* confirms it.

**So: justification, not a second claim. Activity 04 is a consolidation of
`rate.proportional-graph`, the integration node stays deferred, and everything shipped
stands.**

Reading the prompt rather than the rubric split was the right move; both of us had been
inferring from the marks. Recorded against D24 so the deferral trigger is not re-litigated.

---

## 8. State

| | |
|---|---|
| **Curriculum** | Fix the two one-sided attachments (§2); add the §7 attachment rule; add the `transform.translate` activity; declare the two forced `= n` values. |
| **Platform** | Alignment fields as arrays; `declaredParts` in the JSON once `= n` exists. |
| **Closed** | D24 ruled. Activity 04. The hook trigger. Merge-before-regenerate. |
