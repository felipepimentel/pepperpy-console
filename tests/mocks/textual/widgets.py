"""Mock Textual widgets module."""

from typing import Any, Optional

from .widget import Widget


class Footer(Widget):
    """Mock footer widget."""

    pass


class Header(Widget):
    """Mock header widget."""

    pass


class Label(Widget):
    """Mock label widget."""

    def __init__(self, text: str = "", *args: Any, **kwargs: Any) -> None:
        """Initialize the label."""
        super().__init__(*args, **kwargs)
        self.renderable = text


class LoadingIndicator(Widget):
    """Mock loading indicator widget."""

    pass


class Static(Widget):
    """Mock static widget."""

    pass


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


class Input(Widget):
    """Mock input widget."""

    def __init__(self, value: str = "", *args: Any, **kwargs: Any) -> None:
        """Initialize the input."""
        super().__init__(*args, **kwargs)
        self.value = value


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
