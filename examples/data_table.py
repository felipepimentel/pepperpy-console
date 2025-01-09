"""Example of using PepperTable widget."""

from pathlib import Path

from textual.containers import Container

from pepperpy_console import (
    Column,
    Command,
    NotificationCenter,
    PepperApp,
    PepperScreen,
    PepperTable,
)


class MainScreen(PepperScreen):
    """Main application screen."""

    def compose(self):
        """Compose the screen layout."""
        with Container():
            # Add a simple table
            yield PepperTable(
                columns=[
                    Column("id", "ID", width=5),
                    Column("name", "Name", width=20),
                    Column("email", "Email", width=30),
                    Column("role", "Role", width=15),
                ]
            )

            # Add notifications
            yield NotificationCenter()


class ExampleApp(PepperApp):
    """Example application demonstrating table features."""

    TITLE = "PepperPy Table Example"

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
                "Load Data",
                "Load example data into table",
                self.load_example_data,
            ),
            Command(
                "Sort by Name",
                "Sort table by name",
                self.sort_by_name,
            ),
        ])

        # Load themes
        themes_dir = Path(__file__).parent.parent / "pepperpy_console" / "themes"
        await self.load_themes(themes_dir)

        # Load example data
        await self.load_example_data()

    async def load_example_data(self):
        """Load example data into table."""
        data = [
            {
                "id": "1",
                "name": "John Doe",
                "email": "john@example.com",
                "role": "Admin",
            },
            {
                "id": "2",
                "name": "Jane Smith",
                "email": "jane@example.com",
                "role": "User",
            },
            {
                "id": "3",
                "name": "Bob Johnson",
                "email": "bob@example.com",
                "role": "User",
            },
        ]

        table = self.query_one(PepperTable)
        await table.load_data(data)

        notifications = self.query_one(NotificationCenter)
        await notifications.notify(
            f"Loaded {len(data)} rows", type="info", duration=3.0
        )

    async def sort_by_name(self):
        """Sort table by name column."""
        table = self.query_one(PepperTable)
        await table.sort_by("name")

        notifications = self.query_one(NotificationCenter)
        await notifications.notify("Sorted by name", type="info", duration=3.0)


def main():
    """Run the example application."""
    app = ExampleApp()
    app.run()


if __name__ == "__main__":
    main()
