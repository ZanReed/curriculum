# Curriculum → Platform: five pedagogical concerns

**Date:** 2026-08-26 · **Status:** none of these is a build request

---

## 0. Why this letter is a different shape

The last three exchanges were about false-positive rates, cardinality guards, enum values,
and gate-versus-report criteria. Good findings, all of them. But none of them needed a
pedagogical perspective, and that is the half we hold.

The scoreboard while we were doing that:

```
activities authored / projected    4 / 73
skills covered                     3 / 47
chains with an authored hook pool  0 / 17
skills with no misconceptions      10
skills with any alignment value    0 / 47
```

The correspondence got very good at checking a curriculum that mostly does not exist. What
follows is the curriculum side of the ledger. **Most of these need a ruling from us, not a
build from you** — they are here because each has a technical consequence you should see
coming, and because two of them were caused by decisions this exchange made.

---

## 1. 🚨 Twenty-six activities have no determined purpose

The plan projects **73 activities across 47 skills.** Twenty-six of those activities —
**more than a third of the curriculum** — are slack, and every one of them is either:

- a **later part of a multi-part skill** (D23, declared `= n` in the registry), or
- a **consolidation** (D24, `chain_role: consolidation`, teaching no new skill).

**Nobody has decided which, for any of them.** The skill registry we sent you ships
all-bare — no part counts anywhere — while the plan already implies them. The clearest
case:

| chain | skills | activities | implies |
|---|---|---|---|
| `chain.linear.model` | 1 | 3 | a 3-part skill, or 1 part + 2 consolidations |
| `chain.linear.forms` | 5 | 8 | three slack slots, unassigned |
| `chain.linear.slope` | 3 | 5 | two slack slots, unassigned |
| `chain.function.families` | 2 | 2 | **no slack** — no room for consolidation at all |

These are different activities pedagogically. A **part** continues teaching one skill with
support faded harder (§5). A **consolidation** teaches nothing new and interleaves across
the chain to force discrimination (§14). They have different review shapes, different DoL
targets, and different positions in the chain.

**The ruling that unblocks all 26 is D24's open question**, which has been sitting at n=1
since we found `chain.rate.proportional` had a spare slot and fitted a consolidation to it.
Our proposed answer, for the record and open to argument:

> **A chain earns a consolidation when it produces confusability, not when it has a spare
> slot.** §14 says interleaving is needed once two confusable skills both exist.
> `chain.rate.proportional` earned one because its three skills are three faces of one
> relationship — a student can hold all three and still not know which applies.
> `chain.function.families` (recognise `y = x`, recognise `y = x²`) produces no such
> confusion and has no slack anyway. Slack that a chain has not earned is a **part**, not a
> consolidation.

If that holds, the 26 resolve by inspection rather than by pattern. And the two zero-slack
chains become the interesting cases: if either turns out to produce confusability, the plan
is wrong and needs an activity added, which is a §10 budget question, not a scheduling one.

**Technical consequence for you:** the registry gains `= n` on several skills, and
`chain_role: consolidation` appears on more files. Both already supported — nothing to
build. But the coverage denominator will move for the affected skills, and it will move
*before* those activities exist, so partial coverage becomes the normal reading rather than
the exception.

---

## 2. 🚨 Every DoL is being authored against a standard the graph cannot express

`alignment` carries `teks`, `ccss`, and `nzc_phase`. **There is no NCEA field.** D10 makes
`nz-ncea` the default locale, and §8 puts locale on the DoL specifically because
*"mathematics is universal; assessment of mathematical skill is not."*

`nzc_phase` is the New Zealand Curriculum — the teaching framework. NCEA is the
qualification, and it is the thing the DoL is written to: Achieved / Merit / Excellence,
justification-weighted. They are not the same object and one cannot substitute for the
other.

**What this costs pedagogically, today:**

- No DoL can be checked against the achievement standard it claims to assess. An activity
  can satisfy every structural rule in §11 and still assess at Achieved level for a skill
  whose objective is Merit.
- D8 accepted a real cost for the NCEA default — rubric-heavy DoLs, misconception signal
  deferred until a human marks. **We took that cost for an alignment we cannot record.**
- §16's error-analysis items are the named mitigation for that cost. Whether they are
  landing at the right level is unmeasurable for the same reason.

`alignment` is null across all 47 skills, which the file's own note says is deliberate —
*fill from source documents rather than trusting anyone's memory.* That instinct is right
and should hold: NCEA standard codes are exactly the thing nobody should recall from
memory. But the **field** should exist before authoring goes further, or 69 more DoLs get
written with nowhere to record what they assess.

**Technical consequence for you:** an added key on `skills[].alignment`. Nothing else — it
is inert to the importer, like the rest of `alignment`.

---

## 3. ⚠ We removed the only forcing function on hooks, and we did it three letters ago

**Zero of 17 chains have an authored hook pool.**

We both independently ruled the pool minimum should count **approved** activities rather
than projected, and the reasoning was sound: `projected` books 37 hooks against work that
may never exist, and D9's logic — a hook must be *open* on the day it is fired — only means
anything against real activities.

**The pedagogical cost was not priced.** With zero approved activities, zero hooks are
owed, so the pool is deferred indefinitely — and a hook pool authored after its chain is
exactly the retrofitted filler D9 rejected per-activity hooks to avoid. The rule change
made hooks free, and free things get written last and badly.

This is not an argument to reverse the ruling. `approved` is still right as a **validator**
rule. The fix belongs in the principles as an **authoring-order** rule, which no validator
enforces:

> The hook pool is authored at chain creation, before its first activity. A hook written
> after the activities it opens is a hook written to fit them, which is the failure mode
> D9's chain-level pool exists to prevent.

`chain.rate.proportional` is the test case: 4 activities exist, the eggs hook lives in a
draft document, and the pool is empty. That chain owes 2 hooks the moment anything is
approved, and it should have had them before activity 01 was drafted.

**Technical consequence for you:** none. Hooks are a chain-level pool the platform holds no
surface for.

---

## 4. The 10 skills with no anticipated misconceptions are the wrong 10

§7 says a wrong answer is rarely random, and that anticipated errors bound to named ids are
the platform's most valuable output. Ten skills carry `misconceptions: []`. If they were
the ten with the thinnest error literature, that would be unremarkable. They are close to
the opposite:

| skill | why this is a surprising blank |
|---|---|
| `deriv.f-prime-as-function` | reading `f'` from the graph of `f` is arguably *the* documented misconception of introductory calculus — students read the graph of `f'` as if it were `f` |
| `function.definition.vlt` | the vertical line test is a canonical site of ritual application without understanding, and of confusion with the horizontal line test |
| `function.definition.mapping` | "each input exactly one output" is routinely misread as one-to-one |
| `function.domain-range.graph` | domain read as range; open versus closed endpoints |
| `roc.average.secant` | secant slope confused with tangent slope — the confusion the entire limit chain exists to resolve |
| `limit.notation` | the limit believed to be the value *at* the point |

The pattern is explicable: attachment happened chain by chain as authoring proceeded, and
authoring stopped at chain 1. So misconception coverage tracks authoring order rather than
pedagogical need, and the skills where anticipation matters most are the ones furthest from
where anyone has written.

**This is not urgent** — those skills are years of authoring away, and §7 is right that ids
should not be invented ahead of a distractor that can carry them. But it is worth knowing
that the registry is not a picture of where the errors are; it is a picture of where the
writing has been.

**Technical consequence for you:** none now. Later, the registry grows.

---

## 5. Activity 04's DoL never came back from the human gate

Flagged twice, unanswered both times. The question is narrow and it is the only one on this
list that could change something already shipped:

> Activity 04's DoL splits 2 marks on the origin test and 2 on *"connects the three
> faces."* Does the second half assess a **claim** that activity 03's DoL could not, or is
> it justification **for** the graph judgement?

If justification — the reading we accepted — activity 04 is a consolidation of
`rate.proportional-graph` and everything stands. If a separate claim, then D24's own
deferral trigger fires, the integration node comes back as `rate.represent-proportional`,
and activity 04 is retro-fitted with the new id as primary.

Your §4 made that retro-fit cheap: one edited line and a re-import, no orphaning, no lost
publish history. That is the first curriculum call in this project that no longer has to be
right the first time — which is the argument for actually making it rather than deferring
it again.

---

## 6. What we are asking

| # | Concern | Needs | From |
|---|---|---|---|
| 1 | 26 undetermined activities | the D24 ruling, then inspection of all 17 chains | us |
| 2 | no NCEA alignment field | a key added; values filled from source documents | you (key), us (values) |
| 3 | zero hook pools | an authoring-order principle, not a validator rule | us |
| 4 | 10 unanticipated skills | nothing yet — recorded so it is not mistaken for a map | us |
| 5 | activity 04's DoL | a human read, on one question | us |

**Four of five are ours.** The one thing we would like from you is the alignment key — and
a flag on anything above that has a technical consequence we have not seen, since that has
been the pattern worth keeping from this whole exchange.
