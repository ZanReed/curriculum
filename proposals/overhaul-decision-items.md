---
status: ruling record. D55–D69 ruled by Zan 2026-10-20 and 2026-10-21; entries in decision-log-additions.md
written_against: ZanReed/curriculum main @ 2990ba1, graph v0.17.27
inputs: "Two rulings: school-first sequencing and hook concept banks per unit" (D55, D56), "Y9 Algebra: Expressions and Equations — chain stubs" and "Modern Classroom wishlist" (all pasted by Zan, 20 Oct 2026; held in the Claude project, not the repo)
---

# Overhaul decision items: first batch

The series starts at D55 (Zan, 20 Oct). D53 and D54 are taken elsewhere: neither is on `main` or
any remote branch. D55–D57 follow Zan's own numbering. D58 onward are this list's. Every number is
confirmed at commit.

## 0. The direction rulings (the decision draft)

**D55. School-first sequencing: Y9 first, one school unit at a time. Supersedes D38's order,
not its scope.**
- The draft's eight items, unchanged. Y7/Y8 chains stay as full lessons. The first unit is Y9
  Algebra. The school's core tiers (D/C/P) are the scope authority. `band_nz` = the school's
  year, and `nzc_phase` keeps the NZC year. Tier codes stay in stubs only. 9xx ordinals are
  provisional. In-flight Y7 drafts finish when their Y9 unit comes up. The assessment model,
  the linear rebanding, the point-slope method mismatch and the stats format are left open.
- ⇄ New `chain-registry.txt` rows get a pre-merge notice. **Later passes to flag to the platform
  now:** item 6's renumbering pass moves every folder. Per B-195 item 2 that is safe only as a
  path move with every `key:` kept, so the pass should say so in its letter. Item 8's linear
  rebanding changes `band_nz` on skills that are live.
- **RULED 2026-10-20 (Zan): adopted as drafted.** The notice to the platform goes in the next letter.

**D56. Hook concept banks per school unit, screened cumulatively within the year (amends D42).**
- The draft's four items, unchanged. ⇄ None: the hook contract and the hook registry shape are
  untouched.
- **RULED 2026-10-20 (Zan): adopted as drafted.**

Each item gives: the ask, what is already ruled, what it touches on the platform side (⇄), and
what Zan rules.

Checked against v0.17.27 before writing: every prereq the stubs cite exists
(`algebra.notation.write`, `number.exponents.evaluate`, `number.fractions.equivalent`,
`algebra.expressions.like-terms`, `number.factors.hcf-lcm`, `algebra.equations.two-step`,
`algebra.formulae.rearrange`, `number.integers.number-line`, `ext.arith.signed`,
`ext.arith.fractions`). All four reused misconception ids exist. None of the 12 new skill ids or
13 new misconception ids clashes with the graph or `skill-ids-retired.txt`. `numberline`,
`gap_equation`, `fill_blank` and `mc` are all `shipped`. Folders 904–908 are free. None of the
12 glossary words exists yet.

---

## A. Y9 algebra unit (from the chain stubs)

**D57. D24 amendment: a consolidation may reach back to one earlier-chain skill.**
- Already ruled yes (stubs ruling 1). This item only gives it a number and adopts the text:
  "A consolidation may include one skill from an earlier chain when the confusion it targets is
  named and attached to both skills under §7."
- ⇄ The consolidation in 904 would discriminate `algebra.expressions.like-terms` (707). This
  bears on B-195 item 5: a discrimination item is eligible only when *every* skill it covers has a
  ratified skill bank, so this consolidation's mixed-practice items stay dark until 707 has a bank.
- **RULED 2026-10-20 (Zan): adopted as worded. Being taught is enough** for a discrimination item:
  "this lets me know if students need more attention in a specific area". This matches the
  existing D43 amendment of 2026-10-20, item 4 ("eligible only when ALL its `discriminates`
  skills are in the student's pool"), where the pool means taught (item 3). The platform's build
  requiring a ratified skill bank is stricter than the ruled text. Answered in C-148.

**D58. Adopt the Y9 algebra unit: 5 chains, 12 skills, 13 activities.**
- Ask: add `904-chain.algebra.terms` … `908-chain.algebra.inequations` as stubbed. All are on
  `thread.algebra-equations`, `band_nz: Y9`, `calculator: off`, and every skill is 1 part.
  Ordinals are placeholders (D55 item 6).
- Already ruled: `algebra.equations.brackets` stays its own skill, revisited at drafting (stubs
  ruling 2).
- ⇄ Additive only: new skills in the skill registry, five new chain-registry lines, and a
  burndown denominator that rises by 12. No existing key, path or id changes. Notice goes out at
  PR time.
- **RULED 2026-10-20 (Zan): adopted as stubbed.**

**D59. Thirteen new misconception ids, plus one new attachment on an existing Y7 skill.**
- Ask: put the 13 ids in the stubs' table through screening (§7), with their attachments.
- The contract-sensitive part: `mis.forming.order-reversed` also attaches to the existing
  `algebra.notation.write`, whose only attachment today is `mis.notation.letter-as-object`. That
  changes `misconception-attachments.txt`, which the AI grader reads. It needs a pre-merge notice,
  as D48's note item 3 did.
- **RULED 2026-10-20 (Zan): all 13 accepted with the stubs' attachments. order-reversed also
  attaches to `algebra.notation.write` (pre-merge notice owed). A 14th id is added:**
  `mis.inequations.sign-reversed-unneeded`, "Reverses the inequality sign when no negative
  multiplier or divisor is involved (x − 3 > −5 → x < −2; 2x < −6 → x > −3)". It attaches to
  `algebra.inequations.solve` and `algebra.inequations.negative-coefficient`. Carrier: mc;
  fill_blank exact alternates. It is the over-generalised mirror of `sign-not-reversed`. Each
  label names its own direction, so the pair rule is met by wording (§7).

**D60. Form-sensitive grading rule for terms, expand and factorise skills.**
- Ask: make the stubs' "Carriers" section an authoring rule. Never use `fill_blank ==` where the
  form *is* the point. Use `gap_equation` gaps inside the target form, exact `|` alternates, or
  `mc` for bound DoL items. It is the same family as §7's units-dropped rule: a binding that
  cannot fire.
- Where it lands: `authoring-principles.md` §7 (check 1 then syncs the graph), or kept as
  unit-local notes.
- ⇄ Held letter: "can the platform grade *equivalent and in a stated form*?" The stubs say to
  hold it until the first activity shows the cost.
- **RULED 2026-10-21 (Zan): (1) a general rule in `authoring-principles.md` §7, landing with the
  batch PR. (2) The form-grading wish is not held for an activity, and it is not sent yet either:
  it goes on the to-do list below.**

**D61. Widen the Y7 like-terms label to include negative coefficients.**
- Already ruled (stubs ruling 4). The change lands when that activity is drafted.
- ⇄ A label change shows in the skill registry, so it gets the usual notice. The skill id is
  unchanged.
- **RULED 2026-10-21 (Zan): confirmed.** Lands when the Y7 like-terms activity is drafted.

**D62. Glossary: 12 words before the unit's activities (D40).**
- Words: term, like terms, index (variants: power, exponent), expand, factorise, common factor,
  highest common factor, inequation (variant: inequality, ruled in stubs ruling 3), solution set,
  subject, formula, substitute. None exists on main. The "check the Y7 branches" asterisks still
  apply to like terms and highest common factor.
- ⇄ The glossary is mirrored live, but adding words is additive.
- **RULED 2026-10-21 (Zan): adopted as stubbed. `index` has the variants `power` and `exponent`.**
  First ruled (a), keeping "power" free for 702. Revised to (b) the same day after the D63 read:
  NZC Phase 4 Number (Knowledge Y10) says that index, power and exponent are used interchangeably,
  and makes *index* a new Y9 word. Chain 702 uses *index* / *power* in that sense and gets no
  separate "power" term. None of the 12 is on any remote branch either.
  Bodies are written per chain, before each chain's activities.

**D63. Alignment statements S28–S34: human read before commit.**
- Ask: the wording came through a summarising fetch, which RATIFICATION_LOG (2026-09-03) rejects
  as a basis. Someone has to read the Phase 4 page word for word before `alignment-sources.md`
  takes them. `ncea` stays unset, not `[]`.
- The banding splits recorded under D55 item 4 are exponent laws (school Y9, NZC Y10) and the
  inequality reversal (school Y9 P, NZC general rule Y10).
- **RULED 2026-10-21 (Zan): option (b). Claude reads the page's own text and Zan checks it; `ncea`
  stays unset.** The read was done 2026-10-21, and the results are in
  `proposals/d63-nzc-phase4-check-sheet.md`. S28–S33 match and sit where the stubs say. S34 is
  truncated by the stubs. Three more statements, S35–S37, were adopted by Zan 2026-10-21, pending his tick on the sheet. Two findings feed back
  into other items: integer × and ÷ is NZC Y9 (D45 item 2), and the NZC treats index, power and
  exponent as interchangeable (D62).

**Follow-up flagged, not an item:** there is still no integer multiply/divide skill (D45 item 2 is
open), so `algebra.expand.negative` and `algebra.inequations.negative-coefficient` route through
`ext.arith.signed`. Closing D45 item 2 would re-point those two edges.

---

## B. Modern Classroom wishlist

The premise stands: new content is taught live, explicitly. Each item is a direction ruling;
platform asks are sent only when the feature is ready to be used.

**D64. Catch-up videos with pause points (wishlist 1).**
- Ask: scope is catch-up, late joiners, revision and the Y10 spiral. Adopt the 8 design rules
  (the script is the activity, flagged stale when its revision changes, one example per clip,
  example before try, fading across pauses, routing by misconception id, first tries count,
  handwriting with voice-over). Pilot 2–3 activities on an off-the-shelf tool.
- ⇄ None now. Rule 2 (stale flag) and rule 7 (first tries feed the struggling rule) will each
  need a platform hook later. During a third-party pilot, rule 7 can't hold, so pilot data won't
  reach the teacher view.
- Rule: adopt scope and rules / pilot only. Pilot activities.
- **RULED 2026-10-21 (Zan): scope and all 8 rules adopted. Build now, not a third-party pilot. The
  pilot runs on the platform's own player with 1–2 live activities (701 or a Y7 geometry chain).
  The video is hosted outside the platform and embedded, with pause points mapped to items the
  activity already has. The letter was sent now (C-152).** Hosting: YouTube (unlisted) is assumed,
  because the school already points teachers to Khan Academy, which hosts on YouTube. Still to
  confirm with the HoD: the school's policy on teacher-recorded, student-facing video. The player
  is asked to stay hosting-agnostic so a switch costs nothing.

**D65. A parallel DoL form per activity, with one retake (wishlist 2).**
- Curriculum now: every DoL gets a parallel form, seeded like the D43 banks.
- ⇄ **This is a contract question.** Is a seeded DoL the D43 bank format (agreed in C-123 /
  B-161), or a new format? `tools/check_bank.py` is ours. The importer and the retake flow are
  theirs. A one-retake cap and "latest and best" storage are a later ask.
- Rule: adopt the parallel-form authoring rule. Are seeded DoLs the bank format, or something
  separate?
- **RULED 2026-10-21 (Zan): all three adopted. Forms are SEEDED: a retake is a fresh draw, not a
  second hand-written form. The letter was sent now (C-150).** Open on the platform side: where a
  seeded DoL lives (the activity's own seed fence, which lint currently keeps free of the
  bank-only derived/`where` lines under B-162 BE-2, or a DoL bank file the activity points to).
  **Sub-rulings 2026-10-21 (Zan), sent in C-151:** (a) "passed" for a skill is decided by the
  primary-skill item alone. The review-pool item counts for its own skill's data and never blocks
  the pass. (b) On a retake, a rubric-graded item re-asks the same prompt with the first answer
  hidden, and is teacher-marked as before.

**D66. School tier tag on every practice-bank item (wishlist 3).**
- Ask: each bank item carries D, C, P or E (D55 item 5's tier codes). Each unit gets an Exceeding
  problem set.
- ⇄ **This touches work in flight.** It adds a field to the D43 bank format, and the platform's
  mixed practice slice 1 (built, unpushed) reads that format and the mixed_* keys. Its only
  ratified bank is chain 1, which has no tier tags. Under B-195 item 1, a format change needs a
  letter before it merges. The tier-aware *selection* is a later ask. The *field* question should
  go to them early, so slice 1 doesn't ship a format that's about to grow.
- **RULED 2026-10-21 (Zan): all four adopted as recommended. The letter was sent now (C-149).**
  1. Per template: one `tier: D | C | P | E` line, the FIRST line under the template's heading (position fixed by the platform in B-197; check_bank enforces it). Letters only in
     the public repo (D55 item 5).
  2. Optional in the format, so chain 1's ratified bank stays valid and an untagged template has
     no tier and is never filtered. Our `check_bank.py` requires it for new banks from the Y9 unit
     on.
  3. Selection: a skill's criterion is passing its DoL. Before it, the student is served D–C
     templates. After it, P–E templates are added and D–C stay as maintenance.
  4. E material sits in skill banks as E templates. The unit's multi-skill Exceeding problem set
     is separate, for early finishers, and does not feed mixed practice for now.

**D67. Student unit tracker (wishlist 4).**
- The private row-to-skill mapping lives in the Claude project, not this public repo (D55
  item 5). The tracker view is a later ask and depends on the tier-code field.
- Rule: direction only. Park the ask until D66 lands.
- **RULED 2026-10-21 (Zan): rows are keyed by our skill ids. The teacher enters the school's row
  wording in the platform, privately, and it falls back to the skill label plus tier letter where
  none is entered. Statuses: not taught / taught / DoL passed (best attempt) / struggling. "What
  to practise next" comes from the D66 tier unlock. The letter was sent now (C-153).** No school
  text enters this repo.

**D68. A "who needs me" teacher view (wishlist 5).**
- Nothing new for the curriculum. Ask the platform what already exists (the struggling rule
  keys are on main: `mixed_struggling_window`, `mixed_struggling_min_right`).
- Rule: send it as a question in the next letter: yes / no.
- **RULED 2026-10-21 (Zan): ask outright, worded "this is what we want; tell us how much you
  already have". The letter was sent now (C-154).**

**D69. Grades that use mastery (wishlist 6).**
- This depends on the assessment-model ruling and on the department agreeing to it.
- **RULED 2026-10-21 (Zan): parked for the HoD meeting.** It goes into `open-questions.md` in the batch PR. No letter.

**Deliberately not adopted** (recorded so they aren't reopened; whole-unit self-pacing is ruled out because students spread across a unit can't share a hook or a live worked example, not because of the fixed test date, per Zan's 2026-10-21 update): video as first teaching,
whole-unit self-pacing, unlimited retakes, and students choosing their own skill order.

---

## To-do (not yet sent or built)

- [ ] **Platform wish: grade "equivalent AND in a stated form"** (D60). Zan's priority note: building
  features is worth more right now than authoring activities, because the HoD meeting hasn't happened
  yet. Trigger: the stubs' carrier examples. Factorise 18x − 12 should accept 6(3x − 2) and reject
  18x − 12 and 2(9x − 6). Simplify 4a × 3b should accept 12ab and reject 4a×3b and 7ab. Expand
  −2(3x − 5) should accept −6x + 10 and reject −6x − 10. Simplest form should reject 4/6 for 2/3.
  "Equivalent but the wrong form" must be distinguishable from "not equivalent", so that
  `mis.factorise.not-highest` can fire. Send as a C-letter when Zan says go.

