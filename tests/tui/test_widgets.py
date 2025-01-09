"""Tests for the TUI widgets."""

import pytest

from pepperpy_console.tui.widgets.base import PepperWidget


@pytest.mark.asyncio
async def test_widget_initialization():
    """Test that a widget can be initialized with event handling."""
    widget = PepperWidget()
    assert hasattr(widget, "events")


@pytest.mark.asyncio
async def test_widget_event_emission():
    """Test that a widget can emit events."""
    widget = PepperWidget()
    widget.emit_event("test_event", {"value": 42})
    assert len(widget.events) == 1
    assert widget.events[0]["type"] == "test_event"
    assert widget.events[0]["data"] == {"value": 42}


@pytest.mark.asyncio
async def test_widget_event_clearing():
    """Test that a widget can clear its events."""
    widget = PepperWidget()
    widget.emit_event("test_event1", {"value": 1})
    widget.emit_event("test_event2", {"value": 2})
    assert len(widget.events) == 2
    widget.clear_events()
    assert len(widget.events) == 0


@pytest.mark.asyncio
async def test_widget_multiple_events():
    """Test that a widget can handle multiple events."""
    widget = PepperWidget()

    # Emit multiple events
    widget.emit_event("event1", {"value": 1})
    widget.emit_event("event2", {"value": 2})
    widget.emit_event("event3", {"value": 3})

    assert len(widget.events) == 3
    assert widget.events[0]["type"] == "event1"
    assert widget.events[1]["type"] == "event2"
    assert widget.events[2]["type"] == "event3"
