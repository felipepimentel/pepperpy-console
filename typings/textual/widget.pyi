"""Type stubs for Textual Widget class."""

from typing import Any, Protocol, TypeVar

from textual.app import App
from textual.message import Message

T = TypeVar("T")

class Widget(Protocol):
    """Base widget class."""

    id: str
    classes: set[str]
    styles: dict[str, Any]

    @property
    def app(self) -> App[Any] | None:
        """Get the application instance."""
        ...

    def __init__(self) -> None:
        """Initialize the widget."""
        ...

    async def post_message(self, message: Message) -> bool:
        """Post a message to the widget.

        Args:
            message: Message to post.

        Returns:
            bool: Whether the message was handled.
        """
        ...

    async def on_mount(self) -> None:
        """Handle widget mount event."""
        ...

    def remove(self) -> None:
        """Remove the widget."""
        ...

    def refresh(self) -> None:
        """Refresh the widget."""
        ...

    def add_class(self, class_name: str) -> None:
        """Add a CSS class.

        Args:
            class_name: Class name to add.
        """
        ...

    def remove_class(self, class_name: str) -> None:
        """Remove a CSS class.

        Args:
            class_name: Class name to remove.
        """
        ...

    async def mount(self, *widgets: Widget) -> None:
        """Mount child widgets.

        Args:
            *widgets: Widgets to mount.
        """
        ...

    def query(self, selector: str) -> list[Widget]:
        """Query child widgets.

        Args:
            selector: CSS selector.

        Returns:
            List of matching widgets.
        """
        ...

    def remove_children(self) -> None:
        """Remove all child widgets."""
        ...
