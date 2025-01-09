"""Mock command module."""

from typing import Any, Callable, Dict, List, Optional


class Command:
    """Mock command class."""

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

    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the command."""
        return await self.callback(*args, **kwargs)


class CommandGroup:
    """Mock command group for organizing commands."""

    def __init__(self) -> None:
        """Initialize the command group."""
        self.commands: Dict[str, Command] = {}

    def add_command(self, command: Command) -> None:
        """Add a command to the group."""
        self.commands[command.name] = command
        for alias in command.aliases:
            self.commands[alias] = command

    def get_command(self, name: str) -> Optional[Command]:
        """Get a command by name or alias."""
        return self.commands.get(name)
