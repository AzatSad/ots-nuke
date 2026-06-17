"""OTS_NUKE.

▄▀▀▀▀▄ ▀▀▀█▀▀▀ ▄▀▀▀▀  █▄   █ █    █ █    █ ▄▀▀▀▀
▀    ▀    ▀    ▀      ▀ ▀  ▀ ▀    ▀ ▀   ▄▀ ▀
█    █    █     ▀▀▀▀▄ █  █ █ █    █ █▀▀▀▄  ▄▀▀▀
█    █    █         █ █  ▀▄█ █    █ █    █ █
 ▀▀▀▀     ▀     ▀▀▀▀  ▀    ▀  ▀▀▀▀  ▀    ▀  ▀▀▀▀
.
"""

import tomllib
from pathlib import Path
from typing import Final


def _get_project_field(field: str) -> str:
    """Get value in pyproject.toml."""
    pyproject_filename = 'pyproject.toml'
    pyproject_path = Path(__file__).parent.parent / Path(pyproject_filename)

    with Path.open(pyproject_path, 'rb') as pyproject_file:
        pyproject_data = tomllib.load(pyproject_file)

    return str(pyproject_data['project'][field])


NAME: Final[str] = _get_project_field('name')
"""Project name."""

VERSION: Final[str] = _get_project_field('version')
"""Project version."""


def _get_project_information() -> dict[str, str]:
    """Get project information."""
    return {
        'name': NAME,
        'vtrsion': VERSION,
    }


def show_project_logo() -> None:
    """Show project logo."""
    logo = __doc__ or ''
    print(logo.format(version=VERSION))
