from pathlib import Path
from tempfile import TemporaryDirectory
from unittest import TestCase

from engine.model import Table
from engine.parser import parse_markdown


class MarkdownTableTests(TestCase):
   def test_parses_github_style_table(self) -> None:
      markdown = """---
title: Table test
---

| X-Touch | Bitwig |
|---------|--------|
| Channel 1 | Track 1 |
| Channel 2 | Track 2 |
"""

      with TemporaryDirectory() as directory:
         path = Path(directory) / "table.md"
         path.write_text(markdown, encoding="utf-8")
         document = parse_markdown(path)

      tables = [element for element in document.elements if isinstance(element, Table)]
      self.assertEqual(len(tables), 1)
      self.assertEqual(tables[0].headers, ["X-Touch", "Bitwig"])
      self.assertEqual(tables[0].rows, [["Channel 1", "Track 1"], ["Channel 2", "Track 2"]])
