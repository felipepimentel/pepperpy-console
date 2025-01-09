"""Theme system for TUI applications."""

from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, Optional

import structlog
import yaml

logger = structlog.get_logger(__name__)


@dataclass
class ThemeColors:
    """Theme color configuration.

    Attributes:
        primary (str): Primary color
        secondary (str): Secondary color
        accent (str): Accent color
        background (str): Background color
        text (str): Text color
        error (str): Error color
        warning (str): Warning color
        success (str): Success color
        info (str): Info color
        selection (str): Selection color
    """

    primary: str = "#bd93f9"
    secondary: str = "#6272a4"
    accent: str = "#ff79c6"
    background: str = "#282a36"
    text: str = "#f8f8f2"
    error: str = "#ff5555"
    warning: str = "#ffb86c"
    success: str = "#50fa7b"
    info: str = "#8be9fd"
    selection: str = "#44475a"

    def get_variants(self, color: str) -> Dict[str, str]:
        """Get color variants.

        Args:
            color: Base color

        Returns:
            Dict[str, str]: Color variants
        """
        # TODO: Implement color variant generation
        return {"light": color, "dark": color, "hover": color}


@dataclass
class ThemeMetrics:
    """Theme sizing and spacing configuration.

    Attributes:
        spacing (Dict[str, int]): Spacing values
        sizes (Dict[str, int]): Size values
        breakpoints (Dict[str, int]): Breakpoint values
    """

    spacing: Dict[str, int] = field(
        default_factory=lambda: {"xs": 1, "sm": 2, "md": 4, "lg": 8, "xl": 16}
    )

    sizes: Dict[str, int] = field(
        default_factory=lambda: {
            "icon": 1,
            "input": 3,
            "header": 3,
            "footer": 3,
            "sidebar": 30,
        }
    )

    breakpoints: Dict[str, int] = field(
        default_factory=lambda: {"sm": 40, "md": 80, "lg": 120}
    )


@dataclass
class Theme:
    """Theme configuration.

    Attributes:
        name (str): Theme name
        colors (ThemeColors): Color configuration
        metrics (ThemeMetrics): Sizing and spacing configuration
    """

    name: str
    colors: ThemeColors = field(default_factory=ThemeColors)
    metrics: ThemeMetrics = field(default_factory=ThemeMetrics)

    @classmethod
    async def load(cls, path: Path) -> "Theme":
        """Load theme from file.

        Args:
            path: Theme file path

        Returns:
            Theme: Loaded theme
        """
        try:
            with open(path) as f:
                data = yaml.safe_load(f)

            return cls(
                name=data["name"],
                colors=ThemeColors(**data.get("colors", {})),
                metrics=ThemeMetrics(**data.get("metrics", {})),
            )
        except Exception as e:
            logger.error(f"Error loading theme from {path}: {e}")
            raise ValueError(f"Invalid theme file: {e}")

    def generate_css(self) -> str:
        """Generate CSS from theme.

        Returns:
            str: Generated CSS
        """
        return f"""
        /* Theme: {self.name} */
        $primary: {self.colors.primary};
        $secondary: {self.colors.secondary};
        $accent: {self.colors.accent};
        $background: {self.colors.background};
        $text: {self.colors.text};
        $error: {self.colors.error};
        $warning: {self.colors.warning};
        $success: {self.colors.success};
        $info: {self.colors.info};
        $selection: {self.colors.selection};

        * {{
            transition: background 0.3s ease, color 0.3s ease, border-color 0.3s ease;
        }}
        """


class ThemeManager:
    """Theme manager for handling multiple themes.

    Attributes:
        themes (Dict[str, Theme]): Available themes
        current_theme (Optional[Theme]): Currently active theme
    """

    def __init__(self) -> None:
        """Initialize the theme manager."""
        self.themes: Dict[str, Theme] = {}
        self.current_theme: Optional[Theme] = None

    async def load_theme(self, path: Path) -> Theme:
        """Load a theme from file.

        Args:
            path: Theme file path

        Returns:
            Theme: Loaded theme
        """
        theme = await Theme.load(path)
        self.themes[theme.name] = theme
        return theme

    async def load_themes(self, directory: Path) -> None:
        """Load all themes from directory.

        Args:
            directory: Theme directory path
        """
        for path in directory.glob("*.yaml"):
            await self.load_theme(path)

    def set_theme(self, name: str) -> None:
        """Set the active theme.

        Args:
            name: Theme name
        """
        if name in self.themes:
            self.current_theme = self.themes[name]
            logger.info(f"Set theme to {name}")
        else:
            logger.error(f"Theme not found: {name}")

    def get_theme(self, name: str) -> Optional[Theme]:
        """Get a theme by name.

        Args:
            name: Theme name

        Returns:
            Optional[Theme]: Theme if found
        """
        return self.themes.get(name)
