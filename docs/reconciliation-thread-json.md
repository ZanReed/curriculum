# Reconciliation against `thread-01-rate-of-change.json` v0.10.0

**Date:** 2026-08-26 · **Status:** blocker cleared; four prior conclusions corrected

---

## 0. What the file settles

The graph exists and is complete: **47 skills across 17 chains, 73 projected activities,
5 external prerequisites, 18 registered misconceptions, 22 capabilities (18 shipped,
4 proposed), no dangling prereq references.** The `authoring_principles` string is
byte-identical to `authoring-principles.md`, so D13's single-source claim holds exactly.

Three registries are generated and attached. `--strict` is unblocked.

**But the file also contradicts four things this exchange concluded**, one of which I got
wrong and told the platform. Those are §1–§4. The rest is §5 onward.

---

## 1. ⚠ I was wrong: the final-position rule exists

I told the platform the builder had cited *"a rule the corpus does not contain,"* and
warned that an invented rule tends to be applied twice. **That was my error, from
incomplete context.** The rule is real:

```
activity_defaults.chain_rules.final_position:
  "Exit check must include at least one item on the chain's terminal skill and
   one review item from an ancestor at edge distance >= 3."
```

The builder's account described it accurately, including the edge distance. And activity
04 satisfies it exactly: its DoL item 2 is `ext.arith.fractions`, which is **precisely 3
edges** from `rate.proportional-graph` (→ k → unit-rate → fractions). Not "comfortably
more than two rows back" — exactly three, which is the rule's floor.

**This retraction has to reach the platform**, because I asked them to treat a
correctly-applied rule as drift.

The `_docs` correction I sent them stands; this one does not.

---

## 2. 🚨 Rules live in two places, and they disagree

The real finding under §1. **`authoring-principles.md` is not the only source of
authoring rules.** `activity_defaults` in the thread JSON carries a second set, in JSON
rather than prose, and the two are not reconciled:

| Rule | Principles (prose) | `activity_defaults` (JSON) | Status |
|---|---|---|---|
| Final-position exit check, ancestor at distance ≥3 | **absent** | `chain_rules.final_position` | JSON only |
| Review pool broadened to later chain skills, `planting_for` (D16) | decision log | `review_selection.candidate_pool` says ancestors + externals only | prose/log only |
| Hook pool minimum | `ceil(activities / 2)` | `ceil(**projected**_activities / 2)` | **conflict** — see §4 |
| Auto-scores | corrected to server-computed (D8 amendment) | `grading_model` still says client-side, **twice** | JSON stale |
| Approval gate | D6: human read **and** no proposed-capability dependency | `status_values.approved` states only the human read | JSON incomplete |

This is D7's own failure mode — *"two prompts describing one platform"* — reappearing as
two rule sets describing one contract. It is the more dangerous version, because the
prose one is injected into every drafting prompt while the JSON one is what a codebase
would read.

**Ruling needed, and it is the biggest open item in the project right now:** which is
authoritative? My recommendation is that the prose is authoritative for *pedagogy* and
`activity_defaults` becomes a generated projection of it — the same move D7 made for
capabilities and D13 made for the principles. What must not persist is two hand-maintained
sets, because that is precisely what D3 forbids and this exchange has now caught it twice.

---

## 3. 🚨 Activity 01 cannot satisfy the two-rows-back rules, and the graph says why

Computed over the real graph:

```
rate.unit-rate                 ancestors: ext.arith.fractions            max depth 1
rate.constant-of-proportionality  unit-rate (1), fractions (2)           max depth 2
rate.proportional-graph        k (1), coordinate-plane (1),
                               unit-rate (2), fractions (3)              max depth 3
```

**`rate.unit-rate` is the only skill of all 47 whose ancestor depth is less than 2.** It
is also the primary skill of activity 01.

So the platform's resolution of rule 7 rests on a wrong assumption. They wrote that
activity 01 *"satisfies it comfortably (three fraction items, well more than two rows
back)."* All three fraction items sit at **distance 1**. Activity 01 violates rule 7a on
review *and* §8's DoL rule — and it cannot do otherwise, because nothing exists two rows
behind unit rate.

**This is a rule-scope problem, not a corpus problem, and it is narrow.** One skill of 47.
The fix is a floor clause:

> …two or more rows back, **or the deepest available ancestor where the graph is
> shallower than two.**

Without it, a validator running `--strict` fails the first activity of the first chain on
day one, and the only correct response would be to author a fictional intermediate skill
to satisfy it.

*Corollary worth stating:* my rule 7a/7b split still holds and is still the right
annotation — 7b (the DoL carrying spaced retrieval at positions 2+) is confirmed by the
real distances for activities 02, 03 and 04. Only the claim about activity 01 was wrong,
and it was the platform's, not mine.

---

## 4. Hook minimum: projected or approved?

`hook_contract.minimum` reads **`ceil(projected_activities / 2)`**. The architecture doc
and the §11 validator table say the check runs against **approved** activities.

These are very different rules. For `chain.rate.proportional`: projected 4 → **2 hooks
required now**; approved 0 → **0 hooks required now**. Across the whole plan, projected
gives 73 activities → **37 hooks owed** before anything is authored.

Every one of the 17 chains currently has `hooks: []`.

I think **approved** is right — a hook pool sized to a projection is a debt against work
that may never be authored, and D9's reasoning was about a hook being *open* on the day
it is fired, which only makes sense against real activities. But the JSON says otherwise
and it is the machine-readable copy. Rule it.

---

## 5. 🚨 The live misconception bindings reference unregistered ids

The registry holds 18 ids. **None is `mis.rate.*` or `mis.proportional.*`** — the set
begins at `mis.slope.*`. And all three rate skills carry `misconceptions: []`.

Meanwhile the platform reports **13 live bindings** across the four activities, and
`claude_misconception-proposals.md` proposes exactly the `mis.rate.*` /
`mis.proportional.*` ids those bindings would use.

**So the moment `misconception-registry.txt` is generated from this graph, all 13 live
bindings warn — and fail under `--strict`.** The rate chain was authored after the graph
was frozen and its misconceptions were proposed but never merged back.

This also weakens D21. I ratified the two-prefix scheme on the platform's report that the
distinct prefixes help their near-duplicate detector across 13 bindings. That evidence is
real, but the ids it describes **are not in the registry**, so what was ratified is a
naming convention for a set that does not yet exist. The ratification stands; the merge
is outstanding and is now a blocker for `--strict`, not a tidy-up.

*Also empty:* 13 of 47 skills carry no misconceptions at all.

---

## 6. Confirmations — things the file proves right

- **D19 was correct.** `activities: []` in the graph while four exist on the platform. The
  builder-side count would report zero. Making the platform manifest the artifact of
  record was the right call, and this is the drift it prevents, already present.
- **D13 holds exactly.** `authoring_principles` is byte-identical to the `.md`. Zero drift.
- **D9's chain-level rule is explicit in the JSON**: *"Activities never carry hooks; days
  do."* The builder's "natural home for the eggs hook" was loose against a stated rule —
  that flag stands.
- **D22 is confirmed by the plan itself**: 73 activities across 47 skills, 1.55 per skill.
  Activities-per-skill > 1 is the designed norm, not a smell.
- **The four proposed capabilities** are exactly `draggable_curve`, `nway_correspondence`,
  `seeded_data`, `graded_polynomial`. 18 shipped.
- **Review pool includes external prereqs** —
  `review_selection.candidate_pool: "transitive ancestors of primary_skill in this thread
  plus external_prereqs"`. This is why the registry split in §7 is necessary rather than
  tidy.

---

## 7. The three registries — attached

**`skill-registry.txt`** — 47 ids, grouped by chain in teaching order with labels as
comments. All bare: nothing is chunked into multiple parts yet, and
`rate.proportional-graph` ships bare per the platform's correction (activity 04 is a
consolidation, carved out by `chain_role`, not by the denominator).

**`external-prereq-registry.txt`** — a new file, and a new platform ask. The 5 external
prereqs are valid review, DoL and prereq targets but are **not skills this curriculum
teaches**. They must resolve during validation and must never count toward coverage. A
single merged registry cannot express that difference, and merging them would inflate the
denominator from 47 to 52 with five skills that will read *uncovered* forever.

**`chain-registry.txt`** — all 17 chains with folder ordinals fixed now, while renumbering
is still free. Titles are mine and are the one part of this that is a judgement call
rather than a transform; change any of them freely.

*Note for the platform:* their invented example `chain.linear.slope` turned out to be
real — it is chain 2. `proportional.graph-through-origin` was not; `rate.proportional-graph`
is confirmed correct, as they said.

---

## 8. What to do next, in order

1. **Send the retraction** (§1) before the platform acts on my drift flag.
2. **Rule the two-source problem** (§2). Everything else is downstream of knowing which
   copy wins.
3. **Add the floor clause** to the two-rows-back rules (§3), or `--strict` fails activity
   01 permanently.
4. **Rule projected vs approved** for the hook minimum (§4).
5. **Merge the rate misconceptions into the graph** (§5) before generating
   `misconception-registry.txt`, or 13 live bindings break.
6. Ship the three registries.

Items 1–5 are curriculum-side calls. Only 6 involves the platform.
