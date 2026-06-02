# Meeting Minutes → Soap Opera

Transform boring meeting notes into dramatic theatrical recaps with adjustable drama levels.
Because sometimes you need your standup notes served with a side of theatrical flair.

## Features

- 🎭 **3 Drama Levels** — Choose from dramatic, snarky, or neutral styles
- 📝 **Multiple Modes** — Recap, summary, action items, or full transformation
- 🎲 **Reproducible Output** — Use random seed for consistent results
- 📋 **Smart Extraction** — Automatically identify action items
- 🔄 **Flexible Input** — Read from file or stdin
- 🧪 **Well-Tested** — 27+ comprehensive tests
- 📦 **Pure Python** — No external dependencies required

## Installation

Clone the repository and run:

```bash
cd meeting-minutes-soap-opera
python main.py --help
```

### Development Setup

Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

Run tests:

```bash
pytest tests/ -v
```

## Quick Start

### Simple Usage

Transform boring meeting notes into drama:

```bash
# From file
python main.py --file notes.txt

# From stdin
cat notes.txt | python main.py

# With options
python main.py --file notes.txt --mode full --style snarky
python main.py --mode actions --max-items 3
```

### Different Styles

```bash
# Dramatic (default) - Maximum flair
python main.py "Meeting about Q3 roadmap" --style dramatic

# Snarky - Side-eye included
python main.py "Another standup" --style snarky

# Neutral - Professional delivery
python main.py "Budget discussion" --style neutral
```

### Processing Modes

```bash
# Recap - Dramatized version of all notes
python main.py --file notes.txt --mode recap

# Summary - Top meeting points
python main.py --file notes.txt --mode summary --max-items 5

# Actions - Extract action items only
python main.py --file notes.txt --mode actions --max-items 10

# Full - Everything with dramatic treatment
python main.py --file notes.txt --mode full --style snarky
```

### Reproducible Output

Use a seed for consistent output:

```bash
python main.py --file notes.txt --seed 42
```

## Options

- `--file` — Input file with meeting notes (reads stdin if omitted)
- `--mode` — Processing mode: `recap`, `summary`, `actions`, `full`. Default: recap
- `--style` — Drama style: `dramatic`, `snarky`, `neutral`. Default: dramatic
- `--max-items` — Limit summary/action items (1-100). Default: 5
- `--seed` — Random seed for reproducible output
- `--verbose` — Enable debug logging

## Architecture

### Core Modules

- **`core.py`** — Text transformation engine (dramaticize, summarize, extract)
- **`data.py`** — Drama templates and keywords
- **`io.py`** — File I/O and stdin handling
- **`cli.py`** — Command-line interface
- **`validation.py`** — Input validation
- **`config.py`** — Configuration management
- **`logging_config.py`** — Logging setup
- **`exceptions.py`** — Custom exception types

## Testing

Run the comprehensive test suite:

```bash
pytest tests/ -v
```

With coverage report:

```bash
pytest tests/ --cov=meeting_minutes_soap_opera
```

Tests cover:
- Core transformation logic
- Input validation
- Action item extraction
- Summarization
- Style application

## Development

### Code Style

Code is formatted with Black and linted with Ruff:

```bash
black meeting_minutes_soap_opera tests
ruff check . --fix
```

Type checking:

```bash
mypy meeting_minutes_soap_opera
```

### Project Structure

```
meeting-minutes-soap-opera/
├── meeting_minutes_soap_opera/  # Main package
│   ├── core.py                  # Transformation logic
│   ├── data.py                  # Templates and keywords
│   ├── io.py                    # Input/output
│   ├── cli.py                   # CLI interface
│   ├── config.py                # Configuration
│   ├── validation.py            # Input validation
│   ├── logging_config.py        # Logging
│   ├── exceptions.py            # Custom exceptions
│   └── __init__.py              # Package exports
├── tests/                       # Test suite
│   ├── test_core.py             # Core logic tests
│   ├── test_validation.py       # Validation tests
│   └── conftest.py              # Pytest fixtures
├── requirements.txt             # Production dependencies
├── requirements-dev.txt         # Development dependencies
├── pytest.ini                   # Pytest configuration
├── Makefile                     # Development shortcuts
├── tox.ini                      # Multi-Python testing
└── README.md                    # This file
```

## Examples

### Meeting Notes

Input:
```
Discussed Q3 roadmap
Noted API performance issues
Alice to follow up on database optimization
Bob assigned to write performance tests
Action: Schedule follow-up meeting
```

### Dramatic Output
```
In a shocking turn, Discussed Q3 roadmap — dramatically.
Against all odds, Noted API performance issues — with thunderous gravitas.
In a twist no one expected, Alice to follow up on database optimization — as the suspense mounted.
Meanwhile, Bob assigned to write performance tests — under a stormy sky.
In a shocking turn, Action: Schedule follow-up meeting — to the sound of distant keyboards.

Will the action items survive the week?
```

### Snarky Output
```
Plot twist: Discussed Q3 roadmap — with a side of eye-roll.
As if things weren't spicy, Noted API performance issues — while pretending to be surprised.
Cue the side-eye, Alice to follow up on database optimization — as the coffee ran low.
In the latest episode, Bob assigned to write performance tests — with suspicious enthusiasm.
Somehow, Action: Schedule follow-up meeting — as everyone nodded knowingly.

Will the calendar invite strike again?
```

## License

MIT License — See LICENSE file for details

## Contributing

Contributions welcome! See CONTRIBUTING.md for guidelines.

## Changelog

### v0.2.0
- Added comprehensive logging system
- Added input validation with detailed error messages
- Added configuration management module
- Added custom exceptions
- Added comprehensive test suite (27+ tests)
- Improved type hints and docstrings
- Added package entry point (__main__.py)
- Added development infrastructure

### v0.1.0
- Initial release
- Text transformation to dramatic recaps
- Multiple styles (dramatic, snarky, neutral)
- Multiple modes (recap, summary, actions, full)
- Random seed support
- File and stdin input

