# Installation

This guide will help you install PepperPy Console and get started with development.

## Requirements

- Python 3.8 or higher
- pip or Poetry for package management

## Installation Methods

### Using pip

The simplest way to install PepperPy Console is using pip:

```bash
pip install pepperpy-console
```

### Using Poetry

If you prefer using Poetry for dependency management:

```bash
poetry add pepperpy-console
```

## Development Installation

For development, you'll want to clone the repository and install in editable mode:

1. Clone the repository:
```bash
git clone https://github.com/yourusername/pepperpy-console.git
cd pepperpy-console
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Install pre-commit hooks:
```bash
poetry run pre-commit install
```

## Optional Dependencies

PepperPy Console has several optional dependencies for additional features:

### Development Tools
```bash
poetry install --with dev
```

### Documentation Tools
```bash
poetry install --with docs
```

### Testing Tools
```bash
poetry install --with test
```

## Verifying Installation

You can verify your installation by running:

```bash
python -c "import pepperpy; print(pepperpy.__version__)"
```

## Platform Support

PepperPy Console is tested on:

- Linux (Ubuntu, Debian, CentOS)
- macOS (10.15+)
- Windows 10/11

## Troubleshooting

### Common Issues

1. **Poetry installation fails**
   - Ensure you have Python 3.8+
   - Try updating pip: `python -m pip install --upgrade pip`
   - Check Poetry installation guide: [poetry.eustace.io](https://python-poetry.org/docs/)

2. **Import errors**
   - Verify virtual environment is activated
   - Check Python path: `which python`
   - Reinstall package: `pip install --force-reinstall pepperpy-console`

3. **Version conflicts**
   - Use Poetry to resolve dependencies: `poetry update`
   - Check requirements: `poetry show --tree`

### Getting Help

If you encounter issues:

1. Check our [FAQ](https://pepperpy-console.readthedocs.io/en/latest/faq/)
2. Search [GitHub Issues](https://github.com/yourusername/pepperpy-console/issues)
3. Join our [Discord community](https://discord.gg/pepperpy)
4. Open a new issue with:
   - Python version
   - Installation method
   - Error message
   - Steps to reproduce 