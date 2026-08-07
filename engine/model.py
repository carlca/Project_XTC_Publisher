from dataclasses import dataclass, field
from pathlib import Path
from typing import TypeAlias


@dataclass(slots=True)
class Paragraph:
   text: str


@dataclass(slots=True)
class Heading:
   level: int
   text: str


@dataclass(slots=True)
class BulletList:
   items: list[str]


@dataclass(slots=True)
class NumberedList:
   items: list[str]
   start: int = 1


@dataclass(slots=True)
class BlockQuote:
   text: str


@dataclass(slots=True)
class CodeBlock:
   text: str
   language: str = ""


@dataclass(slots=True)
class Directive:
   kind: str
   text: str


@dataclass(slots=True)
class Image:
   path: Path
   alt: str


@dataclass(slots=True)
class Table:
   headers: list[str]
   rows: list[list[str]]


Element: TypeAlias = (
   Paragraph
   | Heading
   | BulletList
   | NumberedList
   | BlockQuote
   | CodeBlock
   | Directive
   | Image
   | Table
)


@dataclass(slots=True)
class Document:
   metadata: dict[str, object]
   elements: list[Element] = field(default_factory=list)
   source: Path | None = None
