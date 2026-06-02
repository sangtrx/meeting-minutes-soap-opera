from __future__ import annotations

import sys


def load_text(path: str | None) -> str:
    if path:
        return open(path, "r", encoding="utf-8").read().strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return "Discussed roadmap, noted blockers, and assigned action items."
