"""Type stubs for Textual App module."""

from typing import Any, Awaitable, Callable, Iterator, Protocol, TypeVar

from textual.screen import Screen
from textual.widget import Widget

T_co = TypeVar("T_co", covariant=True)
ScreenResultType = TypeVar("ScreenResultType")

ComposeResult = Iterator[Widget]

class AwaitMount:
    """Result of a mount operation."""

    def __await__(self) -> Any:
        """Make the class awaitable."""
        ...

class App(Protocol[T_co]):
    """Base application class."""

    notification_center: Any

    async def on_mount(self) -> None:
        """Handle application mount event."""
        ...

    def run(self) -> None:
        """Run the application."""
        ...

    async def mount(self, *widgets: Widget) -> None:
        """Mount widgets.

        Args:
            *widgets: Widgets to mount.
        """
        ...

    def push_screen(
        self,
        screen: Screen[ScreenResultType],
        callback: (
            Callable[[ScreenResultType | None], None]
            | Callable[[ScreenResultType | None], Awaitable[None]]
            | None
        ) = None,
        wait_for_dismiss: bool = False,
    ) -> AwaitMount | Awaitable[ScreenResultType]:
        """Push a screen onto the screen stack.

        Args:
            screen: Screen to push onto the stack.
            callback: Optional callback to execute when screen is dismissed.
            wait_for_dismiss: Whether to wait for screen dismissal.

        Returns:
            The await mount result if not waiting for dismissal,
            or a Future if waiting.
        """
        ...

    def pop_screen(self) -> AwaitMount:
        """Pop a screen from the screen stack.

        Returns:
            The await mount result.
        """
        ...
