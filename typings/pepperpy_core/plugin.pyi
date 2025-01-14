"""Type stubs for pepperpy_core plugin module."""

from typing import Any, Protocol

class PluginConfig:
    """Plugin configuration."""

    def __init__(self, name: str, plugin_dir: str) -> None:
        """Initialize plugin configuration.

        Args:
            name: Plugin name.
            plugin_dir: Plugin directory.

        """
        self.name = name
        self.plugin_dir = plugin_dir

class PluginProtocol(Protocol):
    """Protocol for plugin interface."""

    name: str
    version: str
    description: str

    async def initialize(self, app: Any) -> None:
        """Initialize the plugin.

        Args:
            app: The application instance.

        """
        ...

    async def cleanup(self) -> None:
        """Clean up plugin resources."""
        ...

class PluginManager:
    """Plugin manager."""

    def __init__(self, config: PluginConfig | None = None) -> None:
        """Initialize plugin manager.

        Args:
            config: Optional plugin configuration.

        """
        self.config = config

    async def initialize(self) -> None:
        """Initialize plugin manager."""
        ...

    async def register_plugin(self, plugin: PluginProtocol) -> None:
        """Register a plugin.

        Args:
            plugin: Plugin to register.

        """
        ...
