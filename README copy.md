# Project XTC Publisher

A small Markdown + YAML + Python publishing engine.

## Install

```bash
python -m pip install -r requirements.txt
```

## Build

```bash
python build.py
```

The result is written to `output/project_xtc_preview.pdf`.

## Architecture

- `manuscript/*.md` - content and YAML front matter
- `theme/default.yaml` - presentation
- `publisher/parser.py` - Markdown to document model
- `publisher/renderer.py` - document model to ReportLab PDF
- `build.py` - command-line entry point

The renderer uses structural pattern matching rather than nested `elif` chains.
