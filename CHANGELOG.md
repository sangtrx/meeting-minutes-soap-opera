# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.2.0] - 2026-06-02

### Added
- Comprehensive logging system with configurable debug output
- Input validation module with detailed error messages
- Configuration management module for centralized settings
- Custom exceptions module for better error handling
- Package entry point (`__main__.py`) for `python -m meeting_minutes_soap_opera`
- Comprehensive test suite with 27+ tests covering:
  - Core transformation logic
  - Input validation
  - Style application
  - Action item extraction
  - Summarization
- Development dependencies file (`requirements-dev.txt`)
- Contributing guidelines document
- Enhanced README with detailed examples and architecture
- pytest configuration file

### Changed
- Improved all module docstrings with comprehensive documentation
- Added type hints to all functions and constants
- Enhanced data module with better documentation

## [0.1.0] - 2026-05-XX

### Added
- Initial release
- Text transformation engine with 3 drama styles
- Multiple processing modes (recap, summary, actions, full)
- Automatic action item extraction with keyword matching
- File and stdin input support
- Random seed support for reproducible output
- Command-line interface with argparse
