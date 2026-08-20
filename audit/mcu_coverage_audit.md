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


# Part 2 Continued — Remaining Coverage Audit

# O. Display and Layout Controls

Chapter 7 already establishes the important principle that the X-Touch's displays are part of the control surface's feedback system rather than merely decoration.

The DrivenByMoss reference exposes several additional display controls that are not yet documented operationally.

| Function | Coverage | Proposed action |
|---|---|---|
| DISPLAY MODE — toggle track names in first display | ✗ | Add to Chapter 7 |
| TEMPO/TICKS — switch final segment-display digits between tempo and ticks | ✗ | Add to Chapter 7 |
| GLOBAL VIEW / EDIT — toggle VU meters | ✗ | Add to Chapter 7 |
| AUX — switch Bitwig to Arrange layout | ✗ | Mouse-Free workflow |
| BUSSES — switch Bitwig to Mix layout | ✗ | Mouse-Free workflow |
| OUTPUTS — switch Bitwig to Edit layout | ✗ | Mouse-Free workflow |

## Editorial recommendation

The three display functions belong naturally in Chapter 7.

The layout buttons are different. They are not principally about X-Touch feedback; they are commands for controlling **Bitwig's user interface**.

They therefore fit particularly well with Chapter 13's Mouse-Free / Mouse-Lite objective.

---

# P. Record Arm, Mute and Solo

The channel-strip ARM, MUTE and SOLO buttons are fundamental mixer controls and deserve more explicit treatment than they currently receive.

## Record Arm

| Function | Coverage | Proposed action |
|---|---|---|
| ARM 1–8 — arm individual track | △ | Make explicit |
| SHIFT + ARM — toggle record-arm state across active bank page | ✗ | Add |

The SHIFT behaviour is especially useful because it operates on the **current bank**, reinforcing the banking mental model established earlier in the book.

## Mute

| Function | Coverage | Proposed action |
|---|---|---|
| MUTE 1–8 — mute individual track/layer | △ | Make explicit |
| OPTION + MUTE — clear all mutes | ✗ | Add |
| SHIFT + MUTE — toggle monitor | ✗ | Add |

## Solo

| Function | Coverage | Proposed action |
|---|---|---|
| SOLO 1–8 — solo individual track/layer | △ | Make explicit |
| OPTION + SOLO — clear all solos | ✗ | Add |
| SHIFT + SOLO — toggle auto-monitor | ✗ | Add |

There is also a separate global SOLO command in the Utility section:

- SOLO — deactivate all solos
- SHIFT + SOLO — deactivate all mutes

Care will be required in the manuscript to distinguish **channel-strip SOLO buttons** from the MCU's global SOLO command.

## Editorial recommendation

These should form a coherent **Channel Strip Controls** section rather than being scattered between unrelated chapters.

The useful mental model is:

```text id="7xqfqu"
ARM       Can this track record?
MUTE      Can we hear this track?
SOLO      Do we hear this track in isolation?
SELECT    Is this the track we are working on?
```

That gives the reader meaning before modifier combinations.

---

# Q. Track Banking and Physical Reordering

Chapter 4 already explains BANK and CHANNEL extremely well as ways of moving the eight-strip hardware window across a larger Bitwig project.

That fundamental explanation should remain unchanged.

## Normal operation

| Function | Coverage |
|---|---|
| BANK ←/→ — move by eight tracks | ✓ |
| CHANNEL ←/→ — move by one track | ✓ |

## OPTION-modified operation

| Function | Coverage | Proposed action |
|---|---|---|
| OPTION + BANK ←/→ — move selected device left/right | ✗ | Add with advanced Device workflow |
| OPTION + CHANNEL ←/→ — move selected track left/right | ✗ | Add with advanced track workflow |

This distinction is extremely useful:

```text id="bdnuec"
BANK / CHANNEL
      │
      ├── normally → move the controller's VIEW
      │
      └── OPTION   → move something in the PROJECT
```

That is precisely the kind of pattern Project XTC should teach.

## Device Mode exception

In Device Mode:

```text id="myw0dt"
BANK ←/→       Previous / next device
CHANNEL ←/→    Previous / next parameter page
```

This is already partially covered conceptually in Chapter 11 but should be made explicit.

---

# R. Undo, Redo and Save

| Function | Coverage | Proposed action |
|---|---|---|
| UNDO — undo last action | ✗ | Add |
| SHIFT + UNDO — redo | ✗ | Add |
| SAVE — save current project | ✗ | Add |

These are simple commands but highly relevant to a Mouse-Free workflow.

They do not need lengthy explanations.

A small section such as **Everyday Project Commands** would be sufficient.

---

# S. Bitwig Window and Pane Control

DrivenByMoss maps several MCU buttons to Bitwig interface operations.

| X-Touch / MCU function | Result | Coverage |
|---|---|---|
| MIDI TRACKS / Note Editor | Toggle Note Editor pane | ✗ |
| INPUTS / Automation Editor | Toggle Automation Editor pane | ✗ |
| AUDIO TRACKS / Toggle Device | Toggle plug-in window | ✗ |
| SHIFT + Toggle Device | Toggle layouts | ✗ |
| OPTION + Toggle Device | Toggle selected device expanded state | ✗ |
| AUDIO INSTRUMENT / Mixer | Toggle Mixer pane | ✗ |

These functions are **extremely relevant** to Chapter 13.

They directly reduce the need to manipulate Bitwig's interface with a mouse.

## Editorial recommendation

Chapter 13 should eventually become more concrete by including a section such as:

**Controlling Bitwig's Workspace from the X-Touch**

This would turn the Mouse-Free / Mouse-Lite chapter from an aspiration into a practical workflow.

---

# T. Metronome

| Function | Coverage | Proposed action |
|---|---|---|
| CLICK / Metronome — toggle metronome | ✗ | Add |
| SHIFT + Metronome — toggle metronome ticks | ✗ | Add |
| SHIFT + Master Fader — metronome volume | ✗ | Add |

This is a particularly elegant little group because all three operations concern the same conceptual object.

They should be taught together rather than placing SHIFT + Master Fader solely in the Motor Faders chapter.

---

# U. Overdub

DrivenByMoss distinguishes Arranger and Launcher overdub.

| Function | Coverage |
|---|---|
| OVR / REPLACE — toggle Arranger overdub | ✗ |
| SHIFT + OVR — toggle Launcher overdub | ✗ |
| SHIFT + RECORD — toggle Launcher overdub | ✗ |
| OPTION + RECORD — create clip, start playback and enable overdub | ✗ |

This functionality deserves explanation in terms of **Arranger versus Launcher**, rather than as four arbitrary shortcuts.

There is also a DrivenByMoss preference that can flip the normal and SHIFT-modified Arranger/Launcher Record and Automation behaviours.

That preference makes it especially important that the guide explain the *concept* rather than simply promise that one particular button combination will always behave identically on every installation.

---

# V. F1–F8 and Assignable Functions

The MCU documentation states that the function buttons can be assigned through the DrivenByMoss settings.

| Function | Coverage |
|---|---|
| F1–F8 assignable functions | ✗ |
| Configurable F-button assignments | ✗ |
| Assign arbitrary Action | ✗ |

The preferences section specifically lists configuration for F1–F5.

This apparent F1–F8 / F1–F5 discrepancy should be **verified in the actual current DrivenByMoss settings UI** before we state anything stronger in the manuscript.

## Editorial recommendation

Do not document assumed default functions for F-buttons.

Instead explain them as a **customisable control resource** and show readers where their assignments are configured.

---

# W. Footswitches

DrivenByMoss exposes two MCU footswitch inputs:

- Footswitch 1 / USER A
- Footswitch 2 / USER B

Both are assignable.

**Coverage: ✗**

## Clip Based Looper

One assignable function deserves special attention.

When Clip Based Looper is assigned to a footswitch:

1. The selected MIDI clip slot is used.
2. If empty, a clip is created.
3. The configured New Clip Length is used.
4. Playback starts.
5. Holding the footswitch enables overdub.
6. Releasing it disables overdub.

This is not merely an obscure configuration option; it creates a genuine **hands-free performance workflow**.

## Editorial recommendation

Footswitches probably do not warrant their own chapter, but they deserve a substantial section in advanced workflow material.

---

# X. Extenders

DrivenByMoss supports up to four MCU-compatible devices.

Controllers can be configured as:

- Main
- Extender
- MCU Extender

A Main device provides the master fader and additional commands such as transport.

Multiple Main devices are supported.

Changing the extender configuration requires restarting the extension.

**Current Project XTC coverage: ✗**

## Scope decision required

Project XTC is primarily a guide to the standard Behringer X-Touch.

Therefore extender operation should probably be treated as **optional advanced material or an appendix**, rather than woven through the main learning path.

However, it should not be omitted entirely because the X-Touch Extender is explicitly supported and tested by DrivenByMoss.

---

# Y. Hardware Setup Preferences

The DrivenByMoss Hardware Setup section is much more important to Project XTC than initially apparent.

## X-Touch profile

The reference explicitly recommends the X-Touch profile and states that the controller itself should be in **MC mode**.

**Coverage: △**

Basic setup is already discussed, but the guide should eventually establish a known-good baseline configuration.

## Displays

Relevant options include:

- Main display
- Segment display
- Assignment display
- Display track names in first display
- X-Touch display colours

**Coverage: △**

Chapter 7 explains the hardware feedback well but does not systematically explain the corresponding DrivenByMoss preferences.

## Motor faders

Relevant preferences include:

- Has motor faders
- Use faders like editing knobs

**Coverage: △ / ✗**

The physical faders are well documented; the configurable alternative behaviour is not.

## VU meters

Relevant preferences include:

- enable VU meters
- choose Mackie VU implementation
- always send VU updates

**Coverage: △**

VU feedback is discussed, but configuration is not.

## Vertical Zoom

DrivenByMoss can optionally make UP/DOWN while Zoom is active select parameter modes.

**Coverage: ✗**

This should be documented as an optional behaviour rather than a standard command.

---

# Z. Segment Display Preferences

| Preference | Coverage |
|---|---|
| Display time or beats/measures | ✗ |
| Display tempo or ticks in final three digits | ✗ |

These belong naturally with Chapter 7's display material.

This also reinforces an important editorial principle:

> The guide should distinguish between what the X-Touch **can display** and what the user has **configured it to display**.

---

# AA. Track Preferences

## Include FX and Master tracks

DrivenByMoss can include FX and Master tracks in the normal track bank.

**Coverage: ✗**

This changes what the banking model actually contains and therefore deserves at least a note in the banking chapter or configuration chapter.

## Pin FX tracks to last device

When multiple controllers are used, FX tracks can be pinned to the right-most device.

**Coverage: ✗**

Likely extender/advanced material.

## Flat vs Hierarchical navigation

This is much more important.

DrivenByMoss supports:

### Flat

All tracks are presented together.

Selecting an already selected group can toggle its expanded state.

### Hierarchical

Groups/folders form navigation levels.

- SELECT a group.
- SELECT it again to enter.
- Long-press SELECT to leave.

**Coverage: ✗**

This deserves proper teaching because it fundamentally changes what SELECT and banking mean in a project containing groups.

### Editorial recommendation

Add **Navigating Groups and Folders** as advanced material following the basic banking and SELECT chapters.

---

# AB. Transport Preferences

Three preferences can change transport behaviour.

| Preference | Coverage |
|---|---|
| Behaviour on Stop | ✗ |
| Behaviour on Pause/PLAY stop | ✗ |
| Flip Arranger and Clip Record/Automation | ✗ |

This means that Chapter 10 should avoid presenting every transport behaviour as immutable.

A short configuration note can explain that DrivenByMoss allows some transport actions to be customised.

The Arranger/Launcher flip deserves particular attention for users whose workflow is Launcher-centric.

---

# AC. Play and Sequence Preferences

## Quantize Amount

DrivenByMoss allows the amount applied by Quantize to be configured.

100% aligns notes fully to the grid.

**Coverage: ✗**

At present this is peripheral to the main Project XTC learning path.

**Recommendation:** include in configuration/reference material rather than creating tutorial content unless Quantize itself becomes part of a later workflow chapter.

---

# AD. Workflow Preferences

This is one of the most useful preference groups for Project XTC.

## Exclude deactivated items

Deactivated tracks/items can be hidden from the controller banks.

**Coverage: ✗**

Useful advanced configuration.

## Startup Mode

The initial edit mode can be chosen.

**Coverage: ✗**

Useful configuration.

## New Clip Length

Controls the length of clips created by New/Clip Based Looper functionality.

**Coverage: ✗**

This connects directly to SELECT modifiers and footswitch workflows.

## Zoom

Arrow keys can optionally be used for Arranger zooming.

**Coverage: ✗**

## Select Channel on Fader Touch

**Coverage: △**

Our existing fader discussion should not imply that fader-touch selection is unconditional; it is configurable.

## Activate Volume Mode on Fader Touch

**Coverage: ✗**

This can temporarily put the controller into Volume Mode while a fader is touched.

## Knob Sensitivity Default

**Coverage: ✗**

## Knob Sensitivity Slow

**Coverage: ✗**

## Encoder Knob Slow Down

**Coverage: ✗**

These three are valuable troubleshooting/configuration material, especially if a user finds the X-Touch's encoders too fast or too slow.

---

# AE. Browser Preferences

DrivenByMoss allows unused Browser filter columns to be hidden.

**Coverage: ✗**

This is more significant than it initially sounds.

Chapter 12 teaches Browser Mode as navigation through a hierarchy of choices. Removing irrelevant filter columns can make that hardware workflow substantially faster and easier to comprehend.

**Recommendation:** add this as a practical optimisation near the end of the Browser chapter.

---

# AF. New Clip Length

The reference exposes New Clip Length in several places:

- SHIFT + Track SELECT buttons
- ALT + SELECT
- Workflow preferences
- Clip Based Looper

This is a good example of a feature that appears fragmented when reading a reference manual but becomes coherent when organised around **user intent**.

The Project XTC explanation should therefore introduce the concept once and then show the different ways it is used.

**Coverage: ✗**

---

# AG. Configuration Baseline

The audit has exposed a broader requirement that was not obvious when the first 13 chapters were written.

Project XTC needs to establish a **known configuration baseline**.

At minimum, the guide should record:

- X-Touch firmware expectation
- MC operating mode
- DrivenByMoss X-Touch profile
- display-colour configuration
- fader-touch behaviour
- track-navigation mode
- startup mode
- relevant Browser settings

Without such a baseline, two readers can follow the same instruction and see different behaviour because their DrivenByMoss preferences differ.

**Recommendation: high priority.**

---

# AH. Functions Outside the Main Scope

Not everything in the MCU documentation deserves equal treatment.

Candidates for appendix/reference-only coverage include:

- X-Touch One-specific configuration
- non-X-Touch display protocols
- controllers with only one fader
- Asparion/iCON-specific display options
- generic MCU Extender protocol details
- LOCK, which the source explicitly notes is not present on MCU
- detailed multi-controller FX pinning

These should remain in the audit so that their omission is **deliberate**, rather than accidental.

---

# Part 2 — Completed Assessment

The coverage audit now produces four broad categories.

## 1. Strong existing coverage

The first draft already teaches these concepts well:

- the physical X-Touch
- the eight-channel mental model
- banking
- modes and context
- SELECT as focus
- displays as feedback
- V-Pots as contextual encoders
- motor-fader feedback
- basic transport
- Device Mode concepts
- Browser Mode concepts
- the Mouse-Free / Mouse-Lite philosophy

These should be **preserved rather than rewritten wholesale**.

## 2. Existing chapters needing targeted expansion

The clearest candidates are:

- Chapter 4 — Banks and Channels
- Chapter 6 — SELECT
- Chapter 7 — Displays and Feedback
- Chapter 8 — V-Pots
- Chapter 9 — Motor Faders
- Chapter 10 — Transport Controls
- Chapter 11 — Device Mode
- Chapter 12 — Browser Mode
- Chapter 13 — Mouse-Free / Mouse-Lite Workflow

The additions should remain subordinate to each chapter's existing conceptual purpose.

## 3. Major functionality requiring new teaching material

The strongest candidates are:

- Mixer Edit Modes
- Modifiers
- Marker Mode
- Automation
- Layers / Drum Pads
- Master Edit Mode
- EQ Mode
- Groups and hierarchical navigation
- Bitwig workspace control
- advanced recording / overdub workflows

## 4. Configuration and reference material

A separate configuration section or appendix should cover:

- DrivenByMoss X-Touch profile
- hardware/display preferences
- track-navigation preferences
- workflow preferences
- transport preferences
- Browser preferences
- assignable F-buttons
- footswitches
- extender configuration

---

# Central Finding of Part 2

The audit began with a concern that Project XTC might have **missed a large amount of functionality**.

It has.

But that does **not** mean the existing manuscript is badly structured.

The first 13 chapters largely answer:

> **How should I think about this controller?**

The newly identified material answers:

> **Now that I understand it, what else can I make it do?**

That suggests a natural progression for the finished book:

```text id="edr0eo"
FOUNDATIONS
Understand the hardware and mental model
            │
            ▼
CORE WORKFLOW
Use tracks, faders, transport, devices and Browser
            │
            ▼
ADVANCED CONTROL
Modifiers, edit modes, markers, automation and hierarchy
            │
            ▼
MOUSE-LITE WORKFLOW
Control more of Bitwig directly from the X-Touch
            │
            ▼
CONFIGURATION & REFERENCE
Tune DrivenByMoss and look up individual commands
```

This preserves the accessibility of the first draft while giving us a route to comprehensive coverage.

---

# Part 2 Status

**Part 2 — Coverage Audit: COMPLETE**

The next stage should be **Part 3 — Revision Plan**.

Part 3 should not yet write new chapter prose.

Its job should be to:

1. decide the final high-level Parts of the book;
2. decide which existing chapters remain where they are;
3. identify the exact targeted additions to Chapters 1–13;
4. decide which new chapters are required;
5. determine their order;
6. assign every ✗ and △ item from this audit to a destination;
7. ensure no feature in `mcu_feature_inventory.md` is left unaccounted for;
8. produce a proposed revised `00_contents.md`.

Only after that plan is agreed should the manuscript itself be changed.
