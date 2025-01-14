package main

import (
	"context"
	"fmt"
	"path/filepath"

	"dagger.io/dagger"
)

type MkDocs struct {
	// Source directory containing mkdocs.yml and docs/
	Source *dagger.Directory

	// Python version to use
	PythonVersion string

	// Output directory for built site
	OutputDir string

	// Additional MkDocs plugins to install
	Plugins []string

	// Theme configuration
	Theme string
}

// Default configuration for MkDocs
func New(source *dagger.Directory) *MkDocs {
	return &MkDocs{
		Source:        source,
		PythonVersion: "3.11",
		OutputDir:     "site",
		Theme:         "material",
		Plugins: []string{
			"mkdocs-material",
			"mkdocs-minify-plugin",
			"mkdocs-git-revision-date-localized-plugin",
			"pillow",
			"cairosvg",
		},
	}
}

// Build the documentation site
func (m *MkDocs) Build(ctx context.Context) (*dagger.Directory, error) {
	client := dagger.Connect(ctx)
	defer client.Close()

	container := client.Container().
		From(fmt.Sprintf("python:%s-slim", m.PythonVersion)).
		WithDirectory("/src", m.Source).
		WithWorkdir("/src")

	// Install dependencies
	container = container.WithExec([]string{
		"pip", "install", "--no-cache-dir", "-U", "pip",
	})

	// Install MkDocs and plugins
	container = container.WithExec(append(
		[]string{"pip", "install", "--no-cache-dir"},
		m.Plugins...,
	))

	// Build the site
	container = container.WithExec([]string{
		"mkdocs", "build", "--site-dir", m.OutputDir,
	})

	return container.Directory(m.OutputDir), nil
}

// Deploy to GitHub Pages
func (m *MkDocs) DeployToGitHubPages(ctx context.Context, token string) error {
	client := dagger.Connect(ctx)
	defer client.Close()

	// First build the site
	siteDir, err := m.Build(ctx)
	if err != nil {
		return fmt.Errorf("failed to build site: %w", err)
	}

	// Deploy using gh-pages
	container := client.Container().
		From("node:slim").
		WithDirectory("/site", siteDir).
		WithWorkdir("/site").
		WithEnvVariable("GITHUB_TOKEN", token)

	// Install gh-pages
	container = container.WithExec([]string{
		"npm", "install", "-g", "gh-pages",
	})

	// Deploy
	container = container.WithExec([]string{
		"gh-pages",
		"--dist", ".",
		"--message", "Deploy documentation [skip ci]",
		"--dotfiles",
	})

	return nil
} 