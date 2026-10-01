> **Historical record.** A courier brief pasted to the curriculum builder on 2026-09-25, which
> can't read this repo. It describes the repo as it stood then and is superseded by every later
> commit. The practice it started continues: send the builder a fresh copy of the branch files
> it edits, and have it send back only the lines it changed.

# Repo state brief for the curriculum builder — 2026-09-25

You cannot fetch `ZanReed/curriculum`, so this brief is your picture of it. It supersedes
whatever you last knew. Drafted by the repo session; paste-delivered by the author.

## Decision log high-water mark: D39

Your 25 Sep draft minted D35–D37 unaware the log had reached D35 on 2026-09-05.
Renumbered on commit. The map:

| your draft | committed as | status |
|---|---|---|
| D35 (NZ-first authoring) | **D36** | ratified 2026-09-25 |
| D36 (Tranche-2 deferrals) | **D37** | ratified 2026-09-25 |
| D37 (Y7–13 bottom-up scope) | **D38** | ratified 2026-09-25 |
| — | **D35** | Y8–10 DoLs default auto-scored + error-analysis; rubric at chain finals (ratified 2026-09-05, from the D31–D34 review) |
| — | **D39** | OQ-B ruled 2026-09-25 (below) |

**Before minting a new D-number, ask the author for the current high-water mark.**

## D32 is SUPERSEDED, not held

D36 re-bands both ends of the spine (`deriv.*`/`function.*` → Y12, `limit.*` collapses to
one short chain) on the AS-standards evidence, deliberately overruling the D32 hold with
Phase 5 still unpublished; the supersession is recorded on both entries. The platform's
Phase-5 tickler is now a verification trigger, not a decision trigger. Do not treat the
hold as live, and do not list D32 as needing disposition — it has one.

## D39 — OQ-B is ruled

Threads live in **one graph file**: a top-level `threads` registry, a `thread` tag on each
chain, nothing on skills (derivable via chain), `thread_id` retired. The file renames to
`curriculum-graph.json` in the migration commit. Ruled after a live audit on a synthetic
8-thread / 376-skill scale-up: existing tools run green on the tagged shape unchanged; a
per-thread split saves no bytes, needs a composer in every consumer, and invents a
cross-file duplicate-id failure class. OQ-B is closed; Y7 stubs are unblocked once the
migration lands.

## Other repo facts you may not have

- Graph is **v0.14.0** on main (D31–D34 merged 2026-09-05, as amended by review):
  `nzc_phase` values are statement-grain (`P4.Y10.Algebra:S23`-style, quotes numbered
  S01–S27 in `docs/alignment-sources.md`); `ncea` means **assessed-by only, else empty**;
  six borderline `ncea` keeps stand pending NZ colleague review; sources re-read rule is
  six months.
- `mis.form.m-b-swapped` label is letter-neutral; *factorise* not *factor*;
  `linear.form.standard` says *general form*.
- **Pending application** (ruled, not yet in the graph): the D39 migration (rename +
  threads section, version → 0.15.0), the D36 re-cut, `us-teks → status: dormant`, and the
  extended vocabulary sweep (point–slope, parent function). Sequenced after the
  `chain.linear.slope` hook pool merges, per D38's own ordering.
- **Owed from your side**: the finished `chain.linear.slope` hook pool (min 3 hooks by
  projection). It never traveled to the repo — the holding pen (`chain-hooks.md`) still
  says "no pools authored" for chain 2. Deliver it via the author, with screening notes;
  unscreened hooks land as drafts-pending-screening.
- The workspace `CLAUDE.md` staleness is fixed (2026-09-25): the capability generator is
  frozen behind a fail-loud gate (exit 3) until the platform rebuilds it; the workspace
  graph copy is v0.10.0 and marked stale — the repo is canonical.

## The standing rule this brief exists for

Rulings land in the repo; you cannot see the repo; therefore **any draft you produce that
names D-numbers, banding, alignment semantics, or file structure is stale unless the author
has pasted you a brief like this one dated after the facts you rely on.** Ask for a fresh
one before drafting decision text.
