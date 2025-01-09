"""Mock screen module."""

from .widget import Widget


class Screen(Widget):
    """Mock screen class."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the screen."""
        super().__init__(*args, **kwargs)
