"""Mock app module."""

from typing import Any, List

from .widget import Widget


class App(Widget):
    """Mock app class."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the app."""
        super().__init__(*args, **kwargs)
        self.screen = None


class ComposeResult:
    """Mock compose result class."""

    def __init__(self, widgets: List[Widget]) -> None:
        """Initialize the compose result."""
        self.widgets = widgets
