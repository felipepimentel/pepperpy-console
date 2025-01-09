"""Main application class for PepperPy Console."""

from pathlib import Path
from typing import Any, Dict, Optional, Type

import structlog
from pepperpy_core.plugin import PluginManager
from textual.app import App, ComposeResult
from textual.widgets import Footer, Header

from .commands import Command, CommandPalette
from .help import HelpViewer, KeyboardHelpSection
from .keyboard import KeyBinding, KeyboardManager
from .screens import ErrorScreen, LoadingScreen, PepperScreen
from .theme import ThemeManager

logger = structlog.get_logger(__name__)


class PepperApp(App):
    """Base application class for PepperPy TUI applications.

    This class provides common functionality and styling for PepperPy TUI apps.
    It includes built-in header and footer, theme support, and logging integration.

    Attributes:
        CSS_PATH (Optional[str]): Path to the CSS file for styling
        TITLE (str): Application title displayed in the header
    """

    CSS_PATH = str(Path(__file__).parent / "styles.css")
    TITLE = "PepperPy Application"

    def __init__(
        self,
        screen_map: Optional[Dict[str, Type[PepperScreen]]] = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the PepperApp.

        Args:
            screen_map: Optional mapping of screen names to screen classes
            **kwargs: Additional keyword arguments passed to the parent App class
        """
        super().__init__(**kwargs)

        # Core systems
        self.screen_map = screen_map or {}

        # Feature systems
        self.keyboard = KeyboardManager()
        self.themes = ThemeManager()
        self.commands = CommandPalette()
        self.help = HelpViewer()
        self.plugins = PluginManager()

        logger.info(f"Initializing {self.TITLE}")

    def compose(self) -> ComposeResult:
        """Compose the app layout.

        Returns:
            ComposeResult: The composed widgets
        """
        yield Header()
        yield self.commands
        yield self.help
        yield Footer()

    async def on_mount(self) -> None:
        """Handle the app mount event.

        This method is called when the app is mounted. It sets up the basic layout
        and initializes all systems.
        """
        # Setup keyboard shortcuts
        self.keyboard.register_many([
            KeyBinding("ctrl+p", "show_palette", "Show Command Palette"),
            KeyBinding("?", "toggle_help", "Toggle Help"),
            KeyBinding("ctrl+q", "quit", "Quit Application"),
        ])

        # Register base commands
        self.commands.register_many([
            Command("Toggle Help", "Show/hide help", self.action_toggle_help),
            Command(
                "Switch Theme", "Change application theme", self.action_switch_theme
            ),
            Command("Quit", "Exit application", self.action_quit),
        ])

        # Add keyboard help section
        self.help.add_section(
            KeyboardHelpSection.generate(self.keyboard.get_textual_bindings())
        )

        await self.push_screen("main")

    async def load_plugins(self, directory: Path) -> None:
        """Load plugins from directory.

        Args:
            directory: Plugin directory path
        """
        await self.plugins.load_plugins(directory)
        for plugin in self.plugins.plugins.values():
            await plugin.initialize(self)

    async def load_themes(self, directory: Path) -> None:
        """Load themes from directory.

        Args:
            directory: Theme directory path
        """
        await self.themes.load_themes(directory)
        if self.themes.themes:
            # Set first theme as default
            first_theme = next(iter(self.themes.themes))
            self.themes.set_theme(first_theme)
            await self.update_theme()

    async def update_theme(self) -> None:
        """Update application theme."""
        if self.themes.current_theme:
            # Update CSS variables
            css = self.themes.current_theme.generate_css()
            self.screen.styles.background = self.themes.current_theme.colors.background
            self.screen.styles.color = self.themes.current_theme.colors.text

    async def show_loading(self, message: str = "Loading...") -> None:
        """Show the loading screen.

        Args:
            message: Loading message to display
        """
        screen = LoadingScreen(message=message)
        await self.push_screen(screen)

    async def show_error(self, message: str) -> None:
        """Show the error screen.

        Args:
            message: Error message to display
        """
        screen = ErrorScreen(error_message=message)
        await self.push_screen(screen)

    async def switch_screen(self, name: str) -> None:
        """Switch to a different screen.

        Args:
            name: Name of the screen to switch to
        """
        if name in self.screen_map:
            screen = self.screen_map[name]()
            await self.push_screen(screen)
        else:
            logger.error(f"Screen not found: {name}")

    def action_toggle_help(self) -> None:
        """Toggle help visibility."""
        if self.help.current_section:
            self.help.current_section = None
        else:
            self.help.show_section("Keyboard Shortcuts")

    def action_switch_theme(self) -> None:
        """Show theme selection dialog."""
        # TODO: Implement theme selection
        pass

    def action_show_palette(self) -> None:
        """Show command palette."""
        self.commands.show()
