"""Tests for the screen system."""

import pytest
from textual.widgets import Static

from pepperpy_console.tui.screens import PepperScreen, LoadingScreen


@pytest.mark.asyncio
async def test_pepper_screen_compose():
    """Test that a base screen can compose its layout."""
    screen = PepperScreen()
    widgets = [w async for w in screen.compose()]
    assert len(widgets) == 1
    assert isinstance(widgets[0], Static)
    assert widgets[0].renderable == "Base PepperPy Screen"


@pytest.mark.asyncio
async def test_loading_screen_initialization():
    """Test that a loading screen can be initialized with a custom message."""
    screen = LoadingScreen(message="Custom loading message")
    assert screen.message == "Custom loading message"


@pytest.mark.asyncio
async def test_loading_screen_compose():
    """Test that a loading screen can compose its layout."""
    screen = LoadingScreen(message="Test loading")
    widgets = [w async for w in screen.compose()]
    assert len(widgets) == 2
    assert isinstance(widgets[0], Static)
    assert widgets[0].renderable == "Test loading"
