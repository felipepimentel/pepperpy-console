# CHANGELOG


## v0.1.0 (2025-01-14)

### Chores

- Bump version to 0.2.1 in pyproject.toml
  ([`f6f424e`](https://github.com/felipepimentel/pepperpy-console/commit/f6f424eea718d98ad716a76bdc1f886819f9ab9e))

- Update dependencies and remove unused packages
  ([`b9962bf`](https://github.com/felipepimentel/pepperpy-console/commit/b9962bf5b8e71da1e8549e24cd0f26c73ebb5c79))

- Removed the `coverage` and `pytest-cov` packages from `poetry.lock`. - Updated `pepperpy-core`
  version to 0.2.1 and adjusted its dependencies, including `anyio` and `pydantic`. - Cleaned up the
  lock file by eliminating unnecessary entries and ensuring compatibility with Python 3.12.

### Features

- Add MkDocs Dagger module and reusable workflow
  ([`7bf25d3`](https://github.com/felipepimentel/pepperpy-console/commit/7bf25d372ebf015d843df619367dececa44e94dd))

### Refactoring

- Reorganize project structure from pepperpy_console to pepperpy
  ([`3b0444f`](https://github.com/felipepimentel/pepperpy-console/commit/3b0444f0b7e2852ca480ec2a6af9b009d1603a7a))


## v0.0.1 (2025-01-14)

### Bug Fixes

- Resolve linting and type checking issues
  ([`74ce56c`](https://github.com/felipepimentel/pepperpy-console/commit/74ce56c4be4be3b0e489474cd951161f90cc8325))

- Fix import sorting issues across multiple files

- Fix mypy type checking errors in tabs.py by using _sender attribute

- Update ruff configuration to handle imports better

### Chores

- Bump version to 0.2.1 in pyproject.toml
  ([`2fb1c7b`](https://github.com/felipepimentel/pepperpy-console/commit/2fb1c7b537c20a4a61cbad34b322797969502b7e))

- Update ruff and pytest-asyncio configurations
  ([`9e918d0`](https://github.com/felipepimentel/pepperpy-console/commit/9e918d03c173cebb42790909c460e32f14f0630a))

- Move ruff settings to lint section for better organization - Add
  asyncio_default_fixture_loop_scope configuration for pytest-asyncio

### Refactoring

- Improve container widgets and fix formatting
  ([`2a93e34`](https://github.com/felipepimentel/pepperpy-console/commit/2a93e34b8f5eed3981be91b423cba9d0be2106be))
