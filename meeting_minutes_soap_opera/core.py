from __future__ import annotations

import random

from .data import EMPHASIS, INTROS


def dramaticize(text: str, rng: random.Random) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        lines = [text.strip()] if text.strip() else []
    if not lines:
        return []
    result = []
    for line in lines:
        intro = rng.choice(INTROS)
        emphasis = rng.choice(EMPHASIS)
        result.append(f"{intro} {line} — {emphasis}.")
    return result
