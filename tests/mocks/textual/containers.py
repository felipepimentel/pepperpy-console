"""Mock containers module."""

from .widget import Widget


class Container(Widget):
    """Mock container widget."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the container."""
        super().__init__(*args, **kwargs)


class Horizontal(Container):
    """Mock horizontal container widget."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the horizontal container."""
        super().__init__(*args, **kwargs)


class Vertical(Container):
    """Mock vertical container widget."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize the vertical container."""
        super().__init__(*args, **kwargs)
