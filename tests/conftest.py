"""Test configuration and fixtures."""

import asyncio
from typing import AsyncGenerator

import pytest
from pytest_asyncio import fixture

from tests.mocks.pepperpy_console import PepperApp, PepperCommandSystem, PepperWidget
from tests.mocks.pepperpy_console.theme import ThemeManager
from tests.mocks.textual import MockApp, MockScreen, MockWidget


# Configure pytest-asyncio to use function scope for event_loop by default
def pytest_configure(config):
    """Configure pytest-asyncio."""
    config.addinivalue_line(
        "markers",
        "asyncio: mark test as requiring asyncio event loop",
    )


@pytest.fixture
def command_system() -> PepperCommandSystem:
    """Provide a command system instance."""
    return PepperCommandSystem()


@fixture
async def theme_manager() -> AsyncGenerator[ThemeManager, None]:
    """Provide a theme manager instance."""
    manager = ThemeManager()
    yield manager


@pytest.fixture
def mock_app() -> MockApp:
    """Provide a mock Textual app instance."""
    return MockApp()


@pytest.fixture
def mock_screen() -> MockScreen:
    """Provide a mock Textual screen instance."""
    return MockScreen()


@pytest.fixture
def mock_widget() -> MockWidget:
    """Provide a mock Textual widget instance."""
    return MockWidget()


@pytest.fixture
def pepper_app() -> PepperApp:
    """Provide a PepperApp instance."""
    return PepperApp()


@pytest.fixture
def pepper_widget() -> PepperWidget:
    """Provide a PepperWidget instance."""
    return PepperWidget()
