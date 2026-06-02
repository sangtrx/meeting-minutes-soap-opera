"""Custom exceptions for the application."""


class SoapOperaError(Exception):
    """Base exception for all soap opera errors."""
    pass


class ValidationError(SoapOperaError):
    """Raised when input validation fails."""
    pass


class ProcessingError(SoapOperaError):
    """Raised when processing fails."""
    pass


class ConfigError(SoapOperaError):
    """Raised when configuration is invalid."""
    pass


class IOError(SoapOperaError):
    """Raised when file I/O fails."""
    pass
