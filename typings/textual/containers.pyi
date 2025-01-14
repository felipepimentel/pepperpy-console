"""Type stubs for Textual containers."""

from typing import Any

from textual.widget import Widget

class Container(Widget):
    """Container widget."""

    def __init__(
        self, *, widget_id: str | None = None, classes: str | None = None
    ) -> None:
        """Initialize the container.

        Args:
            widget_id: The ID of the widget in the DOM.
            classes: The CSS classes of the widget.
        """
        ...

    def __enter__(self) -> "Container":
        """Enter the context."""
        ...

    def __exit__(self, *args: Any) -> None:
        """Exit the context."""
        ...

class Vertical(Container):
    """Vertical container."""

    def __init__(
        self, *, widget_id: str | None = None, classes: str | None = None
    ) -> None:
        """Initialize the container.

        Args:
            widget_id: The ID of the widget in the DOM.
            classes: The CSS classes of the widget.
        """
        ...

    def __enter__(self) -> "Vertical":
        """Enter the context."""
        ...

    def __exit__(self, *args: Any) -> None:
        """Exit the context."""
        ...
