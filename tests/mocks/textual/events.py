"""Mock Textual events module."""

from dataclasses import dataclass


@dataclass
class Event:
    """Base event class."""

    pass


@dataclass
class Click(Event):
    """Click event."""

    x: int = 0
    y: int = 0


class Clicked:
    """Clicked event."""

    pass
