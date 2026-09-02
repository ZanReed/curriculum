# curriculum

The curriculum scaffolding for the activity platform's catalogue: the skill
graph, the misconception taxonomy, the authoring principles, and the
registries generated from them. **The activities themselves are not here** —
this is the thing they are authored against, and the catalogue's `.md` files
stay where they are.

This repo is **public** (author-ruled 2026-09-02) so that the cross-side
boundary page can carry a pointer of the same strength as the platform's:
a raw URL, a commit stamp, a sha256, and CI that fails on drift — current
by construction, not by discipline.

## Status: seeded at graph v0.13.0 (2026-09-02)

Seeded from the author's Claude-project export. All four checks green at
seed; the registries were regenerated once under this repo's canonical
filename (the only diff against the export was the generator's own
source-filename header line). Two things the seed deliberately excludes:
the correspondence letters (superseded by the boundary pages, per the
curriculum side's own recommendation) and the activity `.md` files (they
live in the catalogue). One known gap: `decision-log.md` proper (D1–D17)
lives in the catalogue repo's `.docs/`; this repo carries
`decision-log-additions.md` (D18–D30 plus amendments).

## The four checks (`.github/workflows/check.yml`)

1. **Principles sync** — the graph's `authoring_principles` field is
   byte-identical to `authoring-principles.md`. Single-source rule
   (author-ruled 2026-09-02): the `.md` is the ONLY edit surface; after
   editing it, run
   `python3 scripts/check_principles.py thread-01-rate-of-change.json authoring-principles.md --fix`
   and commit both. Never edit the JSON field by hand.
2. **Registry generation** — `python3 generate-registries.py <graph>`
   rewrites `skill-registry.txt`, `misconception-registry.txt`,
   `external-prereq-registry.txt`; CI regenerates and fails on any diff.
   `chain-registry.txt` is excluded and carries no stamp — its display
   titles are authored prose with no source in the graph.
3. **Partition check** — `partition-check.py` fails when prose restates a
   threshold that `activity_defaults` declares (D25).
4. **Referential integrity** — `python3 scripts/check_integrity.py <graph>`:
   no dangling prereq or misconception reference, no orphan misconception,
   the chunking plan's skill set equals the graph's, every registry id
   exists in the graph (`parts` defaults to 1 when undeclared), every
   `= n` matches the graph, chain-registry folder names resolve, and the
   skill registry's declared parts total equals `sum(parts)` — 51 at seed,
   the burndown denominator. Extracting zero ids from a present registry
   is itself a failure (the vacuity guard).

## File map

| file | role |
| --- | --- |
| `thread-01-rate-of-change.json` | the graph — skills, edges, misconceptions, `activity_defaults`, `chunking_plan`, capabilities. Single source of truth. |
| `authoring-principles.md` | the pedagogy prose — single edit surface, injected into the graph by check 1's `--fix` |
| `decision-log-additions.md` | D18–D30 + amendments (D1–D17 live in the catalogue repo's `.docs/decision-log.md`) |
| `open-questions.md` | what is unresolved, and who decides |
| `chain-hooks.md` | the hook holding pen |
| `misconception-proposals-ten-skills.md` | the reasoning behind the 13 ids ratified at v0.12.0 |
| `skill-registry.txt` | GENERATED — never hand-edit |
| `misconception-registry.txt` | GENERATED — never hand-edit |
| `external-prereq-registry.txt` | GENERATED — never hand-edit |
| `chain-registry.txt` | hand-maintained, no stamp (titles are authored prose) |
| `generate-registries.py` | produces the three registries, with a notation gate |
| `partition-check.py` | gates check 3 |
| `fd-check.py` | report, never a gate: functional dependencies in the capability registry (D27) |
| `pair-attachment-report.py` | report, never a gate: one-sided pair-confusion attachments (B10; platform-written, runs here) |
| `scripts/check_principles.py` | check 1 (verify + `--fix` sync) |
| `scripts/check_integrity.py` | check 4 |
| `docs/` | reasoning records: reconciliation, the D24 audit, pedagogical concerns, hook screen, the retired architecture doc (kept only so the retirement is visible — do not restore) |
| `channel/` | the boundary-channel rules and page URLs, the repo spec, the catalogue agent brief, the two handoffs |

## The boundary stamp

Once CI is green on `main`, the platform side's boundary page carries:

> Canonical: `<raw URL>` · Generation stamp: commit `<sha>`, `<timestamp>` ·
> sha256 `<hash>` · Currency guarantee: the four checks fail CI on drift,
> so the copy on `main` is current by construction.

Refreshing that stamp after changes is part of landing them, same as the
platform side's rule for its own generated doc.
