"""Mock accordion widgets module."""

from typing import Any, Dict, Optional

from ..containers import Container
from ..message import Message
from ..widget import Widget


class AccordionItem(Widget):
    """Mock accordion item widget."""

    def __init__(self, title: str, content: str, expanded: bool = False) -> None:
        """Initialize the accordion item."""
        super().__init__()
        self.title = title
        self.content = content
        self.expanded = expanded

    class Clicked(Message):
        """Mock clicked event."""

        def __init__(self, item: "AccordionItem") -> None:
            """Initialize the clicked event."""
            super().__init__()
            self.item = item


class Accordion(Container):
    """Mock accordion widget."""

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        """Initialize the accordion."""
        super().__init__(*args, **kwargs)
        self.items: Dict[str, AccordionItem] = {}

    def add_item(self, title: str, content: str) -> None:
        """Add an item to the accordion."""
        item = AccordionItem(title=title, content=content)
        self.items[title] = item

    def get_item(self, title: str) -> Optional[AccordionItem]:
        """Get an item by title."""
        return self.items.get(title)

    def on_accordion_item_click(self, event: AccordionItem.Clicked) -> None:
        """Handle item click events."""
        item = event.item
        item.expanded = not item.expanded
