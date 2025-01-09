"""Tests for the Pepper console application."""

import pytest

from .mocks import PepperApp


@pytest.mark.asyncio
async def test_app_initialization():
    """Test that the app can be initialized with all components."""
    app = PepperApp()
    assert hasattr(app, "commands")
    assert hasattr(app, "parser")
    assert hasattr(app, "theme_manager")
    assert app.last_command is None


@pytest.mark.asyncio
async def test_app_command_registration():
    """Test that the app can register commands."""
    app = PepperApp()

    async def test_callback():
        return "test"

    app.register_command(
        name="test",
        callback=test_callback,
        description="Test command",
        aliases=["t"],
    )

    command = app.commands.get_command("test")
    assert command is not None
    assert command.name == "test"
    assert command.description == "Test command"
    assert command.callback == test_callback
    assert command.aliases == ["t"]

    # Check alias works
    alias_command = app.commands.get_command("t")
    assert alias_command == command


@pytest.mark.asyncio
async def test_app_command_processing():
    """Test that the app can process commands."""
    app = PepperApp()
    executed = False

    async def test_callback(**kwargs):
        nonlocal executed
        executed = True
        return kwargs

    app.register_command(name="test", callback=test_callback)
    await app.process_command("test arg1 arg2")

    assert executed
    assert app.last_command == {"name": "test", "args": {"args": ["arg1", "arg2"]}}


@pytest.mark.asyncio
async def test_app_invalid_command():
    """Test that the app handles invalid commands gracefully."""
    app = PepperApp()
    await app.process_command("nonexistent")
    assert app.last_command is None

    # Empty or whitespace commands
    await app.process_command("")
    assert app.last_command is None

    await app.process_command("   ")
    assert app.last_command is None
