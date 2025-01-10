# Theme System

PepperPy Console includes a powerful theme system that allows you to customize the appearance of your application. Themes are defined in YAML files and can be switched at runtime.

## Theme Structure

Themes are defined using YAML files with the following structure:

```yaml
name: theme_name
colors:
  primary: "#color_code"
  secondary: "#color_code"
  accent: "#color_code"
  background: "#color_code"
  text: "#color_code"
  error: "#color_code"
  warning: "#color_code"
  success: "#color_code"
styles:
  component_name:
    property: value
    nested_property:
      sub_property: value
```

## Built-in Themes

PepperPy Console comes with several built-in themes:

### Light Theme

```yaml
name: light
colors:
  primary: "#000000"
  secondary: "#ffffff"
  accent: "#0066cc"
  background: "#f5f5f5"
  text: "#333333"
  error: "#ff0000"
  warning: "#ffa500"
  success: "#00ff00"
```

### Dark Theme (Dracula)

```yaml
name: dracula
colors:
  primary: "#bd93f9"
  secondary: "#44475a"
  accent: "#ff79c6"
  background: "#282a36"
  text: "#f8f8f2"
  error: "#ff5555"
  warning: "#ffb86c"
  success: "#50fa7b"
```

### High Contrast

```yaml
name: high_contrast
colors:
  primary: "#ffffff"
  secondary: "#000000"
  accent: "#ffff00"
  background: "#000000"
  text: "#ffffff"
  error: "#ff0000"
  warning: "#ffff00"
  success: "#00ff00"
```

## Using Themes

### Loading Themes

```python
from pepperpy_console import ThemeManager
from pathlib import Path

# Initialize theme manager
theme_manager = ThemeManager()

# Load themes from a directory
await theme_manager.load_themes(Path("themes"))

# Load a single theme
theme = await theme_manager.load_theme(Path("themes/custom.yaml"))
```

### Setting Active Theme

```python
# Set theme by name
theme_manager.set_theme("dracula")

# Get current theme
current_theme = theme_manager.current_theme
```

### Accessing Theme Properties

```python
# Get a theme by name
theme = theme_manager.get_theme("light")

# Access colors
primary_color = theme.colors["primary"]

# Access styles
button_style = theme.styles["button"]
```

## Creating Custom Themes

### Basic Theme

```yaml
name: my_theme
colors:
  primary: "#4a90e2"
  secondary: "#f5f5f5"
  accent: "#ff6b6b"
  background: "#ffffff"
  text: "#333333"
styles:
  button:
    color: primary
    background: secondary
    hover:
      background: accent
  text:
    color: text
```

### Theme with Metrics

```yaml
name: my_theme
colors:
  # ... color definitions ...
metrics:
  spacing:
    xs: 1
    sm: 2
    md: 4
    lg: 8
    xl: 16
  sizes:
    icon: 1
    input: 3
    header: 3
styles:
  # ... style definitions ...
```

## Best Practices

1. **Color Management**
   - Use semantic color names (e.g., primary, secondary)
   - Maintain consistent color relationships
   - Consider accessibility (contrast ratios)

2. **Style Organization**
   - Group related styles together
   - Use consistent naming conventions
   - Document style purposes

3. **Theme Switching**
   - Test theme changes at runtime
   - Provide smooth transitions
   - Handle theme loading errors

4. **Customization**
   - Allow component-level theme overrides
   - Support dynamic theme updates
   - Provide theme extension points

## Example: Complete Theme File

```yaml
name: corporate
colors:
  # Brand colors
  primary: "#0066cc"
  secondary: "#f8f9fa"
  accent: "#ff4081"
  
  # UI colors
  background: "#ffffff"
  surface: "#f5f5f5"
  text: "#212529"
  
  # State colors
  error: "#dc3545"
  warning: "#ffc107"
  success: "#28a745"
  info: "#17a2b8"

metrics:
  spacing:
    xs: 1
    sm: 2
    md: 4
    lg: 8
    xl: 16

  sizes:
    icon: 1
    input: 3
    header: 3
    footer: 3
    sidebar: 30

styles:
  # Button styles
  button:
    color: text
    background: primary
    padding: md
    hover:
      background: accent
    disabled:
      background: secondary
      color: text

  # Text styles
  text:
    color: text
    size: md
    
  heading:
    color: primary
    size: lg
    weight: bold

  # Input styles
  input:
    color: text
    background: surface
    border: primary
    focus:
      border: accent

  # Layout styles
  container:
    padding: lg
    background: background
```

## Theme Migration

When updating themes or switching between themes, consider:

1. **Backward Compatibility**
   - Maintain support for existing theme properties
   - Provide fallback values
   - Document deprecated properties

2. **Theme Validation**
   - Verify required colors and styles
   - Check color format validity
   - Validate style property types

3. **Migration Path**
   - Create theme conversion utilities
   - Document breaking changes
   - Provide migration guides 