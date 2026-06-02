"""Test configuration and fixtures."""

import pytest


@pytest.fixture
def sample_notes() -> str:
    """Sample meeting notes for testing."""
    return """
    Discussed roadmap for Q3
    Noted blockers with deployment
    Alice to follow up on API performance
    Bob assigned to refactor database
    Todo: Add monitoring
    Next steps: Review PR by Friday
    """


@pytest.fixture
def sample_lines() -> list[str]:
    """Sample parsed meeting lines."""
    return [
        "Discussed roadmap for Q3",
        "Noted blockers with deployment",
        "Alice to follow up on API performance",
        "Bob assigned to refactor database",
        "Todo: Add monitoring",
        "Next steps: Review PR by Friday",
    ]
