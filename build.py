from argparse import ArgumentParser
from pathlib import Path

from engine import PDFRenderer, load_theme, parse_markdown


def main() -> None:
   ap = ArgumentParser(description="Build Project XTC Markdown into PDF")
   ap.add_argument("--theme", type=Path, default=Path("theme/default.yaml"))
   ap.add_argument("--manuscript", type=Path, default=Path("manuscript"))
   ap.add_argument("--output", type=Path, default=Path("output/project_xtc_preview.pdf"))
   args = ap.parse_args()
   files = sorted(args.manuscript.glob("*.md"))
   if not files:
      raise SystemExit(f"No Markdown files found in {args.manuscript}")
   docs = [parse_markdown(p) for p in files]
   args.output.parent.mkdir(parents=True, exist_ok=True)
   PDFRenderer(load_theme(args.theme)).render(docs, args.output)
   print(args.output)


if __name__ == "__main__":
   main()
