"""Mock TUI app module."""

from pathlib import Path
from typing import Any, Dict, Optional, Type

from textual.app import App

from ..plugins.example import ExamplePlugin
from .commands import CommandPalette
from .help import HelpViewer
from .keyboard import KeyboardManager
from .screens import LoadingScreen, PepperScreen
from .theme import ThemeManager


class PepperApp(App):
    """Mock base application class for PepperPy TUI applications."""

    def __init__(
        self,
        screen_map: Optional[Dict[str, Type[PepperScreen]]] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the app."""
        super().__init__(**kwargs)
        self.screen_map = screen_map or {}
        self.keyboard = KeyboardManager()
        self.themes = ThemeManager()
        self.commands = CommandPalette()
        self.help = HelpViewer()
        self.plugins = ExamplePlugin()

    async def load_plugins(self, directory: Path) -> None:
        """Load plugins from directory."""
        await self.plugins.load_plugins(directory)

    async def load_themes(self, directory: Path) -> None:
        """Load themes from directory."""
        await self.themes.load_themes(directory)

    async def show_loading(self, message: str = "Loading...") -> None:
        """Show the loading screen."""
        screen = LoadingScreen(message=message)
        await self.push_screen(screen)
