# Chain hooks

Hooks are a chain-level pool (D9): they are **not** welded to any activity — the teacher
fires one when *their* class day begins, because period boundaries are classroom facts the
data model cannot see. Review still keeps position one inside every activity.

Rules live in `authoring_principles` §4 and `activity_defaults.hook_contract`. In short: one
question, thinkable in under a minute, answerable by intuition or a guess, no prerequisite
knowledge needed to *engage*. It must genuinely connect to a skill in the chain, and it must
**not** front-load the lesson — if answering it needs the worked example, it has become
discovery.

**A hook must still be open on the day it is fired.** The pool spans the chain's distinct
conceptual leaps so that whatever day a teacher starts, there is a hook the class cannot
already answer. Two hooks a student can answer after the same early lesson are redundant —
one of them is doing no work on the later days.

**Authoring order.** The pool is authored at chain creation, before the chain's first
activity. The validator minimum counts *approved* activities, so with none approved nothing
is owed — which makes hooks free, and free things get written last and badly. That is the
retrofitted filler D9 rejected per-activity hooks to avoid. This rule is the counterweight and
no validator enforces it.

**Screening.** Every hook here is a draft until a human marks it approved. This doc is the
holding pen; the pool is `chains[].hooks` in the thread JSON.

---

## chain.rate.proportional — **screened and merged (v0.13.0)**

Skills: `rate.unit-rate` · `rate.constant-of-proportionality` · `rate.proportional-graph`
Two hooks, matching `ceil(4 / 2)` on the projection. This chain has two conceptual leaps
worth a hook — comparing rates, and proportional versus not. The constant of proportionality
needs no hook of its own (*k is the unit rate, renamed*), so any unit-rate hook already opens
that day.

**`hook.rate.better-value`** → `rate.unit-rate`

> Two shops sell the same lollies. One sells a bag of 5 for \$4. The other sells a bag of 12
> for \$10. Which bag is better value — and are you sure?

80c versus about 83c. The bigger bag looks like the obvious deal and is not, so the guess is
worth committing to and the reveal is a genuine surprise. Does not disclose the
divide-to-compare method. Not open after activity 01, which is correct for the chain's
opening hook.

**`hook.rate.doubles-or-not`** → `rate.proportional-graph`

> After 2 minutes of filling, a paddling pool is 10 cm deep. After 2 weeks of growing, a
> seedling is 10 cm tall. One of these you can predict at double the time. The other you
> can't. Which is which?

**Stays open after activities 01–02**, which is the property the pool exists for: a student
who can find a unit rate — 5 cm/min, 5 cm/week — will confidently double both, and that is
the error. Probes whether doubling the input doubles the output, which is what a line through
the origin *means*, so it opens the day on `mis.proportional.line-misses-origin`. Names no
graph, origin or line, so it does not front-load. Both quantities are continuous, so every
point on the eventual line means something.

---

### Cut, with reasons

**Former Hook 1 numbers — \$3 for 4 versus \$5 for 7.** Kept the hook, changed the numbers.
\$0.75 versus \$0.71 is a 5% gap, so the reveal was *"you were nearly right either way."* A
hook earns its lesson by making intuition visibly insufficient; here intuition was fine. The
replacement inverts it so the obvious answer is wrong.

**Former Hook 2 — "2 eggs for 3 people… how many for 0 people, and how could you prove it by
graphing?"** Cut for three reasons, the third decisive:
1. The intuition question cannot be wrong — nobody answers anything but zero — so it carries
   no commitment worth testing.
2. *"How could you prove your answer by graphing"* hands over the method. Establishing that a
   proportional graph passes through the origin is the lesson's job.
3. **Eggs are the wrong context for a graph about proportional relationships.** 2 eggs for 3
   people is ⅔ of an egg per person; a proportional graph is a continuous line through the
   origin, and every non-integer point on this one is meaningless. A defect in the context,
   not the wording, so it could not be reworded out.

**"1-litre juice \$2.50 versus 2-litre \$4.50 — is the bigger one always the better deal?"**
Cut as redundant with Hook 1: both answerable the moment a student can compute a unit rate, so
it opened no later day. It also confirmed the intuition rather than surprising — the right
diagnosis, but the remedy was to invert the numbers rather than drop the idea, which is what
the revised Hook 1 now does.

---

## Remaining 16 chains

No pools authored. Under the authoring-order rule each is owed one at chain creation, so the
next is `chain.linear.slope` — 3 skills, 5 activities, minimum 3 hooks by projection.

⚠ **A note on the hook-pool trigger (B6).** The proposed check was *every chain registered in
`chain-registry.txt` has a non-empty hook pool*, on the premise that a chain is registered when
its folder is created. All 17 were registered at once instead, to fix the ordinal numbering
while renumbering was still free — so the check as specified would fail on 16 chains that have
no folders and no activities. **It should key on folder existence, not registry entry.** The
premise was broken by a deliberate choice made for a different reason, which is worth
recording rather than letting the check be written and then switched off.
