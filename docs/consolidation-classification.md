# Does the builder's account change the classification?

**Re:** the original builder's account of what activity 04 was built for
**Date:** 2026-08-26 · **Audience:** platform side, coding agent, curriculum side

---

## 0. Short answer

**The ruling on activity 04 does not change.** `skill: rate.proportional-graph`, with
unit-rate and k as `supporting_skills:`. Every job the builder describes is something
the principles already assign to a *component inside an activity*, not to a skill. No
new node.

**But the account breaks D23 as I wrote it**, and it exposes a category the
classification does not have. A consolidation activity and a part 2 are structurally
different things that currently look identical to the platform, and coverage is about
to be computed on top of that.

Two corrections to the account itself are in §5 — both are places where the builder is
working from a rule the corpus does not contain, which matters more than the activity
question because they will propagate.

---

## 1. Why the ruling survives the account

The builder gives activity 04 three jobs. Each maps to an existing home:

| Stated job | Where it already lives |
|---|---|
| Integrates the three skills into one idea | §1 — consolidation *after* schema exists. A property of when an activity sits, not a competence. |
| Interleaves and discriminates | §14 — a rule about the **independent beat** of any activity, once two confusable skills exist. Not a skill. |
| Chain exit check | §8 — the DoL rule, which is uniform across activities. |

None of the three requires a node, and the durability test from the earlier exchange
still fails: nothing downstream would declare an edge to "integration." The platform's
corpus evidence stands — k is taught as the unit rate renamed in activity 02's own
words, so the "three faces" are two, and "a line through the origin whose steepness is
that number" is the definition of `rate.proportional-graph` rather than a fourth thing.

**One point in the account initially looks like it cuts the other way and does not.**
The builder says the DoL's review item reaches an ancestor three edges back (fraction
arithmetic), which sounds unlike a part 2. It isn't: §8's DoL rule is uniform — one item
on the primary skill, one on a review-pool skill **two or more** rows back — and applies
identically to part 1, part 4, and everything between. Three edges back satisfies it. It
is not evidence of a special position.

---

## 2. What the account does change: consolidation is not a part

The builder is explicit: **"Part 4 teaches no new skill; its job is to weld the three
together."**

That is a different object from a part 2. Compare:

| | **Part 2 of a skill** | **Consolidation** |
|---|---|---|
| Teaches | continues one skill, faded harder (§5) | nothing new |
| Independent beat | practice on that skill | interleaved across the chain (§14) |
| Belongs to | the skill | the chain |
| Skill taught after it? | not until the last part | already fully taught before it |

Under the classification I sent, both are "a second activity naming skill X," and D23
counts both against the skill's declared part count. **That makes coverage lie in the
wrong direction.**

`rate.proportional-graph` is fully taught by activity 03. If activity 04 is counted as
its part 2, the registry declares `rate.proportional-graph = 2`, and coverage reads
**partial (1 of 2)** for a skill that is completely taught. The whole point of the part
count was to stop coverage over-claiming; miscounting a consolidation makes it
*under*-claim instead, which is worse — it hides completed work and will read as a gap
in a burndown both sides are consuming.

---

## 3. The fix: a third chain role, and one platform-readable marker

Every activity in a chain is one of:

1. **Part** — teaches a skill, or continues teaching it. Counts toward that skill's
   declared part count.
2. **Consolidation** — teaches no new skill. Names the chain's terminal skill as primary
   for §2 compliance, and **does not count toward its part count**.
3. Everything else — the platform's existing `role:` vocabulary (`review`, `practice`)
   already covers activities that are not day-of-teaching content.

**The marker has to be a real key, not `x_`.** Coverage depends on it, so the platform
must read it. Proposed:

```meta
key: act.rate.proportional-consolidation
skill: rate.proportional-graph
supporting_skills: rate.unit-rate, rate.constant-of-proportionality
chain_role: consolidation
```

Absent means `part`, so nothing already written needs editing and the ~90% case stays
silent. One value, one meaning.

With that, `rate.proportional-graph = 1` in the registry — correct, since one activity
teaches it — and activity 04 sits in the chain without distorting the skill's coverage.

---

## 4. Three checks that now need rescoping

All three were specified in the last reply assuming part-vs-part. Each false-fires on a
consolidation:

- **The activity-count-exceeds-declared-parts warning (D23).** Would fire on
  `rate.proportional-graph` immediately — two activities, one declared part. Count only
  `chain_role: part` activities against the declared count.
- **The shared-DoL-target guardrail.** "Parts of one skill share a DoL target" is a rule
  *about parts*. A consolidation's DoL is a chain exit check and may legitimately target
  differently. Scope the check to parts.
- **The adjacency check (their §3.5).** A consolidation shares a primary skill with a
  part it need not sit next to — it sits at the end of the chain, which may be several
  activities from the part that taught the skill. Scope to parts, or it warns on every
  chain that ends with one.

Activity 04 happens to pass all three today, because it sits directly after activity 03.
That is luck, not design, and it will stop being true in the first chain where the
terminal skill is taught mid-chain.

---

## 5. Two corrections to the account — these matter more than the activity

Both are cases of the builder applying a rule that is not in the corpus. Flagging them
because they will recur in the next chain if they are not caught.

**5.1 There is no "final-position rule" for the DoL.** The account says the DoL "follows
the final-position rule — one item on the chain's terminal skill plus a review item
reaching an ancestor three edges back." §8 states one DoL rule and it is uniform: exactly
two items, one on the primary skill, one on a review-pool skill two or more rows back.
Activity 04's DoL satisfies it, so nothing is wrong with the activity — but the *rule
being cited does not exist*, and a rule invented once tends to be applied again. If a
final-position DoL variant is genuinely wanted, it is a principles amendment and a
decision-log entry, not a thing to infer from position.

**5.2 Hooks are not homed in activities.** The account calls activity 04 "the natural
home for the eggs hook." D9 and §4 are explicit that hooks are a **chain-level pool** and
activities never carry them — the teacher fires one when their class day starts, because
period boundaries are classroom facts the data model cannot see. Per-activity hooks were
considered and rejected.

The underlying intuition is fine and in fact correct: under the
`Hook · Activity · Activity · Hook · Activity · Activity` layout, hook 2 heads activities
3 and 4, so the eggs hook would in practice open the day that covers activity 04. The
error is only in "home for" — it must not become a field, a pointer, or an ordering
assumption in code. This is the third time a lesson-level concept has tried to land on the
activity (D9 records the first two).

---

## 6. The question the coding agent most needs answered

The builder's own caveat is the important sentence in the account:

> *"the 4th activity should be a consolidation" was a design call I proposed and you
> approved, not something the plan dictated — the projection just said "4 activities."*

So the slot existed first and the purpose was fitted to it. That is backwards from §10,
where content determines activity count ("content that does not fit becomes another
activity in the chain"), and it means **n = 1** for this shape.

**This has to be ruled before the next chain is authored**, because a coding agent or a
drafting model given four activities and one consolidation will infer a pattern from a
single instance:

- **If consolidation is a pattern** — every chain ends with one — then it belongs in the
  principles, the chain projection should budget for it explicitly, and `chain_role`
  becomes something the validator can expect rather than merely tolerate.
- **If it was an opportunistic use of a spare slot**, then it must *not* be replicated by
  pattern-matching, and the projection for chain 2 should be derived from content as §10
  requires, with a consolidation added only if the content argues for one.

I lean toward the first — consolidation is genuinely the highest-value use of a terminal
slot, §1 explicitly reserves richer tasks for the end of a topic, and §14 discrimination
needs a home once several confusable skills exist. But it is a curriculum call, not a
platform one, and it should be made deliberately rather than inherited from the shape of
one projection.

---

## 7. Net changes to what has already been sent

| Item | Change |
|---|---|
| Activity 04's primary skill | **No change.** `rate.proportional-graph`. |
| `rate.proportional-graph` part count | **Changes to 1**, not 2 — activity 04 is not a part. |
| D23 | **Amend.** Only `chain_role: part` activities count against the declared count. |
| New platform ask | `chain_role: part \| consolidation`, absent = part. One key, read by the coverage manifest. |
| DoL guardrail, adjacency check | **Scope to parts.** |
| Principles | Open question in §6 above — is consolidation a chain-terminal pattern? |
