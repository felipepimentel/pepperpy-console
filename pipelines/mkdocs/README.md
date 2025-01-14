# MkDocs Dagger Module

A reusable Dagger module for building and deploying MkDocs documentation sites.

## Features

- Build MkDocs sites with Material theme
- Configurable Python version and plugins
- GitHub Pages deployment support
- Local testing support
- Caching for better performance

## Usage

1. Add this module to your project:

```bash
git clone https://github.com/felipepimentel/pepperpy-console.git
cp -r pepperpy-console/pipelines/mkdocs your-project/pipelines/
```

2. Use the reusable GitHub workflow:

```yaml
name: Deploy Docs
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  docs:
    uses: ./.github/workflows/docs.yml
    secrets:
      token: ${{ secrets.GITHUB_TOKEN }}
```

3. Or use the module directly in your Dagger pipeline:

```go
package main

import (
    "context"
    "os"
    "dagger.io/dagger"
)

func main() {
    ctx := context.Background()
    client, err := dagger.Connect(ctx)
    if err != nil {
        panic(err)
    }
    defer client.Close()

    source := client.Host().Directory(".")
    mkdocs := New(source)
    
    // Build and export
    siteDir, err := mkdocs.Build(ctx)
    if err != nil {
        panic(err)
    }
    
    if err := siteDir.Export(ctx, "site"); err != nil {
        panic(err)
    }
}
```

## Configuration

The module supports the following configuration options:

- `PythonVersion`: Python version to use (default: "3.11")
- `OutputDir`: Output directory for built site (default: "site")
- `Theme`: MkDocs theme to use (default: "material")
- `Plugins`: List of MkDocs plugins to install

## Requirements

- Go 1.21 or later
- Dagger CLI
- Docker 