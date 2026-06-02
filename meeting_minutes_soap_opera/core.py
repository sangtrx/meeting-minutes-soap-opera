"""Core functionality for transforming meeting notes into dramatic recaps."""

from __future__ import annotations

import random

from .data import ACTION_KEYWORDS, STYLES


def split_lines(text: str) -> list[str]:
    """Split text into individual lines, filtering empty ones.
    
    Args:
        text: Input text to split
        
    Returns:
        List of non-empty lines
    """
    lines = [line.strip() for line in text.splitlines() if line.strip()]
    if not lines:
        lines = [text.strip()] if text.strip() else []
    return lines


def dramaticize(text: str, rng: random.Random, style: str = "dramatic") -> list[str]:
    """Transform plain text into dramatic recap lines.
    
    Adds dramatic intros and emphasis based on the selected style.
    
    Args:
        text: Input text to dramaticize
        rng: Random generator for reproducible output
        style: Drama style ('dramatic', 'snarky', 'neutral')
        
    Returns:
        List of dramaticized lines
    """
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
    """Create a summary of the top meeting points.
    
    Args:
        lines: List of lines to summarize
        max_items: Maximum number of items to include
        
    Returns:
        Summarized list of unique items
    """
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
    """Extract action items from meeting notes.
    
    Searches for lines containing action-related keywords.
    
    Args:
        lines: List of meeting note lines
        max_items: Maximum number of action items to extract
        
    Returns:
        List of extracted action items
    """
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
    """Pick a random cliffhanger phrase.
    
    Args:
        rng: Random generator for reproducible output
        style: Drama style for the cliffhanger
        
    Returns:
        A cliffhanger phrase in the selected style
    """
    pack = STYLES.get(style, STYLES["dramatic"])
    return rng.choice(pack["cliffhangers"])
