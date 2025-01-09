"""Simple PepperPy Console application example."""

from pathlib import Path

from textual.containers import Container, Vertical
from textual.widgets import Footer, Header

from pepperpy_console import (
    Command,
    FormField,
    NotificationCenter,
    PepperApp,
    PepperForm,
    PepperScreen,
)


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

    def compose(self):
        """Compose the screen layout."""
        yield Header()
        with Container(id="content"):
            with Vertical(id="form-container"):
                yield PepperForm(
                    fields=[
                        FormField("name", "Name", str),
                        FormField("email", "Email", str),
                        FormField("age", "Age", int, required=False),
                    ]
                )
            with Vertical(id="notification-container"):
                yield NotificationCenter()
        yield Footer()


class ExampleApp(PepperApp):
    """Example application demonstrating basic features."""

    TITLE = "PepperPy Example"

    def __init__(self):
        """Initialize the application."""
        super().__init__(screen_map={"main": MainScreen})
        self.install_screen(MainScreen(), name="main")

    async def on_mount(self):
        """Handle application mount."""
        await super().on_mount()

        # Register custom commands
        self.commands.register_many([
            Command(
                "Show Notification",
                "Display a test notification",
                self.show_test_notification,
            ),
            Command("Clear Form", "Clear the form fields", self.clear_form),
        ])

        # Load themes
        themes_dir = Path(__file__).parent.parent / "pepperpy_console" / "themes"
        await self.load_themes(themes_dir)

        # Load plugins
        plugins_dir = Path(__file__).parent.parent / "pepperpy_console" / "plugins"
        await self.load_plugins(plugins_dir)

    async def show_test_notification(self):
        """Show a test notification."""
        notifications = self.query_one(NotificationCenter)
        await notifications.notify(
            "This is a test notification!", type="info", duration=3.0
        )

    async def clear_form(self):
        """Clear the form fields."""
        form = self.query_one(PepperForm)
        form.clear()


def main():
    """Run the example application."""
    app = ExampleApp()
    app.run()


if __name__ == "__main__":
    main()
