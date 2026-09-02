# Handoff to the activity builder

**Date:** 2026-08-26

Three deliverables below, one blocker, and six questions that need answering before the
blocker clears.

---

## 1. `chain-registry.txt` — done, ships now

Keyed on the folder name as requested (`01-chain.rate.proportional`), ordinal out of the
title. Attached separately.

**Strip the `unit:` lines from all four activity files when this lands.** With the
registry as the source, a file-level `unit:` is a deliberate override that the platform
reports per run — leaving four of them in means the override report fires on 100% of the
catalogue and stops being a signal.

Related, and worth doing at the same time: **the generated catalogue-authoring prompt
should not teach `unit:`.** An AI writing to this format emits a `meta` fence on every
reply, so if the prompt teaches the key, every drafted file will carry one and the
registry stops being the source within a session. (The teacher-facing Copy AI prompt
should keep it — a teacher pasting into a general assistant has no registry.)

---

## 2. `skill:` lines for the four files — as far as they can go

Complete except the `x_` keys, which need the activity contents (see §3, Q4).

**`01-unit-rate.md`**
```meta
key: act.rate.unit-rate
skill: rate.unit-rate
```

**`02-constant-of-proportionality.md`**
```meta
key: act.rate.constant-of-proportionality
skill: rate.constant-of-proportionality
supporting_skills: rate.unit-rate
```

**`03-proportional-graph.md`**
```meta
key: act.rate.proportional-graph
skill: rate.proportional-graph
supporting_skills: rate.constant-of-proportionality
```

**`04-proportional-consolidation.md`**
```meta
key: act.rate.proportional-consolidation
skill: rate.proportional-graph
supporting_skills: rate.unit-rate, rate.constant-of-proportionality
chain_role: consolidation
```

Three notes on the fourth:

- `chain_role: consolidation` is a **new key needing platform support** (D24). It is why
  `rate.proportional-graph` is declared as **1 part, not 2** — activity 04 names the
  skill as primary but does not teach it, and counting it as a part would make coverage
  read *partial (1 of 2)* for a skill that is fully taught by activity 03.
- Absent `chain_role` means `part`, so files 01–03 need nothing.
- Three checks must be scoped to parts only, or they false-fire here: the
  exceeds-declared-parts warning, the shared-DoL-target guardrail, and the part-adjacency
  warning.

---

## 3. Blocked: `skill-registry.txt`

**We cannot produce this without the skill graph.** Everything in our hands names three
skill ids — `rate.unit-rate`, `rate.constant-of-proportionality`,
`rate.proportional-graph`. The other 44 are in the graph, and the graph has not reached
us.

Send the id list in any form (export, paste, a dump of the `skills` array) and the
registry follows immediately. It is a mechanical transform: one id per line, plus an
optional `= n` where a skill is delivered in more than one part.

### Questions

**Q1 — Where does the skill graph currently live, and can you export just the ids?**
The full graph (edges, bands, misconception attachments, descriptions) stays ours and we
do not need it round-tripped — only the id list, so the registry can be built and
`--strict` can run.

**Q2 — Are any skills besides `rate.proportional-graph` multi-part?**
Format is a bare id for one part, `id = 2` for two. If nothing else has been chunked
yet, every other line is bare and we can revisit as chains are authored. (For unauthored
skills the part count is inert anyway — coverage reads *uncovered* regardless of
denominator — so absence is safe rather than a claim.)

**Q3 — `proportional.graph-through-origin` or `rate.proportional-graph`?**
The platform's §3.3 example listed the first; our chain docs and the live misconception
proposal both use the second, and `mis.proportional.line-misses-origin` is attached to
it. Unanswered across two exchanges. If the platform's line was illustrative, we send
`rate.proportional-graph`. If it came from somewhere real, we have two ids for one skill
and the registry is where that gets settled rather than inherited.

**Q4 — For each of the four activities: which skill does each review item and each DoL
item target?**
This is what fills `x_review_skills` and `x_dol_skills`, and without it validator rules 6
and 7 cannot run at all — those are ours and they have no other data source. Either send
the four files and we will read them, or send the mapping directly. Skills, not indices:
positions shift when a file is rewritten and nothing validates the namespace to catch it.

**Q5 — Do any of the four files currently lack a ```meta fence?**
`key:` must go inside one. A bare `key: value` line in prose is just a paragraph.

**Q6 — Does a chain-title change reach already-published rows, or drafts only?**
The platform's first document said `unit` is stamped at publish; the second said a
registry title change rewrites `unit` across the chain on the next import. If it is
drafts-only, a rename leaves two groups in the teacher outline under old and new titles
until everything is re-published — worth knowing before renaming, not after.

---

## 4. Standing context — what to add, and where

The builder should not have to be told these things per task. Proposed placement:

| Layer | Where | What |
|---|---|---|
| Agent brief | `CLAUDE.md`, catalogue root | Hard invariants, the declined list, ownership, routing. Read every session. Short on purpose. |
| Reference | `_docs/` | `curriculum-architecture.md`, `decision-log.md`, `authoring-principles.md`. Consulted, not loaded wholesale. |
| Machine inputs | catalogue root | The three registries. |
| Generated | platform repo | Format spec, drafting prompt, render prompt. **Never copied here** (D7). |

A draft `CLAUDE.md` is attached. Two things it encodes that are worth stating plainly:

- **`_docs/` uses the importer's own ignore rule**, so reference material can live beside
  the content without the file walk seeing it.
- **If a `_docs/` file or a registry looks wrong, file it rather than fix it.** Both sides
  have corrected the other's documents this way already and it works. What must not happen
  is a doc edited on one side to match code on the other — that is exactly the drift D7 and
  D13 exist to prevent, and it has happened twice.

**What we deliberately do not send as standing context:** the import format spec. It is
72KB, it is generated from the importer's own code, and a copy here would drift within
weeks. Point at the generated file instead.
