Fixtures for the tools/ checks, run in CI so the scripts can't rot. Not real activities or banks.
- `bank-unit.md`: a bank with a unit blank and a reserved `!unit-wrong`; tools/check_bank.py and tools/lint_draft.py must pass.
- `bad-side-label.md`: a side label out of proportion with its drawing; tools/check_figures.py must FAIL.
- `bad-flag.md`: `segment A B open`, a flag the figure grammar refuses (read from the pinned facts); tools/check_figures.py must FAIL.
- `bad-caption.md`: a `caption:` line inside a `figure:` column (a second caption that silently wins if it differs: B-151); tools/check_figures.py must FAIL.
- `bad-binding.md`: a misconception binding not attached to any skill the activity names; tools/lint_draft.py must FAIL.
- `banks-tier/` (D66): `good/` tags every template and must pass with `--graph`; `bad-untagged/` (a Y9 skill's template with no `tier:`), `bad-position/` (a `tier:` line that is not the first line under its heading) and `bad-value/` (`d`, `C, P`) must FAIL with `--graph`. The Y8 `banks/rate.unit-rate.md` must still pass untagged with `--graph`: chain 1 stays valid.
