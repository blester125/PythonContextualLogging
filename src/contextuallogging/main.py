# Copyright 2023 Charles Andrews
"""Entrypoint script."""

import logging


def main() -> None:
    """Entrypoint."""
    logging.log(level=logging.INFO, msg="Hello World!")


if __name__ == "__main__":
    main()
