"""Input/output utilities for reading meeting notes."""

from __future__ import annotations

import sys


def load_text(path: str | None) -> str:
    """Load meeting notes from a file or stdin.
    
    Args:
        path: Optional path to file. If None, reads from stdin if available.
        
    Returns:
        Meeting notes text
    """
    if path:
        return open(path, "r", encoding="utf-8").read().strip()
    if not sys.stdin.isatty():
        return sys.stdin.read().strip()
    return "Discussed roadmap, noted blockers, and assigned action items."
