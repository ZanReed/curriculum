#!/usr/bin/env python3
"""Build a chain's catalogue drafts from its source files.

    python3 tools/figs/build.py <chain-module> <src.md> <out.md> <answers.json>

<chain-module> is a module in tools/figs (parallel_lines, area_volume). Each chain module
defines its figures in define(); core.build() replaces the @@FENCE / @@COL placeholders and writes
the answers map for tools/check_figures.py.
"""
import importlib
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import core  # noqa: E402


def main():
    if len(sys.argv) != 5:
        print(__doc__, file=sys.stderr)
        return 2
    module, src, out, answers = sys.argv[1:]
    chain = importlib.import_module(module)
    core.build(chain.define, src, out, answers)
    return 0


if __name__ == "__main__":
    sys.exit(main())
