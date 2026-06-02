from __future__ import annotations

import random

from .data import ACTION_KEYWORDS, STYLES


def split_lines(text: str) -> list[str]:
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        lines = [text.strip()] if text.strip() else []
    return lines


def dramaticize(text: str, rng: random.Random, style: str = "dramatic") -> list[str]:
    lines = split_lines(text)
    if not lines:
        return []
    pack = STYLES.get(style, STYLES["dramatic"])
    result = []
    for line in lines:
        intro = rng.choice(pack["intros"])
        emphasis = rng.choice(pack["emphasis"])
        result.append(f"{intro} {line} — {emphasis}.")
    return result


def summarize(lines: list[str], max_items: int = 3) -> list[str]:
    if not lines:
        return []
    summary: list[str] = []
    for line in lines:
        if line not in summary:
            summary.append(line)
        if len(summary) >= max_items:
            break
    return summary


def extract_action_items(lines: list[str], max_items: int = 5) -> list[str]:
    if not lines:
        return []
    items: list[str] = []
    for line in lines:
        lower = line.lower()
        if any(keyword in lower for keyword in ACTION_KEYWORDS):
            items.append(line)
        if len(items) >= max_items:
            break
    return items


def pick_cliffhanger(rng: random.Random, style: str = "dramatic") -> str:
    pack = STYLES.get(style, STYLES["dramatic"])
    return rng.choice(pack["cliffhangers"])
