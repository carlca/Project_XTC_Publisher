# Project XTC Publisher

A lightweight Markdown → PDF publishing engine written in Python.

Project XTC Publisher was originally developed to produce **Project XTC – X-Touch Companion**, an unofficial guide to the Behringer X-Touch control surface and Bitwig Studio. Although it was created for that book, the engine itself is intentionally generic and can be used for other technical publications.

The design philosophy is simple:

- Markdown contains the manuscript.
- YAML defines the visual theme.
- Python provides the publishing engine.
- ReportLab generates the finished PDF.

The manuscript never contains presentation logic, and the renderer never contains manuscript text.

---

### *** IMPORTANT ***
## Code Formatting

Project XTC Publisher uses **Ruff** to format all Python source code.

The project deliberately uses a **3-space indentation** rather than the more traditional 4 spaces. This is an intentional stylistic choice. It provides a slightly more compact layout while remaining highly readable.

The indentation width is configured in `pyproject.toml`:

```toml
[tool.ruff]
indent-width = 3
line-length = 160
target-version = "py314"
```

If you prefer a different indentation width, simply change the `indent-width` setting and re-run Ruff.

For example, to return to the more conventional 4-space indentation:

```toml
indent-width = 4
```

or, for those who prefer the compactness of 2 spaces:

```toml
indent-width = 2
```

After changing the setting, reformat the project:

```bash
ruff format .
```

The codebase is intentionally written so that formatting is entirely the responsibility of Ruff rather than individual developers.

---

## Current Status

The project is in active development.

Current features include:

- ✓ Markdown manuscript
- ✓ YAML theme
- ✓ PDF generation using ReportLab
- ✓ Headings and paragraphs
- ✓ Numbered and bulleted lists
- ✓ Block quotes
- ✓ Code blocks
- ✓ Callout directives
- ✓ Markdown tables
- ✓ Configurable typography
- ✓ Separation of content and presentation

---

## Project Structure

```text
Project_XTC_Publisher/

├── engine/
│   ├── parser.py
│   ├── renderer.py
│   ├── model.py
│   ├── theme.py
│   └── __init__.py
│
├── manuscript/
│   ├── 00_contents.md
│   ├── 01_meet_the_xtouch.md
│   ├── ...
│
├── theme/
│   └── default.yaml
│
├── tests/
│
├── output/
│
├── build.py
├── pyproject.toml
└── README.md
```

---

## Architecture

The publisher is deliberately divided into four independent stages.

```text
Markdown
      │
      ▼
 Parser
      │
      ▼
Document Model
      │
      ▼
 Renderer
      │
      ▼
   PDF
```

Each stage has a single responsibility.

### Parser

The parser converts Markdown into a neutral document model.

It has no knowledge of ReportLab or PDF generation.

### Document Model

The document model represents the logical structure of the manuscript.

For example:

- headings
- paragraphs
- tables
- code blocks
- block quotes
- exercises
- field notes
- reality checks

### Renderer

The renderer converts the document model into a PDF using ReportLab.

It has no knowledge of Markdown syntax.

### Theme

Visual appearance is defined entirely in YAML.

Typography, spacing, colours, tables and callout boxes are all controlled by the theme rather than being hard-coded.

---

## Design Goals

Project XTC Publisher follows a few simple principles.

- Keep the manuscript readable.
- Separate content from presentation.
- Prefer composition over complexity.
- Avoid unnecessary abstraction.
- Use standard Markdown wherever possible.
- Extend Markdown only where it provides genuine value.
- Keep the codebase small, clean and easy to understand.

---

## Requirements

- Python 3.14 or later
- ReportLab
- markdown-it-py
- PyYAML

---

## Installation

Clone the repository.

```bash
git clone https://github.com/carlca/Project_XTC_Publisher.git
cd Project_XTC_Publisher
```

Create a virtual environment.

```bash
python3.14 -m venv .venv
```

Activate it.

### macOS / Linux

```bash
source .venv/bin/activate
```

Install the dependencies.

```bash
pip install -r requirements.txt
```

---

## Building the Book

Generate the PDF.

```bash
python build.py
```

The finished document is written to:

```text
output/
```

---

## Coding Style

The project uses:

- Ruff formatter
- Python 3.14
- Structural pattern matching (`match`)
- Small, focused functions
- Clear separation of responsibilities

---

## Roadmap

Planned features include:

- SVG diagrams
- Images and screenshots
- Cross references
- Automatic table of contents
- Index generation
- HTML output
- EPUB output

---

## Contributing

Suggestions, bug reports and pull requests are welcome.

Please keep changes focused, well documented and consistent with the existing architecture.

---

## Licence

This project is released under the MIT License.

See the LICENSE file for details.

---

## Acknowledgements

Project XTC Publisher exists because one simple question gradually evolved into something much larger:

*"Can you find the most straightforward guide to setting up the Behringer X-Touch using the Mackie MCU protocol and the DrivenByMoss extension for Bitwig?"*

When no suitable guide could be found, the obvious solution was to write one—and eventually to build a publishing engine to produce it.
