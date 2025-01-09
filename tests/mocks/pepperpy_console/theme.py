"""Mock implementations of theme-related components."""

from typing import Dict, List, Optional


class Theme:
    """Mock implementation of a theme."""

    def __init__(self, name: str, styles: Optional[Dict[str, str]] = None) -> None:
        """Initialize the theme."""
        self.name = name
        self.styles = styles or {}
        self.active = False

    def activate(self) -> None:
        """Activate the theme."""
        self.active = True

    def deactivate(self) -> None:
        """Deactivate the theme."""
        self.active = False


class ThemeManager:
    """Mock implementation of the theme manager."""

    def __init__(self) -> None:
        """Initialize the theme manager."""
        self.themes: Dict[str, Theme] = {}
        self.active_theme: Optional[Theme] = None

    def register_theme(
        self, name: str, styles: Optional[Dict[str, str]] = None
    ) -> Theme:
        """Register a new theme."""
        theme = Theme(name, styles)
        self.themes[name] = theme
        return theme

    def get_theme(self, name: str) -> Optional[Theme]:
        """Get a theme by name."""
        return self.themes.get(name)

    def list_themes(self) -> List[str]:
        """List all registered themes."""
        return list(self.themes.keys())

    def activate_theme(self, name: str) -> bool:
        """Activate a theme by name."""
        theme = self.get_theme(name)
        if theme:
            if self.active_theme:
                self.active_theme.deactivate()
            theme.activate()
            self.active_theme = theme
            return True
        return False

    def get_active_theme(self) -> Optional[Theme]:
        """Get the currently active theme."""
        return self.active_theme
