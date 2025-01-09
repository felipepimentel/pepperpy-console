"""Mock tree widget module."""

from typing import Any, Dict, List, Optional

from ..widget import Widget


class TreeNode:
    """Mock tree node class."""

    def __init__(self, label: str, data: Optional[Dict[str, Any]] = None) -> None:
        """Initialize the node."""
        self.label = label
        self.data = data or {}
        self.parent: Optional[TreeNode] = None
        self.children: List[TreeNode] = []
        self.is_expanded = False

    def add(
        self, label: str, data: Optional[Dict[str, Any]] = None, expand: bool = False
    ) -> "TreeNode":
        """Add a child node."""
        node = TreeNode(label, data)
        node.parent = self
        node.is_expanded = expand
        self.children.append(node)
        return node

    def expand(self) -> None:
        """Expand the node."""
        self.is_expanded = True

    def collapse(self) -> None:
        """Collapse the node."""
        self.is_expanded = False

    def set_icon(self, icon: str) -> None:
        """Set the node icon."""
        self.data["icon"] = icon


class NodeSelected:
    """Mock node selected event."""

    def __init__(self, node: TreeNode) -> None:
        """Initialize the event."""
        self.node = node


class Tree(Widget):
    """Mock tree widget class."""

    NodeSelected = NodeSelected

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the tree."""
        super().__init__(*args, **kwargs)
        self.root = TreeNode("root")
        self.selected_node: Optional[TreeNode] = None

    def select_node(self, node: TreeNode) -> None:
        """Select a node."""
        self.selected_node = node
        self.emit_no_wait("node_selected", node)
