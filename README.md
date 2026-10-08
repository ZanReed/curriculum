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
live in the catalogue). By ruling (curriculum side,
2026-09-02): `decision-log.md` D1–D17 stays in the catalogue repo's
`.docs/` and this pointer is the durable answer — a second copy would be
the hand-carried-copy failure with a new name. This repo carries
`decision-log-additions.md` (D18–D42 plus amendments).

## The eleven checks (`.github/workflows/check.yml`)

1. **Principles sync** — the graph's `authoring_principles` field is
   byte-identical to `authoring-principles.md`. Single-source rule
   (author-ruled 2026-09-02): the `.md` is the ONLY edit surface; after
   editing it, run
   `python3 scripts/check_principles.py curriculum-graph.json authoring-principles.md --fix`
   and commit both. Never edit the JSON field by hand.
2. **Registry generation** — `python3 generate-registries.py <graph>`
   rewrites `skill-registry.txt`, `misconception-registry.txt`,
   `external-prereq-registry.txt` and `misconception-attachments.txt`; CI
   regenerates and fails on any diff.
   `chain-registry.txt` is excluded and carries no stamp — its display
   titles are authored prose with no source in the graph.
3. **Partition check** — `partition-check.py` fails when prose restates a
   threshold that `activity_defaults` declares (D25).
4. **Referential integrity** — `python3 scripts/check_integrity.py <graph>`:
   no dangling prereq or misconception reference, no orphan misconception,
   the chunking plan's skill set equals the graph's, every registry id
   exists in the graph (`parts` defaults to 1 when undeclared), every
   `= n` matches the graph, chain-registry folder names resolve, no id in
   `external-prereq-retired.txt` or `skill-ids-retired.txt` is back in use (D45, D48), every Y7–10 skill
   resolves a reporting strand that agrees with its NZC statements (K, D51), and the
   skill registry's declared parts total equals `sum(parts)` — 51 at seed,
   the burndown denominator. Extracting zero ids from a present registry
   is itself a failure (the vacuity guard).

5. **Thread checks** — `node validate.js <graph>`: the curriculum-owned §11
   thread checks.
6. **Fact-scope registry** (D43) —
   `python3 scripts/generate_fact_registry.py curriculum-graph.json` regenerates
   `fact-scope-registry.json` from the graph's `fact_scope` and
   `activity_defaults.fact_probe`; CI fails on any diff, and the generator itself
   fails on any contract violation (unknown kind, flag or placeholder; missing,
   duplicate or retired id; answer outside D43 item 19; markup in strategy text;
   a family outside exactly one `family_groups` group, or a group outside exactly
   one of the two `probe_parts`).
   To retire a fact or family id, append it to `fact-ids-retired.txt`; never edit
   a fact in place under the same id.
7. **Glossary check** (D40) —
   `python3 scripts/check_glossary.py glossary.md --retired glossary-retired.txt --base <ref>`.
8. **Capabilities** (B14, D27 amendment) —
   `python3 scripts/check_capabilities.py curriculum-graph.json --facts platform-pins/capability-facts.json --pin platform-pins/capability-facts.pin.json`:
   the pinned copy's sha256 matches its `.pin.json`; every capability entry has
   exactly the known fields and vocabulary values; derived fields equal the
   pin; nothing the pin lacks is marked shipped. Prose a fact contradicts is
   flagged, never failed. It never fetches: the scheduled
   `capability-drift.yml` reports when the platform's main moves past the pin,
   and a pin bump (opened by the platform, with pre-merge notice) is the only
   way derived fields change.

9. **Teacher guides** (D50) —
   `python3 scripts/check_guides.py <catalogue> --graph curriculum-graph.json`:
   every catalogue activity ends with exactly one ```` ```teacher-guide ```` fence;
   sections, order and word cap read from `activity_defaults.teacher_guide` (the
   assessment shape for `type: quiz` / `type: exam` files, D51); Marking
   exactly when the DoL has a rubric; no `.guides/` folder left over. The catalogue
   has no CI, so run it there before every batch import; CI runs it against
   `tests/fixtures/guides-catalogue` so the script can't rot.

10. **Tags** (D52) —
   `python3 scripts/check_tags.py <catalogue> --graph curriculum-graph.json --glossary glossary.md`:
   every activity's `tags:` are glossary terms, `tags.min`–`tags.max` of them (assessment files
   exempt). Run with check 9 before every batch import; CI runs it against the fixture.

11. **Hook registry** (D50 note 2026-10-08; C-97) —
   `python3 scripts/generate_hook_registry.py curriculum-graph.json --retired hook-ids-retired.txt`
   regenerates `hook-registry.json` from the graph's chain hook pools for the platform's
   teacher-only chain view; CI fails on any diff. The generator fails, writing nothing, on a
   missing field, a reused or retired hook id, a `connects_to` outside the hook's chain, or
   markup in a prompt or note (hooks are plain text).

To retire a glossary entry, delete it from `glossary.md` and append its id to
`glossary-retired.txt` in the same commit; never edit an `id:` line.

## File map

| file | role |
| --- | --- |
| `curriculum-graph.json` | the graph — the `threads` registry, skills, edges, misconceptions, `activity_defaults`, `chunking_plan` (each chain tagged with its `thread`), capabilities. One file for every thread (D39). Single source of truth. |
| `authoring-principles.md` | the pedagogy prose — single edit surface, injected into the graph by check 1's `--fix` |
| `decision-log-additions.md` | D18–D42 + amendments (D1–D17 live in the catalogue repo's `.docs/decision-log.md`) |
| `open-questions.md` | what is unresolved, and who decides |
| `chain-hooks.md` | the hook holding pen |
| `misconception-proposals-ten-skills.md` | the reasoning behind the 13 ids ratified at v0.12.0 |
| `skill-registry.txt` | GENERATED — never hand-edit |
| `misconception-registry.txt` | GENERATED — never hand-edit |
| `external-prereq-registry.txt` | GENERATED — never hand-edit |
| `misconception-attachments.txt` | GENERATED — never hand-edit. One `skill.id   mis.id` pair per line, projected from `skills[].misconceptions`; read by the platform's AI grading |
| `chain-registry.txt` | hand-maintained, no stamp (titles are authored prose) |
| `glossary.md` | the course glossary (D40) — hand-authored, the only edit surface for glossary words; the platform mirrors it via `import:batch --glossary` |
| `glossary-retired.txt` | retired glossary ids — hand-maintained, append-only, never reused (D40) |
| `fact-scope-registry.json` | GENERATED — never hand-edit. The fluency fact scope for the platform's probe and sprint (D43): families, fact counts, year scope, single values, templates, strategies; header carries a content-hash revision id |
| `fact-ids-retired.txt` | retired fact-scope ids — hand-maintained, append-only, never reused (D43 note 2026-10-03) |
| `external-prereq-retired.txt` | retired external-prereq ids — hand-maintained, append-only, never reused; check 4 (I) enforces it (D45) |
| `skill-ids-retired.txt` | retired skill ids — hand-maintained, append-only, never reused; check 4 (J) enforces it (D48 note) |
| `platform-pins/capability-facts.json` | PINNED copy of the platform's generated capability facts — never hand-edit; replace it whole in a pin-bump PR |
| `platform-pins/capability-facts.pin.json` | the pin: the platform's source commit and the copy's sha256 |
| `generate-registries.py` | produces the three registries and the misconception attachments, with a notation gate |
| `scripts/generate_fact_registry.py` | produces `fact-scope-registry.json` from the graph, with the fact-scope contract gate |
| `partition-check.py` | gates check 3 |
| `fd-check.py` | report, never a gate: functional dependencies in the capability registry (D27) |
| `pair-attachment-report.py` | report, never a gate: one-sided pair-confusion attachments (B10; platform-written, runs here) |
| `scripts/check_principles.py` | check 1 (verify + `--fix` sync) |
| `scripts/check_integrity.py` | check 4 |
| `scripts/check_glossary.py` | the glossary step (D40): well-formed, unique ids/terms/variants, NZ-only bodies, caps, retire-not-rename against the git base |
| `scripts/check_guides.py` | check 9: teacher guides against a catalogue folder (D50) |
| `hook-registry.json` | GENERATED — never hand-edit. Chain hook pools for the platform's teacher view, header revision = sha256 of the canonical body |
| `hook-ids-retired.txt` | retired hook ids — hand-maintained, append-only, never reused (includes ids cut at screening) |
| `scripts/generate_hook_registry.py` | produces `hook-registry.json`, with the hook gate (check 11) |
| `scripts/check_tags.py` | check 10: activity tags against the glossary (D52) |
| `tests/fixtures/guides-catalogue/` | a fixture catalogue for checks 9 and 10, not real activities |
| `scripts/check_capabilities.py` | check 8, plus the drift report the scheduled `capability-drift.yml` runs |
| `validate.js` | the curriculum-owned §11 thread checks — runs in CI (`node validate.js <graph>`); green against v0.13.0 on joining (2026-09-02) |
| `builder.html` | the authoring UI (serve over HTTP, never `file://`). Provenance caveat: this is the July 2026 workspace copy, joined 2026-09-02 so its Save & load prompt text is diffable; reconcile if the Claude project holds a newer descendant |
| `docs/` | reasoning records: reconciliation, the D24 audit, pedagogical concerns, hook screen, the retired architecture doc (kept only so the retirement is visible — do not restore) |
| `channel/` | the boundary-channel rules and page URLs, the repo spec, the catalogue agent brief, the two handoffs |

**Deliberately NOT here: `generate-capabilities.mjs`.** It imported the
platform's TypeScript and could not run in this repo's CI. Since B14 (D27
amendment, 2026-10-03) the platform derives the capability fields it owns
(`status`, `grading.{scoring, captures_response, score_shape}`) into its own
`docs/capability-facts.json`; this repo commits a pinned copy in
`platform-pins/` and check 8 gates the graph against it. The stale workspace
copy is retired with a pointer here. Authored capability prose (`label`,
`medium`, `affords`, `constraints`, `grading.note`) stays ours.

## The boundary stamp

Once CI is green on `main`, the platform side's boundary page carries:

> Canonical: `<raw URL>` · Generation stamp: commit `<sha>`, `<timestamp>` ·
> sha256 `<hash>` · Currency guarantee: the eight checks fail CI on drift,
> so the copy on `main` is current by construction.

Refreshing that stamp after changes is part of landing them, same as the
platform side's rule for its own generated doc.
