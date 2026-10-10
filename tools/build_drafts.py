#!/usr/bin/env python3
"""Build every chain's catalogue drafts from its sources, check them, and (with --check) prove the
catalogue still matches the sources.

Sources live at drafts/<chain folder>/<NN-name>.src.md: the catalogue file with each figure
replaced by a placeholder (@@FENCE name@@, or @@COL name@@ inside a `figure:` column). The figures
are defined once, from their intended measurements, in tools/figs/<module>.py (CHAINS below).

    python3 tools/build_drafts.py                       # build and check every chain (CI)
    python3 tools/build_drafts.py --check CATALOGUE     # ... and diff against the catalogue
    python3 tools/build_drafts.py --out DIR             # keep the built drafts and answers

For each built draft: tools/lint_draft.py and tools/check_figures.py (with the answers the build
wrote) must pass. With --check, every built draft must be byte-identical to
CATALOGUE/<chain folder>/<NN-name>.md. Run --check before every batch import, beside
check_guides.py and check_tags.py (the catalogue has no CI). An edit made to a catalogue file
during a read belongs in its source file; a catalogue file that differs fails here until it is.

Chains without sources (their figures were authored by hand) are not built; the catalogue checks
still cover them.
"""
import argparse
import difflib
import io
import os
import sys
import tempfile
from contextlib import redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "figs"))

import check_figures  # noqa: E402
import core  # noqa: E402
import lint_draft  # noqa: E402

# chain folder -> figure module in tools/figs
CHAINS = {
    "710-chain.measure.area-volume": "area_volume",
    "713-chain.geom.parallel-lines": "parallel_lines",
    "714-chain.geom.transformations": "transformations",
}


def quiet(fn, *args):
    buf = io.StringIO()
    with redirect_stdout(buf):
        code = fn(*args)
    return code, buf.getvalue()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", metavar="CATALOGUE", type=Path)
    ap.add_argument("--out", type=Path)
    args = ap.parse_args()

    out = args.out or Path(tempfile.mkdtemp(prefix="build-drafts-"))
    failures, built = [], 0
    src_root = REPO / "drafts"
    folders = sorted(p.name for p in src_root.iterdir() if p.is_dir()) if src_root.is_dir() else []
    if not folders:
        print("FAIL: no chain sources under drafts/ (vacuity guard)")
        return 1
    for folder in folders:
        if folder not in CHAINS:
            failures.append(f"{folder}: has sources but no figure module in CHAINS")
            continue
        module = __import__(CHAINS[folder])
        core.reset()
        (out / folder).mkdir(parents=True, exist_ok=True)
        for src in sorted((src_root / folder).glob("*.src.md")):
            name = src.name[: -len(".src.md")]
            draft = out / folder / f"{name}.md"
            answers = out / folder / f"{name}.answers.json"
            core.build(module.define, src, draft, answers)
            built += 1
            code, log = quiet(lint_draft.main, str(draft), str(REPO), [])
            if code:
                failures.append(f"{folder}/{name}: lint\n{log}")
            code, log = quiet(check_figures.main, str(draft), str(answers))
            if code:
                failures.append(f"{folder}/{name}: figures\n{log}")
            if args.check:
                cat = args.check / folder / f"{name}.md"
                if not cat.exists():
                    failures.append(f"{folder}/{name}: no catalogue file at {cat}")
                elif cat.read_bytes() != draft.read_bytes():
                    diff = "".join(difflib.unified_diff(
                        cat.read_text(encoding="utf-8").splitlines(True),
                        draft.read_text(encoding="utf-8").splitlines(True),
                        f"catalogue/{folder}/{name}.md", f"built from drafts/{folder}/{src.name}", n=1))
                    failures.append(f"{folder}/{name}: catalogue differs from its source "
                                    f"(make the edit in the .src.md)\n{diff}")
    for f in failures:
        print("FAIL:", f)
    if failures:
        return 1
    where = f", output in {out}" if args.out else ""
    mode = " and match the catalogue" if args.check else ""
    print(f"OK: {built} drafts from {len(folders)} chains build, lint and pass the figure check{mode}{where}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
