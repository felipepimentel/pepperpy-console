"""Tests for the theme system."""

from pathlib import Path
import pytest

from pepperpy_console.tui.theme import Theme, ThemeManager


@pytest.mark.asyncio
async def test_theme_creation():
    """Test that a theme can be created with all attributes."""
    theme = Theme(
        name="test",
        colors={"primary": "#000000"},
        styles={"button": {"color": "primary"}},
    )
    assert theme.name == "test"
    assert theme.colors == {"primary": "#000000"}
    assert theme.styles == {"button": {"color": "primary"}}


@pytest.mark.asyncio
async def test_theme_loading():
    """Test that a theme can be loaded from a file."""
    path = Path("themes/test.yaml")
    theme = await Theme.load(path)
    assert theme.name == "test"
    assert "primary" in theme.colors
    assert "button" in theme.styles


@pytest.mark.asyncio
async def test_theme_manager_initialization():
    """Test that the theme manager can be initialized."""
    manager = ThemeManager()
    assert manager.themes == {}
    assert manager.current_theme is None


@pytest.mark.asyncio
async def test_theme_manager_loading():
    """Test that the theme manager can load themes."""
    manager = ThemeManager()
    path = Path("themes/test.yaml")
    theme = await manager.load_theme(path)
    assert theme.name == "test"
    assert theme == manager.themes[theme.name]


@pytest.mark.asyncio
async def test_theme_manager_setting():
    """Test that the theme manager can set themes."""
    manager = ThemeManager()
    path = Path("themes/test.yaml")
    theme = await manager.load_theme(path)
    manager.set_theme(theme.name)
    assert manager.current_theme == theme


@pytest.mark.asyncio
async def test_theme_manager_getting():
    """Test that the theme manager can get themes."""
    manager = ThemeManager()
    path = Path("themes/test.yaml")
    theme = await manager.load_theme(path)
    assert manager.get_theme(theme.name) == theme
