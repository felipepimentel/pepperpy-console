"""Base widget classes for PepperPy Console."""

from typing import Any

import structlog
from pepperpy_core.events import EventManager
from textual.widget import Widget

logger = structlog.get_logger(__name__)


class PepperWidget(Widget):
    """Base widget class with event handling."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the widget."""
        super().__init__(*args, **kwargs)
        self.events = EventManager()

    async def emit_event(self, event: str, data: Any = None) -> None:
        """Emit a widget event.

        Args:
            event: Event name
            data: Optional event data
        """
        await self.events.emit(event, data)
