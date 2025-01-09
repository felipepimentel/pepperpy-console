"""Command system for CLI operations."""

from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional

import structlog

logger = structlog.get_logger(__name__)


@dataclass
class Command:
    """Base class for CLI commands.

    Attributes:
        name (str): Command name
        description (str): Command description
        callback (Callable): Function to execute when command is called
        arguments (List[Dict[str, Any]]): Command arguments configuration
    """

    name: str
    description: str
    callback: Callable
    arguments: List[Dict[str, Any]] = field(default_factory=list)

    async def execute(self, *args: Any, **kwargs: Any) -> Any:
        """Execute the command.

        Args:
            *args: Positional arguments to pass to the callback
            **kwargs: Keyword arguments to pass to the callback

        Returns:
            Any: Result of the callback execution
        """
        logger.debug(f"Executing command {self.name}")
        return await self.callback(*args, **kwargs)


@dataclass
class CommandGroup:
    """Group of related commands.

    Attributes:
        name (str): Group name
        description (str): Group description
        commands (Dict[str, Command]): Commands in this group
    """

    name: str
    description: str
    commands: Dict[str, Command] = field(default_factory=dict)

    def add_command(self, command: Command) -> None:
        """Add a command to the group.

        Args:
            command (Command): Command to add
        """
        self.commands[command.name] = command
        logger.debug(f"Added command {command.name} to group {self.name}")

    def get_command(self, name: str) -> Optional[Command]:
        """Get a command by name.

        Args:
            name (str): Command name

        Returns:
            Optional[Command]: Command if found, None otherwise
        """
        return self.commands.get(name)
