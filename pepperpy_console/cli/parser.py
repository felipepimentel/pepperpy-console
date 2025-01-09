"""Command line argument parsing."""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

import structlog

from .command import Command, CommandGroup

logger = structlog.get_logger(__name__)


@dataclass
class ArgumentSpec:
    """Specification for a command line argument.

    Attributes:
        name (str): Argument name
        type (type): Expected argument type
        help (str): Help text
        required (bool): Whether the argument is required
        default (Any): Default value if not required
    """

    name: str
    type: type
    help: str
    required: bool = True
    default: Any = None


@dataclass
class ArgumentParser:
    """Enhanced argument parser with validation and logging.

    Attributes:
        program (str): Program name
        description (str): Program description
        commands (Dict[str, Union[Command, CommandGroup]]): Available commands
    """

    program: str
    description: str
    commands: Dict[str, Union[Command, CommandGroup]] = field(default_factory=dict)

    async def parse_args(self, args: List[str]) -> Dict[str, Any]:
        """Parse command line arguments.

        Args:
            args: List of command line arguments

        Returns:
            Dict[str, Any]: Parsed and validated arguments

        Raises:
            ValueError: If validation fails
        """
        if not args:
            return {"help": True}

        command_name = args[0]
        command = self.commands.get(command_name)

        if not command:
            logger.error(f"Unknown command: {command_name}")
            return {"help": True}

        try:
            parsed = await self._parse_command_args(command, args[1:])
            return {"command": command, "args": parsed}
        except Exception as e:
            logger.error(f"Failed to parse arguments: {e}")
            return {"help": True}

    async def _parse_command_args(
        self, command: Command, args: List[str]
    ) -> Dict[str, Any]:
        """Parse arguments for a specific command.

        Args:
            command: Command to parse arguments for
            args: Command arguments

        Returns:
            Dict[str, Any]: Parsed arguments
        """
        result: Dict[str, Any] = {}

        for arg_spec in command.arguments:
            value = self._get_arg_value(args, arg_spec)
            if value is not None:
                result[arg_spec["name"]] = value

        return result

    def _get_arg_value(
        self, args: List[str], arg_spec: Dict[str, Any]
    ) -> Optional[Any]:
        """Extract argument value from command line args.

        Args:
            args: Command line arguments
            arg_spec: Argument specification

        Returns:
            Optional[Any]: Parsed argument value
        """
        name = arg_spec["name"]
        for i, arg in enumerate(args):
            if arg in [f"--{name}", f"-{name[0]}"]:
                if i + 1 < len(args):
                    return self._convert_value(args[i + 1], arg_spec)
        return arg_spec.get("default")
