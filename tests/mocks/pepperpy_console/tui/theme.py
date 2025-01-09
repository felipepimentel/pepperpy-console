"""Mock TUI theme module."""

from pathlib import Path
from typing import Dict, Optional


class Theme:
    """Mock theme class."""

    def __init__(self, name: str) -> None:
        """Initialize the theme."""
        self.name = name

    @classmethod
    async def load(cls, path: Path) -> "Theme":
        """Load a theme from file."""
        return cls(path.stem)


class ThemeManager:
    """Mock theme manager for handling multiple themes."""

    def __init__(self) -> None:
        """Initialize the theme manager."""
        self.themes: Dict[str, Theme] = {}
        self.current_theme: Optional[Theme] = None

    async def load_theme(self, path: Path) -> Theme:
        """Load a theme from file."""
        theme = await Theme.load(path)
        self.themes[theme.name] = theme
        return theme

    async def load_themes(self, directory: Path) -> None:
        """Load all themes from directory."""
        for path in directory.glob("*.yaml"):
            await self.load_theme(path)
        if self.themes:
            # Set first theme as default
            first_theme = next(iter(self.themes))
            self.set_theme(first_theme)

    def set_theme(self, name: str) -> None:
        """Set the active theme."""
        if name in self.themes:
            self.current_theme = self.themes[name]

    def get_theme(self, name: str) -> Optional[Theme]:
        """Get a theme by name."""
        return self.themes.get(name)
