"""Tests for input validation."""

import pytest

from meeting_minutes_soap_opera.validation import (
    validate_max_items,
    validate_mode,
    validate_style,
)
from meeting_minutes_soap_opera.exceptions import ValidationError


class TestValidateMode:
    """Tests for mode validation."""
    
    def test_valid_modes(self):
        """Test all valid modes."""
        modes = ["recap", "summary", "actions", "full"]
        for mode in modes:
            assert validate_mode(mode) == mode
    
    def test_invalid_mode(self):
        """Test invalid mode."""
        with pytest.raises(ValidationError):
            validate_mode("invalid")


class TestValidateStyle:
    """Tests for style validation."""
    
    def test_valid_styles(self):
        """Test all valid styles."""
        styles = ["dramatic", "snarky", "neutral"]
        for style in styles:
            assert validate_style(style) == style
    
    def test_invalid_style(self):
        """Test invalid style."""
        with pytest.raises(ValidationError):
            validate_style("bogus")


class TestValidateMaxItems:
    """Tests for max items validation."""
    
    def test_valid_max_items(self):
        """Test valid max items."""
        for val in [1, 5, 50, 100]:
            assert validate_max_items(val) == val
    
    def test_invalid_type(self):
        """Test non-integer input."""
        with pytest.raises(ValidationError):
            validate_max_items("5")
    
    def test_min_boundary(self):
        """Test minimum boundary."""
        with pytest.raises(ValidationError):
            validate_max_items(0)
    
    def test_max_boundary(self):
        """Test maximum boundary."""
        with pytest.raises(ValidationError):
            validate_max_items(101)
