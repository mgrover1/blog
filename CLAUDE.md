# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Is

Max Grover's personal website and blog, built with MyST Markdown (mystmd) using the book-theme template. Deployed to GitHub Pages via GitHub Actions.

## Build Commands

- **Build site:** `myst build --html` (output in `_build/html/`)
- **Local preview (Sphinx):** `make live` (runs sphinx-autobuild on port 9999)
- **Install deps:** `uv pip install --system -r requirements.txt -r execute-requirements.txt`

## Architecture

**Site generator:** MyST Markdown (`myst.yml` is the primary config). There is a legacy Sphinx config (`conf.py`, `Makefile`) still present.

**Content structure:**
- `posts/` — Blog posts organized by year (2021-2025), written in `.md` or `.ipynb`
- Root `.md` files — Top-level pages (index, about, talks, workshops, media, blog)
- `config_data/` — YAML data files for talks and teaching galleries
- `_static/`, `_templates/` — Theme customization assets

**Custom plugins** (`src/`):
- `blogpost.py` — MyST executable plugin that provides a `postlist` directive (renders blog post cards) and generates RSS/Atom feeds (`rss.xml`, `atom.xml`)
- `socialpost.mjs` — Social post transform plugin
- `unist.py` — Helper for building unist AST nodes (used by blogpost.py)

**Blog post format:** Markdown files with YAML frontmatter (`title`, `date`, `author`, `tags`, `description`). Posts in `posts/drafts/` are excluded from the blog listing.

**TOC:** Defined in `myst.yml` using file patterns (e.g., `posts/2025/**{.ipynb,.md}`).

## CI/CD

GitHub Actions (`.github/workflows/deploy-site.yml`):
- Triggers on push to `main`, PRs, and manual dispatch
- Uses Python 3.12 + uv
- Builds with `myst build --html`, deploys to `gh-pages` branch on main pushes
