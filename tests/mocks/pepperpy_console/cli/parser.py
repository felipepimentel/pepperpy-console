"""Mock parser module."""

from typing import Any, Dict, Optional, Tuple


class CommandParser:
    """Mock command parser for CLI input."""

    async def parse(self, input_text: str) -> Optional[Tuple[str, Dict[str, Any]]]:
        """Parse command input into command name and arguments."""
        if not input_text or input_text.isspace():
            return None

        parts = input_text.strip().split()
        command_name = parts[0]
        args = {}

        if len(parts) > 1:
            args["args"] = parts[1:]

        return command_name, args
