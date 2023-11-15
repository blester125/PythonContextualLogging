# Copyright 2023 Charles Andrews
# fmt: off
"""[![Build Status](https://github.com/cfandrews/PythonContextualLogging/actions/workflows/build.yml/badge.svg)](https://github.com/cfandrews/PythonContextualLogging/actions)
[![Documentation Status](https://github.com/cfandrews/PythonContextualLogging/actions/workflows/documentation.yml/badge.svg)](https://github.com/cfandrews/PythonContextualLogging/actions)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)
[![Linting: Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/charliermarsh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)

Pure-Python semantic logging library with thread-local context.

[Source](https://github.com/cfandrews/PythonContextualLogging/)  
[Documentation](https://cfandrews.github.io/PythonContextualLogging/contextuallogging.html)
"""  # noqa: W291, D205, D415
# fmt: on

from __future__ import annotations

from typing import Final

from ._main import main

__all__: Final[list[str]] = ["main"]
__docformat__: Final[str] = "google"
