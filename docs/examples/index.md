# Examples

This section provides practical examples of using PepperPy Console in various scenarios.

## Basic Application

A simple application with a welcome screen:

```python
from pepperpy import PepperApp, PepperScreen, Static

class WelcomeScreen(PepperScreen):
    async def compose(self):
        yield Static("Welcome to PepperPy Console!")

class MyApp(PepperApp):
    async def on_mount(self):
        await self.push_screen(WelcomeScreen())

if __name__ == "__main__":
    app = MyApp()
    app.run()
```

## Command-Line Interface

Example of building a CLI application with commands:

```python
from pepperpy import PepperApp, Command, CommandGroup

class CLIApp(PepperApp):
    def __init__(self):
        super().__init__()
        self.setup_commands()

    def setup_commands(self):
        async def greet(name: str):
            return f"Hello, {name}!"

        async def add(a: str, b: str):
            try:
                result = float(a) + float(b)
                return f"Sum: {result}"
            except ValueError:
                return "Error: Please provide valid numbers"

        self.commands.add_command(Command(
            name="greet",
            callback=greet,
            description="Greet someone"
        ))

        self.commands.add_command(Command(
            name="add",
            callback=add,
            description="Add two numbers"
        ))

if __name__ == "__main__":
    app = CLIApp()
    app.run()
```

## Data Table Application

Example of creating a data table interface:

```python
from pepperpy import (
    PepperApp,
    PepperScreen,
    PepperTable,
    Column,
    NotificationCenter
)

class DataTableScreen(PepperScreen):
    def __init__(self):
        super().__init__()
        self.table = PepperTable()
        self.notifications = NotificationCenter()

    def setup_table(self):
        self.table.add_column(Column("ID", justify="center"))
        self.table.add_column(Column("Name"))
        self.table.add_column(Column("Value"))

        # Add some data
        self.table.add_row("1", "Item 1", "100")
        self.table.add_row("2", "Item 2", "200")
        self.table.add_row("3", "Item 3", "300")

    async def compose(self):
        self.setup_table()
        yield self.notifications
        yield self.table

class DataApp(PepperApp):
    async def on_mount(self):
        await self.push_screen(DataTableScreen())

if __name__ == "__main__":
    app = DataApp()
    app.run()
```

## Plugin Example

Creating and using a custom plugin:

```python
from pathlib import Path
from pepperpy import (
    PepperApp,
    Plugin,
    Command,
    PepperScreen,
    PepperWidget,
    Static
)

class CustomWidget(PepperWidget):
    def compose(self):
        yield Static("Custom Plugin Widget")

class CustomPlugin(Plugin):
    def __init__(self, name: str):
        super().__init__(name)
        self.setup_commands()

    def setup_commands(self):
        async def custom_command():
            return "Custom command executed!"

        self.commands["custom"] = Command(
            name="custom",
            callback=custom_command,
            description="Execute custom command"
        )

class PluginApp(PepperApp):
    async def on_mount(self):
        # Load plugins
        plugin_dir = Path("plugins")
        await self.load_plugins(plugin_dir)

if __name__ == "__main__":
    app = PluginApp()
    app.run()
```

## Form Application

Example of creating a form interface:

```python
from pepperpy import (
    PepperApp,
    PepperScreen,
    PepperForm,
    FormField,
    NotificationCenter
)

class LoginScreen(PepperScreen):
    def __init__(self):
        super().__init__()
        self.form = PepperForm()
        self.notifications = NotificationCenter()

    def setup_form(self):
        self.form.add_field(
            FormField("username", "Username", field_type="text")
        )
        self.form.add_field(
            FormField("password", "Password", field_type="password")
        )

    async def on_form_submit(self, data):
        # Handle form submission
        username = data.get("username")
        password = data.get("password")
        await self.notifications.notify(
            f"Login attempt: {username}",
            type="info"
        )

    async def compose(self):
        self.setup_form()
        yield self.notifications
        yield self.form

class FormApp(PepperApp):
    async def on_mount(self):
        await self.push_screen(LoginScreen())

if __name__ == "__main__":
    app = FormApp()
    app.run()
```

## Theme Switching Example

Example of an application with theme switching:

```python
from pathlib import Path
from pepperpy import (
    PepperApp,
    PepperScreen,
    Static,
    Command
)

class ThemeScreen(PepperScreen):
    async def compose(self):
        yield Static("Press 't' to switch theme")

class ThemeApp(PepperApp):
    def __init__(self):
        super().__init__()
        self.setup_commands()

    def setup_commands(self):
        async def switch_theme():
            themes = list(self.themes.themes.keys())
            current = themes.index(self.themes.current_theme.name)
            next_theme = themes[(current + 1) % len(themes)]
            self.themes.set_theme(next_theme)
            return f"Switched to theme: {next_theme}"

        self.commands.add_command(Command(
            name="theme",
            callback=switch_theme,
            description="Switch theme"
        ))

    async def on_mount(self):
        # Load themes
        themes_dir = Path("themes")
        await self.load_themes(themes_dir)
        self.themes.set_theme("light")
        
        # Show main screen
        await self.push_screen(ThemeScreen())

if __name__ == "__main__":
    app = ThemeApp()
    app.run()
```

## Loading Screen Example

Example of using loading screens:

```python
from pepperpy import (
    PepperApp,
    PepperScreen,
    LoadingScreen,
    Static
)
import asyncio

class DataScreen(PepperScreen):
    async def on_mount(self):
        # Show loading screen
        await self.app.push_screen(
            LoadingScreen("Loading data...")
        )
        
        try:
            # Simulate data loading
            await asyncio.sleep(2)
            
            # Process complete
            await self.app.pop_screen()
            await self.app.push_screen(
                Static("Data loaded successfully!")
            )
        except Exception as e:
            # Handle error
            await self.app.pop_screen()
            await self.app.push_screen(
                ErrorScreen(str(e))
            )

class LoadingApp(PepperApp):
    async def on_mount(self):
        await self.push_screen(DataScreen())

if __name__ == "__main__":
    app = LoadingApp()
    app.run()
``` 