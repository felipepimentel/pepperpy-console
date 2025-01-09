"""Mock implementations of PepperPy Console components."""

from typing import Any, Callable, Dict, List, Optional

from ..textual import MockApp, MockWidget


class PepperCommand:
    """Mock implementation of a Pepper command."""

    def __init__(
        self,
        name: str,
        callback: Callable,
        description: str = "",
        aliases: Optional[List[str]] = None,
    ) -> None:
        """Initialize the command."""
        self.name = name
        self.callback = callback
        self.description = description
        self.aliases = aliases or []


class PepperCommandSystem:
    """Mock implementation of the command system."""

    def __init__(self) -> None:
        """Initialize the command system."""
        self.commands: Dict[str, PepperCommand] = {}
        self.aliases: Dict[str, str] = {}

    def register_command(
        self,
        name: str,
        callback: Callable,
        description: str = "",
        aliases: Optional[List[str]] = None,
    ) -> None:
        """Register a new command."""
        command = PepperCommand(name, callback, description, aliases)
        self.commands[name] = command
        if aliases:
            for alias in aliases:
                self.aliases[alias] = name

    def get_command(self, name: str) -> Optional[PepperCommand]:
        """Get a command by name or alias."""
        if name in self.commands:
            return self.commands[name]
        if name in self.aliases:
            return self.commands[self.aliases[name]]
        return None


class PepperWidget(MockWidget):
    """Mock implementation of the Pepper widget."""

    def __init__(self) -> None:
        """Initialize the widget."""
        super().__init__()
        self.content = ""

    def update_content(self, content: str) -> None:
        """Update the widget content."""
        self.content = content


class PepperApp(MockApp):
    """Mock implementation of the Pepper application."""

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__()
        self.commands = PepperCommandSystem()
        self.parser = None
        self.theme_manager = None
        self.last_command: Optional[Dict[str, Any]] = None

    def register_command(
        self,
        name: str,
        callback: Callable,
        description: str = "",
        aliases: Optional[List[str]] = None,
    ) -> None:
        """Register a new command."""
        self.commands.register_command(name, callback, description, aliases)

    async def process_command(self, command_str: str) -> None:
        """Process a command string."""
        if not command_str or command_str.isspace():
            return

        parts = command_str.split()
        cmd_name = parts[0]
        args = parts[1:] if len(parts) > 1 else []

        command = self.commands.get_command(cmd_name)
        if command:
            result = await command.callback(args=args)
            self.last_command = {"name": cmd_name, "args": result}
