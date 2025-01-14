"""Example demonstrating plugin system usage."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol

from textual.containers import Container, Vertical
from textual.widgets import Static

from pepperpy.tui.app import PepperApp
from pepperpy.tui.screens import PepperScreen
from pepperpy.tui.widgets.base import PepperWidget

if TYPE_CHECKING:
    from collections.abc import Iterator


class PluginProtocol(Protocol):
    """Protocol for plugin interface."""

    name: str
    version: str
    description: str

    async def initialize(self, app: PepperApp) -> None:
        """Initialize the plugin.

        Args:
            app: The application instance.

        """

    async def cleanup(self) -> None:
        """Clean up plugin resources."""


class CustomWidget(PepperWidget, Static):
    """Custom widget for the example plugin."""

    DEFAULT_CSS = """
    CustomWidget {
        width: 100%;
        height: auto;
        padding: 1;
        border: solid $accent;
    }
    """

    def __init__(self, **kwargs: str | float | bool | None) -> None:
        """Initialize the widget."""
        super().__init__(**kwargs)
        self.text = "Hello from custom widget!"

    def render(self) -> str:
        """Render the widget content."""
        return self.text

    async def update_text(self, text: str) -> None:
        """Update widget text.

        Args:
            text: New text to display.

        """
        self.text = text
        self.refresh()


class CustomPlugin:
    """Example plugin implementation."""

    name = "custom"
    version = "1.0.0"
    description = "Example plugin with custom widget"

    def __init__(self) -> None:
        """Initialize the plugin."""
        self.widget: CustomWidget | None = None
        self._app: PepperApp | None = None

    async def initialize(self, app: PepperApp) -> None:
        """Initialize the plugin.

        Args:
            app: The application instance.

        """
        self._app = app
        self.widget = CustomWidget()
        if app.notification_center:
            await app.notification_center.emit_event(
                "notification",
                {
                    "message": "Custom plugin initialized!",
                    "severity": "information",
                },
            )

    async def cleanup(self) -> None:
        """Clean up plugin resources."""
        if self.widget:
            self.widget.remove()

    async def update_widget(self) -> None:
        """Update widget text."""
        if self.widget and self._app and self._app.notification_center:
            await self.widget.update_text("Updated from plugin!")
            await self._app.notification_center.emit_event(
                "notification",
                {
                    "message": "Widget updated successfully!",
                    "severity": "information",
                },
            )


class MainScreen(PepperScreen):
    """Main application screen."""

    DEFAULT_CSS = """
    MainScreen {
        align: center middle;
    }
    """

    def compose(self) -> Iterator[Container]:
        """Compose the screen layout."""
        with Container(), Vertical():
            yield Container()


class PluginApp(PepperApp):
    """Example application demonstrating plugin system."""

    TITLE = "PepperPy Plugin Example"

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__()
        self.plugin = CustomPlugin()

    async def on_mount(self) -> None:
        """Handle application mount event."""
        await super().on_mount()
        await self.plugin_manager.initialize()
        await self.plugin_manager.register_plugin(self.plugin)
        await self.switch_screen(MainScreen())


def main() -> None:
    """Run the plugin example."""
    app = PluginApp()
    app.run()


if __name__ == "__main__":
    main()
