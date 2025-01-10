# Quick Start Guide

This guide will help you get started with PepperPy Console quickly.

## Basic Application

Create your first PepperPy Console application:

```python
from pepperpy_console import PepperApp, PepperScreen, Static

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

Save this as `app.py` and run:
```bash
python app.py
```

## Adding Commands

Create a CLI application with commands:

```python
from pepperpy_console import PepperApp, Command

class CLIApp(PepperApp):
    def __init__(self):
        super().__init__()
        self.setup_commands()

    def setup_commands(self):
        async def greet(name: str):
            return f"Hello, {name}!"

        self.commands.add_command(Command(
            name="greet",
            callback=greet,
            description="Greet someone"
        ))

app = CLIApp()
app.run()
```

## Creating Forms

Build an interactive form:

```python
from pepperpy_console import (
    PepperApp,
    PepperScreen,
    PepperForm,
    FormField
)

class LoginScreen(PepperScreen):
    def __init__(self):
        super().__init__()
        self.form = PepperForm()

    def setup_form(self):
        self.form.add_field(
            FormField("username", "Username", field_type="text")
        )
        self.form.add_field(
            FormField("password", "Password", field_type="password")
        )

    async def compose(self):
        self.setup_form()
        yield self.form

app = PepperApp()
app.push_screen(LoginScreen())
app.run()
```

## Using Themes

Apply and switch themes:

```python
from pathlib import Path
from pepperpy_console import PepperApp, PepperScreen, Static

class ThemedApp(PepperApp):
    async def on_mount(self):
        # Load themes
        await self.themes.load_themes(Path("themes"))
        self.themes.set_theme("dark")
        
        # Show screen
        await self.push_screen(WelcomeScreen())

app = ThemedApp()
app.run()
```

## Creating Tables

Display data in tables:

```python
from pepperpy_console import (
    PepperApp,
    PepperScreen,
    PepperTable,
    Column
)

class DataScreen(PepperScreen):
    def __init__(self):
        super().__init__()
        self.table = PepperTable()

    def setup_table(self):
        self.table.add_column(Column("ID"))
        self.table.add_column(Column("Name"))
        self.table.add_column(Column("Value"))

        self.table.add_row("1", "Item 1", "100")
        self.table.add_row("2", "Item 2", "200")

    async def compose(self):
        self.setup_table()
        yield self.table

app = PepperApp()
app.push_screen(DataScreen())
app.run()
```

## Handling Events

Respond to user interactions:

```python
from pepperpy_console import (
    PepperApp,
    PepperScreen,
    PepperWidget,
    Event
)

class ClickableWidget(PepperWidget):
    def on_click(self, event: Event):
        print(f"Clicked at: {event.x}, {event.y}")

class InteractiveScreen(PepperScreen):
    async def compose(self):
        yield ClickableWidget()

app = PepperApp()
app.push_screen(InteractiveScreen())
app.run()
```

## Using Plugins

Create and use plugins:

```python
from pepperpy_console import Plugin, Command

class MyPlugin(Plugin):
    def __init__(self, name: str):
        super().__init__(name)
        self.setup_commands()

    def setup_commands(self):
        async def plugin_command():
            return "Plugin command executed!"

        self.commands["plugin_cmd"] = Command(
            name="plugin_cmd",
            callback=plugin_command,
            description="Execute plugin command"
        )

# In your app
app = PepperApp()
plugin = MyPlugin("my_plugin")
app.register_plugin(plugin)
app.run()
```

## Next Steps

- Explore the [CLI System Guide](cli/index.md)
- Learn about the [TUI Framework](tui/index.md)
- Customize with [Themes](themes/index.md)
- Check out more [Examples](examples/index.md)
- Read the [API Reference](api/index.md)

## Getting Help

- Join our [Discord community](https://discord.gg/pepperpy)
- Check the [FAQ](https://pepperpy-console.readthedocs.io/en/latest/faq/)
- Open an [Issue](https://github.com/yourusername/pepperpy-console/issues) 