# Copyright 2023 Charles Andrews
"""Contains utilities for modifying the global contextuallogging configuration."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from logging import Handler, StreamHandler
from typing import TYPE_CHECKING

from contextuallogging._contextual_formatter import ContextualFormatter

if TYPE_CHECKING:
    from json import JSONEncoder


@dataclass
class Configuration:
    """Global configuration definition for the contextuallogging package."""

    handlers: list[Handler]
    """Handlers which will be attached to all loggers constructed by this package.

    By default, this will be a single handler which sends log messages to sys.stderr,
    mirroring the behavior of the built-in logging package.
    """

    encoder: JSONEncoder | None
    """JSON encoder to use when constructing new ContextualFormatter objects.

    By default, this will be None and will result in the default encoder of
    ContextualFormatter being used.
    """

    def __post_init__(self) -> None:
        """Performs post-constructor setup.

        This method ensures that all handlers have their formatters set to unique
        ContextualFormatter instances which use the configured JSON encoder.
        """
        for handler in self.handlers:
            handler.setFormatter(ContextualFormatter(encoder=self.encoder))


_CONFIGURATION: Configuration = Configuration(
    handlers=[StreamHandler(sys.stderr)],
    encoder=None,
)


def get_configuration() -> Configuration:
    """Gets the current global package configuration.

    Returns:
        Configuration: The current global package configuration.
    """
    return _CONFIGURATION


def set_configuration(configuration: Configuration) -> None:
    """Sets the global package configuration.

    Args:
        configuration (Configuration): The new global package configuration.
    """
    global _CONFIGURATION  # noqa: PLW0603
    _CONFIGURATION = configuration
