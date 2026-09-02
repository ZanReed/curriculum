# Curriculum architecture — reference for the codebase

Derived from `authoring-principles.md`, `decision-log.md`, `markdown-import-format.md`,
`open-questions.md`, and the two in-flight `claude/` drafts. Decision references (D1–D17)
point at `decision-log.md`, section references (§1–§16) at `authoring-principles.md`.

This document describes what the data model *is*, so code organization can mirror it.
It does not restate authoring guidance except where guidance implies a constraint the
code has to carry.

---

## 1. What is being built

An explicit-instruction mathematics curriculum — intro algebra through calculus and
statistics — delivered as **20–25 minute activities** that a platform ingests. It is
built for novice learners acquiring new content: full guidance during acquisition,
support faded gradually, retrieval spaced deliberately, misconceptions anticipated
and named (§1).

Target scale: 47 skills currently in the graph, 0 covered. The six original seed
activities were deleted (D15 amendment); the curriculum starts clean and is authored
NCEA-first (D10).

---

## 2. The object model

Five first-class entities. The relationship that governs everything else: **skills are
durable, activities are disposable** (D1).

| Entity | Id shape | Lifetime | Notes |
|---|---|---|---|
| **Skill** | `rate.unit-rate` | permanent | node in a DAG; carries `band_nz`, `band_us`, `misconceptions[]` |
| **Chain** | `chain.rate.proportional` | permanent | ordered group of skills; owns `hooks: []`; carries a *declared* activity projection |
| **Activity** | opaque | disposable | targets exactly one primary skill; has `status` |
| **Misconception** | `mis.rate.ratio-inverted` | permanent | registry entry: `{ id, label }` |
| **Capability** | registry key | permanent | `status: shipped \| proposed`, constraints, grading model |

### 2.1 Skills form a DAG (D2)

An edge asserts **"you cannot hold this skill without that one."** It is not a
sequencing preference. Two skills that merely tend to be taught together get **no edge**.

Edges are authored at write time, never as a cleanup pass. The reason is economic: the
graph turns review selection from ~900 judgment calls into a query — *ancestors weighted
by staleness × distance × error rate*. That query is the point of the whole structure.

Dual band labels (`band_nz` / `band_us`, Y8–Y13 ↔ Grade 7–Calculus) are **independently
editable and deliberately not synced** (D14) — a skill can genuinely land at different
points in the two systems. Do not add a sync constraint.

### 2.2 Everything references skill ids, never activity ids (D1)

Review pointers, DoL items, misconception attachments, progress data — all of it points
at skill ids. Activities get split, rewritten, and forked; anything holding an activity
id breaks on every rewrite.

**Code consequence:** activity ids should never appear in a foreign key from data that
is meant to survive a rewrite. If a schema field wants an activity id, that is a smell —
check whether it should be a skill id.

---

## 3. The activity contract

Every activity has three components in a fixed order (D4, §3):

```
review → lesson → DoL
             │
             └─ worked → faded → independent   (three mandatory beats, §5)
```

The platform treats all three components **identically feature-wise** — the division
informs the teacher and student, it does not gate anything. But the *authoring* order is
not negotiable, because each position carries a mechanism:

- **Review first** — retrieval of prior skills activates the schema the new content
  attaches to. Placed after the lesson it degrades into practice-of-what-was-just-taught,
  which already lives in the independent beat.
- **Faded is mandatory** (D5) — demonstration straight to independent practice is the most
  common failure in explicit-instruction materials, and it is exactly what an LLM drafter
  produces unprompted. **This is a hard validation error, not a warning.** Mechanical
  enforcement replaced human vigilance on purpose.
- **DoL closes** — and is the only locale-bearing component (§8).

**Time budget** (§10, hard cap 20–25 min): review 4 · worked 3 · faded 6 · independent 8 ·
DoL 3. Overflow becomes another activity in the chain. The faded beat is never compressed
to make room. The cold-start exception was proposed and **cut** (D17, principle G) — the
budget is inviolable.

**DoL shape** (§8): exactly two items — one on the primary skill, one on a review-pool
skill two or more rows back. Contextual items require units in the answer.

---

## 4. Hooks are a chain-level pool

The one structural rule most likely to be mis-implemented, because the obvious model is
wrong (D9).

- Hooks live on the **chain**, in a `hooks: []` array. **Activities never carry a hook.**
- Pool minimum: **`ceil(activities / 2)`** per chain.
- Deployment is **teacher-timed**. The teacher fires a hook when *their* class day begins,
  because period boundaries are classroom facts the data model cannot see — one class
  covers three activities on a block day, another one and a half.
- Review still keeps position one *inside* every activity, always.

The chain **renders** as `Hook · Activity · Activity · Hook · Activity · Activity …` — a
hook heading each pair it opens. This is a layout of the plan on the page: it makes the
`ceil(activities / 2)` ratio a visible cadence so no span of activities displays without
an opener above it. **It orders the pool; it does not schedule it.** With an odd activity
count, the last hook opens the final single activity.

Rejected alternatives, recorded so they are not rebuilt: per-activity hooks (73 obligatory
hooks guarantees filler), one-hook-per-chain (fails the daily requirement on multi-day
chains), one-per-period (unaddressable — the data model cannot see period boundaries).

**Pool coverage rule:** a hook must still be *open* on the day it is fired. Two hooks a
student can answer after the same early lesson are redundant. The pool should span the
chain's distinct conceptual leaps.

---

## 5. Derived state is never declared (D3)

**The single most load-bearing rule for code organization.**

Progress, coverage, chain burndown, review candidates, and wish rankings are **computed**
from `activities[]` + the graph + the registry at render time. They are never stored.

This rule exists because the failure has already happened three times: an `authored[]`
list per chain duplicating what `activities[]` knew (drifted on the first deletion, and
the burndown lied); two prompts describing one platform; a hand-typed format prompt
describing a moved-on codebase. Human-maintained copies of derivable facts drift silently
and are believed confidently.

**The one exception:** per-chain activity *projections* stay declared. An estimate is a
fact about intent, not something derivable.

**Code consequence:** any new field that could be computed from `activities[]` should be
a function, not a column. If a cached projection is genuinely needed for performance, it
must be invalidated by the same write path that touches `activities[]`, never
hand-maintained.

---

## 6. The review pool, and planting

Review draws from the primary skill's **ancestor pool** — skills upstream in the graph
(§6). Not siblings, not vibes.

Broadened by **D16**: the pool is *ancestors of the primary skill, plus ancestors of any
later skill in the same chain*. Items in the second category are marked **`planting_for`**
and the validator **notes** them rather than warning. This exists because an item warming a
skill a later chain member depends on is doing legitimate work, and the alternative fix —
adding the edge — would have violated D2 by asserting a dependency that is not real.

Selection weights: **staleness × distance × error rate**. At least one item must reach two
or more rows back. Chain position governs the slice — Part 1 gets full prerequisite-targeted
review; Part 2+ gets a 60-second retrieval of the previous part only, with recovered
minutes going to independent practice.

**Retrieval is closed-book** (§15, D17-C). An item whose answer is visible on screen tests
navigation, not retention.

> **Ambient constraint — needs implementing.** Per `open-questions.md`, §15 was amended:
> nothing a review item retrieves may appear on the activity's `reference` panel, because
> the panel is open-book for the whole activity. The author choosing sheet content is
> simultaneously choosing what the review may ask. **This is a checkable cross-component
> rule** — see §11 below, it is not yet reflected in the principles text.

---

## 7. Misconceptions are first-class

A wrong answer is rarely random. Anticipated wrong answers bind to **named misconception
ids** (§7). Every mapped distractor is a sensor; this data is the platform's most valuable
output.

**The taxonomy is the user's — the platform never owns the ids.** Ids are opaque tags
validated against the registry.

- **Id shape:** `mis.` followed by dot-separated kebab-case segments. Anything else is not
  a binding.
- **Binding syntax, identical at all three sites:** append `:: <id>`. The id is recognized
  by *shape*, wherever it sits, so the feedback text is optional.
- **Placement rule (§7):** distractor maps go **only on auto-scored, per-item captured
  types** (multiple choice, graph, fill-in-the-blank). On a teacher-graded item the map
  produces no aggregate signal until a human marks it — it is dead weight there.
- **Never invent an id inline.** An unregistered anticipated error goes in a note for a
  human to promote.

**Validation posture:** warnings, never hard failures, except under `--strict`. An
id-shaped token that isn't valid warns and stays visible as feedback text; ordinary prose
containing dots (`e.g.`, `3.14`) must never trip the detector.

**Bindings that can never fire are worse than none** — the data then says "students didn't
make this mistake." Two known traps: a graph `mistake:` the parser cannot read compiles to
a matcher that never fires; a blank mistake equal to the correct answer never fires because
correctness is decided first.

**Error-analysis items** ("a student wrote X — find the error", §16, D17-D) carry extra
weight under NCEA-first: they are the one format keeping misconception targeting in
auto-scorable form inside a justification locale, and therefore the main automatic data
source when most DoLs are rubric-graded.

---

## 8. Grading is two axes, not one (D8)

A single `graded` boolean misclassified `explain` (captured but never scored) and hid that
rubric types yield structured data only after human grading.

**scoring** (`auto` / `rubric` / `none`) **× captures_response**, plus `score_shape` and
`authoritativeness`.

Platform ground truth:
- Auto-scores are **client-computed and advisory**.
- Only **teacher-entered grades are server-authoritative**.
- Distractor maps yield aggregate misconception signal **only** on auto-scored, per-item
  captured types.

**Assessment policy is the teacher's** (D12): the DoL is *always captured*; whether it
counts for a grade is a toggle. Record always, grade optionally — a teacher who ungrades a
check must not thereby destroy the misconception data.

---

## 9. Locale lives on the DoL only

Mathematics is universal; assessment of mathematical skill is not (§8). The same skill
terminates in a procedural computation under one qualification and a justified argument
under another.

- **Review and lesson are locale-neutral.** The DoL swaps and the rest stands.
- **Default locale: NZ NCEA** (D10) — Achieved / Merit / Excellence, justification-weighted.
  Authored NCEA-first, not dual-tracked.
- TEKS and NZCE remain selectable. The **NZCE swap happens at the seam** when Years 11–13
  content gazettes (staged 2028–2030) — which is exactly what the seam exists for.
- **Accepted data consequence:** NCEA-style DoLs lean on rubric-graded `shortanswer`, so
  misconception aggregates arrive only after human grading (D8). Mitigated by
  error-analysis items.

---

## 10. Capabilities, wishes, and the human gate

### 10.1 One registry; all prompts are projections of it (D7)

Platform capabilities live in JSON with `status`, constraints, and grading model. **The
drafting prompt and the render prompt are generated from the registry plus the graph**;
the import-format rules are stored once and injected. A correction propagates without
editing prose.

The authoring-principles document is likewise stored once (`authoring_principles` in the
thread JSON) and injected at the top of every drafting prompt (D13, D17) — the same
anti-drift move applied to pedagogy rather than capability. The schema encodes structure
but not reasoning; a model given only the schema follows it faithfully and misses the
train of thought.

**Compose only from `shipped` capabilities, inside their stated constraints** (§9). The
registry, not intuition, is the boundary.

### 10.2 The wish queue

If the pedagogically ideal move needs an unshipped capability: author the **fallback**
(the best version buildable today) and record the **wish** against the proposed capability.
A wish without a working fallback is a **blocker**, and a blocker caps the activity at
`draft`. The queue ranks itself by blocked-activity count.

Currently proposed capabilities (surfaced by the deleted seed batch, D15): `draggable_curve`,
`nway_correspondence`, `seeded_data`, `graded_polynomial`.

### 10.3 Status machine (D6, D12)

```
draft ──(human reads end to end)──┐
                                  ├──> approved
       (no dependency on any      │
        `proposed` capability) ───┘
```

- **Drafts do not count.** They are invisible to every progress count. If drafts counted,
  the burndown would measure generation, not curriculum.
- **Approval is blocked** while the activity depends on any `proposed` capability — an
  approved activity needing an unbuilt feature is a promise the platform cannot keep. This
  gate already caught exactly that on seed data.
- Everything a model drafts is a draft (§12). Plausible prose at volume is the failure mode;
  the human read is the quality mechanism, not optional overhead.

---

## 11. What the validator enforces

Consolidated from the decisions above — this is the checkable set.

| Rule | Severity | Source |
|---|---|---|
| Activity has a `faded` beat | **hard error** | D5 |
| Activity targets exactly one primary skill | error | §2 |
| Chain hook count ≥ `ceil(approved activities / 2)` | error | D9 |
| Approval blocked while any dependency is `proposed` | error | D6 |
| Drafts excluded from all progress/coverage counts | invariant | D6 |
| DoL has exactly two items; second is ≥2 rows back | error | §8 |
| ≥1 review item reaches ≥2 rows back | error | §6 |
| Review item outside ancestor pool but ancestral to a later chain skill → `planting_for` | **note, not warning** | D16 |
| Nothing a review item retrieves appears on the activity's `reference` panel | error *(to build)* | §15 amendment |
| Distractor map present on a non-auto-scored type | warning | §7 |
| `mis.*` id not in registry | warning (`--strict`: fail) | import spec |
| Id-shaped token that is not a valid id | warning; stays as feedback text | import spec |
| Contextual DoL item answer carries units | error | §8 |

---

## 12. Ingestion

Two paths, and they are deliberately different.

### 12.1 Markdown import (the teacher/AI path)

`markdownToTiptap.ts` is authoritative; the doc mirrors it. The importer is
**deterministic, additive, and never destructive** — anything it doesn't understand is
flattened to plain text with a visible warning, never dropped silently and never able to
corrupt the document. **Any answer inside a degraded construct is masked to `______`**, so
a degraded block can be published without leaking its key.

Block vocabulary: `graph`, `numberline`, `dataplot`, `mc`, `match`, `order`, `objectives`,
`worked`, `faded`, `explain`, `shortanswer`, `essay`, `columns`, `callout`, `definitions`,
`table`, `meta`, `reference`.

Three of these are **side channels** producing no body block: `meta`, `reference`,
`definitions`.

**`meta` never overwrites.** A key applies only where the activity has no value yet. This
matters because an AI writing to this format will emit a `meta` fence on *every* reply,
including when the user is pasting one extra section into a finished activity — that paste
must not silently rename the course. **Tags are the exception and they union**; nothing is
ever removed by an import.

**The platform numbers questions itself.** A numbered line that is *not* a question is the
trap: among questions it is demoted to prose; separated from them by a fence or paragraph
it becomes its own `ordered_list` restarting at 1, printing two items labelled `1` and an
answer key matching neither.

### 12.2 Batch import (the curriculum path)

`pnpm import:batch` validates `:: mis.*` bindings against the registry.

**Misconception bindings are deliberately not taught by the Copy-AI prompt** — an assistant
with no copy of the registry would invent plausible-looking ids and fragment the data. The
batch path is where bindings are authored, because it is the path that can validate them.

---

## 13. What was considered and declined

Do not rebuild these without reopening the decision. A proposal that violates one of these
*without naming it* is drift.

- **Fork lineage tracking** (D11 corollary) — **declined by the user.** Teachers are
  professionals; their edits are their responsibility; tracking architecture is not worth
  building. Accepted consequence: aggregate misconception data may silently thin where
  teachers cut mapped items.
- **Per-activity hooks** (D9) — 73 obligatory hooks guarantees filler.
- **Hand-declared derivable state** (D3) — `authored[]` was the original sin.
- **A cold-start budget exception** (D17, principle G) — cut; the budget is inviolable.
- **A single `graded` boolean** (D8) — misclassifies `explain` and hides deferred signal.
- **Adding a prerequisite edge to legitimize a sibling-review item** (D16) — would assert a
  dependency that is not real; `planting_for` exists instead.
- **`revision:` and `grading:` meta keys** — removed 2026-08-24. A file still carrying
  either warns and imports fine otherwise.

Deliberate defaults are *not* neutral (D11): the platform gives teachers tools rather than
rules and lets them modify anything, but defaults (review-first, faded present) are chosen
deliberately, because most users never change defaults. Neutrality about defaults is
impossible — only accident vs. intent.

---

## 14. Known drift risks

1. **The registry is a copy of the codebase** (D7 cost). Mitigated by sourcing it from the
   platform team's answers; the eventual fix is **build-time generation from the schema**
   (open item O4). This is the highest-value piece of code to write against this document.
2. **One hand-carried sync exists.** The import-format rules stored in the builder's *Save
   & load* tab are a copy of the user's prompt. When the platform prompt updates, it must be
   re-pasted there, or the render prompt injects the stale version. Everything else in the
   system is single-sourced — this one is not, and it is the known weak point.
3. **§6 vs D16.** The principles text still describes the review pool as ancestors-only;
   D16 broadened it to include ancestors of later chain skills, marked `planting_for`.
   Implement D16; the principles text needs the amendment.
4. **§15 vs the reference-panel rule.** `open-questions.md` records that §15 was amended
   with the ambient open-book rule, but the principles text does not yet contain it. The
   rule is real and checkable — see §11.

---

## 15. Naming conventions, consolidated

```
skill          <domain>.<kebab-skill>          rate.unit-rate
chain          chain.<domain>.<name>           chain.rate.proportional
misconception  mis.<domain>.<kebab-error>      mis.rate.ratio-inverted
```

Misconception prefixes may subdivide a chain by error *kind* — the in-flight proposal uses
`mis.rate.*` for computation errors and `mis.proportional.*` for conceptual errors about
proportional relationships, mirroring how `roc` and `deriv` stay distinct within the
calculus arc. Whether that subdivision is kept is the user's call and is currently
unratified.
