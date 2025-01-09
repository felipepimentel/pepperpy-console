"""Tests for the CLI parser."""

import pytest

from pepperpy_console.cli.parser import CommandParser


@pytest.mark.asyncio
async def test_command_parser_initialization():
    """Test that the command parser can be initialized."""
    parser = CommandParser()
    assert parser is not None


@pytest.mark.asyncio
async def test_command_parser_empty_input():
    """Test that the parser returns None for empty input."""
    parser = CommandParser()
    result = await parser.parse("")
    assert result is None


@pytest.mark.asyncio
async def test_command_parser_whitespace():
    """Test that the parser returns None for whitespace input."""
    parser = CommandParser()
    result = await parser.parse("   ")
    assert result is None


@pytest.mark.asyncio
async def test_command_parser_simple_command():
    """Test that the parser correctly parses a simple command."""
    parser = CommandParser()
    result = await parser.parse("test")
    assert result is not None
    command_name, args = result
    assert command_name == "test"
    assert args == {}


@pytest.mark.asyncio
async def test_command_parser_with_arguments():
    """Test that the parser correctly parses a command with arguments."""
    parser = CommandParser()
    result = await parser.parse("test arg1 arg2")
    assert result is not None
    command_name, args = result
    assert command_name == "test"
    assert args == {"args": ["arg1", "arg2"]}
