# Contributing to PepperPy Console

Thank you for your interest in contributing to PepperPy Console! This document provides guidelines and instructions for contributing to the project.

## Development Setup

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

## Code Style

We follow strict code style guidelines to maintain consistency:

- Follow PEP 8 guidelines
- Use black for code formatting with line length of 88
- Use double quotes for strings
- Use type hints for all function parameters and return types
- Use async/await for I/O operations
- Follow the principle of least privilege

## Documentation

All code contributions should include appropriate documentation:

- Use Google-style docstrings
- Include type hints in docstrings
- Provide usage examples for complex functions
- Keep documentation up-to-date with code changes

Example:
```python
async def process_data(data: Dict[str, Any]) -> List[str]:
    """Process the input data and return a list of results.
    
    Args:
        data: A dictionary containing the data to process.
            Must include 'id' and 'value' keys.
            
    Returns:
        A list of processed string results.
        
    Raises:
        ValueError: If required keys are missing from data.
        
    Example:
        >>> data = {"id": "123", "value": "test"}
        >>> await process_data(data)
        ["123: test"]
    """
```

## Testing

All new features and bug fixes should include tests:

- Write unit tests using pytest
- Use pytest-asyncio for async tests
- Mock external dependencies
- Maintain test coverage above 80%
- Run tests before submitting PR:
```bash
poetry run pytest
```

## Git Workflow

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following our code style guidelines

3. Write tests for your changes

4. Run quality checks:
```bash
poetry run pytest
poetry run ruff check .
poetry run mypy .
```

5. Commit your changes following conventional commits:
```bash
git commit -m "feat: add new feature"
git commit -m "fix: resolve issue with..."
git commit -m "docs: update documentation"
```

6. Push your changes:
```bash
git push origin feature/your-feature-name
```

7. Create a Pull Request

## Pull Request Guidelines

When submitting a PR:

1. Fill out the PR template completely
2. Link any related issues
3. Ensure all tests pass
4. Maintain code coverage
5. Update documentation as needed
6. Add yourself to CONTRIBUTORS.md if not already there

## Issue Reporting

When creating an issue:

1. Use the issue template
2. Provide a clear description
3. Include steps to reproduce
4. Add relevant system information
5. Label the issue appropriately

## Security

- Never commit sensitive data
- Use environment variables for configuration
- Follow secure coding practices
- Report security issues privately

## Code Review

All code reviews should check for:

- Code style compliance
- Test coverage
- Documentation completeness
- Performance implications
- Security considerations
- Error handling

## Release Process

1. Update version in pyproject.toml
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Build and publish to PyPI

## Getting Help

- Join our Discord community
- Check the documentation
- Ask questions in GitHub Discussions
- Contact maintainers directly for security issues

## Project Structure

```
pepperpy-console/
├── docs/               # Documentation
├── pepperpy_console/   # Main package
│   ├── cli/           # CLI components
│   ├── tui/           # TUI components
│   ├── themes/        # Theme system
│   └── plugins/       # Plugin system
├── tests/             # Test suite
├── examples/          # Example code
└── scripts/           # Development scripts
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License. 