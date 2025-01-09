"""Mock implementation of base widget components."""

from typing import Any, Dict, Optional

from ....textual import MockWidget


class PepperWidget(MockWidget):
    """Mock implementation of the base Pepper widget."""

    def __init__(self) -> None:
        """Initialize the widget."""
        super().__init__()
        self.styles: Dict[str, Any] = {}
        self.parent: Optional["PepperWidget"] = None
        self.visible = True
        self.focused = False

    def show(self) -> None:
        """Show the widget."""
        self.visible = True

    def hide(self) -> None:
        """Hide the widget."""
        self.visible = False

    def focus(self) -> None:
        """Focus the widget."""
        self.focused = True

    def blur(self) -> None:
        """Remove focus from the widget."""
        self.focused = False

    def add_class(self, class_name: str) -> None:
        """Add a CSS class to the widget."""
        if "classes" not in self.styles:
            self.styles["classes"] = set()
        self.styles["classes"].add(class_name)

    def remove_class(self, class_name: str) -> None:
        """Remove a CSS class from the widget."""
        if "classes" in self.styles:
            self.styles["classes"].discard(class_name)

    def has_class(self, class_name: str) -> bool:
        """Check if the widget has a CSS class."""
        return "classes" in self.styles and class_name in self.styles["classes"]
