# CLAUDE.md — curriculum catalogue

Orientation for any agent working in this repository. Short by design: the full
reasoning lives in `.docs/`, and this file exists to tell you when to go read it.

---

## What this repo is

A mathematics curriculum catalogue — activity source files, plus three registries the
platform importer consumes. The **platform lives in a different repository** and is not
yours to change from here.

```
01-chain.rate.proportional/     chain folder; ordinal = teaching order
  01-unit-rate.md               activity source (authored, not generated)
  02-constant-of-proportionality.md
  03-proportional-graph.md
  04-proportional-consolidation.md
skill-registry.txt              valid skill ids (+ optional part counts)
chain-registry.txt              folder → display title
misconception-registry.txt      valid mis.* ids
.docs/                          reference; skipped by the importer's file walk
```

The importer's walk collects `.md` files and skips dot-directories. `.docs/` is therefore
invisible to it by rule rather than by convention — a `_docs/` holding `.md` reference
files **would** be imported.

---

## Hard invariants

Breaking one of these is a bug even when the code passes. Each names the decision it
comes from; `.docs/decision-log.md` has the reasoning and the cost.

1. **Derived state is never stored.** Progress, coverage, burndown, review candidates —
   all computed. The one logged exception is the platform's coverage manifest (D19); do
   not add a second. (D3)
2. **Durable data references skill ids, never activity ids.** Activities get split and
   rewritten; anything holding an activity id breaks on every rewrite. (D1)
3. **Activity identity is the `key:` field, not the file path.** Paths are browsing
   decoration. Never derive identity from location. (D18)
4. **A missing faded beat is a hard error, not a warning.** Deliberately mechanical —
   it replaced human vigilance because it is the failure a reviewer skimming plausible
   prose misses most often. Do not downgrade it. (D5)
5. **Drafts are invisible to every count.** If drafts counted, the burndown would
   measure generation rather than curriculum. (D6)
6. **Grading is two axes** — `scoring` (auto/rubric/none) × `captures_response` — plus
   `score_shape` and authoritativeness. Do not collapse to a boolean. Auto-scores are
   server-computed and advisory; only teacher-entered grades are authoritative. (D8)
7. **Hooks are a chain-level pool. Activities never carry them.** Not a field, not a
   pointer, not an ordering assumption. This has tried to land on the activity three
   times. (D9)
8. **Keys beginning `x_` are skipped silently — read nothing, validate nothing.** The
   namespace is unvalidated by design; the importer's per-run receipt naming ignored
   `x_` keys is the only sensor on it and is not optional. (D20)
9. **Never write back to a catalogue `.md`.** These are authored source, not render
   targets. The importer reads and writes its own database.

---

## Declined — do not re-propose without reopening the decision

Naming one of these and arguing against it is fine. Proposing it in ignorance is drift.

- Fork lineage tracking (D11)
- Per-activity hooks (D9)
- Hand-declared derivable state (D3)
- A cold-start exception to the 20–25 minute budget (D17-G)
- A single `graded` boolean (D8)
- Adding a prerequisite edge to legitimise a sibling-review item — use `planting_for` (D16)
- `revision:` / `grading:` meta keys (removed 2026-08-24)

---

## Ownership

| | Owner |
|---|---|
| Skill graph, edges, bands, descriptions, misconception attachments | **curriculum side** |
| The three registries | **curriculum side** — the platform consumes them |
| Capability registry, import behaviour, grading engine | **platform side** |
| `.docs/` | **curriculum side** |

If a `.docs/` file or a registry looks wrong, **file it — do not fix it.** Both sides
have already corrected the other's documents this way, and it works. The one thing that
must not happen is a doc edited on one side to match code on the other; that is the
drift D7 and D13 exist to prevent.

---

## Where to read further

| If you are touching… | Read |
|---|---|
| the data model, entity relationships, validator ownership | `.docs/curriculum-architecture.md` |
| why anything is the way it is, or what was already declined | `.docs/decision-log.md` |
| what a validator rule is actually asserting pedagogically | `.docs/authoring-principles.md` |
| import syntax, fences, meta keys | the platform repo's generated format doc — **not** a copy here |

The last row matters: the format spec is generated from the importer's own code (D7).
A copy in this repo would drift within weeks. It has happened twice.

---

## Two live gaps

- **`skill-registry.txt` is incomplete.** Until the full id set lands, `--strict` cannot
  run and coverage is uncomputable.
- **Consolidation-as-pattern is unruled.** `chain_role: consolidation` exists on one
  activity, and the four-activity projection came before the consolidation was designed
  for the slot. Do not infer that chains end with a consolidation from n = 1. (D24)
