# TUI Framework

The Text User Interface (TUI) framework in PepperPy Console provides a rich set of components for building terminal-based user interfaces. Built on top of Textual, it offers screens, widgets, and event handling capabilities.

## Core Components

### PepperApp

The main application class that serves as the entry point for your TUI application:

```python
from pepperpy import PepperApp, Static

class MyApp(PepperApp):
    def compose(self) -> ComposeResult:
        yield Static("Welcome to my app!")

app = MyApp()
app.run()
```

### Screens

The framework provides several screen types for different purposes:

#### PepperScreen

Base screen class that all custom screens should inherit from:

```python
from pepperpy import PepperScreen, Static

class MyScreen(PepperScreen):
    async def compose(self):
        yield Static("My Custom Screen")
```

#### LoadingScreen

A built-in screen for displaying loading states:

```python
from pepperpy import LoadingScreen

# In your app
await app.push_screen(LoadingScreen("Loading data..."))
```

#### ErrorScreen

A screen for displaying error messages:

```python
from pepperpy import ErrorScreen

# In your app
await app.push_screen(ErrorScreen("An error occurred"))
```

### Widgets

The framework includes a variety of widgets for building user interfaces:

#### PepperWidget

Base widget class with event handling capabilities:

```python
from pepperpy import PepperWidget

class MyWidget(PepperWidget):
    def __init__(self):
        super().__init__()
        self.events = []  # Track widget events

    def emit_event(self, event_type: str, data: dict):
        self.events.append({"type": event_type, "data": data})
```

## Event System

The TUI framework includes a robust event system for handling user interactions:

```python
from pepperpy import EventManager

# Create an event manager
event_manager = EventManager()

# Register an event handler
async def handle_click(data):
    print(f"Click event: {data}")

event_manager.on("click", handle_click)

# Emit an event
await event_manager.emit("click", {"x": 10, "y": 20})

# Remove a handler
event_manager.off("click", handle_click)
```

## Theme System

The framework supports customizable themes:

```python
from pepperpy import ThemeManager
from pathlib import Path

# Initialize theme manager
theme_manager = ThemeManager()

# Load themes from directory
await theme_manager.load_themes(Path("themes"))

# Set active theme
theme_manager.set_theme("dark")
```

### Theme File Example (YAML)

```yaml
name: dark
colors:
  primary: "#bd93f9"
  secondary: "#44475a"
  accent: "#ff79c6"
  background: "#282a36"
  text: "#f8f8f2"
styles:
  button:
    color: text
    background: secondary
    hover:
      background: accent
  text:
    color: text
```

## Best Practices

1. **Screen Management**
   - Use appropriate screen types for different scenarios
   - Clean up resources when removing screens
   - Handle screen transitions smoothly

2. **Widget Design**
   - Keep widgets focused and single-purpose
   - Use proper event handling
   - Follow the composition pattern

3. **Event Handling**
   - Use typed event data
   - Handle events asynchronously
   - Clean up event listeners

4. **Theme Usage**
   - Use theme variables instead of hardcoded values
   - Provide fallback styles
   - Test with different themes

## Examples

### Complete Application Example

```python
from pepperpy import (
    PepperApp,
    PepperScreen,
    PepperWidget,
    Static,
    ThemeManager
)

class WelcomeWidget(PepperWidget):
    def compose(self):
        yield Static("Welcome to My App!")

class MainScreen(PepperScreen):
    async def compose(self):
        yield WelcomeWidget()

class MyApp(PepperApp):
    async def on_mount(self):
        # Load themes
        await self.themes.load_themes(Path("themes"))
        self.themes.set_theme("dark")
        
        # Show main screen
        await self.push_screen(MainScreen())

app = MyApp()
app.run()
```

### Custom Widget with Events

```python
from pepperpy import PepperWidget, Static

class ClickableWidget(PepperWidget):
    def compose(self):
        yield Static("Click me!")

    def on_click(self):
        self.emit_event("widget_clicked", {
            "timestamp": time.time()
        })
```

### Screen with Loading State

```python
from pepperpy import PepperScreen, LoadingScreen

class DataScreen(PepperScreen):
    async def load_data(self):
        # Show loading screen
        await self.app.push_screen(LoadingScreen("Loading data..."))
        
        try:
            # Load data
            await self.fetch_data()
        finally:
            # Remove loading screen
            await self.app.pop_screen()
``` 