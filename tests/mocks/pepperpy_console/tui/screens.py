"""Mock implementations of TUI screen components."""

from typing import Optional

from ...textual import MockScreen, MockWidget


class PepperScreen(MockScreen):
    """Mock implementation of the Pepper screen."""

    def __init__(self) -> None:
        """Initialize the screen."""
        super().__init__()
        self.title = "Pepper Console"
        self.active_widget: Optional[MockWidget] = None

    def focus(self, widget: MockWidget) -> None:
        """Focus a widget."""
        self.active_widget = widget


class LoadingScreen(PepperScreen):
    """Mock implementation of the loading screen."""

    def __init__(self) -> None:
        """Initialize the loading screen."""
        super().__init__()
        self.title = "Loading..."
        self.message = "Please wait..."

    def update_message(self, message: str) -> None:
        """Update the loading message."""
        self.message = message
