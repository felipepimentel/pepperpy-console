"""Tests for the theme management system."""

from tests.mocks.pepperpy_console.theme import ThemeManager


def test_theme_registration():
    """Test that themes can be registered and retrieved."""
    manager = ThemeManager()
    theme = manager.register_theme("test", {"color": "red"})

    assert theme.name == "test"
    assert theme.styles == {"color": "red"}
    assert not theme.active

    retrieved = manager.get_theme("test")
    assert retrieved == theme


def test_theme_activation():
    """Test that themes can be activated and deactivated."""
    manager = ThemeManager()
    theme1 = manager.register_theme("theme1")
    theme2 = manager.register_theme("theme2")

    # Activate first theme
    assert manager.activate_theme("theme1")
    assert theme1.active
    assert not theme2.active
    assert manager.get_active_theme() == theme1

    # Activate second theme
    assert manager.activate_theme("theme2")
    assert not theme1.active
    assert theme2.active
    assert manager.get_active_theme() == theme2


def test_theme_listing():
    """Test that themes can be listed."""
    manager = ThemeManager()
    manager.register_theme("theme1")
    manager.register_theme("theme2")
    manager.register_theme("theme3")

    themes = manager.list_themes()
    assert len(themes) == 3
    assert "theme1" in themes
    assert "theme2" in themes
    assert "theme3" in themes


def test_invalid_theme_activation():
    """Test that activating an invalid theme fails gracefully."""
    manager = ThemeManager()
    theme = manager.register_theme("test")
    manager.activate_theme("test")

    # Try to activate non-existent theme
    assert not manager.activate_theme("nonexistent")
    assert theme.active
    assert manager.get_active_theme() == theme


def test_theme_styles():
    """Test that theme styles are properly managed."""
    manager = ThemeManager()
    styles = {
        "background": "black",
        "foreground": "white",
        "accent": "blue",
    }
    theme = manager.register_theme("test", styles)

    assert theme.styles == styles
    for key, value in styles.items():
        assert theme.styles[key] == value
