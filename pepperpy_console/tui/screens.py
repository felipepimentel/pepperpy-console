"""Screen classes for PepperPy Console."""

from typing import AsyncIterator

from textual.screen import Screen
from textual.widgets import LoadingIndicator, Static
from textual.app import App, ComposeResult

from .widgets.base import PepperWidget


class PepperScreen(Screen):
    """Base screen class for PepperPy Console.

    All screens should inherit from this class.
    """

    BINDINGS = []

    async def compose(self) -> AsyncIterator[Static]:
        """Compose the screen layout.

        This method should be overridden by subclasses.

        Yields:
            Static: Screen widgets
        """
        yield Static("Base PepperPy Screen")


class LoadingScreen(Screen):
    """Loading screen widget.

    Attributes:
        message (str): Loading message to display
    """

    def __init__(self, message: str = "Loading...") -> None:
        """Initialize the loading screen.

        Args:
            message: Loading message to display
        """
        super().__init__()
        self.message = message

    async def compose(self) -> AsyncIterator[Static]:
        """Compose the loading screen.

        Returns:
            AsyncIterator[Static]: Loading screen composition result
        """
        yield Static(self.message)
        yield LoadingIndicator()

    async def remove(self) -> None:
        """Remove the screen from the app."""
        pass


class ErrorScreen(Screen):
    """Error screen with an error message.

    Attributes:
        message (str): Error message
    """

    def __init__(self, message: str) -> None:
        """Initialize the error screen.

        Args:
            message: Error message
        """
        super().__init__()
        self.message = message

    async def compose(self) -> AsyncIterator[Static]:
        """Compose the error screen layout.

        Yields:
            Static: Screen widgets
        """
        yield Static(f"Error: {self.message}")
