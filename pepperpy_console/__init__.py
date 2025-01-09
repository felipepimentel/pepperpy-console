"""PepperPy Console - TUI and CLI capabilities for PepperPy applications."""

from pepperpy_core.plugin import PluginConfig
from pepperpy_core.plugin import plugin as Plugin

from .cli.command import Command as CLICommand
from .cli.command import CommandGroup
from .cli.parser import ArgumentParser, ArgumentSpec
from .tui.app import PepperApp
from .tui.commands import Command, CommandPalette
from .tui.help import HelpSection, HelpViewer
from .tui.keyboard import KeyBinding, KeyboardManager
from .tui.screens import ErrorScreen, LoadingScreen, PepperScreen
from .tui.theme import Theme, ThemeColors, ThemeManager, ThemeMetrics
from .tui.widgets import (
    AlertDialog,
    ConfirmDialog,
    Dialog,
    FormField,
    ModelInput,
    Navigation,
    Notification,
    NotificationCenter,
    PepperForm,
    PepperTable,
    Progress,
    SpinnerProgress,
    ValidatedInput,
)
from .tui.widgets.base import PepperWidget

__version__ = "0.0.1"

__all__ = [
    # TUI Components
    "PepperApp",
    "PepperScreen",
    "LoadingScreen",
    "ErrorScreen",
    "PepperWidget",
    "ValidatedInput",
    "ModelInput",
    "PepperTable",
    "Column",
    "PepperForm",
    "FormField",
    "Navigation",
    "MenuItem",
    "Progress",
    "SpinnerProgress",
    "NotificationCenter",
    "Notification",
    "Dialog",
    "ConfirmDialog",
    "AlertDialog",
    # Feature Systems
    "KeyboardManager",
    "KeyBinding",
    "ThemeManager",
    "Theme",
    "ThemeColors",
    "ThemeMetrics",
    "CommandPalette",
    "Command",
    "HelpViewer",
    "HelpSection",
    # CLI Components
    "CLICommand",
    "CommandGroup",
    "ArgumentParser",
    "ArgumentSpec",
    # Plugin System (from pepperpy-core)
    "Plugin",
    "PluginConfig",
]
