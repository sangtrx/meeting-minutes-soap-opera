"""Meeting Minutes Soap Opera — Transform boring meeting notes into dramatic recaps.

This package provides utilities for turning dry meeting notes into entertaining
theatrical recaps with configurable drama levels.

Core API:
    - dramaticize() — Transform text into dramatic recap lines
    - summarize() — Create a meeting summary
    - extract_action_items() — Extract action items from notes
    - pick_cliffhanger() — Generate a cliffhanger phrase
    - split_lines() — Parse meeting notes into lines
    - load_text() — Load notes from file or stdin

Example:
    >>> from meeting_minutes_soap_opera import dramaticize, load_text
    >>> import random
    >>> notes = load_text("meeting.txt")
    >>> lines = notes.split("\\n")
    >>> rng = random.Random(42)
    >>> dramatic = dramaticize(notes, rng, style="dramatic")
"""

__version__ = "0.2.0"

from .core import dramaticize, extract_action_items, pick_cliffhanger, split_lines, summarize
from .io import load_text

__all__ = [
    "dramaticize",
    "extract_action_items",
    "load_text",
    "pick_cliffhanger",
    "split_lines",
    "summarize",
    "__version__",
]
