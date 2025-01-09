"""Screen components for TUI applications."""

from typing import Any

import structlog
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Label, LoadingIndicator

logger = structlog.get_logger(__name__)


class PepperScreen(Screen):
    """Base screen with common functionality.

    This class provides a base for all application screens with common
    layout and styling.
    """

    DEFAULT_CSS = """
    PepperScreen {
        background: $background;
        color: $text;
    }

    PepperScreen Container {
        width: 100%;
        height: 100%;
        padding: 1;
    }

    PepperScreen ScrollableContainer {
        width: 100%;
        height: 100%;
        border: solid $primary;
    }
    """

    def compose(self):
        """Compose the screen layout."""
        yield Container()


class LoadingScreen(PepperScreen):
    """Loading screen with progress indicator.

    This screen is shown during long-running operations.
    """

    DEFAULT_CSS = """
    LoadingScreen {
        align: center middle;
    }

    LoadingScreen Label {
        color: $text;
        margin: 1;
    }

    LoadingScreen LoadingIndicator {
        color: $primary;
    }
    """

    def __init__(self, *args: Any, message: str = "Loading...", **kwargs: Any) -> None:
        """Initialize the loading screen.

        Args:
            *args: Positional arguments
            message: Loading message
            **kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.message = message

    def compose(self):
        """Compose the loading screen layout."""
        yield Container()
        yield Label(self.message)
        yield LoadingIndicator()


class ErrorScreen(PepperScreen):
    """Error screen for displaying error messages.

    This screen is shown when an error occurs.
    """

    DEFAULT_CSS = """
    ErrorScreen {
        align: center middle;
    }

    ErrorScreen Label {
        color: $error;
        margin: 1;
    }
    """

    def __init__(self, *args: Any, error_message: str, **kwargs: Any) -> None:
        """Initialize the error screen.

        Args:
            *args: Positional arguments
            error_message: Error message
            **kwargs: Keyword arguments
        """
        super().__init__(*args, **kwargs)
        self.error_message = error_message

    def compose(self):
        """Compose the error screen layout."""
        yield Container()
        yield Label(self.error_message)
