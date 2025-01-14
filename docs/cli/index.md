# CLI System

The CLI (Command Line Interface) system in PepperPy Console provides a flexible way to create and manage commands. It includes support for command groups, aliases, and plugins.

## Components

### Command

The `Command` class represents a single command that can be executed. Each command has:

- A name
- A callback function (async)
- An optional description
- Optional aliases

```python
from pepperpy import Command

async def my_command(arg1, arg2):
    return f"Processing {arg1} and {arg2}"

cmd = Command(
    name="process",
    callback=my_command,
    description="Process two arguments",
    aliases=["proc", "p"]
)

# Execute the command
result = await cmd.execute("value1", "value2")
```

### Command Group

The `CommandGroup` class allows you to organize related commands together:

```python
from pepperpy import Command, CommandGroup

group = CommandGroup()

# Add commands to the group
group.add_command(cmd1)
group.add_command(cmd2)

# Get a command by name
command = group.get_command("process")

# List all commands
commands = group.list_commands()
```

### Command Parser

The `CommandParser` class handles parsing command strings into executable commands:

```python
from pepperpy import CommandParser

parser = CommandParser()

# Parse a command string
result = await parser.parse("process arg1 arg2")
if result:
    command_name, args = result
    # command_name = "process"
    # args = {"args": ["arg1", "arg2"]}
```

## Plugin System

The CLI system includes a plugin architecture for extending functionality:

```python
from pepperpy import Plugin, PluginManager
from pathlib import Path

# Create a plugin
class MyPlugin(Plugin):
    def __init__(self, name: str):
        super().__init__(name)
        # Add custom commands
        self.commands["my_command"] = Command(...)

# Use the plugin manager
manager = PluginManager()
await manager.load_plugins(Path("plugins"))

# Get a plugin
plugin = manager.get_plugin("my_plugin")
```

## Best Practices

1. **Async Commands**: Always use async functions for command callbacks
2. **Type Hints**: Use type hints for command parameters
3. **Documentation**: Provide clear descriptions for commands
4. **Error Handling**: Handle command errors gracefully
5. **Validation**: Validate command arguments before execution

## Example: Building a CLI Application

Here's a complete example of building a CLI application:

```python
from pepperpy import PepperApp, Command, CommandGroup

class MyApp(PepperApp):
    def __init__(self):
        super().__init__()
        self.setup_commands()

    def setup_commands(self):
        # Create commands
        async def hello(name: str):
            return f"Hello, {name}!"

        async def goodbye(name: str):
            return f"Goodbye, {name}!"

        # Add commands to the app
        self.commands.add_command(Command(
            name="hello",
            callback=hello,
            description="Say hello"
        ))

        self.commands.add_command(Command(
            name="goodbye",
            callback=goodbye,
            description="Say goodbye"
        ))

app = MyApp()
app.run()
```

## Advanced Topics

### Custom Command Arguments

You can create commands with custom argument parsing:

```python
async def custom_command(*args, **kwargs):
    # Access raw arguments
    positional_args = args
    keyword_args = kwargs
    return "Command executed"

cmd = Command(
    name="custom",
    callback=custom_command,
    description="Command with custom arguments"
)
```

### Command Middleware

You can implement middleware for commands using Python decorators:

```python
def require_auth(f):
    async def wrapper(*args, **kwargs):
        # Add authentication logic here
        return await f(*args, **kwargs)
    return wrapper

@require_auth
async def protected_command():
    return "Access granted"
```

### Error Handling

Implement proper error handling in your commands:

```python
async def safe_command(*args):
    try:
        # Command logic here
        result = process_args(*args)
        return result
    except ValueError as e:
        return f"Invalid input: {e}"
    except Exception as e:
        return f"Error: {e}"
``` 