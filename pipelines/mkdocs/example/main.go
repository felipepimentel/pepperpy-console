package main

import (
	"context"
	"fmt"
	"os"

	"dagger.io/dagger"
)

func main() {
	ctx := context.Background()

	// Initialize Dagger client
	client, err := dagger.Connect(ctx, dagger.WithLogOutput(os.Stdout))
	if err != nil {
		panic(err)
	}
	defer client.Close()

	// Get source directory
	source := client.Host().Directory(".")

	// Create new MkDocs module
	mkdocs := New(source)

	// Customize configuration if needed
	mkdocs.PythonVersion = "3.11"
	mkdocs.Plugins = append(mkdocs.Plugins, "mkdocs-awesome-pages-plugin")

	// Build documentation
	siteDir, err := mkdocs.Build(ctx)
	if err != nil {
		panic(err)
	}

	// Export the built site
	if err := siteDir.Export(ctx, "site"); err != nil {
		panic(err)
	}

	// Deploy to GitHub Pages if token is available
	if token := os.Getenv("GITHUB_TOKEN"); token != "" {
		if err := mkdocs.DeployToGitHubPages(ctx, token); err != nil {
			panic(err)
		}
	}
} 