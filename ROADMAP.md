# Project XTC Publisher Roadmap

This document describes the planned evolution of Project XTC Publisher.

The roadmap is intentionally pragmatic. New features are only added when they support real publishing requirements rather than adding complexity for its own sake.

---

# Current Status

The project has reached the point where it can successfully produce the first chapters of **Project XTC – X-Touch Companion**.

Current capabilities include:

- Markdown manuscript
- YAML-based theme
- ReportLab PDF generation
- Headings and paragraphs
- Lists
- Block quotes
- Code blocks
- Callout directives
- Markdown tables
- Configurable typography
- Separation of content and presentation

---

# Version 0.1 — Foundation ✅

The initial objective was to prove the overall architecture.

Completed:

- ✓ Project structure
- ✓ Python publishing engine
- ✓ Markdown parser
- ✓ Document model
- ✓ YAML theme
- ✓ PDF renderer
- ✓ Basic manuscript support
- ✓ Callout blocks
- ✓ Table support
- ✓ Ruff formatting
- ✓ GitHub repository

This version establishes the foundation upon which all future development will build.

---

# Version 0.2 — Publishing Essentials

The next milestone focuses on producing a professional-quality technical book.

Planned:

- SVG diagram support
- Screenshots
- Figure captions
- Image scaling
- Automatic page breaks
- Better table formatting
- Improved typography
- Internal hyperlinks
- PDF metadata

The aim is that every feature should directly improve the published book.

---

# Version 0.3 — Intelligent Documents

This version introduces semantic features that make large manuscripts easier to maintain.

Planned:

- Cross references
- Automatic chapter numbering
- Automatic figure numbering
- Automatic table numbering
- Automatic table of contents
- Footnotes
- Bibliography support

Authors should no longer need to manually maintain references.

---

# Version 0.4 — Technical Publishing

Support for larger technical publications.

Planned:

- Index generation
- Glossary
- Acronyms
- Appendix support
- Multi-level contents
- Multiple page templates

---

# Version 0.5 — Additional Output Formats

The internal document model should be capable of producing multiple output formats.

Planned:

- HTML
- EPUB
- Documentation website
- Single-page HTML export

The manuscript should remain unchanged regardless of the output format.

---

# Version 0.6 — Theme System

Expand the YAML theme into a complete styling system.

Planned:

- Multiple themes
- Light and dark themes
- Print theme
- Screen theme
- Font packs
- Colour palettes

The renderer should require no code changes when switching themes.

---

# Version 0.7 — Authoring Tools

Improve the writing experience.

Ideas include:

- Live preview
- Incremental rebuilds
- Build statistics
- Broken reference detection
- Theme validation
- Markdown validation

---

# Version 1.0 — First Stable Release

The project reaches production quality.

Goals:

- Stable API
- Complete documentation
- Comprehensive tests
- Reliable PDF generation
- Production-ready publishing workflow

Version 1.0 should be capable of producing an entire technical book from Markdown alone.

---

# Design Principles

Every feature should support these principles.

## Keep it simple

The engine should remain easy to understand.

Complexity should never be introduced without a clear benefit.

## Separate responsibilities

Markdown contains content.

YAML contains presentation.

Python contains behaviour.

## Prefer standards

Use established technologies wherever possible.

- Markdown
- YAML
- ReportLab
- Python

Avoid inventing new languages or file formats.

## Keep the manuscript readable

The manuscript should remain pleasant to read in any Markdown editor.

The publishing engine exists to improve the output, not complicate the source.

## Grow only when needed

New features should be driven by real publishing requirements.

Project XTC itself serves as the primary test case for future development.

---

# Long-Term Vision

Project XTC Publisher began as a tool for producing a single book.

The long-term goal is to create a lightweight, elegant publishing engine suitable for technical books, user manuals and documentation while remaining small enough for one developer to understand in its entirety.

If the architecture remains clean, the codebase should continue to feel approachable many years into the future.
