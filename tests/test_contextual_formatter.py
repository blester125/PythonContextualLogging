# Copyright 2023 Charles Andrews
"""Unit tests for contextuallogging._contextual_formatter."""

import logging  # noqa: I001
from logging import LogRecord
from unittest.mock import patch

import pytest
from assertpy import assert_that

from contextuallogging import ContextualFormatter


class TestContextualFormatter:
    """Unit tests for contextuallogging.ContextualFormatter."""

    @staticmethod
    @pytest.fixture()
    def contextual_formatter() -> ContextualFormatter:
        """Constructs a ContextualFormatter.

        Returns:
            ContextualFormatter: The ContextualFormatter.
        """
        return ContextualFormatter()

    @staticmethod
    @pytest.mark.parametrize(
        ("record", "expected"),
        [
            (
                LogRecord(
                    name="name",
                    level=logging.INFO,
                    pathname="pathname",
                    lineno=0,
                    msg="msg",
                    args=None,
                    exc_info=None,
                ),
                '{"level": "INFO", "logger": "name", "message": "msg", "timestamp": '
                '"2023-11-18T08:21:14.722896Z"}',
            ),
            (
                LogRecord(
                    name="name",
                    level=logging.INFO,
                    pathname="pathname",
                    lineno=0,
                    msg="%s",
                    args=("message",),
                    exc_info=None,
                ),
                '{"level": "INFO", "logger": "name", "message": "message", '
                '"timestamp": "2023-11-18T08:21:14.722896Z"}',
            ),
            (
                LogRecord(
                    name="name",
                    level=logging.INFO,
                    pathname="pathname",
                    lineno=0,
                    msg="msg\n",
                    args=None,
                    exc_info=None,
                ),
                '{"level": "INFO", "logger": "name", "message": "msg\\n", '
                '"timestamp": "2023-11-18T08:21:14.722896Z"}',
            ),
            (
                LogRecord(
                    name="name",
                    level=logging.INFO,
                    pathname="pathname",
                    lineno=0,
                    msg="msg",
                    args=None,
                    exc_info=(RuntimeError, RuntimeError(), None),
                ),
                '{"exception": null, "level": "INFO", "logger": "name", "message": '
                '"msg", "timestamp": "2023-11-18T08:21:14.722896Z"}',
            ),
            (
                LogRecord(
                    name="name",
                    level=logging.INFO,
                    pathname="pathname",
                    lineno=0,
                    msg="msg",
                    args=None,
                    exc_info=None,
                    sinfo="sinfo",
                ),
                '{"level": "INFO", "logger": "name", "message": "msg", "stack": '
                '"sinfo", "timestamp": "2023-11-18T08:21:14.722896Z"}',
            ),
        ],
    )
    @patch("time.time", lambda: 0)
    def test_format(
        contextual_formatter: ContextualFormatter,
        record: LogRecord,
        expected: str,
    ) -> None:
        """Tests happy path cases of ContextualFormatter.format().

        Args:
            contextual_formatter (ContextualFormatter): The ContextualFormatter.
            record (LogRecord): The LogRecord to format.
            expected (str): The expected formatted LogRecord.
        """
        record.created = 1700295674.722896
        assert_that(contextual_formatter.format(record=record)).is_equal_to(expected)
