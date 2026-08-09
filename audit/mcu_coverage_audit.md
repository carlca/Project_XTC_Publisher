# Project XTC — DrivenByMoss MCU Coverage Audit

> **Purpose:** Compare the current Project XTC manuscript against the DrivenByMoss Mackie MCU feature set.
>
> **Source manuscript:** Project XTC Chapters 1–13
>
> **Reference:** DrivenByMoss `Mackie/Mackie-MCU.md`
>
> Status:
>
> * **✓ Covered adequately**
> * **△ Covered, but needs expansion or greater precision**
> * **✗ Missing**
> * **N/A Outside the intended X-Touch scope**

---

# 1. Initial Assessment

The existing Project XTC manuscript is strongest at explaining the **conceptual operation** of the X-Touch:

* banks and channels
* modes and context
* SELECT and focus
* displays and feedback
* V-Pots
* motor faders
* basic transport
* Device Mode
* Browser Mode
* development of a Mouse-Free / Mouse-Lite workflow

The principal weakness is not incorrect material, but **incomplete coverage of the deeper DrivenByMoss command set**.

In particular, modifier combinations involving:

* SHIFT
* OPTION
* CONTROL
* ALT

are currently under-represented.

The audit should therefore preserve the explanatory structure of Chapters 1–13 while adding the advanced functionality without turning the book into a button-reference manual.

---

# 2. Transport — Chapter 10

## Basic transport

| Feature                          | Status | Current location | Action                                       |
| -------------------------------- | ------ | ---------------- | -------------------------------------------- |
| PLAY — start playback            | ✓      | Chapter 10       | None                                         |
| STOP — stop playback             | ✓      | Chapter 10       | Expand exact repeated/double-click behaviour |
| RECORD — start recording         | ✓      | Chapter 10       | Expand modifier functions                    |
| REWIND — move play cursor left   | ✓      | Chapter 10       | Add marker modifier                          |
| FORWARD — move play cursor right | ✓      | Chapter 10       | Add marker modifier                          |
| Jog Wheel — move play cursor     | ✓      | Chapter 10       | Add modifier functions                       |

The fundamental transport model is already explained very well. The missing material should be added **after** the reader understands those basic controls, rather than inserted into their introductory descriptions.

## PLAY modifiers

| Feature                                  | Status | Proposed action   |
| ---------------------------------------- | ------ | ----------------- |
| Double-click PLAY — cursor to song start | ✗      | Add to Chapter 10 |
| SHIFT + PLAY — toggle repeat             | ✗      | Add to Chapter 10 |
| OPTION + PLAY — toggle Punch In          | ✗      | Add to Chapter 10 |
| OPTION + SHIFT + PLAY — toggle Punch Out | ✗      | Add to Chapter 10 |

**Editorial recommendation:** Introduce these together under a section such as **Beyond Basic Playback**.

The existing PLAY explanation should remain simple. The modifier commands can then be introduced as a second layer.

## STOP modifiers / repeated presses

| Feature                                | Status | Proposed action |
| -------------------------------------- | ------ | --------------- |
| STOP — stop playback                   | ✓      | Already taught  |
| STOP again — cursor to song start      | ✗      | Add             |
| Double-click STOP — cursor to song end | ✗      | Add             |

This is a good example of functionality that should be taught as a small workflow rather than merely listed.

## RECORD modifiers

| Feature                                                | Status | Proposed action |
| ------------------------------------------------------ | ------ | --------------- |
| RECORD — start/stop recording                          | ✓      | Already taught  |
| SHIFT + RECORD — Launcher overdub                      | ✗      | Add             |
| OPTION + RECORD — create clip, play and enable overdub | ✗      | Add             |

**Editorial note:** OPTION + RECORD is significant enough to deserve an explanation and practical example rather than a one-line reference entry.

## Marker navigation from Transport

| Feature                           | Status | Proposed action |
| --------------------------------- | ------ | --------------- |
| OPTION + REWIND — previous marker | ✗      | Add             |
| OPTION + FORWARD — next marker    | ✗      | Add             |

These should be cross-linked conceptually with Marker Mode rather than taught as unrelated REWIND/FAST FORWARD tricks.

---

# 3. Jog Wheel — Chapter 10

The existing chapter explains the Jog Wheel clearly as a means of navigating the timeline, but DrivenByMoss gives it substantially more functionality.

| Feature                                                  | Status | Proposed action                                                                 |
| -------------------------------------------------------- | ------ | ------------------------------------------------------------------------------- |
| Jog Wheel — move play cursor                             | ✓      | Already covered                                                                 |
| SHIFT + Jog Wheel — fine positioning                     | △      | Chapter discusses precise positioning, but modifier should be stated explicitly |
| OPTION + Jog Wheel — tempo                               | ✗      | Add                                                                             |
| OPTION + SHIFT + Jog Wheel — fine tempo                  | ✗      | Add                                                                             |
| CONTROL + Jog Wheel — loop start                         | ✗      | Add                                                                             |
| CONTROL + SHIFT + Jog Wheel — fine loop-start adjustment | ✗      | Add                                                                             |
| ALT + Jog Wheel — loop length                            | ✗      | Add                                                                             |
| ALT + SHIFT + Jog Wheel — fine loop-length adjustment    | ✗      | Add                                                                             |

**Editorial recommendation:** This deserves a compact visual table after the reader has mastered basic Jog Wheel navigation.

The underlying pattern is elegant:

```text
No modifier       → Position
OPTION            → Tempo
CONTROL           → Loop Start
ALT                → Loop Length

+ SHIFT            → Fine adjustment
```

Teaching the pattern is much easier than asking the reader to memorise eight unrelated commands.

---

# 4. Marker Functions

Marker functionality is one of the clearest omissions from the present manuscript.

| Feature                                          | Status | Proposed location          |
| ------------------------------------------------ | ------ | -------------------------- |
| MARKER — enter Marker Mode                       | ✗      | New Marker section/chapter |
| SHIFT + MARKER — toggle marker display           | ✗      | Same                       |
| OPTION + MARKER — create marker at play position | ✗      | Same                       |
| OPTION + REWIND — previous marker                | ✗      | Same + Chapter 10          |
| OPTION + FORWARD — next marker                   | ✗      | Same + Chapter 10          |
| V-Pot press in Marker Mode — play from marker    | ✗      | Same                       |

**Recommendation:** Do not bury Marker Mode inside Chapter 10.

It forms a coherent workflow of its own:

```text
Create Marker
     │
     ▼
See Markers
     │
     ▼
Navigate Markers
     │
     ▼
Start Playback
```

A dedicated **Markers and Navigation** section would make the OPTION + MARKER function that prompted this audit much easier to understand.

---

# 5. V-Pots — Chapter 8

Chapter 8 already does an excellent job of explaining what V-Pots *are*: endless rotary encoders, push switches and LED rings whose meanings change according to context.

However, the exact DrivenByMoss push operations are largely absent.

| Feature                                  | Status | Proposed action                          |
| ---------------------------------------- | ------ | ---------------------------------------- |
| Turn V-Pot — change current parameter    | ✓      | Covered                                  |
| Press V-Pot — context-sensitive action   | △      | Explained conceptually but not precisely |
| Press V-Pot — reset parameter to default | ✗      | Add                                      |
| SHIFT + press — centre value             | ✗      | Add                                      |
| CONTROL + press — minimum                | ✗      | Add                                      |
| ALT + press — maximum                    | ✗      | Add                                      |
| OPTION + press on Send — toggle Send     | ✗      | Add                                      |

This is an ideal place to replace some of the present deliberate vagueness with concrete functionality now that we have an authoritative reference.

A useful memory model would be:

```text
PRESS             → Default
SHIFT + PRESS     → Centre
CONTROL + PRESS   → Minimum
ALT + PRESS       → Maximum
OPTION + PRESS    → Context-specific
                     (e.g. Send on/off)
```

---

# 6. Motor Faders — Chapter 9

The basic motor-fader behaviour is **✓ covered adequately**.

The chapter correctly establishes:

* eight channel faders plus master fader
* physical movement changing Bitwig
* Bitwig changes moving the physical faders
* bank changes recalling new positions
* bidirectional feedback

Areas requiring expansion:

| Feature                                                | Status | Proposed action                       |
| ------------------------------------------------------ | ------ | ------------------------------------- |
| Track faders control banked track volume               | ✓      | Covered                               |
| Fader touch can select track                           | △      | Verify exact wording and expand       |
| Master fader controls master volume                    | ✓      | Covered                               |
| Touch Master Fader selects Master track                | △      | Expand                                |
| Touch Master Fader enters Master Edit Mode             | ✗      | Add when Master Mode is introduced    |
| SHIFT + Master Fader — metronome volume                | ✗      | Add                                   |
| FLIP — use faders like knobs                           | ✗      | Add                                   |
| SHIFT + FLIP — Instrument/Audio/Hybrid ↔ Effect tracks | ✗      | Add                                   |
| LOCK — lock faders                                     | ✗      | Add if applicable to X-Touch workflow |

The most important discovery here is **Master Edit Mode**. Touching the master fader is not merely a volume operation; it opens another layer of controller functionality.

That deserves treatment beyond Chapter 9's introductory explanation.

---

# 7. SELECT — Chapter 6

The current SELECT chapter establishes the essential concept extremely well:

> selection establishes focus.

That material should remain.

However, DrivenByMoss layers many advanced commands onto SELECT.

| Feature                                                        | Status | Proposed action |
| -------------------------------------------------------------- | ------ | --------------- |
| SELECT — select track                                          | ✓      | Covered         |
| SHIFT + SELECT — multi-select                                  | ✗      | Add             |
| OPTION + SELECT — stop playing clip                            | ✗      | Add             |
| CONTROL + SELECT — open/close group                            | ✗      | Add             |
| ALT + SELECT — set new clip length                             | ✗      | Add             |
| SEND + SELECT — choose Send 1–8                                | ✗      | Add             |
| SELECT selected group — enter group in hierarchical navigation | ✗      | Add later       |
| Long SELECT — leave group/folder                               | ✗      | Add later       |
| SELECT selected instrument track — enter Layer/Drum Pad Mode   | ✗      | Add later       |

**Editorial recommendation:** Do not put all of these into the introductory SELECT chapter.

Chapter 6 should continue teaching:

> **SELECT = focus**

The modifier and hierarchical functions belong in later advanced material, with cross-references back to Chapter 6.

---

# 8. Banks and Channels — Chapter 4

The core banking model is already covered:

| Feature                                            | Status |
| -------------------------------------------------- | ------ |
| BANK changes the visible/banked group of tracks    | ✓      |
| CHANNEL moves through tracks in smaller increments | ✓      |
| Eight physical strips represent a moving window    | ✓      |

Advanced functions are missing:

| Feature                                               | Status | Proposed action                                                                  |
| ----------------------------------------------------- | ------ | -------------------------------------------------------------------------------- |
| OPTION + BANK — move selected device left/right       | ✗      | Device/advanced section                                                          |
| OPTION + CHANNEL — move selected track left/right     | ✗      | Advanced navigation                                                              |
| BANK in Device Mode — previous/next device            | △      | Device Mode discusses device navigation conceptually; exact controls need adding |
| CHANNEL in Device Mode — previous/next parameter page | △      | Same                                                                             |

This is a particularly good example of why the existing mental-model chapters should not simply be expanded into reference manuals.

BANK and CHANNEL mean one thing in normal track navigation and another in Device Mode. The book should teach those differences **when the relevant context is introduced**.

---

# 9. Device Mode — Chapter 11

Chapter 11 already provides a strong conceptual explanation of:

```text
Track
  ↓
Device
  ↓
Parameter Page
  ↓
Parameter
```

It also explains eight-parameter pages and navigating device chains.

Coverage becomes weaker when we compare the text with the exact MCU operations.

| Feature                                          | Status | Proposed action      |
| ------------------------------------------------ | ------ | -------------------- |
| DEVICE — enter Device Mode                       | ✓      | Covered conceptually |
| V-Pots 1–8 — current device parameters           | ✓      | Covered              |
| BANK ←/→ — previous/next device                  | △      | Make explicit        |
| CHANNEL ←/→ — previous/next parameter page       | △      | Make explicit        |
| CONTROL held — display devices on selected track | ✗      | Add                  |
| CONTROL + V-Pot press — select displayed device  | ✗      | Add                  |
| OPTION held — display parameter pages            | ✗      | Add                  |
| OPTION + V-Pot press — select parameter page     | ✗      | Add                  |
| OPTION + DEVICE — pin cursor device              | ✗      | Add                  |
| DEVICE again — Project/Track Parameter Mode      | ✗      | Add                  |

This is one of the chapters that will benefit most from the audit.

The existing explanation gives us the **mental model**; the missing DrivenByMoss commands give us the **efficient physical workflow**.

---

# 10. Browser Mode — Chapter 12

Chapter 12 is conceptually thorough but deliberately non-specific about several controls.

DrivenByMoss lets us make it much more practical.

| Feature                                | Status | Proposed action                                              |
| -------------------------------------- | ------ | ------------------------------------------------------------ |
| BROWSER — open Browser                 | ✓      | Covered                                                      |
| Track Control knobs — navigate columns | △      | Navigation explained generally; identify controls explicitly |
| Press V-Pot — enter filter/results     | △      | Add exact behaviour                                          |
| Press again — confirm                  | △      | Add                                                          |
| Jog Wheel — scroll results             | △      | Add explicitly                                               |
| BROWSER / ENTER — confirm and close    | △      | Add                                                          |
| CANCEL / SHIFT + BROWSER — discard     | △      | Add                                                          |
| UP/DOWN — previous/next Browser tab    | ✗      | Add                                                          |
| LEFT — insert before current device    | ✗      | Add                                                          |
| RIGHT — insert after current device    | ✗      | Add                                                          |
| ZOOM — replace current device          | ✗      | Add                                                          |
| SHIFT + BROWSER — insert before        | ✗      | Add entry workflow                                           |
| OPTION + BROWSER — insert after        | ✗      | Add entry workflow                                           |

The present Browser chapter explains *why* and *how to think about* Browser Mode very effectively.

The audit suggests that its revision should now add a **concrete control map**.

---

# 11. Major Areas Apparently Missing Entirely

The first audit pass has already identified several substantial areas that are not simply minor omissions from existing chapters.

## Automation

**✗ Major gap**

DrivenByMoss provides:

* READ/OFF
* OPTION + READ/OFF
* WRITE
* TRIM
* TOUCH
* LATCH

This is enough functionality to justify dedicated teaching rather than a footnote.

**Candidate new chapter:** **Automation from the X-Touch**

---

## Layer / Drum Pad Modes

**✗ Major gap**

DrivenByMoss supports entering instrument layers/drum pads and controlling:

* Volume
* Pan
* Sends
* Mute
* Solo

This deserves consideration as advanced Device/Instrument material.

---

## Master Edit Mode

**✗ Major gap**

Touching the Master Fader provides access to:

* master volume
* master panorama
* audio-engine control
* previous project
* next project

This is sufficiently unusual that readers are unlikely to discover it accidentally.

---

## Marker Mode

**✗ Major gap**

This is the omission that triggered the audit and should definitely be added.

---

## EQ Mode

**✗ Major gap**

DrivenByMoss provides a dedicated EQ edit mode and, in Bitwig, can automatically add EQ+ when required.

This probably belongs adjacent to Device Mode rather than as an isolated chapter.

---

## Track / Volume / Panorama / Send Edit Modes

**△ Partially represented conceptually, insufficiently documented operationally**

The book already discusses pan, sends, V-Pots and tracks, but does not yet systematically explain the DrivenByMoss edit modes:

* Track (`tr`)
* Volume (`Vl`)
* Panorama (`Pn`)
* Send 1–8 (`S1`–`S8`)

These may warrant a unified **Mixer Edit Modes** chapter.

---

# 12. Emerging Editorial Structure

It is too early to renumber or rewrite the manuscript, but the audit is already suggesting a useful distinction:

```text
PART I
Understanding the X-Touch
        ↓
Existing conceptual chapters

PART II
Working with the X-Touch
        ↓
Existing practical chapters,
expanded with exact controls

PART III
Advanced Control
        ↓
Modifiers
Automation
Markers
Mixer Edit Modes
Layers / Drum Pads
Master Mode
Advanced Device functions
```

This is preferable to turning Chapters 1–13 into enormous encyclopaedic chapters.

The existing book's strength is that it **teaches ideas before commands**.

The feature audit should preserve that strength while ensuring that the advanced commands are no longer allowed to escape.
