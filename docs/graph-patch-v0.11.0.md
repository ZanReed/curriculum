# Graph patch — `thread-01-rate-of-change.json` v0.10.0 → v0.11.0

Every change the reconciliation identified, in one place. Five edits: one merge, three
corrections, one addition.

Verified against the file: none of the four new ids collides with the existing 18, and
all three target skills exist with `misconceptions: []`.

---

## 1. Merge the rate misconceptions — **do this before regenerating the registry**

The catalogue's `misconception-registry.txt` is currently the **good** copy: 13 live
bindings validate against it, strict run green. The graph is the stale one. Regenerating
from the graph today replaces a working registry with one that fails all 13.

Ratifies `claude_misconception-proposals.md`, which has been sitting proposed. Four ids,
each backed by a distractor that already exists in the authored activities — every one a
live sensor rather than a dead binding.

**Append to `misconceptions` (18 → 22):**

```json
{ "id": "mis.rate.ratio-inverted",                   "label": "Divides the quantities the wrong way round — x ÷ y instead of y ÷ x" },
{ "id": "mis.rate.compares-totals",                  "label": "Compares total amounts (or picks by quantity) instead of the amount per one" },
{ "id": "mis.proportional.one-pair-assumed-constant","label": "Concludes a relationship is proportional from one pair without checking the ratio is constant" },
{ "id": "mis.proportional.line-misses-origin",       "label": "Believes a proportional graph need not pass through the origin" }
```

**Attach to skills:**

| skill | `misconceptions` becomes |
|---|---|
| `rate.unit-rate` | `["mis.rate.ratio-inverted", "mis.rate.compares-totals"]` |
| `rate.constant-of-proportionality` | `["mis.rate.ratio-inverted", "mis.proportional.one-pair-assumed-constant"]` |
| `rate.proportional-graph` | `["mis.proportional.line-misses-origin"]` |

This also completes D21: the two-prefix scheme was ratified on the platform's
near-duplicate evidence, but the ids it described lived only in the catalogue. After this
merge the ratification describes something that exists.

*Still deferred, correctly:* `mis.rate.units-dropped`. It has no sensor —
numeric blanks carry no units and contextual checks are rubric-graded. Worth noting that
`mis.slope.units-dropped` and `mis.deriv.units-dropped` are **already registered**, so the
naming is settled and only the sensor is missing. The cheapest route is the error-analysis
mc the proposal describes; under D10 (NCEA-first, rubric-heavy) that item type is the main
auto-scorable data source anyway.

---

## 2. 🚨 `grading_model` — the false claim, fix first

Two sentences assert auto-scores are client-computed. Both are false about this platform:
grading runs server-side and has no client caller. This is the row to fix even if the
two-source question stays open, because it is the machine-readable copy and a session told
to align code to it would move grading client-side and reopen the answer-leak surface the
sanitize-and-strip design exists to close.

**`scoring`** — replace `auto = client-side against a baked key` with:

> `auto = server-computed against a baked key, advisory`

**`authoritative`** — replace the sentence beginning *"All auto scores are
client-computed…"* with:

> Only teacher-entered grades are server-authoritative. Auto scores are server-computed
> but advisory — the raw responses are the trustworthy signal, the correctness booleans
> ride along unverified.

What the original got right and must survive: the **advisory vs authoritative**
distinction. Only the *where it computes* clause was wrong. This does not reopen D8.

---

## 3. `hook_contract.minimum` — projected → approved

```
- "ceil(projected_activities / 2) hooks per chain"
+ "ceil(approved_activities / 2) hooks per chain"
```

`projected` books 37 hooks across the plan against work that may never be authored, and
D9's reasoning — a hook must be *open* on the day it is fired — only means anything
against activities that exist. Both sides independently reached `approved`.

All 17 chains currently hold `hooks: []`, which under `approved` is correct (0 approved
activities), and under `projected` was a 37-hook debt.

---

## 4. `status_values.approved` — add D6's second condition

The entry states only the human read. D6 gates approval on **two** conditions.

```
- "Read end to end by a human and judged teachable."
+ "Read end to end by a human and judged teachable, AND depending on no capability
+  whose status is 'proposed'. Publishing is the mechanism; this is the predicate."
```

Without the second clause, an activity depending on `seeded_data` or
`nway_correspondence` can be marked approved — which is the exact failure D6 was written
for, after the four-way correspondence activity was marked approved while needing an
unshipped capability.

---

## 5. `review_selection` — add the D16 broadening and the floor clause

**`candidate_pool`** currently reads *"transitive ancestors of primary_skill in this
thread plus external_prereqs."* D16 broadened it and the JSON never received the change:

```
+ "...plus transitive ancestors of any later skill in the same chain, marked
+  planting_for. D16: adding a prereq edge instead would assert a dependency that is
+  not real (D2)."
```

**`constraint`** needs the floor clause, or `--strict` fails activity 01 permanently.
`rate.unit-rate` is the only skill of 47 whose ancestor depth is below 2 — its sole
prereq is `ext.arith.fractions`, at distance 1 — so nothing exists two rows behind it:

```
- "at least one item per slice must come from edge_distance >= 2"
+ "at least one item per slice must come from edge_distance >= 2, OR from the deepest
+  ancestor available where the graph is shallower than 2. The floor exists because
+  the graph is shallow at the top of the curriculum; without it the first activity of
+  the first chain fails validation and the only way to satisfy the rule would be to
+  author a fictional intermediate skill."
```

The same floor applies to `chain_rules.final_position` (edge distance ≥ 3) and to §8's
DoL rule. Write it once and have both cite it.

**`chain_rules.final_position` is correct and stays.** It is the rule I wrongly told the
platform did not exist. Activity 04 satisfies it exactly — `ext.arith.fractions` is
precisely 3 edges from `rate.proportional-graph`.

---

## 6. Not changed, and why

- **`alignment` stays null.** The file's own note is right: *"fill from source documents
  rather than trusting anyone's memory of them."* Worth flagging separately that the
  alignment object has `teks`, `ccss` and `nzc_phase` but **no NCEA field**, while D10
  makes `nz-ncea` the default locale. `nzc_phase` is the NZ Curriculum, not NCEA. That is
  a gap to fill from source documents, not from here.
- **`activities: []`** stays empty. The platform's coverage manifest is the artifact of
  record (D19) and this array is the duplicate that would drift — it already has, reading
  0 while four exist.
- **`authoring_principles`** is byte-identical to the `.md`. Nothing to do; D13 holds.

---

## 7. The larger question this patch does not settle

Five of these six edits exist because **authoring rules live in two places** —
`authoring-principles.md` in prose and `activity_defaults` in JSON — with no rule about
which wins.

My earlier recommendation (prose authoritative, JSON becomes a generated projection) was
under-specified: generating structured constraints *from* prose is not tractable. **The
workable version is a partition, not a projection:**

- **Any fact a validator reads** — phase budgets, edge distances, hook minimums, status
  values, contract shape — lives in `activity_defaults` and **nowhere else**. The prose
  cites the key rather than restating the value.
- **Any reasoning a drafter needs** — why review comes first, why faded is mandatory, what
  a hook is for — lives in the prose and **nowhere else**.
- Nothing appears in both. Where prose must reference a threshold, it names the JSON key.

Under that partition each of the five conflicts resolves by asking one question: does a
validator read this? Final-position, hook minimum, edge distances, status values,
grading model → JSON. The reasoning behind each → prose.
