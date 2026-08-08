from __future__ import annotations

import re
from pathlib import Path

import yaml
from markdown_it import MarkdownIt
from markdown_it.token import Token

from .model import (
   BlockQuote,
   BulletList,
   CodeBlock,
   Diagram,
   Directive,
   Document,
   Element,
   Heading,
   NumberedList,
   Paragraph,
   Table,
)

_FRONT = re.compile(
   r"\A---\s*\n(.*?)\n---\s*\n",
   re.S,
)

_DIRECTIVE = re.compile(r"^:::\s*([a-z0-9-]+)(?:\s+([a-z0-9-]+))?\s*$")


def _extract_front_matter(
   text: str,
) -> tuple[dict[str, object], str]:
   match = _FRONT.match(text)

   if not match:
      return {}, text

   data = yaml.safe_load(match.group(1)) or {}

   if not isinstance(data, dict):
      raise ValueError("YAML front matter must be a mapping")

   return data, text[match.end() :]


def _parse_diagram(
   name: str | None,
   content: list[str],
) -> Diagram:
   if not name:
      raise ValueError("Diagram directive requires a name")

   caption = ""

   for line in content:
      stripped = line.strip()

      if not stripped:
         continue

      if stripped.startswith("caption:"):
         value = stripped[len("caption:") :].strip()

         if value:
            try:
               parsed = yaml.safe_load(value)
            except yaml.YAMLError as exc:
               raise ValueError(f"Invalid diagram caption: {value}") from exc

            caption = str(parsed) if parsed is not None else ""

         continue

      raise ValueError(f"Unknown content in diagram {name!r}: {stripped!r}")

   return Diagram(
      name=name,
      caption=caption,
   )


def _extract_directives(
   text: str,
) -> tuple[
   str,
   dict[str, Directive | Diagram],
]:
   lines = text.splitlines()

   output: list[str] = []

   directives: dict[
      str,
      Directive | Diagram,
   ] = {}

   index = 0
   count = 0

   while index < len(lines):
      match = _DIRECTIVE.match(lines[index].strip())

      if not match:
         output.append(lines[index])
         index += 1
         continue

      kind = match.group(1)
      argument = match.group(2)

      index += 1

      content: list[str] = []

      while index < len(lines) and lines[index].strip() != ":::":
         content.append(lines[index])
         index += 1

      if index == len(lines):
         raise ValueError(f"Unclosed directive: {kind}")

      key = f"XTC_DIRECTIVE_{count}"
      count += 1

      if kind == "diagram":
         directives[key] = _parse_diagram(
            argument,
            content,
         )

      else:
         if argument is not None:
            raise ValueError(f"Directive {kind!r} does not accept an argument")

         directives[key] = Directive(
            kind,
            "\n".join(content).strip(),
         )

      output.extend(
         (
            "",
            key,
            "",
         )
      )

      index += 1

   return "\n".join(output), directives


def _parse_table(
   tokens: list[Token],
   start: int,
) -> tuple[Table, int]:
   headers: list[str] = []
   rows: list[list[str]] = []

   current_row: list[str] | None = None
   in_header = False

   index = start + 1

   while index < len(tokens):
      token = tokens[index]

      match token.type:
         case "thead_open":
            in_header = True

         case "thead_close":
            in_header = False

         case "tr_open":
            current_row = []

         case "inline" if current_row is not None:
            current_row.append(token.content.strip())

         case "tr_close" if current_row is not None:
            if in_header and not headers:
               headers = current_row
            else:
               rows.append(current_row)

            current_row = None

         case "table_close":
            if not headers:
               raise ValueError("Markdown table has no header row")

            return (
               Table(
                  headers=headers,
                  rows=rows,
               ),
               index + 1,
            )

      index += 1

   raise ValueError("Unclosed Markdown table")


def parse_markdown(
   path: Path,
) -> Document:
   raw = path.read_text(encoding="utf-8")

   metadata, body = _extract_front_matter(raw)

   body, directives = _extract_directives(body)

   markdown = MarkdownIt(
      "commonmark",
      {"html": False},
   ).enable("table")

   tokens = markdown.parse(body)

   elements: list[Element] = []
   index = 0

   while index < len(tokens):
      token = tokens[index]

      match token.type:
         case "heading_open":
            level = int(token.tag[1])

            elements.append(
               Heading(
                  level,
                  tokens[index + 1].content,
               )
            )

            index += 3

         case "paragraph_open":
            text = tokens[index + 1].content.strip()

            elements.append(
               directives.get(
                  text,
                  Paragraph(text),
               )
            )

            index += 3

         case "bullet_list_open" | "ordered_list_open":
            ordered = token.type == "ordered_list_open"

            start = (
               int(
                  token.attrs.get(
                     "start",
                     1,
                  )
               )
               if ordered
               else 1
            )

            items: list[str] = []

            index += 1

            while index < len(tokens) and tokens[index].type not in (
               "bullet_list_close",
               "ordered_list_close",
            ):
               if tokens[index].type == "inline":
                  items.append(tokens[index].content)

               index += 1

            elements.append(
               NumberedList(
                  items,
                  start,
               )
               if ordered
               else BulletList(items)
            )

            index += 1

         case "blockquote_open":
            parts: list[str] = []

            index += 1

            while index < len(tokens) and tokens[index].type != "blockquote_close":
               if tokens[index].type == "inline":
                  parts.append(tokens[index].content)

               index += 1

            elements.append(BlockQuote("\n".join(parts)))

            index += 1

         case "fence" | "code_block":
            elements.append(
               CodeBlock(
                  token.content.rstrip(),
                  token.info.strip(),
               )
            )

            index += 1

         case "table_open":
            table, index = _parse_table(
               tokens,
               index,
            )

            elements.append(table)

         case _:
            index += 1

   return Document(
      metadata=metadata,
      elements=elements,
      source=path,
   )
