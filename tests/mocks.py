"""Mock classes for testing."""

from typing import Any, Callable, Dict, List


class MockEventManager:
    """Mock event manager for testing."""

    def __init__(self) -> None:
        """Initialize the mock event manager."""
        self.handlers: Dict[str, List[Callable]] = {}

    async def emit(self, event: str, data: Any = None) -> None:
        """Emit an event."""
        if event in self.handlers:
            for handler in self.handlers[event]:
                await handler(data)

    def on(self, event: str) -> Callable:
        """Register an event handler."""

        def decorator(func: Callable) -> Callable:
            if event not in self.handlers:
                self.handlers[event] = []
            self.handlers[event].append(func)
            return func

        return decorator


class MockPluginManager:
    """Mock plugin manager for testing."""

    def __init__(self) -> None:
        """Initialize the mock plugin manager."""
        self.plugins = {}

    async def load_plugins(self, directory: str) -> None:
        """Mock loading plugins."""
        pass
