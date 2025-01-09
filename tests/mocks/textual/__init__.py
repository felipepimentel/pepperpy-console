"""Mock implementation of Textual components for testing."""

from typing import Any, Dict, List, Optional


class MockScreen:
    """Mock implementation of Textual Screen."""

    def __init__(self) -> None:
        """Initialize the mock screen."""
        self.styles: Dict[str, Any] = {}
        self.widgets: List["MockWidget"] = []

    def mount(self, widget: "MockWidget") -> None:
        """Mount a widget to the screen."""
        self.widgets.append(widget)


class MockWidget:
    """Mock implementation of Textual Widget."""

    def __init__(self) -> None:
        """Initialize the mock widget."""
        self.parent: Optional[MockWidget] = None
        self.children: List[MockWidget] = []
        self.styles: Dict[str, Any] = {}
        self.classes: List[str] = []

    def mount(self, widget: "MockWidget") -> None:
        """Mount a child widget."""
        widget.parent = self
        self.children.append(widget)

    def add_class(self, class_name: str) -> None:
        """Add a CSS class to the widget."""
        if class_name not in self.classes:
            self.classes.append(class_name)


class MockApp:
    """Mock implementation of Textual App."""

    def __init__(self) -> None:
        """Initialize the mock app."""
        self.screen = MockScreen()
        self.widgets: List[MockWidget] = []
        self.running = False

    async def run(self) -> None:
        """Run the mock app."""
        self.running = True

    def mount(self, widget: MockWidget) -> None:
        """Mount a widget to the app."""
        self.widgets.append(widget)
        self.screen.mount(widget)


class MockMessage:
    """Mock implementation of Textual Message."""

    def __init__(self, sender: Any = None) -> None:
        """Initialize the mock message."""
        self.sender = sender
