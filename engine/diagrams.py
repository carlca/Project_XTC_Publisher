from __future__ import annotations

from collections.abc import Callable

from reportlab.graphics.shapes import (
   Drawing,
   Line,
   Polygon,
   Rect,
   String,
)
from reportlab.lib import colors

DiagramFactory = Callable[[], Drawing]


# ---------------------------------------------------------------------------
# Shared styling
# ---------------------------------------------------------------------------

_LINE_COLOUR = colors.HexColor("#666666")
_BORDER_COLOUR = colors.HexColor("#888888")
_FILL_COLOUR = colors.HexColor("#F5F5F5")
_TEXT_COLOUR = colors.HexColor("#222222")
_MUTED_TEXT_COLOUR = colors.HexColor("#666666")

_FONT = "Helvetica"
_FONT_SIZE = 11
_SMALL_FONT_SIZE = 9


# ---------------------------------------------------------------------------
# Drawing helpers
# ---------------------------------------------------------------------------


def _text(
   drawing: Drawing,
   x: float,
   y: float,
   value: str,
   *,
   size: float = _FONT_SIZE,
   anchor: str = "middle",
   colour=_TEXT_COLOUR,
) -> None:
   drawing.add(
      String(
         x,
         y,
         value,
         fontName=_FONT,
         fontSize=size,
         fillColor=colour,
         textAnchor=anchor,
      )
   )


def _box(
   drawing: Drawing,
   x: float,
   y: float,
   width: float,
   height: float,
   label: str,
   *,
   fill=_FILL_COLOUR,
   stroke=_BORDER_COLOUR,
) -> None:
   drawing.add(
      Rect(
         x,
         y,
         width,
         height,
         rx=5,
         ry=5,
         fillColor=fill,
         strokeColor=stroke,
         strokeWidth=1,
      )
   )

   _text(
      drawing,
      x + width / 2,
      y + height / 2 - 4,
      label,
   )


def _arrow_head_down(
   drawing: Drawing,
   x: float,
   y: float,
   *,
   size: float = 5,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Polygon(
         [
            x,
            y,
            x - size,
            y + size * 1.6,
            x + size,
            y + size * 1.6,
         ],
         fillColor=colour,
         strokeColor=colour,
      )
   )


def _arrow_head_up(
   drawing: Drawing,
   x: float,
   y: float,
   *,
   size: float = 5,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Polygon(
         [
            x,
            y,
            x - size,
            y - size * 1.6,
            x + size,
            y - size * 1.6,
         ],
         fillColor=colour,
         strokeColor=colour,
      )
   )


def _arrow_head_right(
   drawing: Drawing,
   x: float,
   y: float,
   *,
   size: float = 5,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Polygon(
         [
            x,
            y,
            x - size * 1.6,
            y + size,
            x - size * 1.6,
            y - size,
         ],
         fillColor=colour,
         strokeColor=colour,
      )
   )


def _arrow_head_left(
   drawing: Drawing,
   x: float,
   y: float,
   *,
   size: float = 5,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Polygon(
         [
            x,
            y,
            x + size * 1.6,
            y + size,
            x + size * 1.6,
            y - size,
         ],
         fillColor=colour,
         strokeColor=colour,
      )
   )


def _down_arrow(
   drawing: Drawing,
   x: float,
   y1: float,
   y2: float,
   *,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Line(
         x,
         y1,
         x,
         y2 + 8,
         strokeColor=colour,
         strokeWidth=1.2,
      )
   )

   _arrow_head_down(
      drawing,
      x,
      y2,
      colour=colour,
   )


def _right_arrow(
   drawing: Drawing,
   x1: float,
   x2: float,
   y: float,
   *,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Line(
         x1,
         y,
         x2 - 8,
         y,
         strokeColor=colour,
         strokeWidth=1.2,
      )
   )

   _arrow_head_right(
      drawing,
      x2,
      y,
      colour=colour,
   )


def _left_arrow(
   drawing: Drawing,
   x1: float,
   x2: float,
   y: float,
   *,
   colour=_LINE_COLOUR,
) -> None:
   drawing.add(
      Line(
         x1 + 8,
         y,
         x2,
         y,
         strokeColor=colour,
         strokeWidth=1.2,
      )
   )

   _arrow_head_left(
      drawing,
      x1,
      y,
      colour=colour,
   )


# ---------------------------------------------------------------------------
# Figure 5.1
#
# mode-overview
# ---------------------------------------------------------------------------


def mode_overview() -> Drawing:
   width = 440
   height = 230

   drawing = Drawing(
      width,
      height,
   )

   top_width = 150
   top_height = 40
   top_x = (width - top_width) / 2
   top_y = 175

   _box(
      drawing,
      top_x,
      top_y,
      top_width,
      top_height,
      "X-Touch Controls",
   )

   mode_width = 110
   mode_height = 38
   mode_y = 88

   mixer_x = 20
   device_x = (width - mode_width) / 2
   browser_x = width - 20 - mode_width

   # Central stem from the X-Touch.
   centre_x = width / 2
   branch_y = 148

   drawing.add(
      Line(
         centre_x,
         top_y,
         centre_x,
         branch_y,
         strokeColor=_LINE_COLOUR,
         strokeWidth=1.2,
      )
   )

   # Horizontal branch.
   mixer_centre = mixer_x + mode_width / 2
   device_centre = device_x + mode_width / 2
   browser_centre = browser_x + mode_width / 2

   drawing.add(
      Line(
         mixer_centre,
         branch_y,
         browser_centre,
         branch_y,
         strokeColor=_LINE_COLOUR,
         strokeWidth=1.2,
      )
   )

   # Downward branches into the three modes.
   for x in (
      mixer_centre,
      device_centre,
      browser_centre,
   ):
      _down_arrow(
         drawing,
         x,
         branch_y,
         mode_y + mode_height,
      )

   _box(
      drawing,
      mixer_x,
      mode_y,
      mode_width,
      mode_height,
      "Mixer Mode",
   )

   _box(
      drawing,
      device_x,
      mode_y,
      mode_width,
      mode_height,
      "Device Mode",
   )

   _box(
      drawing,
      browser_x,
      mode_y,
      mode_width,
      mode_height,
      "Browser Mode",
   )

   # What the same controls represent in each mode.
   _text(
      drawing,
      mixer_centre,
      48,
      "Tracks",
      size=10,
   )

   _text(
      drawing,
      device_centre,
      48,
      "Parameters",
      size=10,
   )

   _text(
      drawing,
      browser_centre,
      48,
      "Choices",
      size=10,
   )

   for x in (
      mixer_centre,
      device_centre,
      browser_centre,
   ):
      _down_arrow(
         drawing,
         x,
         mode_y - 4,
         62,
      )

   return drawing


# ---------------------------------------------------------------------------
# Figure 7.1
#
# feedback-loop
# ---------------------------------------------------------------------------


def feedback_loop() -> Drawing:
   width = 440
   height = 180

   drawing = Drawing(
      width,
      height,
   )

   box_width = 120
   box_height = 42

   left_x = 45
   right_x = width - 45 - box_width
   box_y = 70

   _box(
      drawing,
      left_x,
      box_y,
      box_width,
      box_height,
      "X-Touch",
   )

   _box(
      drawing,
      right_x,
      box_y,
      box_width,
      box_height,
      "Bitwig",
   )

   upper_y = box_y + 30
   lower_y = box_y + 12

   # X-Touch -> Bitwig
   _right_arrow(
      drawing,
      left_x + box_width,
      right_x,
      upper_y,
   )

   _text(
      drawing,
      width / 2,
      upper_y + 11,
      "commands",
      size=_SMALL_FONT_SIZE,
      colour=_MUTED_TEXT_COLOUR,
   )

   # Bitwig -> X-Touch
   _left_arrow(
      drawing,
      left_x + box_width,
      right_x,
      lower_y,
   )

   _text(
      drawing,
      width / 2,
      lower_y - 16,
      "feedback",
      size=_SMALL_FONT_SIZE,
      colour=_MUTED_TEXT_COLOUR,
   )

   return drawing


# ---------------------------------------------------------------------------
# Figure 9.1
#
# fader-feedback
# ---------------------------------------------------------------------------


def fader_feedback() -> Drawing:
   width = 440
   height = 220

   drawing = Drawing(
      width,
      height,
   )

   box_width = 135
   box_height = 46

   left_x = 55
   right_x = width - 55 - box_width
   box_y = 90

   _box(
      drawing,
      left_x,
      box_y,
      box_width,
      box_height,
      "Motor Fader",
   )

   _box(
      drawing,
      right_x,
      box_y,
      box_width,
      box_height,
      "Bitwig",
   )

   upper_y = box_y + 32
   lower_y = box_y + 14

   # Physical movement becomes control data.
   _right_arrow(
      drawing,
      left_x + box_width,
      right_x,
      upper_y,
   )

   _text(
      drawing,
      width / 2,
      upper_y + 11,
      "control",
      size=_SMALL_FONT_SIZE,
      colour=_MUTED_TEXT_COLOUR,
   )

   # Bitwig's state drives the motor fader.
   _left_arrow(
      drawing,
      left_x + box_width,
      right_x,
      lower_y,
   )

   _text(
      drawing,
      width / 2,
      lower_y - 16,
      "feedback",
      size=_SMALL_FONT_SIZE,
      colour=_MUTED_TEXT_COLOUR,
   )

   # User interaction.
   user_x = left_x + box_width / 2

   _text(
      drawing,
      user_x,
      35,
      "You",
      size=11,
   )

   drawing.add(
      Line(
         user_x,
         48,
         user_x,
         box_y - 8,
         strokeColor=_LINE_COLOUR,
         strokeWidth=1.2,
      )
   )

   _arrow_head_up(
      drawing,
      user_x,
      box_y,
   )

   _text(
      drawing,
      user_x + 18,
      63,
      "move",
      size=_SMALL_FONT_SIZE,
      anchor="start",
      colour=_MUTED_TEXT_COLOUR,
   )

   return drawing


# ---------------------------------------------------------------------------
# Figure 11.1
#
# device-hierarchy
# ---------------------------------------------------------------------------


def device_hierarchy() -> Drawing:
   width = 440
   height = 300

   drawing = Drawing(
      width,
      height,
   )

   box_width = 150
   box_height = 38
   x = (width - box_width) / 2

   track_y = 245
   device_y = 165
   page_y = 85

   _box(
      drawing,
      x,
      track_y,
      box_width,
      box_height,
      "Selected Track",
   )

   _down_arrow(
      drawing,
      width / 2,
      track_y - 5,
      device_y + box_height + 8,
   )

   _box(
      drawing,
      x,
      device_y,
      box_width,
      box_height,
      "Selected Device",
   )

   _down_arrow(
      drawing,
      width / 2,
      device_y - 5,
      page_y + box_height + 8,
   )

   _box(
      drawing,
      x,
      page_y,
      box_width,
      box_height,
      "Parameter Page",
   )

   _down_arrow(
      drawing,
      width / 2,
      page_y - 5,
      38,
   )

   _text(
      drawing,
      width / 2,
      18,
      "Parameters 1–8",
      size=11,
   )

   return drawing


# ---------------------------------------------------------------------------
# Figure 12.1
#
# browser-workflow
# ---------------------------------------------------------------------------


def browser_workflow() -> Drawing:
   width = 440
   height = 360

   drawing = Drawing(
      width,
      height,
   )

   box_width = 170
   box_height = 38
   x = (width - box_width) / 2

   stages = [
      ("Selected Track", 305),
      ("Browser", 235),
      ("Search / Navigate", 165),
      ("Choose an Item", 95),
      ("Add to Project", 25),
   ]

   for index, (label, y) in enumerate(stages):
      _box(
         drawing,
         x,
         y,
         box_width,
         box_height,
         label,
      )

      if index < len(stages) - 1:
         next_y = stages[index + 1][1]

         _down_arrow(
            drawing,
            width / 2,
            y - 4,
            next_y + box_height + 7,
         )

   return drawing


# ---------------------------------------------------------------------------
# Diagram registry
# ---------------------------------------------------------------------------


DIAGRAMS: dict[str, DiagramFactory] = {
   "mode-overview": mode_overview,
   "feedback-loop": feedback_loop,
   "fader-feedback": fader_feedback,
   "device-hierarchy": device_hierarchy,
   "browser-workflow": browser_workflow,
}


def render_diagram(
   name: str,
) -> Drawing:
   """
   Create a named diagram.

   Diagram names are kept in an explicit registry so that manuscript
   errors fail loudly rather than silently producing a missing figure.
   """

   factory = DIAGRAMS.get(name)

   if factory is None:
      available = ", ".join(sorted(DIAGRAMS))

      raise ValueError(f"Unknown diagram: {name!r}. Available diagrams: {available}")

   return factory()
