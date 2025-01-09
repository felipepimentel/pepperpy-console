"""Tests for the TUI application."""

from pathlib import Path
import pytest
from unittest.mock import AsyncMock

from pepperpy_console.tui.app import PepperApp
from pepperpy_console.tui.screens import PepperScreen


@pytest.fixture
def app():
    """Create a PepperApp instance for testing."""
    return PepperApp()


@pytest.mark.asyncio
async def test_app_initialization(app):
    """Test that the application can be initialized."""
    assert app.screen_map == {}
    assert app.themes is not None
    assert app.keyboard is not None
    assert app.commands is not None
    assert app.help is not None
    assert app.plugins is not None


@pytest.mark.asyncio
async def test_app_screen_management(app):
    """Test screen management."""

    # Create a test screen
    class TestScreen(PepperScreen):
        pass

    # Add screen to map
    app.screen_map["test"] = TestScreen

    # Show loading screen
    await app.show_loading("Test loading")
    assert app.screen is not None


@pytest.mark.asyncio
async def test_app_plugin_loading(app):
    """Test plugin loading."""
    # Create a test plugin directory
    plugin_dir = Path(__file__).parent / "test_plugins"
    plugin_dir.mkdir(exist_ok=True)

    # Test loading plugins
    mock_load = AsyncMock()
    app.plugins.load_plugins = mock_load
    await app.load_plugins(plugin_dir)
    mock_load.assert_called_once_with(plugin_dir)


@pytest.mark.asyncio
async def test_app_theme_loading(app):
    """Test theme loading."""
    # Load themes from the themes directory
    themes_dir = Path(__file__).parent.parent.parent / "pepperpy_console" / "themes"
    await app.load_themes(themes_dir)
