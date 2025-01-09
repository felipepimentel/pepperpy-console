"""Mock events module."""

from dataclasses import dataclass
from typing import Any, Dict, Optional


@dataclass
class Event:
    """Mock base event class."""

    name: str
    data: Optional[Dict[str, Any]] = None


class EventManager:
    """Mock event manager for handling events."""

    def __init__(self) -> None:
        """Initialize the event manager."""
        self.events: Dict[str, Event] = {}

    def emit(self, event: Event) -> None:
        """Emit an event."""
        self.events[event.name] = event

    def get_event(self, name: str) -> Optional[Event]:
        """Get an event by name."""
        return self.events.get(name)

    def clear(self) -> None:
        """Clear all events."""
        self.events.clear()
