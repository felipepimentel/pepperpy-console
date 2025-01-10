# API Reference

This section provides detailed documentation for the PepperPy Console API.

## Core Components

### PepperApp

The main application class that serves as the entry point for PepperPy Console applications.

```python
class PepperApp:
    """Base application class for PepperPy Console."""
    
    def __init__(self):
        """Initialize the application."""
        
    async def on_mount(self):
        """Called when the application is mounted."""
        
    async def push_screen(self, screen: PepperScreen):
        """Push a screen onto the screen stack."""
        
    async def pop_screen(self):
        """Pop the top screen from the screen stack."""
        
    async def load_plugins(self, plugin_dir: Path):
        """Load plugins from the specified directory."""
        
    async def load_themes(self, themes_dir: Path):
        """Load themes from the specified directory."""
        
    def run(self):
        """Run the application."""
```

### PepperScreen

Base class for all screens in PepperPy Console.

```python
class PepperScreen:
    """Base class for screens."""
    
    async def compose(self) -> AsyncGenerator:
        """Compose the screen layout."""
        
    async def on_mount(self):
        """Called when the screen is mounted."""
        
    async def on_unmount(self):
        """Called when the screen is unmounted."""
```

### Command

Represents a CLI command that can be executed.

```python
class Command:
    """Represents a CLI command."""
    
    def __init__(
        self,
        name: str,
        callback: Callable,
        description: str = "",
        arguments: List[str] = None
    ):
        """Initialize a command."""
```

## Widgets

### PepperWidget

Base class for all widgets in PepperPy Console.

```python
class PepperWidget:
    """Base class for widgets."""
    
    async def compose(self) -> AsyncGenerator:
        """Compose the widget layout."""
```

### PepperTable

Widget for displaying tabular data.

```python
class PepperTable(PepperWidget):
    """Widget for displaying tabular data."""
    
    def add_column(self, column: Column):
        """Add a column to the table."""
        
    def add_row(self, *values: str):
        """Add a row to the table."""
```

### PepperForm

Widget for creating forms.

```python
class PepperForm(PepperWidget):
    """Widget for creating forms."""
    
    def add_field(self, field: FormField):
        """Add a field to the form."""
        
    async def on_submit(self, data: Dict[str, Any]):
        """Called when the form is submitted."""
```

## Theme System

### ThemeManager

Manages application themes.

```python
class ThemeManager:
    """Manages application themes."""
    
    def load_theme(self, theme_file: Path):
        """Load a theme from a file."""
        
    def set_theme(self, theme_name: str):
        """Set the active theme."""
```

### Theme

Represents a color and style theme.

```python
class Theme:
    """Represents a theme."""
    
    def __init__(self, name: str, colors: Dict[str, str], styles: Dict[str, str]):
        """Initialize a theme."""
```

## Plugin System

### Plugin

Base class for plugins.

```python
class Plugin:
    """Base class for plugins."""
    
    def __init__(self, name: str):
        """Initialize a plugin."""
        
    def register(self, app: PepperApp):
        """Register the plugin with the application."""
```

## Events

### Event

Base class for events.

```python
class Event:
    """Base class for events."""
    
    def __init__(self, sender: Any):
        """Initialize an event."""
```

### NotificationCenter

Manages application notifications.

```python
class NotificationCenter:
    """Manages application notifications."""
    
    async def notify(self, message: str, type: str = "info"):
        """Send a notification."""
```

## Utilities

### CommandParser

Parses command strings into executable commands.

```python
class CommandParser:
    """Parses command strings."""
    
    def parse(self, command_str: str) -> Tuple[Command, List[str]]:
        """Parse a command string."""
```

### LoadingScreen

Screen for displaying loading states.

```python
class LoadingScreen(PepperScreen):
    """Screen for displaying loading states."""
    
    def __init__(self, message: str = "Loading..."):
        """Initialize a loading screen."""
```

### ErrorScreen

Screen for displaying errors.

```python
class ErrorScreen(PepperScreen):
    """Screen for displaying errors."""
    
    def __init__(self, message: str):
        """Initialize an error screen."""
```

## Constants

```python
DEFAULT_THEME = "light"
PLUGIN_ENTRY_POINT = "pepperpy.plugins"
THEME_FILE_EXTENSION = ".json"
```

## Type Hints

```python
CommandCallback = Callable[..., Awaitable[str]]
ThemeColors = Dict[str, str]
ThemeStyles = Dict[str, str]
ScreenStack = List[PepperScreen]
```

## Exceptions

```python
class PepperError(Exception):
    """Base exception for PepperPy Console."""

class CommandError(PepperError):
    """Raised when there is an error with a command."""

class ThemeError(PepperError):
    """Raised when there is an error with a theme."""

class PluginError(PepperError):
    """Raised when there is an error with a plugin."""
``` 