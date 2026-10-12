"""chain.number.place-value (701-): place value, powers of ten, rounding.

The chain has no figures: place-value tables are pipe tables with blanks, and number lines are
written in words until the platform's decimal-step tolerance fix is live (brief, 2026-10-12).
build_drafts.py needs a figure module for every chain with sources, so define() is empty.

Register it in tools/build_drafts.py:
    "701-chain.number.place-value": "place_value",
"""

from core import FIGS, ANS, fig  # noqa: F401


def define():
    """No figures in this chain."""
