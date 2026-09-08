# Ratification log

Companion to `decision-log-additions.md`. One sitting per section; append, never clobber.
Protocol: prediction-before-reveal (the expectation is stated before the recommendation is
shown; the outcome grades foresight, not the final call).

## Sitting 2026-09-03 — D31–D34 (NZ alignment pass, `nz-alignment` branch, PR #1)

Contract: author can state what each decision commits the curriculum to and defend it (§12).
Evidence: the branch itself — decision text, graph values, `docs/alignment-sources.md` quotes.

| item | expectation stated | outcome | decision | reading assigned |
|---|---|---|---|---|
| D31 alignment recording | strand-level values; quotes in the graph next to values; silent skills marked "optional non-NCEA content" | surprised (granularity partial; evidence-location and silent-skills both diverged) | build | `docs/alignment-sources.md` preamble + D31 entry — the pointer-vs-copy argument |
| D32 calculus re-band | bands: no opinion (noted the qualification revamp forces future revision — matches the branch's own open question); keep the US map | no-opinion (map fork predicted) | build | AS91262 + AS91578 explanatory-notes sections of `docs/alignment-sources.md` + D32 entry |
| D33 locale contents + proxy | author against old NCEA standards until the successor is published; no expectation on entry contents | predicted on the proxy fork (contents fork no-opinion) | build | the `nz-ncea` locale entry (`activity_defaults.locales`) + the §8 hunk — the text every rubric DoL is authored against |
| D34 NZ vocabulary | ids keep US spelling; everything student-facing goes NZ | predicted (branch adds one deliberate exception: *parent function* stays) | build | — |

**Summary: 2/4 predicted, 1 surprised, 1 no-opinion.** All four ratified as `build` — no
amendments, no demotions. The surprises cluster where the branch applied the project's
anti-hand-carried-copy principle to external documents (D31), which is the reading to do first.

Pre-reveal confidence: D31 med · D32 med · D33 low · D34 med. The one low (D33 proxy call)
predicted correctly; the one surprise came at med — calibration is honest but the D31
principle-application blind spot is real.

## Sitting 2026-09-05 — re-ratification after the critical review

The review's rulings were taken decision by decision (2026-09-05) and this sitting closed
them: the author scanned all 21 statement-grain bindings (confirmed as bound), ruled
keep-for-now on the six borderline `ncea` values (explicitly pending NZ colleague review),
and confirmed the five load-bearing amendment sentences verbatim.

| item | outcome of the arc | decision |
|---|---|---|
| D31 (shape, values, statement grain, `ncea` definition) | review overturned the sitting-1 build with material defects; amended twice | amend → ratified as amended |
| D32 (calculus re-band) | review showed the evidence rule applied to one end only | demote → **held** until Phase 5 publishes |
| D33 (locale contents; E bar) | review caught the §8 contradiction; bar moved to chain level | amend → ratified as amended |
| D34 (vocabulary) | two factual slips corrected; two stays recorded as judgment calls | amend → ratified as amended |
| D35 (Y8–10 auto-scored default) | new item from the review's counter-proposal | build → ratified |

**Prediction accuracy across the arc:** the review contradicted the sitting-1 expectation on
four of five items (D35 was net-new, no prior opinion). Sitting 1's four `build` grades were
honest foresight readings at the time; what they missed — provenance of the values, the §8
interaction, the false vocabulary premise — is exactly what the log's superseding note
records, and the telemetry grades the re-decisions as surprised accordingly.

Landing: decision-log header flipped to ratified (D32 held); graph at v0.14.0; OQ2 closed by
quotation. Merge of PR #1 is a separate act and not part of this record.

---

**SUPERSEDED 2026-09-03, before landing.** External review (the drafter's own critical
second look, plus verification of its checkable claims against the artifacts) surfaced
material the sitting did not have: the alignment values were populated from summarising
fetches rather than human reads; factual slips in D34 (NZ *general form* exists;
*factor* → *factorise* missed); a dangling Y13 map row; D25-violating prose in the locales;
and a D33 E-bar that quietly contradicts §8. The four `build` decisions above are void as
ratifications; a fresh sitting is required on the amended branch. The prediction grades
stand — they measure foresight at the time, and the surprise list just grew.
