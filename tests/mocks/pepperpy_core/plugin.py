"""Mock plugin module for pepperpy-core."""

from dataclasses import dataclass
from typing import Any, Callable, Dict, List, Optional


@dataclass
class PluginConfig:
    """Mock plugin configuration."""

    name: str
    version: str
    description: str
    requires: List[str]
    hooks: List[str]
    settings: Dict[str, Any]


class Plugin:
    """Mock plugin base class."""

    def __init__(self) -> None:
        """Initialize the plugin."""
        self.config = None
        self.app = None

    def configure(self) -> PluginConfig:
        """Configure the plugin."""
        raise NotImplementedError

    async def initialize(self) -> None:
        """Initialize the plugin."""
        pass

    async def cleanup(self) -> None:
        """Clean up plugin resources."""
        pass

    @staticmethod
    def hook(event: str) -> Callable:
        """Register a hook handler."""

        def decorator(func: Callable) -> Callable:
            return func

        return decorator


class PluginManager:
    """Mock plugin manager."""

    def __init__(self) -> None:
        """Initialize the plugin manager."""
        self.plugins: Dict[str, Plugin] = {}

    async def load_plugins(self, directory: str) -> None:
        """Mock loading plugins."""
        pass

    def get_plugin(self, name: str) -> Optional[Plugin]:
        """Get a plugin by name."""
        return self.plugins.get(name)


# Export plugin as a module-level variable
plugin = Plugin
