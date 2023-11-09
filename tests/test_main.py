# Copyright 2023 Charles Andrews
"""Unit tests for contextuallogging.main."""
from contextuallogging import main


class TestMain:
    """Unit tests for contextuallogging.Main."""

    @staticmethod
    def test_main() -> None:
        """Unit test for happy-path cases of contextuallogging.Main.main."""
        main()
