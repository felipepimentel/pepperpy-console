"""Simple PepperPy Console application example."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING

from pepperpy import (
    Command,
    FormField,
    NotificationCenter,
    PepperApp,
    PepperForm,
    PepperScreen,
)
from textual.containers import Container, Vertical
from textual.widgets import Footer, Header

if TYPE_CHECKING:
    from collections.abc import Iterator


class MainScreen(PepperScreen):
    """Main application screen."""

    DEFAULT_CSS = """
    Screen {
        background: $surface;
        color: $text;
        align: center middle;
    }

    #content {
        width: 80%;
        height: auto;
        background: $boost;
        border: solid $primary;
        padding: 1;
    }

    #form-container {
        width: 100%;
        height: auto;
        margin: 1;
    }

    #notification-container {
        width: 100%;
        height: auto;
        margin: 1;
    }
    """

    def compose(self) -> Iterator[Container | Header | Footer]:
        """Compose the screen layout."""
        yield Header()
        with Container(id="content"):
            with Vertical(id="form-container"):
                yield PepperForm(
                    fields=[
                        FormField("name", "Name", str),
                        FormField("email", "Email", str),
                        FormField("age", "Age", int, required=False),
                    ],
                )
            with Vertical(id="notification-container"):
                yield NotificationCenter()
        yield Footer()


class ExampleApp(PepperApp):
    """Example application demonstrating basic features."""

    TITLE = "PepperPy Example"

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(screen_map={"main": MainScreen})
        self.install_screen(MainScreen(), name="main")

    async def on_mount(self) -> None:
        """Handle application mount."""
        await super().on_mount()

        # Register custom commands
        await self.command_manager.register_many(
            [
                Command(
                    name="Show Notification",
                    description="Display a test notification",
                    callback=self.show_test_notification,
                ),
                Command(
                    name="Clear Form",
                    description="Clear the form fields",
                    callback=self.clear_form,
                ),
            ],
        )

        # Load themes
        themes_dir = Path(__file__).parent.parent / "pepperpy" / "themes"
        await self.load_themes(themes_dir)

        # Load plugins
        plugins_dir = Path(__file__).parent.parent / "pepperpy" / "plugins"
        await self.load_plugins(plugins_dir)

    async def show_test_notification(self) -> None:
        """Show a test notification."""
        notifications = self.query_one(NotificationCenter)
        await notifications.notify(
            "This is a test notification!",
            severity="info",
            timeout=3.0,
        )

    async def clear_form(self) -> None:
        """Clear the form fields."""
        form = self.query_one(PepperForm)
        await form.clear()


def main() -> None:
    """Run the example application."""
    app = ExampleApp()
    app.run()


if __name__ == "__main__":
    main()
