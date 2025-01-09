"""Mock app module."""

from typing import Any, Dict, Optional

from textual.app import App

from .cli.command import Command, CommandGroup
from .cli.parser import CommandParser
from .tui.theme import ThemeManager


class PepperApp(App):
    """Mock Pepper console application."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the app."""
        super().__init__(*args, **kwargs)
        self.commands = CommandGroup()
        self.parser = CommandParser()
        self.theme_manager = ThemeManager()
        self.last_command: Optional[Dict[str, Any]] = None

    async def process_command(self, input_text: str) -> None:
        """Process a command input."""
        result = await self.parser.parse(input_text)
        if result:
            command_name, args = result
            command = self.commands.get_command(command_name)
            if command:
                self.last_command = {"name": command_name, "args": args}
                await command.execute(**args)

    def register_command(
        self,
        name: str,
        callback: Any,
        description: str = "",
        aliases: Optional[list[str]] = None,
    ) -> None:
        """Register a new command."""
        command = Command(name, callback, description, aliases)
        self.commands.add_command(command)
