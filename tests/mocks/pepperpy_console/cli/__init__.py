"""Mock implementations of CLI-related components."""

from typing import Any, Callable, Dict, List, Optional


class Command:
    """Mock implementation of a CLI command."""

    def __init__(
        self,
        name: str,
        callback: Callable[..., Any],
        description: str = "",
        aliases: Optional[List[str]] = None,
    ) -> None:
        """Initialize the command."""
        self.name = name
        self.callback = callback
        self.description = description
        self.aliases = aliases or []


class CommandGroup:
    """Mock implementation of a command group."""

    def __init__(self, name: str, description: str = "") -> None:
        """Initialize the command group."""
        self.name = name
        self.description = description
        self.commands: Dict[str, Command] = {}
        self.aliases: Dict[str, str] = {}

    def command(
        self,
        name: str,
        description: str = "",
        aliases: Optional[List[str]] = None,
    ) -> Callable:
        """Decorator to register a command."""

        def decorator(func: Callable) -> Callable:
            cmd = Command(name, func, description, aliases)
            self.commands[name] = cmd
            if aliases:
                for alias in aliases:
                    self.aliases[alias] = name
            return func

        return decorator

    def get_command(self, name: str) -> Optional[Command]:
        """Get a command by name or alias."""
        if name in self.commands:
            return self.commands[name]
        if name in self.aliases:
            return self.commands[self.aliases[name]]
        return None


class CommandParser:
    """Mock implementation of a command parser."""

    def __init__(self) -> None:
        """Initialize the command parser."""
        self.groups: Dict[str, CommandGroup] = {}

    def group(self, name: str, description: str = "") -> CommandGroup:
        """Create a new command group."""
        group = CommandGroup(name, description)
        self.groups[name] = group
        return group

    def parse(self, command_str: str) -> Optional[Dict[str, Any]]:
        """Parse a command string."""
        if not command_str or command_str.isspace():
            return None

        parts = command_str.split()
        if len(parts) < 2:
            return None

        group_name, cmd_name, *args = parts
        group = self.groups.get(group_name)
        if not group:
            return None

        command = group.get_command(cmd_name)
        if not command:
            return None

        return {
            "group": group_name,
            "command": cmd_name,
            "args": args,
        }
