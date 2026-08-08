from __future__ import annotations

import html
import re
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
   KeepTogether,
   PageBreak,
   Preformatted,
   SimpleDocTemplate,
   Spacer,
   Table as RLTable,
   TableStyle,
)
from reportlab.platypus import Paragraph as RLParagraph

from .model import (
   BlockQuote,
   BulletList,
   CodeBlock,
   Directive,
   Document,
   Heading,
   Image,
   NumberedList,
   Paragraph,
   Table,
)


class PDFRenderer:
   def __init__(self, theme: dict):
      self.theme = theme

      self.font = self._find_and_register_font(
         preferred=self.theme["fonts"]["preferred"],
         filenames={
            "DejaVu Sans": "DejaVuSans.ttf",
            "Liberation Sans": "LiberationSans-Regular.ttf",
         },
         fallback="Helvetica",
      )

      self.mono_font = self._find_and_register_font(
         preferred=self.theme["fonts"].get(
            "monospace",
            [
               "DejaVu Sans Mono",
               "Liberation Mono",
               "Courier",
            ],
         ),
         filenames={
            "DejaVu Sans Mono": "DejaVuSansMono.ttf",
            "Liberation Mono": "LiberationMono-Regular.ttf",
         },
         fallback="Courier",
      )

      print(f"Body font: {self.font}")
      print(f"Mono font: {self.mono_font}")

      self.styles = self._styles()

   @staticmethod
   def _font_directories() -> list[Path]:
      home = Path.home()

      return [
         # macOS — fonts installed for the current user
         home / "Library" / "Fonts",

         # macOS — fonts available to all users
         Path("/Library/Fonts"),

         # macOS — system fonts
         Path("/System/Library/Fonts"),

         # Homebrew font locations
         Path("/opt/homebrew/share/fonts"),
         Path("/usr/local/share/fonts"),

         # Common Linux locations
         Path("/usr/share/fonts/truetype/dejavu"),
         Path("/usr/share/fonts/truetype/liberation2"),
         Path("/usr/share/fonts"),
      ]

   def _find_and_register_font(
      self,
      preferred: list[str],
      filenames: dict[str, str],
      fallback: str,
   ) -> str:
      for name in preferred:
         if name == fallback:
            continue

         filename = filenames.get(name)

         if filename is None:
            continue

         for directory in self._font_directories():
            path = directory / filename

            if path.is_file():
               pdfmetrics.registerFont(
                  TTFont(name, str(path))
               )

               print(
                  f"Found {name}: {path}"
               )

               return name

            # Some Linux installations place fonts more deeply
            # inside /usr/share/fonts.
            if (
               directory == Path("/usr/share/fonts")
               and directory.is_dir()
            ):
               matches = list(
                  directory.rglob(filename)
               )

               if matches:
                  path = matches[0]

                  pdfmetrics.registerFont(
                     TTFont(name, str(path))
                  )

                  print(
                     f"Found {name}: {path}"
                  )

                  return name

      print(
         f"Warning: no suitable TrueType font found; "
         f"falling back to {fallback}"
      )

      return fallback

   def _style(
      self,
      name,
      key,
      parent="BodyText",
      bold=False,
   ):
      cfg = self.theme["typography"][key]
      base = getSampleStyleSheet()[parent]

      return ParagraphStyle(
         name,
         parent=base,
         fontName=self.font,
         fontSize=cfg["font_size_pt"],
         leading=cfg["leading_pt"],
         textColor=colors.HexColor(
            cfg.get("colour", "#000000")
         ),
         alignment=(
            TA_CENTER
            if cfg.get("alignment") == "centre"
            else TA_LEFT
         ),
         spaceBefore=cfg.get(
            "space_before_pt",
            0,
         ),
         spaceAfter=cfg.get(
            "space_after_pt",
            0,
         ),
         keepWithNext=cfg.get(
            "keep_with_next",
            False,
         ),
      )

   def _styles(self):
      return {
         "book": self._style(
            "Book",
            "book_title",
            "Title",
         ),
         "subtitle": self._style(
            "Subtitle",
            "book_subtitle",
            "Heading2",
         ),
         "chapter": self._style(
            "Chapter",
            "chapter_title",
            "Heading1",
         ),
         "h2": self._style(
            "H2",
            "section_heading",
            "Heading2",
         ),
         "h3": self._style(
            "H3",
            "subsection_heading",
            "Heading3",
         ),
         "body": self._style(
            "Body",
            "body",
         ),
         "caption": self._style(
            "Caption",
            "caption",
         ),
      }

   @staticmethod
   def _markup(text: str) -> str:
      escaped = html.escape(text)

      escaped = re.sub(
         r"\*\*(.+?)\*\*",
         r"<b>\1</b>",
         escaped,
      )

      escaped = re.sub(
         r"(?<!\*)\*([^*]+?)\*(?!\*)",
         r"<i>\1</i>",
         escaped,
      )

      escaped = escaped.replace(
         "\n",
         "<br/>",
      )

      return escaped

   def _directive(
      self,
      d: Directive,
   ):
      cfg = self.theme.get(
         "directives",
         {},
      ).get(
         d.kind,
         {
            "label": d.kind.replace(
               "-",
               " ",
            ).title(),
            "background": "#F3F3F3",
            "border_colour": "#AAAAAA",
            "padding_pt": 9,
         },
      )

      content = RLParagraph(
         (
            f"<b>{html.escape(cfg['label'])}</b>"
            f"<br/>{self._markup(d.text)}"
         ),
         self.styles["body"],
      )

      table = RLTable(
         [[content]],
         colWidths=[165 * mm],
      )

      table.setStyle(
         TableStyle(
            [
               (
                  "BACKGROUND",
                  (0, 0),
                  (-1, -1),
                  colors.HexColor(
                     cfg["background"]
                  ),
               ),
               (
                  "BOX",
                  (0, 0),
                  (-1, -1),
                  0.8,
                  colors.HexColor(
                     cfg["border_colour"]
                  ),
               ),
               (
                  "LEFTPADDING",
                  (0, 0),
                  (-1, -1),
                  cfg["padding_pt"],
               ),
               (
                  "RIGHTPADDING",
                  (0, 0),
                  (-1, -1),
                  cfg["padding_pt"],
               ),
               (
                  "TOPPADDING",
                  (0, 0),
                  (-1, -1),
                  cfg["padding_pt"],
               ),
               (
                  "BOTTOMPADDING",
                  (0, 0),
                  (-1, -1),
                  cfg["padding_pt"],
               ),
            ]
         )
      )

      return KeepTogether(
         [
            table,
            Spacer(1, 8),
         ]
      )

   def render(
      self,
      documents: list[Document],
      output: Path,
   ) -> None:
      margins = self.theme["page"]["margins_mm"]

      doc = SimpleDocTemplate(
         str(output),
         pagesize=A4,
         leftMargin=margins["left"] * mm,
         rightMargin=margins["right"] * mm,
         topMargin=margins["top"] * mm,
         bottomMargin=margins["bottom"] * mm,
      )

      story = []

      for idx, document in enumerate(documents):
         if idx:
            story.append(
               PageBreak()
            )

         meta = document.metadata

         story += [
            RLParagraph(
               "Project XTC",
               self.styles["book"],
            ),
            RLParagraph(
               (
                  "<b>X-Touch Companion</b><br/>"
                  "<font size='11'>"
                  "The Unofficial Guide to the "
                  "Behringer X-Touch, Bitwig Studio "
                  "and DrivenByMoss"
                  "</font>"
               ),
               self.styles["subtitle"],
            ),
         ]

         title = meta.get(
            "title",
            (
               document.source.stem
               if document.source
               else "Untitled"
            ),
         )

         chapter = meta.get("chapter")

         label = (
            f"Chapter {chapter} - {title}"
            if chapter
            else str(title)
         )

         story.append(
            RLParagraph(
               html.escape(label),
               self.styles["chapter"],
            )
         )

         for element in document.elements:
            match element:
               case Paragraph(text):
                  story += [
                     RLParagraph(
                        self._markup(text),
                        self.styles["body"],
                     ),
                     Spacer(1, 8),
                  ]

               case Heading(level, text):
                  story.append(
                     RLParagraph(
                        html.escape(text),
                        (
                           self.styles["h2"]
                           if level == 2
                           else self.styles["h3"]
                        ),
                     )
                  )

               case BulletList(items):
                  story.append(
                     RLParagraph(
                        "<br/>".join(
                           f"• {self._markup(x)}"
                           for x in items
                        ),
                        self.styles["body"],
                     )
                  )

                  story.append(
                     Spacer(1, 8)
                  )

               case NumberedList(items, start):
                  story.append(
                     RLParagraph(
                        "<br/>".join(
                           f"{n}. {self._markup(x)}"
                           for n, x in enumerate(
                              items,
                              start,
                           )
                        ),
                        self.styles["body"],
                     )
                  )

                  story.append(
                     Spacer(1, 8)
                  )

               # case BulletList(items):
               #    story.append(
               #       RLParagraph(
               #          "<br/>".join(
               #             f"• {html.escape(x)}"
               #             for x in items
               #          ),
               #          self.styles["body"],
               #       )
               #    )

               #    story.append(
               #       Spacer(1, 8)
               #    )

               # case NumberedList(items, start):
               #    story.append(
               #       RLParagraph(
               #          "<br/>".join(
               #             f"{n}. {html.escape(x)}"
               #             for n, x in enumerate(
               #                items,
               #                start,
               #             )
               #          ),
               #          self.styles["body"],
               #       )
               #    )

               #    story.append(
               #       Spacer(1, 8)
               #    )

               case BlockQuote(text):
                  story.append(
                     RLParagraph(
                        (
                           f"<i>"
                           f"{self._markup(text)}"
                           f"</i>"
                        ),
                        self.styles["body"],
                     )
                  )

                  story.append(
                     Spacer(1, 8)
                  )

               case CodeBlock(text, language):
                  story.append(
                     Preformatted(
                        text,
                        ParagraphStyle(
                           "Code",
                           parent=self.styles[
                              "body"
                           ],
                           fontName=self.mono_font,
                           fontSize=9.5,
                           leading=12,
                           backColor=colors.HexColor(
                              "#F5F5F5"
                           ),
                           borderPadding=6,
                        ),
                     )
                  )

                  story.append(
                     Spacer(1, 8)
                  )

               case Directive():
                  story.append(
                     self._directive(element)
                  )

               case Table(headers, rows):
                  cfg = self.theme.get(
                     "tables",
                     {},
                  )

                  data = [
                     [
                        RLParagraph(
                           (
                              f"<b>"
                              f"{self._markup(cell)}"
                              f"</b>"
                           ),
                           self.styles["body"],
                        )
                        for cell in headers
                     ],
                     *[
                        [
                           RLParagraph(
                              self._markup(cell),
                              self.styles["body"],
                           )
                           for cell in row
                        ]
                        for row in rows
                     ],
                  ]

                  column_widths = [
                     doc.width / len(headers)
                  ] * len(headers)

                  table = RLTable(
                     data,
                     colWidths=column_widths,
                     repeatRows=1,
                  )

                  table.setStyle(
                     TableStyle(
                        [
                           (
                              "BACKGROUND",
                              (0, 0),
                              (-1, 0),
                              colors.HexColor(
                                 cfg.get(
                                    "header_background",
                                    "#EEEEEE",
                                 )
                              ),
                           ),
                           (
                              "GRID",
                              (0, 0),
                              (-1, -1),
                              cfg.get(
                                 "border_width_pt",
                                 0.5,
                              ),
                              colors.HexColor(
                                 cfg.get(
                                    "border_colour",
                                    "#BFBFBF",
                                 )
                              ),
                           ),
                           (
                              "LEFTPADDING",
                              (0, 0),
                              (-1, -1),
                              cfg.get(
                                 "cell_padding_pt",
                                 5,
                              ),
                           ),
                           (
                              "RIGHTPADDING",
                              (0, 0),
                              (-1, -1),
                              cfg.get(
                                 "cell_padding_pt",
                                 5,
                              ),
                           ),
                           (
                              "TOPPADDING",
                              (0, 0),
                              (-1, -1),
                              cfg.get(
                                 "cell_padding_pt",
                                 5,
                              ),
                           ),
                           (
                              "BOTTOMPADDING",
                              (0, 0),
                              (-1, -1),
                              cfg.get(
                                 "cell_padding_pt",
                                 5,
                              ),
                           ),
                           (
                              "VALIGN",
                              (0, 0),
                              (-1, -1),
                              "TOP",
                           ),
                        ]
                     )
                  )

                  story.extend(
                     (
                        table,
                        Spacer(1, 8),
                     )
                  )

               case Image(path, alt):
                  pass

               case _:
                  raise TypeError(
                     "Unsupported element: "
                     f"{type(element).__name__}"
                  )

      doc.build(story)
