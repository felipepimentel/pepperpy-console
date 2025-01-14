"""Example application demonstrating table functionality."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, cast

from pepperpy_console.tui.app import PepperApp
from pepperpy_console.tui.commands import Command
from pepperpy_console.tui.screens import PepperScreen
from pepperpy_console.tui.widgets.containers import PepperVertical
from pepperpy_console.tui.widgets.notification import NotificationCenter
from pepperpy_console.tui.widgets.table import Column, PepperTable

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator

    from textual.widgets import Static


class BaseCommand:
    """Base class for commands."""

    def __init__(self, app: PepperApp) -> None:
        """Initialize the command.

        Args:
            app: The application instance.

        """
        self.app = app


class LoadDataCommand(BaseCommand, Command):
    """Command to load example data."""

    name = "load_data"
    description = "Load example data"
    category = "Data"
    shortcut = None

    async def execute(self, *args: object, **kwargs: object) -> None:
        """Execute the command."""
        app = cast("ExampleApp", self.app)
        await app.load_example_data()


class SortByNameCommand(BaseCommand, Command):
    """Command to sort by name."""

    name = "sort_by_name"
    description = "Sort table by name"
    category = "Data"
    shortcut = None

    async def execute(self, *args: object, **kwargs: object) -> None:
        """Execute the command."""
        app = cast("ExampleApp", self.app)
        await app.sort_by_name()


class MainScreen(PepperScreen):
    """Main application screen."""

    async def compose(
        self,
    ) -> AsyncGenerator[
        Static | PepperVertical | PepperTable | NotificationCenter, None
    ]:
        """Compose the screen layout."""
        # Create container
        container = PepperVertical(
            widget_id="main-container",
            classes="pepper-vertical",
        )
        yield container

        # Add a simple table
        table = PepperTable(
            columns=[
                Column("name", "Name", width=20),
                Column("age", "Age", width=10),
                Column("city", "City", width=20),
            ],
            widget_id="data-table",
            classes="pepper-table",
        )
        yield table

        # Add notifications
        notifications = NotificationCenter(
            widget_id="notifications",
            classes="notification-center",
        )
        yield notifications


class ExampleApp(PepperApp):
    """Example application demonstrating table functionality."""

    TITLE = "PepperPy Table Example"

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(screen_map={"main": MainScreen})
        self.table: PepperTable | None = None
        self.notifications: NotificationCenter | None = None

    async def on_mount(self) -> None:
        """Handle application mount."""
        # Install main screen
        await self.push_screen(MainScreen())

        # Get references to widgets
        if self.screen:
            self.table = self.screen.query_one("#data-table", PepperTable)
            self.notifications = self.screen.query_one(
                "#notifications", NotificationCenter
            )

        # Register custom commands
        self.command_manager.register_command(LoadDataCommand(self))
        self.command_manager.register_command(SortByNameCommand(self))

        # Load themes
        themes_dir = Path(__file__).parent.parent / "pepperpy_console" / "themes"
        await self.load_themes(themes_dir)

    async def load_example_data(self) -> None:
        """Load example data into the table."""
        if self.table is None or self.notifications is None:
            return

        data = [
            {"name": "John", "age": 30, "city": "New York"},
            {"name": "Alice", "age": 25, "city": "London"},
            {"name": "Bob", "age": 35, "city": "Paris"},
        ]
        await self.table.load_data(data)
        await self.notifications.notify(
            "Data loaded successfully", severity="information"
        )

    async def sort_by_name(self) -> None:
        """Sort table by name column."""
        if self.table is None or self.notifications is None:
            return

        await self.table.sort_by("name")
        await self.notifications.notify("Table sorted by name", severity="information")


def main() -> None:
    """Run the example application."""
    app = ExampleApp()
    app.run()


if __name__ == "__main__":
    main()
