"""Mock TUI module."""

from .events import Event, EventManager
from .screens import LoadingScreen, PepperScreen
from .theme import Theme, ThemeManager
from .widgets.base import PepperWidget

__all__ = [
    "Event",
    "EventManager",
    "LoadingScreen",
    "PepperScreen",
    "Theme",
    "ThemeManager",
    "PepperWidget",
]
