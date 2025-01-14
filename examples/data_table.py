"""Example application demonstrating table functionality."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, cast

from textual.containers import Container

from pepperpy_console.tui.app import PepperApp
from pepperpy_console.tui.commands import Command
from pepperpy_console.tui.screens.base import PepperScreen
from pepperpy_console.tui.widgets.notification import NotificationCenter
from pepperpy_console.tui.widgets.table import Column, PepperTable

if TYPE_CHECKING:
    from textual.app import ComposeResult


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

    def compose(self) -> ComposeResult:
        """Compose the screen layout."""
        with Container():
            # Add a simple table
            yield PepperTable(
                columns=[
                    Column("name", "Name", width=20),
                    Column("age", "Age", width=10),
                    Column("city", "City", width=20),
                ],
            )

            # Add notifications
            yield NotificationCenter()


class ExampleApp(PepperApp):
    """Example application demonstrating table functionality."""

    TITLE = "PepperPy Table Example"

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__(screen_map={"main": MainScreen})
        self.table: PepperTable | None = None
        self.notifications: NotificationCenter | None = None
        self.install_screen(MainScreen(), name="main")

    async def on_mount(self) -> None:
        """Handle application mount."""
        # Get references to widgets
        screen = self.query_one(MainScreen)
        self.table = screen.query_one(PepperTable)
        self.notifications = screen.query_one(NotificationCenter)

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
        self.notifications.notify("Data loaded successfully", severity="information")

    async def sort_by_name(self) -> None:
        """Sort table by name column."""
        if self.table is None or self.notifications is None:
            return

        await self.table.sort_by("name")
        self.notifications.notify("Table sorted by name", severity="information")


def main() -> None:
    """Run the example application."""
    app = ExampleApp()
    app.run()


if __name__ == "__main__":
    main()
