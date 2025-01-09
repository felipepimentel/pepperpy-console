"""Mock plugin module."""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional


@dataclass
class PluginConfig:
    """Mock plugin configuration."""

    name: str
    version: str
    description: str
    requires: List[str]
    hooks: List[str]
    settings: Dict[str, Any]


class MockPluginManager:
    """Mock plugin manager for testing."""

    def __init__(self) -> None:
        """Initialize the mock plugin manager."""
        self.plugins: Dict[str, Any] = {}

    async def load_plugins(self, directory: str) -> None:
        """Mock loading plugins."""
        pass

    def get_plugin(self, name: str) -> Optional[Any]:
        """Get a plugin by name."""
        return self.plugins.get(name)
