"""Mock basic widgets module."""

from typing import Any, Callable, Optional

from ..events import Clicked
from ..widget import Widget


class Footer(Widget):
    """Mock footer widget."""

    pass


class Header(Widget):
    """Mock header widget."""

    pass


class Input(Widget):
    """Mock input widget."""

    def __init__(self, value: str = "", *args: Any, **kwargs: Any) -> None:
        """Initialize the input."""
        super().__init__(*args, **kwargs)
        self.value = value


class Label(Widget):
    """Mock label widget."""

    def __init__(self, text: str = "", *args: Any, **kwargs: Any) -> None:
        """Initialize the label."""
        super().__init__(*args, **kwargs)
        self.renderable = text


class ListView(Widget):
    """Mock list view widget."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the list view."""
        super().__init__(*args, **kwargs)
        self.items = []

    def clear(self) -> None:
        """Clear all items."""
        self.items = []

    def append(self, item: Any) -> None:
        """Add an item."""
        self.items.append(item)


class LoadingIndicator(Widget):
    """Mock loading indicator widget."""

    pass


class Static(Widget):
    """Mock static widget."""

    Clicked = Clicked

    def __init__(self, text: str = "", *args: Any, **kwargs: Any) -> None:
        """Initialize the static widget."""
        super().__init__(*args, **kwargs)
        self.renderable = text


class Tree(Widget):
    """Mock tree widget."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the tree."""
        super().__init__(*args, **kwargs)
        self.root = TreeNode("root")


class TreeNode:
    """Mock tree node."""

    def __init__(self, label: str) -> None:
        """Initialize the node."""
        self.label = label
        self.parent: Optional[TreeNode] = None
        self.children = []

    def add(self, label: str) -> "TreeNode":
        """Add a child node."""
        node = TreeNode(label)
        node.parent = self
        self.children.append(node)
        return node


class Button(Widget):
    """Mock button widget."""

    class Pressed:
        """Mock button pressed event."""

        def __init__(self, button: "Button") -> None:
            """Initialize the event."""
            self.button = button

    def __init__(
        self,
        label: str = "",
        variant: str = "default",
        on_click: Optional[Callable] = None,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """Initialize the button."""
        super().__init__(*args, **kwargs)
        self.label = label
        self.variant = variant
        self.on_click = on_click

    def press(self) -> None:
        """Press the button."""
        if self.on_click:
            self.on_click()
        self.emit_no_wait("pressed", self)
