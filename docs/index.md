# PepperPy Console Documentation

Welcome to the PepperPy Console documentation! This documentation will help you understand and use the PepperPy Console library effectively.

## Overview

PepperPy Console is a powerful Python library for building text-based user interfaces (TUI) with a focus on extensibility and ease of use. It provides:

- A robust CLI system with command and plugin support
- A flexible TUI framework built on top of Textual
- Theme management for customizable appearances
- Event system for handling user interactions
- Plugin architecture for extending functionality

## Quick Start

### Installation

```bash
pip install pepperpy-console
```

### Basic Usage

```python
from pepperpy_console import PepperApp

class MyApp(PepperApp):
    def compose(self):
        yield Static("Hello, PepperPy!")

app = MyApp()
app.run()
```

## Documentation Sections

- [CLI System](cli/index.md) - Command-line interface components
- [TUI Framework](tui/index.md) - Text user interface components
- [Theme System](themes/index.md) - Theme management and customization
- [Examples](examples/index.md) - Code examples and tutorials
- [API Reference](api/index.md) - Detailed API documentation

## Features

- **Modular Architecture**: Built with extensibility in mind
- **Theme Support**: Customizable appearance with theme files
- **Plugin System**: Easy to extend with custom plugins
- **Event Handling**: Robust event system for user interactions
- **Type Safety**: Full type hints support
- **Async Support**: Built with asyncio for modern Python applications

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 