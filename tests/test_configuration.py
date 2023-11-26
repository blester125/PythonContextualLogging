# Copyright 2023 Charles Andrews
"""Unit tests for contextuallogging._configuration."""

import sys  # noqa: I001
from json import JSONEncoder
from logging import Handler, StreamHandler
from typing import Final

from assertpy import assert_that

from contextuallogging import Configuration, get_configuration, set_configuration


class TestConfiguration:
    """Unit tests for contextuallogging.Configuration."""

    @staticmethod
    def test_post_init() -> None:
        """Tests happy path cases of Configuration.__post_init__()."""
        handler: Final[Handler] = StreamHandler(sys.stdin)
        encoder: Final[JSONEncoder] = JSONEncoder()
        _: Final[Configuration] = Configuration(
            handlers=[handler],
            encoder=encoder,
        )
        assert_that(
            getattr(handler.formatter, "_ContextualFormatter__encoder"),  # noqa: B009
        ).is_same_as(
            encoder,
        )


def test_get_configuration_set_configuration() -> None:
    """Tests happy path cases of get_configuration() and set_configuration()."""
    configuration: Final[Configuration] = Configuration(
        handlers=[StreamHandler(sys.stdout)],
        encoder=None,
    )
    set_configuration(configuration=configuration)
    assert_that(get_configuration()).is_equal_to(configuration)
