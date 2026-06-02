# Contributing to Meeting Minutes Soap Opera

Thank you for your interest in contributing! This document outlines the process for contributing to the project.

## Development Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/meeting-minutes-soap-opera.git
cd meeting-minutes-soap-opera
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install development dependencies:
```bash
pip install -r requirements-dev.txt
```

## Code Style

We follow PEP 8 with these tools:

- **Black** — Code formatting (line length: 100)
- **Ruff** — Linting
- **mypy** — Type checking

Before submitting a PR, run:

```bash
black meeting_minutes_soap_opera tests
ruff check . --fix
mypy meeting_minutes_soap_opera
```

## Testing

We use pytest for testing. Ensure all tests pass:

```bash
pytest tests/ -v
```

For coverage:

```bash
pytest tests/ --cov=meeting_minutes_soap_opera
```

## Commit Messages

Use clear, descriptive messages:

- ✅ Good: `Add action item extraction`
- ✅ Good: `Fix style application for dramatic mode`
- ❌ Avoid: `Fix bug` or `Update code`

## Pull Request Process

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing-feature`
3. Make your changes
4. Add tests for new functionality
5. Run the full test suite: `pytest tests/ -v`
6. Commit with clear messages
7. Push to your fork and open a PR

## Types of Contributions

### Bug Fixes
- Create a test that reproduces the bug
- Fix the issue
- Verify the test passes

### New Features
- Discuss in an issue first (for larger features)
- Write tests using TDD
- Update README with examples
- Add comprehensive docstrings

### Documentation
- Fix typos and improve clarity
- Add examples
- Improve technical accuracy

## Code Guidelines

### Type Hints
All functions should have type hints:

```python
def extract_action_items(lines: list[str], max_items: int = 5) -> list[str]:
    """Extract action items from meeting notes."""
    ...
```

### Docstrings
Use Google-style docstrings:

```python
def function_name(param1: str, param2: int) -> str:
    """Brief description.
    
    Args:
        param1: Description of param1
        param2: Description of param2
        
    Returns:
        Description of return value
    """
```

### Error Handling
Use custom exceptions from `exceptions.py`:

```python
from meeting_minutes_soap_opera.exceptions import ValidationError

def validate(data: str) -> str:
    if not data:
        raise ValidationError("Data cannot be empty")
    return data
```

## Questions?

- Open an issue for bugs and features
- Discuss in existing issues before major work
- Tag issues with appropriate labels

Thank you for contributing! 🎭
