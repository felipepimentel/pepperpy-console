"""Mock package initialization."""

from .pepperpy_console import (
    PepperApp,
    PepperCommand,
    PepperCommandSystem,
    PepperWidget,
)
from .pepperpy_console.cli import Command, CommandGroup, CommandParser
from .pepperpy_console.theme import Theme, ThemeManager
from .pepperpy_console.tui.screens import LoadingScreen, PepperScreen
from .pepperpy_console.tui.widgets.accordion import Accordion, AccordionItem
from .textual import MockApp, MockMessage, MockScreen, MockWidget

__all__ = [
    "Accordion",
    "AccordionItem",
    "Command",
    "CommandGroup",
    "CommandParser",
    "LoadingScreen",
    "MockApp",
    "MockMessage",
    "MockScreen",
    "MockWidget",
    "PepperApp",
    "PepperCommand",
    "PepperCommandSystem",
    "PepperScreen",
    "PepperWidget",
    "Theme",
    "ThemeManager",
]
