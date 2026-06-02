"""Configuration management for the application."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AppConfig:
    """Application configuration settings.
    
    Attributes:
        mode: Processing mode (recap, summary, actions, full)
        style: Drama style (dramatic, snarky, neutral)
        max_items: Maximum summary/action items
        seed: Random seed for reproducibility
        verbose: Enable debug logging
    """
    mode: str = "recap"
    style: str = "dramatic"
    max_items: int = 5
    seed: int | None = None
    verbose: bool = False
    
    def to_dict(self) -> dict:
        """Convert config to dictionary."""
        return {
            "mode": self.mode,
            "style": self.style,
            "max_items": self.max_items,
            "seed": self.seed,
            "verbose": self.verbose,
        }


# Global config instance
_config: AppConfig | None = None


def get_config() -> AppConfig:
    """Get the global application configuration."""
    global _config
    if _config is None:
        _config = AppConfig()
    return _config


def set_config(config: AppConfig) -> None:
    """Set the global application configuration."""
    global _config
    _config = config
