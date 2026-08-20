# Project XTC — MCU Coverage Audit

## Part 2: Existing Manuscript vs DrivenByMoss MCU Functionality

### Audit key

- **✓ Covered** — adequately explained in the existing manuscript
- **△ Partial** — concept is present, but important DrivenByMoss functionality is missing
- **✗ Missing** — functionality is not presently taught
- **N/A** — not relevant to the standard Behringer X-Touch or outside the intended scope

The purpose of this audit is **not** to turn Project XTC into a transcription of the DrivenByMoss reference manual.

The aim is to identify everything the X-Touch can usefully do, then decide how that functionality can be taught in a logical and approachable order.

---

# A. SELECT and Track Focus

## Basic selection

| Function | Coverage | Notes |
|---|---|---|
| SELECT 1–8 selects a track | ✓ | Central subject of Chapter 6 |
| Selection establishes controller focus | ✓ | Explained extensively |
| Device Mode follows selected track | ✓ | Explained |
| Browser Mode follows selected track | ✓ | Explained |
| Scribble strips respond to selection | ✓ | Explained |

Chapter 6 is particularly strong conceptually. Its central idea — thinking of SELECT as establishing **focus** rather than merely highlighting a track — should remain intact.

## Advanced SELECT functions

| Function | Coverage | Action |
|---|---|---|
| SHIFT + SELECT — multi-select tracks | ✗ | Add to advanced material |
| OPTION + SELECT — stop playing clip | ✗ | Add |
| CONTROL + SELECT — open/close group | ✗ | Add |
| ALT + SELECT — set new clip length | ✗ | Add |
| SEND + SELECT 1–8 — directly select Send 1–8 | ✗ | Add with Send Mode |
| SELECT selected group — enter group in hierarchical navigation | ✗ | Add |
| Long SELECT — leave group/folder | ✗ | Add |
| SELECT selected instrument track — enter Layer/Drum Pad Mode | ✗ | Add with Layer Mode |

### Editorial decision

Do **not** put all of this into Chapter 6.

Chapter 6 succeeds precisely because it teaches one powerful idea:

> **SELECT establishes focus.**

The modifier functions should appear later, once the reader understands the modifier system and the modes to which they apply.

---

# B. V-Pots

## Basic operation

| Function | Coverage | Notes |
|---|---|---|
| V-Pots are endless encoders | ✓ | Chapter 8 |
| V-Pots are pushable | ✓ | Chapter 8 |
| LED rings provide value feedback | ✓ | Chapter 8 |
| Function changes with current mode | ✓ | Major theme of Chapter 8 |
| PAN control | ✓ | Covered |
| SEND control | ✓ | Covered conceptually |
| Device parameter control | ✓ | Covered |
| Browser navigation | ✓ | Covered conceptually |

Chapter 8 gives an excellent mental model for the V-Pots.

However, its description of **pressing** a V-Pot is deliberately generic. DrivenByMoss gives us several concrete behaviours which should now be added.

## V-Pot press modifiers

| Function | Coverage | Action |
|---|---|---|
| Press — reset parameter to default | ✗ | Add |
| SHIFT + Press — centre value | ✗ | Add |
| CONTROL + Press — minimum | ✗ | Add |
| ALT + Press — maximum | ✗ | Add |
| OPTION + Press on Send — toggle Send on/off | ✗ | Add |

### Natural teaching pattern

These commands have a very memorable structure:

```text
PRESS              Default
SHIFT + PRESS      Centre
CONTROL + PRESS    Minimum
ALT + PRESS        Maximum
OPTION + PRESS     Context-specific
```

That is considerably easier to learn than five unrelated commands.

**Status of Chapter 8 overall: △**

The conceptual material is strong; the operational layer needs expansion.

---

# C. Motor Faders

## Core functionality

| Function | Coverage | Notes |
|---|---|---|
| Eight channel motor faders | ✓ | Chapter 9 |
| Separate Master fader | ✓ | Covered |
| Faders send changes to Bitwig | ✓ | Covered |
| Bitwig sends values back to faders | ✓ | Covered extensively |
| Bank changes reposition faders | ✓ | Covered |
| Touch sensitivity | ✓ | Covered |
| Automation playback moves faders | ✓ | Covered |
| Writing automation physically | ✓ | Covered conceptually |

Chapter 9 is already one of the more complete chapters.

## Missing operational functions

| Function | Coverage | Action |
|---|---|---|
| Fader touch selects its track | △ | Touch is discussed, but this specific DrivenByMoss behaviour needs documenting |
| Master-fader touch selects Master track | ✗ | Add |
| Master-fader touch enters Master Edit Mode | ✗ | Add with Master Mode |
| SHIFT + Master Fader — metronome volume | ✗ | Add |
| FLIP — use faders like editing knobs | ✗ | Add |
| SHIFT + FLIP — toggle regular/effect tracks | ✗ | Add |
| LOCK — lock faders | N/A / verify | Source notes that LOCK is not an MCU control |

There is also an important **preference dependency**: DrivenByMoss provides *Select Channel on Fader Touch* and *Activate Volume Mode on Fader Touch*. These should eventually be explained as configuration choices rather than unconditional hardware behaviour.

**Status of Chapter 9 overall: △**

---

# D. Transport

This is one of the largest areas requiring expansion.

## PLAY

| Function | Coverage | Action |
|---|---|---|
| PLAY — start/stop playback | ✓ | Covered |
| Double-click PLAY — play cursor to start | ✗ | Add |
| SHIFT + PLAY — toggle repeat | ✗ | Add |
| OPTION + PLAY — Punch In | ✗ | Add |
| OPTION + SHIFT + PLAY — Punch Out | ✗ | Add |

## STOP

| Function | Coverage | Action |
|---|---|---|
| STOP — stop playback | ✓ | Covered |
| STOP again — cursor to song start | ✗ | Add |
| Double-click STOP — cursor to song end | ✗ | Add |

## RECORD

| Function | Coverage | Action |
|---|---|---|
| RECORD — start/stop recording | ✓ | Covered |
| SHIFT + RECORD — Launcher overdub | ✗ | Add |
| OPTION + RECORD — create clip, play and overdub | ✗ | Add |

The `OPTION + RECORD` command deserves more than a reference-table entry because it implements an entire clip-recording workflow with one operation.

## REWIND / FORWARD

| Function | Coverage | Action |
|---|---|---|
| REWIND — cursor backwards | ✓ | Covered |
| FORWARD — cursor forwards | ✓ | Covered |
| OPTION + REWIND — previous marker | ✗ | Add |
| OPTION + FORWARD — next marker | ✗ | Add |

## Jog Wheel

| Function | Coverage | Action |
|---|---|---|
| Jog — play position | ✓ | Covered |
| SHIFT + Jog — fine position | △ | Make explicit |
| OPTION + Jog — tempo | ✗ | Add |
| OPTION + SHIFT + Jog — fine tempo | ✗ | Add |
| CONTROL + Jog — loop start | ✗ | Add |
| CONTROL + SHIFT + Jog — fine loop start | ✗ | Add |
| ALT + Jog — loop length | ✗ | Add |
| ALT + SHIFT + Jog — fine loop length | ✗ | Add |

Again there is an excellent pattern:

```text
                NORMAL          + SHIFT
Jog             Position        Fine position
OPTION + Jog    Tempo           Fine tempo
CONTROL + Jog   Loop start      Fine loop start
ALT + Jog       Loop length     Fine loop length
```

This is exactly the sort of thing Project XTC can make considerably easier to understand than a flat command list.

## Other transport-area controls

| Function | Coverage |
|---|---|
| SCRUB — cycle editing modes | ✗ |
| Arrow buttons — keyboard cursor keys | ✗ |
| ZOOM + arrows — Arranger zoom/track height | ✗ |
| NUDGE — Tap Tempo | ✗ |
| REPEAT — toggle repeat | △ |

**Status of Chapter 10 overall: △**

Its basic explanation is good. Its advanced command coverage is currently sparse.

---

# E. Marker Workflow

This is the feature that originally triggered the audit.

| Function | Coverage |
|---|---|
| MARKER — enter Marker Mode | ✗ |
| SHIFT + MARKER — show/hide markers | ✗ |
| OPTION + MARKER — insert marker at play position | ✗ |
| OPTION + REWIND — previous marker | ✗ |
| OPTION + FORWARD — next marker | ✗ |
| V-Pot press in Marker Mode — play from marker | ✗ |

**Status: ✗ Entire workflow missing**

This should not merely become six extra bullets in Chapter 10.

There is a coherent workflow here:

```text
             OPTION + MARKER
                    │
                    ▼
              Create Marker
                    │
                    ▼
               MARKER Mode
                    │
                    ▼
          Markers on V-Pots
              ╱           ╲
             ╱             ╲
      OPTION + <<       OPTION + >>
      Previous            Next
             ╲             ╱
              ╲           ╱
               Navigate
```

### Editorial recommendation

Create a proper **Markers and Navigation** section, potentially within a later advanced-workflow chapter.

This is exactly the sort of useful functionality that a new X-Touch owner could otherwise use the controller for years without discovering.

---

# F. Device Mode

Chapter 11 provides an excellent conceptual hierarchy:

```text
Track
  ↓
Device
  ↓
Parameter Page
  ↓
Parameter
```

The missing material is mainly about **how to navigate that hierarchy efficiently from the hardware**.

| Function | Coverage | Action |
|---|---|---|
| DEVICE enters Device Mode | ✓ | Covered |
| V-Pots control eight parameters | ✓ | Covered |
| BANK ←/→ — previous/next device | △ | Make explicit |
| CHANNEL ←/→ — previous/next parameter page | △ | Make explicit |
| Hold CONTROL — display devices | ✗ | Add |
| CONTROL + V-Pot press — select device | ✗ | Add |
| Hold OPTION — display parameter pages | ✗ | Add |
| OPTION + V-Pot press — select page | ✗ | Add |
| OPTION + DEVICE — pin cursor device | ✗ | Add |
| DEVICE pressed again — Project/Track Parameter Mode | ✗ | Add |

### Editorial recommendation

This material belongs **inside Chapter 11**, because it strengthens rather than distracts from the existing hierarchy.

The reader already understands *what* a device and parameter page are. We can now teach the shortcuts that make navigating them fast.

**Status of Chapter 11 overall: △ approaching ✓ after revision**

---

# G. Browser Mode

Chapter 12 is another strong conceptual chapter, but the reference documentation gives us much more precise hardware behaviour.

| Function | Coverage | Action |
|---|---|---|
| BROWSER/USER — enter Browser | ✓ | Covered |
| Track Control knobs — navigate columns | △ | Make explicit |
| V-Pot press — enter filter/results | △ | Make explicit |
| Second press — confirm | ✗ | Add |
| Jog Wheel — scroll results | △ | Make explicit |
| BROWSER or ENTER — confirm and close | △ | Add exact behaviour |
| CANCEL — discard | △ | Add exact behaviour |
| SHIFT + BROWSER — discard while browsing | ✗ | Add |
| UP — previous Browser tab | ✗ | Add |
| DOWN — next Browser tab | ✗ | Add |
| LEFT — insert before device | ✗ | Add |
| RIGHT — insert after device | ✗ | Add |
| ZOOM — replace selected device | ✗ | Add |

There are also commands for **entering** the Browser with an insertion intention:

| Function | Coverage |
|---|---|
| BROWSER — browse presets | ✓/△ |
| SHIFT + BROWSER — insert device before current device | ✗ |
| OPTION + BROWSER — insert device after current device | ✗ |

Notice that `SHIFT + BROWSER` is context-sensitive: outside Browser Mode it initiates insertion before the current device; while browsing it can discard the selection.

That is worth explaining rather than merely listing.

**Status of Chapter 12 overall: △**

---

# H. Assignment / Mixer Edit Modes

This is a substantial gap.

DrivenByMoss defines a family of explicit modes:

```text
TRACK       Track Edit Mode
TRACK ×2    Volume Edit Mode
PAN         Panorama Edit Mode
SEND        Send Edit Mode
DEVICE      Device Edit Mode
EQ          Equalizer Edit Mode
INSTRUMENT  Instrument Device Edit Mode
```

The existing book explains modes conceptually, and individual chapters discuss pan, sends and devices, but does not yet systematically teach this family as a whole.

## Track Edit Mode

**✗ Operational coverage missing**

The eight V-Pots control:

1. Volume
2. Panorama
3. Crossfader
4. Send 1
5. Send 2
6. Send 3
7. Send 4
8. Send 5

SHIFT provides fine adjustment.

A preference can remove Crossfader and expose Send 6 instead.

## Volume Edit Mode

**✗ Missing**

`TRACK` pressed twice assigns the eight V-Pots to the volumes of the eight channels.

## Panorama Edit Mode

**△ Concept covered, mode operation incomplete**

`PAN` assigns the eight V-Pots to channel panorama.

## Send Modes 1–8

**△ Concept covered, operation incomplete**

- SEND enters Send Mode.
- Repeated SEND presses cycle Send 1–8.
- SHIFT + SEND cycles backwards.
- SEND + SELECT 1–8 directly selects a send.
- V-Pots control that send across the eight channels.

### Editorial recommendation

This warrants a new **Mixer Edit Modes** chapter.

Trying to distribute these facts between the existing V-Pot, Modes and SELECT chapters would obscure the very elegant relationship between them.

---

# I. Automation

**Status: ✗ Major missing area**

DrivenByMoss exposes:

| Control | Function |
|---|---|
| READ/OFF | Disable Arranger automation recording |
| OPTION + READ/OFF | Reset automation overrides |
| WRITE | Write mode |
| TRIM | Maps to Read because Bitwig has no Trim mode |
| TOUCH | Touch mode |
| LATCH | Latch mode |

Chapter 9 already prepares the reader beautifully for this by explaining touch-sensitive motor faders and automation physically.

That gives us a natural progression:

```text
Chapter 9
Motor Faders
     │
     ▼
Why touch sensitivity matters
     │
     ▼
Advanced chapter
Automation from the X-Touch
```

### Editorial recommendation

**Dedicated chapter.**

This is too important to become an appendix table.

---

# J. Layer / Drum Pad Modes

**Status: ✗ Missing**

For a selected track containing an instrument with layers or drum pads:

- press SELECT again to enter the layer/drum-pad hierarchy;
- use Mode buttons to choose editing modes;
- control Volume, Pan, Sends, Mute and Solo;
- long-press SELECT to leave.

### Editorial recommendation

Probably advanced material following Device Mode rather than an addition to Chapter 6.

It demonstrates the same hierarchical idea already established by the book:

```text
Track
  ↓
Instrument
  ↓
Layer / Drum Pad
  ↓
Volume / Pan / Sends / etc.
```

---

# K. Master Edit Mode

**Status: ✗ Missing**

Touching the Master Fader enters Master Edit Mode.

The V-Pots then expose:

| V-Pot | Function |
|---|---|
| 1 | Master volume; press to reset |
| 2 | Master panorama; press to reset |
| 3–5 | Audio-engine on/off controls |
| 7 | Previous project |
| 8 | Next project |

This is a particularly good candidate for Project XTC because it is **highly discoverable once documented and almost invisible if it isn't**.

A user could own an X-Touch for years without guessing that touching the master fader exposes project-switching commands on V-Pots 7 and 8.

---

# L. Equalizer Mode

**Status: ✗ Missing**

EQ Mode behaves similarly to Device Mode but targets the track equalizer.

For Bitwig the reference specifies **EQ+**.

An especially useful feature is:

> If the selected track has no equalizer when EQ Mode is activated, DrivenByMoss automatically adds one.

That deserves prominent treatment because pressing EQ can therefore **modify the project**, rather than merely changing the controller's view.

---

# M. Automation, Utility and Global Buttons

A further group of physical controls is barely represented at present.

| Function | Coverage |
|---|---|
| UNDO | ✗ |
| SHIFT + UNDO — Redo | ✗ |
| SAVE | ✗ |
| Note Editor pane | ✗ |
| Automation Editor pane | ✗ |
| Toggle plug-in window | ✗ |
| Toggle layouts | ✗ |
| Toggle device expanded state | ✗ |
| Toggle Mixer pane | ✗ |
| Metronome | ✗ |
| SHIFT + Metronome — ticks | ✗ |
| SOLO — clear all solos | ✗ |
| SHIFT + SOLO — clear all mutes | ✗ |
| OVR — Arranger overdub | ✗ |
| SHIFT + OVR — Launcher overdub | ✗ |
| DROP — duplicate selected track | ✗ |

These are especially relevant to Chapter 13's goal of moving towards a **Mouse-Free (or Mouse-Lite) Workflow**.

Rather than scattering them randomly through earlier chapters, many could form a section built around:

> **Things you no longer need to reach for the mouse to do.**

---

# N. DrivenByMoss Preferences

**Status: largely ✗**

The reference contains numerous preferences affecting X-Touch behaviour:

- X-Touch hardware profile
- display configuration and colours
- VU meters
- fader behaviour
- track-bank composition
- flat vs hierarchical track navigation
- startup mode
- fader-touch selection
- temporary Volume Mode on fader touch
- knob sensitivity
- encoder slowdown
- Browser filter visibility
- Stop/Pause behaviour
- Record/Automation Arranger-vs-Launcher behaviour
- assignable F-buttons
- footswitch assignments

These should **not** all be woven into the normal chapters.

### Editorial recommendation

Create a dedicated **Configuring DrivenByMoss for the X-Touch** chapter or appendix.

That would also give us somewhere authoritative to record which settings Project XTC assumes when describing behaviour elsewhere.

---

# Part 2 — Interim Finding

The audit does **not** suggest that Chapters 1–13 need wholesale rewriting.

Quite the opposite.

Their main strength is that they establish the mental model:

```text
Hardware
   ↓
Mode
   ↓
Focus
   ↓
Feedback
   ↓
Action
```

The DrivenByMoss reference supplies the deeper operational layer that belongs **on top of that foundation**.

The emerging editorial strategy should therefore be:

1. **Preserve Chapters 1–13 as the learning foundation.**
2. **Make targeted additions where advanced behaviour naturally belongs.**
3. **Create new chapters for coherent advanced subjects.**
4. **Use tables and quick-reference material only after the behaviour has been explained.**
5. **Keep the DrivenByMoss inventory as the completeness checklist so no command disappears during restructuring.**

## Strong candidates for new chapters

The audit currently suggests:

- **Mixer Edit Modes**
- **Markers and Advanced Navigation**
- **Automation**
- **Layers and Drum Pads**
- **Master and EQ Modes**
- **Modifiers and Advanced Shortcuts**
- **Configuring DrivenByMoss**

The exact titles and order should wait until the remainder of the audit has been classified.

---

# Next Part of the Audit

The next pass should finish the remaining areas:

- display and layout controls
- ARM / MUTE / SOLO behaviour
- track banking and physical track/device movement
- utilities
- metronome and overdub
- assignable F-buttons
- footswitches
- extender functionality
- hardware preferences
- track-navigation preferences
- transport preferences
- workflow preferences
- Browser preferences

After those have been classified, the audit will be complete enough to design the **revised table of contents** before we alter any manuscript chapters.
