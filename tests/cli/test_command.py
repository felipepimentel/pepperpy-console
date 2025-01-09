"""Tests for the CLI command system."""

import pytest

from pepperpy_console.cli.command import Command, CommandGroup


@pytest.mark.asyncio
async def test_command_creation():
    """Test that a command can be created with all attributes."""

    async def callback():
        return "test"

    command = Command(
        name="test",
        callback=callback,
        description="Test command",
        aliases=["t", "tst"],
    )
    assert command.name == "test"
    assert command.description == "Test command"
    assert command.callback == callback
    assert command.aliases == ["t", "tst"]


@pytest.mark.asyncio
async def test_command_execution():
    """Test that a command can be executed with arguments."""

    async def callback(*args, **kwargs):
        return args, kwargs

    command = Command(name="test", callback=callback)
    result = await command.execute("arg1", "arg2", kwarg1="value1")
    args, kwargs = result
    assert args == ("arg1", "arg2")
    assert kwargs == {"kwarg1": "value1"}


@pytest.mark.asyncio
async def test_command_group():
    """Test command group functionality."""

    async def callback():
        return "test"

    group = CommandGroup()
    command = Command(name="test", callback=callback, aliases=["t"])

    group.add_command(command)

    assert group.get_command("test") == command
    assert group.get_command("t") == command
    assert group.get_command("nonexistent") is None


@pytest.mark.asyncio
async def test_command_group_multiple_commands():
    """Test command group with multiple commands."""

    async def callback1():
        return "test1"

    async def callback2():
        return "test2"

    group = CommandGroup()
    command1 = Command(name="test1", callback=callback1)
    command2 = Command(name="test2", callback=callback2)

    group.add_command(command1)
    group.add_command(command2)

    assert group.get_command("test1") == command1
    assert group.get_command("test2") == command2
