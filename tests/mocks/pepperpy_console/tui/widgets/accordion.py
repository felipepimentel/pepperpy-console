"""Mock implementations of accordion-related components."""

from typing import Any, List, Optional

from ....textual import MockWidget


class AccordionItem(MockWidget):
    """Mock implementation of an accordion item."""

    def __init__(self, title: str, content: str = "") -> None:
        """Initialize the accordion item."""
        super().__init__()
        self.title = title
        self.content = content
        self.is_expanded = False

    def toggle(self) -> None:
        """Toggle the expanded state."""
        self.is_expanded = not self.is_expanded

    def on_click(self) -> None:
        """Handle click events."""
        self.toggle()


class Accordion(MockWidget):
    """Mock implementation of an accordion widget."""

    def __init__(
        self, *args: Any, items: Optional[List[tuple[str, str]]] = None, **kwargs: Any
    ) -> None:
        """Initialize the accordion."""
        super().__init__(*args, **kwargs)
        self.items: List[AccordionItem] = []
        self.allow_multiple = True
        if items:
            self._setup_items(items)

    def _setup_items(self, items: List[tuple[str, str]]) -> None:
        """Setup accordion items."""
        for title, content in items:
            item = AccordionItem(title=title, content=content)
            self.items.append(item)

    def add_item(self, title: str, content: str = "") -> AccordionItem:
        """Add a new item to the accordion."""
        item = AccordionItem(title=title, content=content)
        self.items.append(item)
        return item

    def on_accordion_item_click(self, event: Any) -> None:
        """Handle item click events."""
        clicked_item = event.sender
        if not self.allow_multiple:
            # Collapse other items
            for item in self.items:
                if item != clicked_item and item.is_expanded:
                    item.toggle()
        clicked_item.toggle()
