"""Simple PepperPy Console application example."""

from __future__ import annotations

from typing import TYPE_CHECKING

from textual.containers import Container, Vertical
from textual.widgets import Footer, Header

from pepperpy.tui.app import PepperApp
from pepperpy.tui.forms import PepperForm
from pepperpy.tui.screens import PepperScreen

if TYPE_CHECKING:
    from collections.abc import Iterator

    from textual.widgets._widget import Widget


class ExampleForm(PepperForm):
    """Example form with various field types."""

    def compose(self) -> Iterator[Container]:
        """Compose the form layout."""
        with Container(), Vertical():
            yield Container()

    async def on_submit(self, data: dict[str, str | float | bool | None]) -> None:
        """Handle form submission.

        Args:
            data: Form data.

        """
        if self.app and self.app.notification_center:
            await self.app.notification_center.emit_event(
                "notification",
                {
                    "message": f"Form submitted with data: {data}",
                    "severity": "information",
                },
            )


class MainScreen(PepperScreen):
    """Main application screen."""

    def compose(self) -> Iterator[Widget]:
        """Compose the screen layout."""
        yield Header()
        yield ExampleForm()
        yield Footer()


class ExampleApp(PepperApp):
    """Example application demonstrating basic features."""

    TITLE = "PepperPy Example"

    def __init__(self) -> None:
        """Initialize the application."""
        super().__init__()

    async def on_mount(self) -> None:
        """Handle application mount event."""
        await super().on_mount()
        await self.switch_screen(MainScreen())
