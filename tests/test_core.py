"""Tests for core meeting note transformation."""

import random

import pytest

from meeting_minutes_soap_opera.core import (
    dramaticize,
    extract_action_items,
    pick_cliffhanger,
    split_lines,
    summarize,
)


class TestSplitLines:
    """Tests for line splitting."""
    
    def test_split_simple_lines(self):
        """Test splitting simple multi-line text."""
        text = "Line 1\nLine 2\nLine 3"
        result = split_lines(text)
        assert len(result) == 3
        assert result[0] == "Line 1"
    
    def test_split_removes_empty_lines(self):
        """Test that empty lines are filtered."""
        text = "Line 1\n\nLine 3\n\n"
        result = split_lines(text)
        assert len(result) == 2
        assert "" not in result
    
    def test_split_strips_whitespace(self):
        """Test that lines are stripped."""
        text = "  Line 1  \n\t Line 2 \t"
        result = split_lines(text)
        assert result[0] == "Line 1"
        assert result[1] == "Line 2"
    
    def test_split_empty_input(self):
        """Test splitting empty input."""
        result = split_lines("")
        assert result == []


class TestDramaticize:
    """Tests for dramaticization."""
    
    def test_dramaticize_basic(self, sample_notes):
        """Test basic dramaticization."""
        rng = random.Random(42)
        result = dramaticize(sample_notes, rng, style="dramatic")
        assert isinstance(result, list)
        assert len(result) > 0
        assert all(isinstance(line, str) for line in result)
    
    def test_dramaticize_with_seed(self, sample_notes):
        """Test that same seed produces same output."""
        rng1 = random.Random(42)
        result1 = dramaticize(sample_notes, rng1, style="dramatic")
        
        rng2 = random.Random(42)
        result2 = dramaticize(sample_notes, rng2, style="dramatic")
        
        assert result1 == result2
    
    def test_dramaticize_different_styles(self, sample_notes):
        """Test dramaticization with different styles."""
        rng = random.Random(42)
        styles = ["dramatic", "snarky", "neutral"]
        results = []
        for style in styles:
            rng = random.Random(42)
            result = dramaticize(sample_notes, rng, style=style)
            results.append(result)
        
        # Results should be different due to different templates
        assert results[0] != results[1] or results[0] != results[2]
    
    def test_dramaticize_empty_input(self):
        """Test dramaticizing empty text."""
        rng = random.Random(42)
        result = dramaticize("", rng)
        assert result == []


class TestSummarize:
    """Tests for summarization."""
    
    def test_summarize_basic(self, sample_lines):
        """Test basic summarization."""
        result = summarize(sample_lines, max_items=3)
        assert len(result) <= 3
        assert all(isinstance(line, str) for line in result)
    
    def test_summarize_respects_max(self, sample_lines):
        """Test that max_items is respected."""
        result = summarize(sample_lines, max_items=2)
        assert len(result) == 2
    
    def test_summarize_removes_duplicates(self):
        """Test that duplicates are removed."""
        lines = ["item1", "item2", "item1", "item3", "item2"]
        result = summarize(lines, max_items=10)
        assert len(result) == 3
    
    def test_summarize_empty_input(self):
        """Test summarizing empty list."""
        result = summarize([], max_items=3)
        assert result == []


class TestExtractActionItems:
    """Tests for action item extraction."""
    
    def test_extract_action_items(self, sample_lines):
        """Test basic action item extraction."""
        result = extract_action_items(sample_lines)
        assert len(result) > 0
        assert any("follow" in line.lower() or "todo" in line.lower() for line in result)
    
    def test_extract_respects_max(self, sample_lines):
        """Test that max_items is respected."""
        result = extract_action_items(sample_lines, max_items=2)
        assert len(result) <= 2
    
    def test_extract_finds_keywords(self):
        """Test that keywords are found."""
        lines = [
            "No action here",
            "TODO: Something",
            "Regular item",
            "Action needed",
        ]
        result = extract_action_items(lines)
        assert len(result) > 0
        assert any("TODO" in line or "Action" in line for line in result)
    
    def test_extract_empty_input(self):
        """Test extracting from empty list."""
        result = extract_action_items([])
        assert result == []


class TestPickCliffhanger:
    """Tests for cliffhanger selection."""
    
    def test_pick_cliffhanger_basic(self):
        """Test basic cliffhanger selection."""
        rng = random.Random(42)
        result = pick_cliffhanger(rng, style="dramatic")
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_pick_cliffhanger_with_seed(self):
        """Test that same seed produces same cliffhanger."""
        result1 = pick_cliffhanger(random.Random(42), style="dramatic")
        result2 = pick_cliffhanger(random.Random(42), style="dramatic")
        assert result1 == result2
    
    def test_pick_cliffhanger_different_styles(self):
        """Test cliffhangers for different styles."""
        styles = ["dramatic", "snarky", "neutral"]
        cliffhangers = []
        for style in styles:
            cliffhanger = pick_cliffhanger(random.Random(42), style=style)
            cliffhangers.append(cliffhanger)
        
        # All should be strings
        assert all(isinstance(c, str) for c in cliffhangers)
