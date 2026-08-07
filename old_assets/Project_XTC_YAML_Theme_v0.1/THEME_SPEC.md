# Project XTC YAML Theme Specification — v0.1

The theme controls presentation only. Manuscript content remains in Markdown, and Python converts the parsed document model into PDF output.

## Principles

- The file should be understandable without reading the renderer.
- Values describe publishing concepts, not ReportLab classes.
- Content revisions and style revisions remain separate.
- Unknown keys should raise a clear validation error.
- Points are used for typography and spacing; millimetres for page margins.

## Main sections

- `meta`
- `page`
- `fonts`
- `colours`
- `typography`
- `hardware_labels`
- `directives`
- `media`
- `tables`
- `lists`
- `pagination`
- `output`

## Deliberate omissions from v0.1

- multiple page templates;
- print bleed and crop marks;
- separate screen and print themes;
- EPUB- and HTML-specific options.
