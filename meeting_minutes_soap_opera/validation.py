"""Input validation utilities."""

from __future__ import annotations


class ValidationError(ValueError):
    """Raised when input validation fails."""
    pass


def validate_mode(mode: str) -> str:
    """Validate processing mode.
    
    Args:
        mode: Mode to validate ('recap', 'summary', 'actions', 'full')
        
    Returns:
        Valid mode
        
    Raises:
        ValidationError: If mode is invalid
    """
    valid_modes = ("recap", "summary", "actions", "full")
    if mode not in valid_modes:
        raise ValidationError(f"Mode must be one of {valid_modes}, got {mode}")
    return mode


def validate_style(style: str) -> str:
    """Validate drama style.
    
    Args:
        style: Style to validate ('dramatic', 'snarky', 'neutral')
        
    Returns:
        Valid style
        
    Raises:
        ValidationError: If style is invalid
    """
    valid_styles = ("dramatic", "snarky", "neutral")
    if style not in valid_styles:
        raise ValidationError(f"Style must be one of {valid_styles}, got {style}")
    return style


def validate_max_items(max_items: int) -> int:
    """Validate maximum items count.
    
    Args:
        max_items: Maximum items to validate
        
    Returns:
        Valid max_items value
        
    Raises:
        ValidationError: If value is invalid
    """
    if not isinstance(max_items, int):
        raise ValidationError(f"max_items must be an integer, got {type(max_items).__name__}")
    if max_items < 1:
        raise ValidationError(f"max_items must be at least 1, got {max_items}")
    if max_items > 100:
        raise ValidationError(f"max_items must be at most 100, got {max_items}")
    return max_items
