"""Notification system for TUI applications."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import TYPE_CHECKING, Literal

import structlog
from rich.text import Text
from textual.containers import Container
from textual.widgets import Static

from .base import EventData, PepperWidget

if TYPE_CHECKING:
    from textual.app import ComposeResult


logger = structlog.get_logger(__name__)


@dataclass
class Notification:
    """Notification message configuration.

    Attributes:
        message (str): Notification message
        type (str): Message type (info, warning, error)
        timestamp (datetime): Creation timestamp
        duration (Optional[float]): Display duration in seconds

    """

    message: str
    type: Literal["info", "warning", "error"] = "info"
    timestamp: datetime = field(default_factory=datetime.now)
    duration: float | None = 5.0


class NotificationWidget(PepperWidget, Static):
    """Widget for displaying a single notification.

    Attributes:
        notification (Notification): Notification to display

    """

    DEFAULT_CSS = """
    $primary: #bd93f9;
    $secondary: #6272a4;
    $accent: #ff79c6;
    $background: #282a36;
    $text: #f8f8f2;
    $error: #ff5555;
    $warning: #ffb86c;
    $success: #50fa7b;
    $info: #8be9fd;
    $selection: #44475a;

    NotificationWidget {
        padding: 1 2;
        margin: 1 0;
        border: solid $primary;
    }

    NotificationWidget.-info {
        border: solid $info;
    }

    NotificationWidget.-warning {
        border: solid $warning;
    }

    NotificationWidget.-error {
        border: solid $error;
    }
    """

    def __init__(
        self,
        *args: tuple[()],
        notification: Notification,
        **kwargs: dict[str, EventData],
    ) -> None:
        """Initialize the notification widget.

        Args:
            notification: The notification to display.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self.notification = notification
        self.add_class(f"-{notification.type}")

    def render(self) -> Text:
        """Render the notification.

        Returns:
            Text: Rich text representation

        """
        style = {"info": "blue", "warning": "yellow", "error": "red"}.get(
            self.notification.type,
            "white",
        )

        return Text.assemble(
            (f"[{self.notification.timestamp.strftime('%H:%M:%S')}] ", "dim"),
            (self.notification.message, style),
        )


class NotificationCenter(PepperWidget, Container):
    """Notification center for managing multiple notifications.

    Attributes:
        max_notifications (int): Maximum number of visible notifications
        notifications (List[Notification]): Active notifications

    """

    DEFAULT_CSS = """
    $primary: #bd93f9;
    $secondary: #6272a4;
    $accent: #ff79c6;
    $background: #282a36;
    $text: #f8f8f2;
    $error: #ff5555;
    $warning: #ffb86c;
    $success: #50fa7b;
    $info: #8be9fd;
    $selection: #44475a;

    NotificationCenter {
        dock: bottom;
        layer: notification;
        width: 100%;
        margin: 2 4;
    }
    """

    def __init__(
        self,
        *args: tuple[()],
        max_notifications: int = 5,
        **kwargs: dict[str, EventData],
    ) -> None:
        """Initialize the notification center.

        Args:
            max_notifications: The maximum number of notifications to display.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        """
        super().__init__(*args, **kwargs)
        self.max_notifications = max_notifications
        self.notifications: list[Notification] = []

    def compose(self) -> ComposeResult:
        """Compose the notification center layout."""
        for notification in reversed(self.notifications):
            yield NotificationWidget(notification=notification)

    def notify(
        self,
        message: str,
        *,
        title: str = "",  # Required by Widget interface
        severity: Literal["information", "warning", "error"] = "information",
        timeout: float | None = None,
    ) -> None:
        """Show a notification.

        Args:
            message: Notification message
            title: Optional notification title (required by Widget interface)
            severity: Message severity
            timeout: Optional display timeout

        """
        # Map severity to notification type
        notification_type: Literal["info", "warning", "error"]
        if severity == "information":
            notification_type = "info"
        elif severity == "warning":
            notification_type = "warning"
        else:
            notification_type = "error"

        notification = Notification(
            message=message,
            type=notification_type,
            duration=timeout,
        )
        self.notifications.append(notification)

        # Remove old notifications if over limit
        while len(self.notifications) > self.max_notifications:
            self.notifications.pop(0)

        # Refresh notifications synchronously
        self.query("NotificationWidget").remove()
        for notification in self.notifications:
            self.mount(NotificationWidget(notification=notification))

    async def remove_notification(self, notification: Notification) -> None:
        """Remove a notification.

        Args:
            notification: Notification to remove

        """
        if notification in self.notifications:
            self.notifications.remove(notification)
            await self.refresh_notifications()

    async def refresh_notifications(self) -> None:
        """Refresh the notification display."""
        self.query("NotificationWidget").remove()
        for notification in self.notifications:
            self.mount(NotificationWidget(notification=notification))

    def clear_all(self) -> None:
        """Clear all notifications."""
        self.notifications.clear()
        self.remove_children()
