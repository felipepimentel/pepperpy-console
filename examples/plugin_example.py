"""Example demonstrating plugin system usage."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Protocol

from pepperpy import NotificationCenter, PepperApp, PepperScreen, PepperWidget
from textual.containers import Container, Vertical
from textual.widgets import Static

if TYPE_CHECKING:
    from collections.abc import Iterator


class PluginProtocol(Protocol):
    """Protocol for plugin interface."""

    name: str
    version: str
    description: str

    async def initialize(self, app: PepperApp) -> None:
        """Initialize the plugin."""
        ...

    async def cleanup(self) -> None:
        """Clean up plugin resources."""
        ...


class CustomWidget(PepperWidget, Static):
    """Custom widget for the example plugin."""

    DEFAULT_CSS = """
    $primary: #bd93f9;
    $secondary: #6272a4;
    $accent: #ff79c6;
    $background: #282a36;
    $text: #f8f8f2;
    $error: #ff5555;
    $warning: #ffb86c;
    $success: #50fa7b;
    $info: #8be9fd;
    $selection: #44475a;

    CustomWidget {
        background: $selection;
        color: $text;
        border: solid $primary;
        padding: 1;
        margin: 1;
        width: 100%;
        height: auto;
        text-align: center;
    }
    """

    def __init__(self, **kwargs: str | float | bool | None) -> None:
        """Initialize the widget."""
        super().__init__(**kwargs)
        self.text = "Custom Plugin Widget"

    def render(self) -> str:
        """Render the widget."""
        return self.text

    async def update_text(self, text: str) -> None:
        """Update widget text.

        Args:
            text: New text to display

        """
        self.text = text
        self.refresh()


class CustomPlugin(PluginProtocol):
    """Example plugin implementation."""

    name = "custom"
    version = "1.0.0"
    description = "Example plugin with custom widget"

    def __init__(self) -> None:
        """Initialize the plugin."""
        self.widget: CustomWidget | None = None

    async def initialize(self, app: PepperApp) -> None:
        """Initialize the plugin.

        Args:
            app: Application instance

        """
        # Create widget
        self.widget = CustomWidget()

        # Add to main screen
        screen = app.query_one(MainScreen)
        content = screen.query_one("#content")
        content.mount(self.widget)

        # Update text periodically
        app.set_interval(2.0, self.update_widget)

    async def cleanup(self) -> None:
        """Clean up plugin resources."""
        if self.widget:
            self.widget.remove()

    async def update_widget(self) -> None:
        """Update widget text."""
        if self.widget:
            await self.widget.update_text("Updated: " + self.widget.text)


class MainScreen(PepperScreen):
    """Main application screen."""

    DEFAULT_CSS = """
    #content {
        width: 100%;
        height: 100%;
        padding: 1;
    }
    """

    def compose(self) -> Iterator[Container]:
        """Compose the screen layout."""
        with Container():
            with Vertical(id="content"):
                pass
            yield NotificationCenter()


class PluginApp(PepperApp):
    """Example application demonstrating plugin system."""

    TITLE = "PepperPy Plugin Example"

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(screen_map={"main": MainScreen})
        self.install_screen(MainScreen(), name="main")

    async def on_mount(self) -> None:
        """Handle application mount."""
        await super().on_mount()

        # Load built-in plugins
        plugins_dir = Path(__file__).parent.parent / "pepperpy" / "plugins"
        await self.load_plugins(plugins_dir)

        # Register custom plugin
        custom_plugin = CustomPlugin()
        await self.plugin_manager.register_plugin("custom", custom_plugin)
        await custom_plugin.initialize(self)

        # Show notification
        notifications = self.query_one(NotificationCenter)
        await notifications.notify("Loaded plugin successfully", severity="success")


def main() -> None:
    """Run the plugin example."""
    app = PluginApp()
    app.run()


if __name__ == "__main__":
    main()
