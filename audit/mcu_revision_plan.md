# Project XTC — Revision Plan

## Part 3: Turning the MCU Audit into the Expanded Book

### Purpose

Parts 1 and 2 established:

1. what functionality DrivenByMoss exposes through the Mackie MCU implementation;
2. which of those functions Project XTC already covers;
3. which are partially covered;
4. which are currently missing.

Part 3 determines **where that material should go**.

The objective is not simply completeness.

Project XTC should remain a guide that teaches the X-Touch progressively rather than becoming a reformatted command reference.

---

# 1. Preserve the Existing Learning Path

The first important decision is:

> **Do not rebuild Chapters 1–13 from scratch.**

The existing sequence establishes a useful progression:

```text
Meet the hardware
       ↓
Understand channels and banks
       ↓
Understand modes
       ↓
Understand focus and SELECT
       ↓
Understand feedback
       ↓
Learn the principal physical controls
       ↓
Use Devices and Browser
       ↓
Move towards a Mouse-Lite workflow
```

The feature audit does not invalidate this structure.

Instead, it reveals a second level of knowledge that can be taught once this foundation exists.

---

# 2. Proposed Overall Structure

The expanded book should be divided into four broad Parts.

## Part I — Understanding the X-Touch

This is primarily conceptual.

Existing chapters remain largely intact:

1. Meet the X-Touch
2. Hardware Tour
3. The Mental Model
4. Banks and Channels
5. Modes
6. The SELECT Button
7. Displays and Feedback

The reader should reach the end of Part I understanding **what the controller is doing and why**.

---

## Part II — Working with the X-Touch

This is the practical core.

Existing chapters:

8. V-Pots (Rotary Encoders)
9. Motor Faders
10. Transport Controls
11. Device Mode
12. Browser Mode

These chapters require targeted expansion following the audit.

The reader should reach the end of Part II able to operate the main everyday functions confidently.

---

## Part III — Going Deeper

This is where most of the newly identified DrivenByMoss functionality belongs.

Provisional new chapters:

13. Modifiers and Advanced Controls
14. Mixer Edit Modes
15. Markers and Advanced Navigation
16. Automation
17. Groups, Layers and Drum Pads
18. Master and EQ Modes
19. Advanced Recording and Overdub

The exact division remains subject to refinement.

The important principle is that these are **coherent workflows**, not miscellaneous collections of shortcuts.

---

## Part IV — Building the Workflow

The existing Chapter 13 currently points towards this material.

Rather than leaving it as the conclusion of the basic chapters, it may ultimately work better **after the advanced material**.

Candidate structure:

20. Towards a Mouse-Free (or Mouse-Lite) Workflow
21. Configuring DrivenByMoss for the X-Touch
22. Customisation and Expansion
23. Quick Reference

This would allow the Mouse-Lite chapter to draw upon everything the reader has learned.

---

# 3. Important Proposed Change: Move Chapter 13

The existing Chapter 13 is currently:

> **Towards a Mouse-Free (or Mouse-Lite) Workflow**

Its subject is essentially the destination of the whole guide.

The audit has identified several functions that belong naturally to that goal:

- toggling the Note Editor;
- toggling the Automation Editor;
- toggling the Mixer;
- toggling plug-in windows;
- changing Bitwig layouts;
- undo and redo;
- saving;
- marker navigation;
- project switching;
- custom function buttons;
- footswitch workflows.

Consequently, Chapter 13 may currently occur **too early**.

## Recommendation

Do not rewrite it yet.

When the new advanced chapters exist, move it towards the end of the book and revise it as a synthesis chapter.

Its purpose then becomes:

> **Now that we know what the X-Touch can do, how much of a real Bitwig session can we conduct without reaching for the mouse?**

That is much stronger than merely introducing the possibility halfway through the finished book.

---

# 4. Targeted Revision — Chapter 4: Banks and Channels

## Preserve

- the eight-strip window mental model;
- the BANK versus CHANNEL distinction;
- the relationship between physical strips and Bitwig tracks.

## Add later

A short **Beyond Navigation** section explaining:

```text
BANK / CHANNEL
      │
      ├── Normal
      │     move the controller's view
      │
      └── OPTION
            move something in the project
```

Specifically:

- OPTION + BANK LEFT/RIGHT — move the selected device;
- OPTION + CHANNEL LEFT/RIGHT — move the selected track.

## Cross-reference

Device Mode changes the meanings of BANK and CHANNEL.

Do not explain Device Mode fully here; point forward to its chapter.

---

# 5. Targeted Revision — Chapter 5: Modes

Chapter 5 becomes increasingly important after the audit.

## Preserve

The existing concept that the same hardware controls can mean different things according to the current mode.

## Add

Introduce the broader family of DrivenByMoss modes without explaining them all yet:

- Track
- Volume
- Panorama
- Send
- Device
- EQ
- Instrument
- Browser
- Marker
- Master

This gives the reader a map.

Later chapters teach the individual destinations.

## Possible diagram revision

The existing `mode-overview` diagram could eventually be expanded to distinguish:

```text
             X-Touch Modes
                   │
       ┌───────────┴───────────┐
       │                       │
   Mixing/Edit             Workflow
      Modes                  Modes
       │                       │
 Track / Pan / Send      Browser / Marker
 Device / EQ / etc.
```

No diagram change should be made until the chapter structure is final.

---

# 6. Targeted Revision — Chapter 6: SELECT

## Preserve

The chapter's central idea:

> **SELECT establishes focus.**

## Add only a small teaser

Explain that SELECT acquires additional meanings when combined with modifiers or when navigating hierarchical structures.

Do not place the complete modifier table here.

## Advanced material assigned elsewhere

- SHIFT + SELECT — multi-selection;
- OPTION + SELECT — stop clip;
- CONTROL + SELECT — group control;
- ALT + SELECT — new clip length;
- SEND + SELECT — direct Send selection;
- repeated SELECT — enter groups or layers;
- long SELECT — leave a hierarchy.

These should be taught in the contexts where they make sense.

---

# 7. Targeted Revision — Chapter 7: Displays and Feedback

## Preserve

The existing feedback-loop explanation.

## Add

- DISPLAY MODE;
- TEMPO/TICKS;
- VU-meter toggle;
- configurable time versus beats/measures display;
- configurable tempo versus ticks;
- X-Touch display colours.

## Important distinction

Introduce explicitly:

> **Displayed information can depend on both the current controller state and the DrivenByMoss configuration.**

This prevents the guide from promising identical displays for differently configured systems.

---

# 8. Targeted Revision — Chapter 8: V-Pots

## Preserve

The current explanation of:

- endless encoders;
- LED rings;
- contextual assignment;
- push capability.

## Add

A compact section on **pressing rather than turning**:

| Action | Result |
|---|---|
| Press | Default value |
| SHIFT + Press | Centre |
| CONTROL + Press | Minimum |
| ALT + Press | Maximum |
| OPTION + Press | Context-specific function |

Explain Send on/off as the principal OPTION example.

## Cross-reference

Marker, Browser, Device and other modes give V-Pot presses additional context-specific meanings.

---

# 9. Targeted Revision — Chapter 9: Motor Faders

## Preserve

Almost all of the existing conceptual material.

## Add

- fader-touch selection as a configurable option;
- temporary Volume Mode on fader touch;
- Master Fader selecting the Master track;
- SHIFT + Master Fader controlling metronome volume;
- FLIP.

## Move elsewhere

Do not explain Master Edit Mode fully here.

Introduce it and point forward.

The existing promise that automation will be discussed later should point explicitly to the new Automation chapter.

---

# 10. Targeted Revision — Chapter 10: Transport Controls

This requires one of the largest expansions.

## Preserve

Basic PLAY, STOP, RECORD, REWIND, FORWARD and Jog Wheel explanations.

## Add sections rather than enlarging every introductory paragraph

### Beyond PLAY

- double-click PLAY;
- SHIFT + PLAY;
- OPTION + PLAY;
- OPTION + SHIFT + PLAY.

### Beyond STOP

- repeated STOP;
- double-click STOP.

### Recording shortcuts

- SHIFT + RECORD;
- OPTION + RECORD.

### Marker navigation

- OPTION + REWIND;
- OPTION + FORWARD.

Then point to the Marker chapter.

### The Jog Wheel as a Multi-Purpose Control

Teach the pattern:

| Modifier | Coarse | + SHIFT |
|---|---|---|
| none | Position | Fine position |
| OPTION | Tempo | Fine tempo |
| CONTROL | Loop start | Fine loop start |
| ALT | Loop length | Fine loop length |

## Also add

- SCRUB;
- NUDGE / Tap Tempo;
- ZOOM;
- arrow controls.

## Configuration note

STOP and PLAY behaviour can be affected by DrivenByMoss preferences.

---

# 11. Targeted Revision — Chapter 11: Device Mode

This chapter should receive a substantial practical upgrade.

## Preserve

The existing hierarchy:

```text
Track
 ↓
Device
 ↓
Parameter Page
 ↓
Parameter
```

## Map the hardware directly onto it

```text
BANK LEFT/RIGHT
      ↓
    Device

CHANNEL LEFT/RIGHT
      ↓
Parameter Page

V-Pots 1–8
      ↓
 Parameters
```

This is a strong candidate for a revised diagram.

## Add

- CONTROL held — expose devices;
- CONTROL + V-Pot — select device;
- OPTION held — expose parameter pages;
- OPTION + V-Pot — select page;
- OPTION + DEVICE — pin cursor device;
- DEVICE again — Project/Track Parameters.

This should make Chapter 11 substantially more useful without making it harder to understand.

---

# 12. Targeted Revision — Chapter 12: Browser Mode

## Preserve

The existing conceptual Browser workflow.

## Add a concrete hardware map

- V-Pots — Browser columns;
- V-Pot press — enter/select;
- Jog Wheel — results;
- ENTER/BROWSER — confirm;
- CANCEL — discard;
- UP/DOWN — Browser tabs;
- LEFT/RIGHT — insertion position;
- ZOOM — replacement.

## Add entry shortcuts

- SHIFT + BROWSER — insert before;
- OPTION + BROWSER — insert after.

## Add optimisation

Explain that unwanted Browser filter columns can be hidden in DrivenByMoss preferences.

This turns configuration into a practical workflow improvement rather than a dry preference-list item.

---

# 13. New Chapter — Modifiers and Advanced Controls

This chapter should introduce the modifier vocabulary itself.

The goal is **not** to reproduce every combination.

Teach how to think about:

- SHIFT;
- OPTION;
- CONTROL;
- ALT.

Show recurring patterns discovered in the audit.

For example:

```text
SHIFT       Often modifies precision or secondary behaviour

OPTION      Often changes the object or action being manipulated

CONTROL     Often exposes structural or minimum-value functions

ALT         Often exposes maximum or length functions
```

These should be presented as tendencies, **not universal rules**.

Then point readers to the context-specific chapters.

This chapter gives us somewhere to explain modifier logic once instead of reintroducing SHIFT, OPTION, CONTROL and ALT repeatedly.

---

# 14. New Chapter — Mixer Edit Modes

Teach these as one related system:

- Track Edit Mode;
- Volume Edit Mode;
- Panorama Edit Mode;
- Send 1–8 modes.

A useful overview:

```text
TRACK         Selected-track parameters
TRACK ×2      Eight track volumes
PAN           Eight track panoramas
SEND          Eight track send levels
```

Then explain:

- SEND cycling;
- SHIFT + SEND;
- SEND + SELECT.

This is much more coherent than distributing the information between Chapters 5, 6 and 8.

---

# 15. New Chapter — Markers and Advanced Navigation

Teach the complete marker workflow.

## Create

OPTION + MARKER

## Display

SHIFT + MARKER

## Enter Marker Mode

MARKER

## Choose marker

V-Pot press

## Navigate

OPTION + REWIND / FORWARD

This chapter should include a practical exercise:

```text
Create three markers
      ↓
Name them in Bitwig
      ↓
Enter Marker Mode
      ↓
Jump between them
      ↓
Navigate previous/next
```

This directly addresses the functionality that prompted the audit.

---

# 16. New Chapter — Automation

This is a definite new chapter.

## Begin from Chapter 9

Remind the reader that touch-sensitive motor faders become particularly valuable during automation.

## Teach

- READ/OFF;
- WRITE;
- TOUCH;
- LATCH;
- TRIM and Bitwig's limitation;
- OPTION + READ/OFF.

## Explain modes conceptually

Do not assume that names such as Touch and Latch are self-explanatory.

The chapter should explain **what happens when the user touches, moves and releases a fader** in each mode.

This could become one of the most practically useful chapters in the guide.

---

# 17. New Chapter — Groups, Layers and Drum Pads

This chapter develops the hierarchical ideas already introduced by SELECT and Device Mode.

Possible progression:

```text
Project
   ↓
Group
   ↓
Track
   ↓
Instrument
   ↓
Layer / Drum Pad
```

## Teach

- flat versus hierarchical track navigation;
- entering a group;
- leaving a group;
- entering Layer/Drum Pad Mode;
- controlling volume, pan and sends;
- mute and solo within layers.

This keeps hierarchical SELECT behaviour out of the introductory SELECT chapter.

---

# 18. New Chapter — Master and EQ Modes

These are currently paired provisionally because both are specialised edit modes.

## Master Mode

Teach:

- touch Master Fader;
- master volume;
- master panorama;
- audio engine;
- previous and next project.

## EQ Mode

Teach:

- entering EQ Mode;
- relationship to Device Mode;
- EQ+;
- automatic insertion when no EQ exists.

## Warning required

The automatic EQ+ insertion should be explicitly flagged:

> **Entering EQ Mode can modify the Bitwig project by inserting a device.**

If this chapter becomes too large or conceptually awkward, Master and EQ can later be separated.

---

# 19. New Chapter — Advanced Recording and Overdub

This chapter remains provisional.

It would unify:

- Arranger versus Launcher recording;
- Arranger overdub;
- Launcher overdub;
- OPTION + RECORD;
- New Clip Length;
- clip creation;
- Clip Based Looper;
- footswitch overdub workflow.

The advantage is that these commands become a **recording workflow**, rather than a collection of shortcuts.

Whether this deserves a complete chapter should be reconsidered once drafting begins.

---

# 20. Revised Mouse-Free / Mouse-Lite Chapter

Move the present Chapter 13 here.

Then expand it to synthesise:

- Note Editor;
- Automation Editor;
- Mixer pane;
- layouts;
- plug-in windows;
- device expansion;
- Browser;
- Device Mode;
- Marker navigation;
- SAVE;
- UNDO/REDO;
- project switching;
- F-buttons;
- footswitches.

The chapter can then answer a more interesting question:

> **How far can we actually get through a Bitwig session using the X-Touch as the principal interface?**

---

# 21. New Configuration Chapter

Provisional title:

## Configuring DrivenByMoss for the X-Touch

Establish the book's baseline:

- firmware;
- MC mode;
- X-Touch profile;
- display colours;
- VU configuration;
- track-navigation style;
- fader-touch options;
- Startup Mode;
- Browser filters;
- knob sensitivity;
- transport behaviour.

Clearly distinguish:

**Recommended Project XTC baseline**

from:

**Personal workflow choices**

That will prevent configuration preferences from being mistaken for requirements.

---

# 22. Customisation and Expansion

Potential material:

- F-buttons;
- assignable actions;
- Footswitch 1;
- Footswitch 2;
- Clip Based Looper;
- X-Touch Extender;
- multi-controller configuration.

This might become a short chapter or appendix.

---

# 23. Quick Reference

Only after all teaching chapters are complete should we build a command reference.

Possible organisation:

## By physical control

```text
PLAY
PLAY + SHIFT
PLAY + OPTION
...
```

## By task

```text
Markers
Automation
Devices
Recording
Navigation
...
```

Ideally provide **both indexes**.

This gives experienced readers rapid lookup without forcing beginners to learn from tables.

---

# 24. Proposed New Chapter Sequence

At this stage, the working sequence is:

```text
PART I — UNDERSTANDING THE X-TOUCH

01  Meet the X-Touch
02  Hardware Tour
03  The Mental Model
04  Banks and Channels
05  Modes
06  The SELECT Button
07  Displays and Feedback


PART II — WORKING WITH THE X-TOUCH

08  V-Pots (Rotary Encoders)
09  Motor Faders
10  Transport Controls
11  Device Mode
12  Browser Mode


PART III — GOING DEEPER

13  Modifiers and Advanced Controls
14  Mixer Edit Modes
15  Markers and Advanced Navigation
16  Automation
17  Groups, Layers and Drum Pads
18  Master and EQ Modes
19  Advanced Recording and Overdub


PART IV — BUILDING THE WORKFLOW

20  Towards a Mouse-Free (or Mouse-Lite) Workflow
21  Configuring DrivenByMoss for the X-Touch
22  Customisation and Expansion
23  Quick Reference
```

This numbering is **provisional**.

No manuscript filenames should be renamed yet.

---

# 25. Feature-Assignment Check

Before Part 3 can be declared complete, every △ and ✗ item from `mcu_coverage_audit.md` should be mapped to one of:

```text
Existing chapter revision
        │
        ├── Chapter 4
        ├── Chapter 5
        ├── ...
        └── Chapter 12

New teaching chapter
        │
        ├── Modifiers
        ├── Mixer Modes
        ├── Markers
        ├── Automation
        ├── Hierarchies
        ├── Master/EQ
        └── Recording

Workflow synthesis
        │
        └── Mouse-Free / Mouse-Lite

Configuration/reference
        │
        ├── DrivenByMoss Configuration
        ├── Customisation
        └── Quick Reference

Explicitly out of scope
```

Nothing should remain simply **✗ Missing** once Part 3 is finished.

That is the final completeness test.

---

# 26. Part 3 Status

**Revision architecture established.**

The next Part 3 task is **not yet manuscript writing**.

It should be a **feature-assignment matrix**:

1. take every missing or partial item identified in Part 2;
2. assign it to the proposed chapter that will own it;
3. identify any duplication between chapters;
4. identify anything that belongs only in configuration/reference material;
5. explicitly mark anything deliberately out of scope.

Once that matrix contains no unassigned features, we can confidently produce the revised `00_contents.md`.

Only then should we start editing Chapters 1–13 or writing the new chapters.


# Part 3 Continued — Feature Assignment Matrix

## Purpose

This matrix assigns the incomplete and missing functionality identified in `mcu_coverage_audit.md` to a definite destination in the revised Project XTC structure.

Every item should end in one of four states:

- **Existing chapter revision**
- **New teaching chapter**
- **Configuration / reference material**
- **Deliberately out of scope**

Some features appear in more than one chapter because they are relevant in more than one context. In those cases, one chapter is designated the **primary teaching location** and the other receives only a reminder or cross-reference.

The objective is that no meaningful X-Touch/DrivenByMoss feature remains merely marked **Missing**.

---

# 1. Chapter 4 — Banks and Channels

## Primary additions

| Feature | Destination | Treatment |
|---|---|---|
| OPTION + BANK LEFT/RIGHT — move selected device | Chapter 4 + Chapter 11 | Brief introduction here; full explanation in Device Mode |
| OPTION + CHANNEL LEFT/RIGHT — move selected track | Chapter 4 | Explain as physical project reordering |
| BANK behaviour changes in Device Mode | Chapter 4 + Chapter 11 | Cross-reference only here |
| CHANNEL behaviour changes in Device Mode | Chapter 4 + Chapter 11 | Cross-reference only here |
| FX/Master tracks optionally included in track bank | Chapter 21 | Configuration note referenced from Chapter 4 |
| Flat versus hierarchical banking | Chapter 17 | Mention only that alternate navigation models exist |

## Editorial purpose

Chapter 4 remains principally about:

> **The eight-channel physical window onto a larger project.**

Advanced variations should not obscure that model.

---

# 2. Chapter 5 — Modes

## Primary additions

| Feature | Destination | Treatment |
|---|---|---|
| Track Edit Mode | Chapter 5 → Chapter 14 | Introduce name only |
| Volume Edit Mode | Chapter 5 → Chapter 14 | Introduce name only |
| Panorama Edit Mode | Chapter 5 → Chapter 14 | Introduce name only |
| Send Edit Modes | Chapter 5 → Chapter 14 | Introduce name only |
| Device Edit Mode | Chapter 5 → Chapter 11 | Existing coverage |
| EQ Mode | Chapter 5 → Chapter 18 | Introduce name |
| Instrument Mode | Chapter 5 / Chapter 17 | Clarify relationship to instruments/layers |
| Browser Mode | Chapter 5 → Chapter 12 | Existing coverage |
| Marker Mode | Chapter 5 → Chapter 15 | Introduce name |
| Master Edit Mode | Chapter 5 → Chapter 18 | Introduce name |
| Project/Track Parameter Mode | Chapter 5 → Chapter 11 | Mention as Device-related mode |

## Editorial purpose

Chapter 5 becomes the **map of the mode system**, not the place where all modes are exhaustively documented.

---

# 3. Chapter 6 — SELECT

## Primary additions

| Feature | Primary destination | Secondary reference |
|---|---|---|
| SHIFT + SELECT — multi-select | Chapter 13 | Chapter 6 teaser |
| OPTION + SELECT — stop playing clip | Chapter 19 | Chapter 6 teaser |
| CONTROL + SELECT — open/close group | Chapter 17 | Chapter 6 teaser |
| ALT + SELECT — new clip length | Chapter 19 | Chapter 6 teaser |
| SEND + SELECT — directly choose Send 1–8 | Chapter 14 | Chapter 6 teaser |
| Repeated SELECT enters group | Chapter 17 | Chapter 6 |
| Long SELECT leaves group | Chapter 17 | Chapter 6 |
| Repeated SELECT enters Layers/Drum Pad Mode | Chapter 17 | Chapter 6 |

## Editorial purpose

Preserve:

> **SELECT establishes focus.**

Do not turn Chapter 6 into a modifier-reference chapter.

---

# 4. Chapter 7 — Displays and Feedback

## Primary additions

| Feature | Destination |
|---|---|
| DISPLAY MODE — toggle track names | Chapter 7 |
| TEMPO/TICKS display toggle | Chapter 7 |
| GLOBAL VIEW / EDIT — toggle VU meters | Chapter 7 |
| Display time versus beats/measures | Chapter 7 + Chapter 21 |
| Tempo versus ticks preference | Chapter 7 + Chapter 21 |
| X-Touch display colours | Chapter 21 |
| VU meter configuration | Chapter 21 |
| Main/segment/assignment display preferences | Chapter 21 |
| Always-send-VU preference | Chapter 21 |

## Editorial distinction

Chapter 7 explains **what feedback means**.

Chapter 21 explains **how that feedback is configured**.

---

# 5. Chapter 8 — V-Pots

## Primary additions

| Feature | Destination |
|---|---|
| V-Pot press — reset to default | Chapter 8 |
| SHIFT + press — centre | Chapter 8 |
| CONTROL + press — minimum | Chapter 8 |
| ALT + press — maximum | Chapter 8 |
| OPTION + press — context-sensitive | Chapter 8 |
| OPTION + press on Send — toggle Send | Chapter 14, referenced from Chapter 8 |
| Knob sensitivity default | Chapter 21 |
| Slow sensitivity | Chapter 21 |
| Encoder slowdown | Chapter 21 |

## Pattern to teach

```text
PRESS              Default
SHIFT + PRESS      Centre
CONTROL + PRESS    Minimum
ALT + PRESS        Maximum
OPTION + PRESS     Context-dependent
```

---

# 6. Chapter 9 — Motor Faders

## Primary additions

| Feature | Destination |
|---|---|
| Select channel on fader touch | Chapter 9 + Chapter 21 |
| Activate Volume Mode on fader touch | Chapter 9 + Chapter 21 |
| Master-fader touch selects Master track | Chapter 9 |
| Master-fader touch enters Master Edit Mode | Chapter 18 |
| SHIFT + Master Fader — metronome volume | Chapter 19 |
| FLIP — use faders like knobs | Chapter 13 / Chapter 14 |
| SHIFT + FLIP — regular tracks vs Effect tracks | Chapter 13 |
| Motor-fader preference | Chapter 21 |

## Explicit cross-reference

Chapter 9's existing discussion of automation should point forward to **Chapter 16 — Automation**.

---

# 7. Chapter 10 — Transport Controls

## PLAY family

| Feature | Destination |
|---|---|
| Double PLAY — cursor to song start | Chapter 10 |
| SHIFT + PLAY — Repeat | Chapter 10 |
| OPTION + PLAY — Punch In | Chapter 10 |
| OPTION + SHIFT + PLAY — Punch Out | Chapter 10 |

## STOP family

| Feature | Destination |
|---|---|
| STOP again — cursor to start | Chapter 10 |
| Double STOP — cursor to end | Chapter 10 |
| Configurable Stop behaviour | Chapter 21 |

## RECORD family

| Feature | Primary destination |
|---|---|
| SHIFT + RECORD — Launcher overdub | Chapter 19 |
| OPTION + RECORD — create clip/play/overdub | Chapter 19 |
| Record behaviour preference | Chapter 21 |

Chapter 10 should mention these and point forward rather than fully teaching Launcher workflows.

## REWIND/FORWARD

| Feature | Destination |
|---|---|
| OPTION + REWIND — previous marker | Chapter 15, introduced in Chapter 10 |
| OPTION + FORWARD — next marker | Chapter 15, introduced in Chapter 10 |

## Jog Wheel

| Feature | Destination |
|---|---|
| SHIFT + Jog — fine position | Chapter 10 |
| OPTION + Jog — tempo | Chapter 10 |
| OPTION + SHIFT + Jog — fine tempo | Chapter 10 |
| CONTROL + Jog — loop start | Chapter 10 |
| CONTROL + SHIFT + Jog — fine loop start | Chapter 10 |
| ALT + Jog — loop length | Chapter 10 |
| ALT + SHIFT + Jog — fine loop length | Chapter 10 |

## Other navigation controls

| Feature | Destination |
|---|---|
| Arrow buttons behave as keyboard arrows | Chapter 10 |
| ZOOM + horizontal arrows | Chapter 10 |
| ZOOM + vertical arrows / track height | Chapter 10 |
| Optional vertical Zoom parameter-mode behaviour | Chapter 21 |
| SCRUB cycles editing modes | Chapter 10 |
| NUDGE performs Tap Tempo | Chapter 10 |
| REPEAT button | Chapter 10 |

---

# 8. Chapter 11 — Device Mode

## Primary additions

| Feature | Destination |
|---|---|
| BANK LEFT/RIGHT — previous/next device | Chapter 11 |
| CHANNEL LEFT/RIGHT — parameter pages | Chapter 11 |
| Hold CONTROL — expose devices | Chapter 11 |
| CONTROL + V-Pot press — choose device | Chapter 11 |
| Hold OPTION — expose parameter pages | Chapter 11 |
| OPTION + V-Pot press — choose page | Chapter 11 |
| OPTION + DEVICE — pin cursor device | Chapter 11 |
| DEVICE again — Project/Track Parameter Mode | Chapter 11 |
| Project/Track parameter control | Chapter 11 |
| OPTION + BANK moves device outside Device Mode | Chapter 11 + Chapter 4 |

## Diagram candidate

Revise the device hierarchy diagram to map:

```text
BANK               Device
CHANNEL             Parameter Page
V-Pots              Parameters
```

---

# 9. Chapter 12 — Browser Mode

## Primary additions

| Feature | Destination |
|---|---|
| Track-control knobs navigate columns | Chapter 12 |
| V-Pot press enters filter/results | Chapter 12 |
| V-Pot press confirms | Chapter 12 |
| Jog Wheel scrolls results | Chapter 12 |
| BROWSER/ENTER confirms and closes | Chapter 12 |
| CANCEL discards | Chapter 12 |
| SHIFT + BROWSER while browsing discards | Chapter 12 |
| UP/DOWN — Browser tabs | Chapter 12 |
| LEFT — insert before | Chapter 12 |
| RIGHT — insert after | Chapter 12 |
| ZOOM — replace device | Chapter 12 |
| SHIFT + BROWSER from normal operation — insert before | Chapter 12 |
| OPTION + BROWSER — insert after | Chapter 12 |
| Hide unwanted Browser filter columns | Chapter 21, practical note in Chapter 12 |

---

# 10. Chapter 13 — Modifiers and Advanced Controls

## Primary ownership

This chapter owns the **modifier vocabulary**, not every modifier combination.

| Feature | Destination |
|---|---|
| SHIFT concept | Chapter 13 |
| OPTION concept | Chapter 13 |
| CONTROL concept | Chapter 13 |
| ALT concept | Chapter 13 |
| UNDO | Chapter 13 / Chapter 20 |
| SHIFT + UNDO — Redo | Chapter 13 / Chapter 20 |
| SAVE | Chapter 13 / Chapter 20 |
| FLIP | Chapter 13 |
| SHIFT + FLIP | Chapter 13 |
| CANCEL outside Browser — Escape | Chapter 13 |
| ENTER outside Browser — Enter | Chapter 13 |

## Modifier examples

Use examples already taught elsewhere rather than duplicating complete command sets.

The chapter should explain that modifier meanings are **patterns and tendencies**, not guarantees.

---

# 11. Chapter 14 — Mixer Edit Modes

## Track Edit Mode

Owns:

- TRACK enters Track Edit Mode;
- TRACK again enters Volume Edit Mode;
- PAN twice alternative where documented;
- track-parameter V-Pot assignments;
- fine adjustment with SHIFT;
- Crossfader/Sends preference variation.

## Volume Mode

Owns:

- eight V-Pots controlling channel volumes;
- SHIFT fine control.

## Panorama Mode

Owns:

- PAN;
- eight panorama controls;
- SHIFT fine control.

## Send Modes

Owns:

- SEND;
- repeated SEND cycles Send 1–8;
- SHIFT + SEND cycles backwards;
- SEND + SELECT 1–8 direct selection;
- V-Pots control send across eight tracks;
- SHIFT fine control;
- OPTION + V-Pot press toggles Send.

## Related channel-strip controls

Briefly cross-reference:

- ARM;
- MUTE;
- SOLO;
- faders;
- SELECT.

These remain general channel-strip functions rather than Edit Mode functions.

---

# 12. Chapter 15 — Markers and Advanced Navigation

## Primary ownership

| Feature | Destination |
|---|---|
| MARKER — enter Marker Mode | Chapter 15 |
| SHIFT + MARKER — show/hide markers | Chapter 15 |
| OPTION + MARKER — create marker | Chapter 15 |
| OPTION + REWIND — previous marker | Chapter 15 |
| OPTION + FORWARD — next marker | Chapter 15 |
| V-Pot press on marker — play from marker | Chapter 15 |

This chapter closes the gap that originally triggered the full audit.

---

# 13. Chapter 16 — Automation

## Primary ownership

| Feature | Destination |
|---|---|
| READ/OFF | Chapter 16 |
| OPTION + READ/OFF — reset overrides | Chapter 16 |
| WRITE | Chapter 16 |
| TRIM maps to Read | Chapter 16 |
| TOUCH | Chapter 16 |
| LATCH | Chapter 16 |
| Motor-fader touch behaviour during automation | Chapter 16 |
| Automation playback feedback | Chapter 16, building on Chapter 9 |
| Flip Arranger/Clip automation preference | Chapter 21 |

## Important teaching requirement

Explain the behaviour of each automation mode in terms of:

> **touch → move → release**

rather than merely defining button labels.

---

# 14. Chapter 17 — Groups, Layers and Drum Pads

## Group navigation

Owns:

- flat navigation;
- hierarchical navigation;
- SELECT group;
- SELECT again to enter;
- long SELECT to leave;
- CONTROL + SELECT group expansion;
- flat-mode expanded-state behaviour.

## Layers / Drum Pads

Owns:

- enter Layers Mode by repeated SELECT;
- leave Layers Mode by long SELECT;
- Volume;
- Panorama;
- Sends;
- Mute;
- Solo.

## Configuration

Choice of flat/hierarchical navigation is configured in Chapter 21.

---

# 15. Chapter 18 — Master and EQ Modes

## Master Edit Mode

Owns:

| Control | Function |
|---|---|
| Master-fader touch | Enter Master Mode |
| V-Pot 1 | Master volume |
| V-Pot 1 press | Reset master volume |
| V-Pot 2 | Master panorama |
| V-Pot 2 press | Reset panorama |
| V-Pots 3–5 press | Audio-engine controls |
| V-Pot 7 press | Previous project |
| V-Pot 8 press | Next project |

## EQ Mode

Owns:

- EQ button;
- EQ+ association;
- Device-Mode-like parameter navigation;
- automatic EQ+ insertion when no EQ exists.

## Required warning

> Entering EQ Mode may modify the Bitwig project by inserting EQ+.

---

# 16. Chapter 19 — Advanced Recording and Overdub

## Record/overdub ownership

| Feature | Destination |
|---|---|
| SHIFT + RECORD — Launcher overdub | Chapter 19 |
| OPTION + RECORD — create clip/play/overdub | Chapter 19 |
| OVR — Arranger overdub | Chapter 19 |
| SHIFT + OVR — Launcher overdub | Chapter 19 |
| Arranger vs Launcher distinction | Chapter 19 |
| New Clip Length | Chapter 19 |
| ALT + SELECT — choose new clip length | Chapter 19 |
| SHIFT + Track SELECT — choose new clip length | Chapter 19 |
| Clip Based Looper | Chapter 22, introduced here |
| Footswitch overdub workflow | Chapter 22, referenced here |
| Flip Arranger/Clip Record preference | Chapter 21 |

## Status

This chapter remains provisional, but the matrix confirms that it has enough coherent material to justify its existence.

---

# 17. Chapter 20 — Towards a Mouse-Free (or Mouse-Lite) Workflow

The existing Chapter 13 moves here and becomes a synthesis chapter.

## New material to incorporate

| Function | Destination |
|---|---|
| Note Editor pane toggle | Chapter 20 |
| Automation Editor pane toggle | Chapter 20 |
| Mixer pane toggle | Chapter 20 |
| Plug-in window toggle | Chapter 20 |
| SHIFT + Toggle Device — layouts | Chapter 20 |
| OPTION + Toggle Device — expanded state | Chapter 20 |
| AUX — Arrange layout | Chapter 20 |
| BUSSES — Mix layout | Chapter 20 |
| OUTPUTS — Edit layout | Chapter 20 |
| UNDO/REDO | Chapter 20, initially taught in Chapter 13 |
| SAVE | Chapter 20, initially taught in Chapter 13 |
| Marker navigation | Chapter 20, taught in Chapter 15 |
| Device/Browser workflows | Chapter 20 |
| Project switching | Chapter 20, taught in Chapter 18 |
| Metronome operations | Chapter 20 / Chapter 19 |
| Custom buttons | Chapter 22 |
| Footswitch workflows | Chapter 22 |

## Purpose

This chapter should demonstrate **complete workflows**, not introduce unfamiliar commands.

---

# 18. Chapter 21 — Configuring DrivenByMoss for the X-Touch

## Baseline configuration

Owns:

- recommended firmware level;
- MC operating mode;
- DrivenByMoss X-Touch profile;
- X-Touch display colours.

## Display preferences

Owns:

- main display;
- segment display;
- assignment display;
- track-name display;
- time vs beats/measures;
- tempo vs ticks;
- VU configuration.

## Fader preferences

Owns:

- motor-fader setting;
- use faders like knobs;
- select channel on fader touch;
- activate Volume Mode on touch.

## Navigation preferences

Owns:

- flat versus hierarchical track navigation;
- include FX/Master tracks;
- exclude deactivated items;
- startup mode.

## Transport preferences

Owns:

- Stop behaviour;
- Pause/PLAY-stop behaviour;
- Arranger/Launcher Record/Automation flip.

## Encoder preferences

Owns:

- default sensitivity;
- slow sensitivity;
- encoder slowdown.

## Browser preferences

Owns:

- hidden Browser filter columns.

## Other

- New Clip Length default;
- Zoom behaviour;
- Quantize amount.

---

# 19. Chapter 22 — Customisation and Expansion

## Function buttons

Owns:

- assignable F-buttons;
- arbitrary Action assignment;
- discrepancy between F1–F8 general documentation and F1–F5 preference listing must be verified before final publication.

## Footswitches

Owns:

- Footswitch 1 / USER A;
- Footswitch 2 / USER B;
- custom assignments;
- Clip Based Looper.

## Extenders

Owns:

- Main;
- Extender;
- MCU Extender;
- multiple devices;
- restart requirement after configuration changes;
- master/transport role of Main unit.

## Optional material

- FX-track pinning with multiple controllers.

---

# 20. Chapter 23 — Quick Reference

Every practical command taught in Chapters 1–22 should eventually appear here.

## Two indexes

### By physical control

Examples:

```text
PLAY
SHIFT + PLAY
OPTION + PLAY

MARKER
SHIFT + MARKER
OPTION + MARKER
```

### By task

Examples:

```text
Playback
Recording
Markers
Automation
Devices
Browser
Mixing
Groups
Configuration
```

The reference must be **generated from the finished teaching structure**, not used to design it.

---

# 21. General Channel-Strip Controls

Several functions do not justify separate chapters but need a clear teaching home.

## ARM

| Feature | Destination |
|---|---|
| ARM individual track | Chapter 14 |
| SHIFT + ARM across bank | Chapter 14 |

## MUTE

| Feature | Destination |
|---|---|
| MUTE individual track/layer | Chapter 14 |
| OPTION + MUTE — clear all mutes | Chapter 14 |
| SHIFT + MUTE — monitor | Chapter 14 |

## SOLO

| Feature | Destination |
|---|---|
| SOLO individual track/layer | Chapter 14 |
| OPTION + SOLO — clear solos | Chapter 14 |
| SHIFT + SOLO — auto-monitor | Chapter 14 |
| Global SOLO — clear all solos | Chapter 13 / Chapter 20 |
| SHIFT + global SOLO — clear all mutes | Chapter 13 / Chapter 20 |

Care must be taken to distinguish channel-strip buttons from global MCU commands.

---

# 22. Metronome

## Primary destination

Chapter 19 or Chapter 20, with basic use also appearing in Chapter 10 where appropriate.

Owns:

- CLICK / Metronome;
- SHIFT + Metronome — ticks;
- SHIFT + Master Fader — metronome volume.

The three controls should be explained together as one workflow.

---

# 23. Project Operations

| Feature | Primary destination |
|---|---|
| SAVE | Chapter 13 / Chapter 20 |
| UNDO | Chapter 13 / Chapter 20 |
| REDO | Chapter 13 / Chapter 20 |
| DROP — duplicate selected track | Chapter 13 / Chapter 20 |
| Previous/next project | Chapter 18 / Chapter 20 |

---

# 24. Functions Assigned to Configuration / Reference Only

The following need documenting but do not require major tutorial treatment:

- Quantize Amount;
- low-level display protocol choices not relevant to X-Touch;
- always-send-VU option;
- multi-controller FX pinning;
- Extender restart requirement;
- detailed generic MCU display settings not used by the X-Touch profile.

These belong in Chapter 21, Chapter 22 or Chapter 23.

---

# 25. Deliberately Out of Scope

The following should remain represented in the audit but need not become normal Project XTC teaching material unless the scope later expands.

## Other hardware-specific behaviour

- X-Touch One-specific functionality;
- Asparion-specific settings;
- iCON-specific settings;
- single-fader-controller options unrelated to the X-Touch;
- non-X-Touch display implementations.

## LOCK

The source notes that LOCK is not present on the standard MCU.

Unless testing shows a relevant X-Touch mapping, it should be marked:

**N/A — no normal X-Touch teaching requirement.**

## Deep MCU protocol implementation

Project XTC is a user's companion, not an MCU protocol-development specification.

Raw MIDI implementation details remain outside scope unless they directly help diagnose a practical X-Touch problem.

---

# 26. Items Requiring Verification Before Publication

The audit has identified a small number of points that should be tested rather than simply copied from the reference.

## F-button count

The general functionality documentation refers to F1–F8.

The preferences documentation specifically lists F1–F5.

**Action:** verify against the current DrivenByMoss configuration UI.

## Modifier labels

The physical X-Touch button legends and DrivenByMoss terminology should be checked so that OPTION, CONTROL and ALT are named exactly as readers see them.

## EQ automatic insertion

Verify that current DrivenByMoss/Bitwig behaviour still inserts EQ+ automatically when entering EQ Mode on a track without an equalizer.

## Master Mode audio-engine controls

Verify the exact current behaviour of V-Pots 3–5.

## Track navigation preferences

Verify the current UI names for Flat and Hierarchical navigation.

## Fader-touch behaviour

Verify defaults for:

- Select Channel on Fader Touch;
- Activate Volume Mode on Fader Touch.

These are preferences and should never be described as unconditional unless the Project XTC baseline explicitly enables them.

---

# 27. Duplication Rules

Some functionality naturally appears in more than one chapter.

To prevent repetition, use the following rule:

> **Teach once, remind elsewhere.**

Examples:

### OPTION + REWIND

- **Teach:** Chapter 15 — Markers
- **Mention:** Chapter 10 — Transport

### SHIFT + Master Fader

- **Teach:** Metronome workflow
- **Mention:** Chapter 9 — Motor Faders

### OPTION + BANK

- **Teach:** Chapter 11 — Device Mode
- **Mention:** Chapter 4 — Banking

### Browser filters

- **Teach configuration:** Chapter 21
- **Practical recommendation:** Chapter 12

### Fader-touch selection

- **Explain effect:** Chapter 9
- **Explain configuration:** Chapter 21

This approach preserves completeness without making the book repetitive.

---

# 28. Feature Assignment Outcome

All major △ and ✗ items identified by Part 2 now have a destination.

The revised structure accounts for:

- banking variants;
- modifier behaviour;
- SELECT modifiers;
- display controls;
- V-Pot press functions;
- fader-touch options;
- advanced transport;
- Jog Wheel modifiers;
- Marker Mode;
- Device navigation;
- Browser controls;
- mixer edit modes;
- channel ARM/MUTE/SOLO controls;
- Automation modes;
- group navigation;
- Layers and Drum Pads;
- Master Mode;
- EQ Mode;
- advanced recording;
- Arranger/Launcher overdub;
- New Clip Length;
- Bitwig pane/layout control;
- metronome functions;
- Save/Undo/Redo;
- F-buttons;
- footswitches;
- Clip Based Looper;
- Extenders;
- DrivenByMoss hardware/workflow/transport/Browser preferences.

No substantial X-Touch-relevant feature identified by the coverage audit remains without a proposed home.

---

# 29. Part 3 Completeness Check

The editorial pipeline is now:

```text
DrivenByMoss MCU Reference
            │
            ▼
mcu_feature_inventory.md
            │
            ▼
mcu_coverage_audit.md
            │
            ▼
revision_plan.md
            │
            ├── Existing chapter revisions
            ├── New teaching chapters
            ├── Configuration/reference
            └── Explicit exclusions
            │
            ▼
Revised Contents
            │
            ▼
Manuscript Revision
```

The feature-assignment stage is therefore **complete**.

---

# 30. Next Part 3 Task

The next task is to turn this architecture into the **proposed revised Contents page**.

That should include:

1. final Part names;
2. final chapter titles;
3. provisional chapter numbers;
4. identification of existing versus new chapters;
5. movement of the current Mouse-Free / Mouse-Lite chapter;
6. the proposed Configuration and Quick Reference material.

Before renaming any manuscript files, the revised Contents should be reviewed as a whole.

Only after the Contents structure is agreed should chapter renumbering and manuscript revision begin.


# Part 3 Continued — Proposed Revised Contents

## Purpose

The feature-assignment matrix has now given every significant DrivenByMoss/X-Touch function a proposed home.

The next step is to turn those assignments into a coherent book structure.

This proposed Contents page is still an **editorial plan**.

No existing manuscript files should be renamed or renumbered until this structure has been reviewed and agreed.

---

# 31. Structural Principles

The revised Contents should satisfy several goals.

## Preserve the existing learning curve

The first twelve chapters already provide a strong progression from:

- hardware;
- mental model;
- banks;
- modes;
- focus;
- feedback;

through to:

- V-Pots;
- motor faders;
- transport;
- devices;
- Browser.

That sequence should remain substantially intact.

## Introduce advanced material only after the foundations

Features such as:

- modifiers;
- edit modes;
- markers;
- automation;
- hierarchical navigation;

become much easier to understand once the reader already knows the controller's basic mental model.

## Keep workflow separate from reference

A beginner should not have to learn from a command table.

Conversely, an experienced reader should not have to search through tutorial prose merely to remember what `OPTION + MARKER` does.

The finished book therefore needs both:

1. **teaching chapters**;
2. **reference material**.

## Finish with synthesis

**Towards a Mouse-Free (or Mouse-Lite) Workflow** should remain the destination of the teaching journey.

It should bring together functionality already taught rather than introduce a new collection of unexplained commands.

---

# 32. Proposed Five-Part Structure

The revised book is best organised into five Parts:

```text
PART I     UNDERSTANDING THE X-TOUCH

PART II    WORKING WITH THE X-TOUCH

PART III   GOING DEEPER

PART IV    BUILDING THE WORKFLOW

PART V     CONFIGURATION AND REFERENCE
```

This gives each stage a distinct purpose.

---

# Part I — Understanding the X-Touch

## 1. Meet the X-Touch

**Existing chapter**

Purpose:

Introduce the controller, its relationship with Bitwig and DrivenByMoss, and the overall philosophy of the guide.

---

## 2. A Tour of the Hardware

**Existing chapter**

Purpose:

Introduce the physical surface before asking the reader to understand its deeper behaviour.

---

## 3. The Mental Model

**Existing chapter**

Purpose:

Introduce the central principle that physical controls acquire meaning from context.

---

## 4. Banks and Channels

**Existing chapter — targeted revision**

Add later:

- OPTION-modified movement;
- distinction between moving the controller's view and moving objects in the project;
- cross-reference to Device Mode.

---

## 5. Modes

**Existing chapter — targeted revision**

Expand into a map of the broader mode system:

- Track;
- Volume;
- Panorama;
- Send;
- Device;
- EQ;
- Instrument;
- Browser;
- Marker;
- Master.

Individual modes are explained later.

---

## 6. The SELECT Button

**Existing chapter — targeted revision**

Preserve:

> **SELECT establishes focus.**

Add only enough material to alert the reader that SELECT acquires additional functions with modifiers and hierarchical navigation.

---

## 7. Displays and Feedback

**Existing chapter — targeted revision**

Add:

- display-mode controls;
- segment-display behaviour;
- VU controls;
- distinction between current state and configured display behaviour.

---

# Part II — Working with the X-Touch

## 8. V-Pots (Rotary Encoders)

**Existing chapter — targeted revision**

Add:

- default;
- centre;
- minimum;
- maximum;
- context-dependent push operations.

---

## 9. Motor Faders

**Existing chapter — targeted revision**

Add:

- configurable fader-touch behaviour;
- Master Fader behaviour;
- FLIP introduction;
- explicit forward reference to Automation.

---

## 10. Transport Controls

**Existing chapter — substantial revision**

Retain the approachable introduction to:

- PLAY;
- STOP;
- RECORD;
- REWIND;
- FORWARD;
- Jog Wheel.

Then add:

- PLAY modifiers;
- STOP variants;
- Jog Wheel modifiers;
- ZOOM;
- SCRUB;
- NUDGE;
- arrow-key navigation;
- references to Marker and advanced Recording chapters.

---

## 11. Device Mode

**Existing chapter — substantial revision**

Preserve the hierarchy:

```text
Track
   ↓
Device
   ↓
Parameter Page
   ↓
Parameter
```

Add the exact hardware navigation:

```text
BANK        → Device
CHANNEL     → Parameter Page
V-Pots      → Parameters
```

Also add:

- CONTROL device selection;
- OPTION parameter-page selection;
- device pinning;
- Project/Track Parameter Mode.

---

## 12. Browser Mode

**Existing chapter — substantial revision**

Add the precise Browser control map:

- V-Pots;
- V-Pot presses;
- Jog Wheel;
- Browser tabs;
- insertion position;
- replacement;
- confirm;
- cancel;
- insert-before/after shortcuts.

---

# Part III — Going Deeper

This Part contains the major functionality discovered during the MCU audit.

The reader is no longer learning what the X-Touch is.

The reader is learning **how much more it can do**.

---

## 13. Modifiers and Advanced Controls

**New chapter**

Purpose:

Introduce:

- SHIFT;
- OPTION;
- CONTROL;
- ALT;

as a vocabulary for extending existing controls.

Also introduce everyday advanced commands such as:

- UNDO;
- REDO;
- SAVE;
- FLIP;
- ENTER;
- CANCEL.

Do not attempt to catalogue every modifier combination.

Teach recurring patterns and point to the chapters where individual combinations are used.

---

## 14. Mixer Edit Modes

**New chapter**

Teach as a related family:

- Track Edit Mode;
- Volume Edit Mode;
- Panorama Edit Mode;
- Send Modes 1–8.

Also provide the main home for:

- ARM;
- MUTE;
- SOLO;
- direct Send selection;
- Send toggle;
- fine adjustments.

Central idea:

> **The same eight channel controls can expose different mixer dimensions.**

---

## 15. Markers and Advanced Navigation

**New chapter**

Teach the complete marker workflow:

- create a marker;
- display markers;
- enter Marker Mode;
- navigate previous/next;
- start playback from a marker.

Key commands include:

- OPTION + MARKER;
- SHIFT + MARKER;
- OPTION + REWIND;
- OPTION + FORWARD.

This is the chapter that directly resolves the omission which originally triggered the MCU audit.

---

## 16. Automation

**New chapter**

Teach:

- READ/OFF;
- WRITE;
- TOUCH;
- LATCH;
- TRIM;
- reset automation overrides.

Build directly on Chapter 9's explanation of touch-sensitive motor faders.

Automation modes should be explained in terms of:

```text
Touch
   ↓
Move
   ↓
Release
   ↓
What happens next?
```

rather than as a table of button names.

---

## 17. Groups, Layers and Drum Pads

**New chapter**

Develop the book's hierarchical mental model.

Teach:

```text
Project
   ↓
Group
   ↓
Track
   ↓
Instrument
   ↓
Layer / Drum Pad
```

Include:

- flat navigation;
- hierarchical navigation;
- entering groups;
- leaving groups;
- entering Layer/Drum Pad Mode;
- Volume;
- Panorama;
- Sends;
- Mute;
- Solo.

---

## 18. Master and EQ Modes

**New chapter**

### Master Mode

Teach:

- entering Master Edit Mode;
- Master volume;
- Master panorama;
- audio-engine controls;
- previous/next project.

### EQ Mode

Teach:

- entering EQ Mode;
- relationship with Device Mode;
- EQ+;
- automatic insertion behaviour.

Include a clear warning where entering EQ Mode may modify the Bitwig project.

If drafting reveals that these two subjects do not sit comfortably together, they may later be separated.

---

## 19. Advanced Recording and Overdub

**New chapter**

Bring together:

- Arranger recording;
- Launcher recording;
- Arranger overdub;
- Launcher overdub;
- OPTION + RECORD;
- New Clip Length;
- clip creation;
- OVR;
- Clip Based Looper concepts.

The emphasis should be on **recording workflows**, not on memorising shortcut combinations.

---

# Part IV — Building the Workflow

## 20. Towards a Mouse-Free (or Mouse-Lite) Workflow

**Existing Chapter 13 — moved and substantially expanded**

This becomes the synthesis chapter for the entire teaching section.

The existing chapter should retain its central philosophy:

> The aim is not to eliminate the mouse.

> The aim is to stop reaching for it automatically.

The revised chapter can now demonstrate complete workflows involving:

- transport;
- mixing;
- devices;
- Browser;
- markers;
- automation;
- groups;
- recording;
- Note Editor;
- Automation Editor;
- Mixer pane;
- Bitwig layouts;
- plug-in windows;
- Undo/Redo;
- Save;
- project switching.

The chapter should introduce **very little new functionality**.

Its purpose is to show how the capabilities already learned fit together.

The final destination remains:

> **You simply make music.**

---

# Part V — Configuration and Reference

This material supports the teaching chapters without interrupting their flow.

---

## 21. Configuring DrivenByMoss for the X-Touch

**New chapter**

Establish a recommended Project XTC baseline.

Cover:

- X-Touch firmware;
- MC mode;
- DrivenByMoss X-Touch profile;
- display colours;
- display preferences;
- VU configuration;
- fader preferences;
- fader-touch behaviour;
- flat/hierarchical track navigation;
- Startup Mode;
- Browser filters;
- encoder sensitivity;
- transport preferences;
- New Clip Length;
- other workflow preferences.

Distinguish clearly between:

### Project XTC recommended baseline

and:

### Personal workflow choices

---

## 22. Customisation and Expansion

**New chapter**

Cover:

- assignable F-buttons;
- arbitrary actions;
- Footswitch 1;
- Footswitch 2;
- Clip Based Looper;
- X-Touch Extender;
- multiple MCU-compatible controllers;
- optional multi-controller workflows.

Material specific to hardware other than the X-Touch should remain out of scope unless directly relevant to an X-Touch/Extender configuration.

---

# Reference Material

## Quick Reference

**New reference section — not necessarily a numbered teaching chapter**

The final implementation should provide two routes into the same information.

### By physical control

For example:

```text
PLAY
SHIFT + PLAY
OPTION + PLAY
OPTION + SHIFT + PLAY

MARKER
SHIFT + MARKER
OPTION + MARKER
```

### By task

For example:

```text
Playback
Navigation
Recording
Mixing
Markers
Automation
Devices
Browser
Groups
Configuration
```

The Quick Reference should be created **after the teaching chapters are final**, so it reflects the book rather than dictating its structure.

---

# Appendices — Provisional

The following may eventually be better treated as appendices rather than normal chapters.

## Appendix A — X-Touch Extender

Possible material:

- Main;
- Extender;
- MCU Extender;
- restart requirements;
- multi-unit arrangement;
- master/transport responsibilities.

Whether this remains in Chapter 22 or becomes an appendix can be decided during drafting.

## Appendix B — Verification and Version Notes

Possible material:

- Bitwig version tested;
- DrivenByMoss version tested;
- X-Touch firmware tested;
- known configuration differences;
- behaviour requiring version-specific qualification.

This would be particularly useful because DrivenByMoss continues to evolve.

---

# 33. Proposed Reader Journey

The revised structure creates a clear progression.

```text
PART I
UNDERSTAND
"What is this controller doing?"

        ↓

PART II
OPERATE
"How do I use the main controls?"

        ↓

PART III
EXPLORE
"What else can DrivenByMoss make it do?"

        ↓

PART IV
INTEGRATE
"How do I turn all of this into a workflow?"

        ↓

PART V
CONFIGURE
"How do I tune it for the way I work?"

        ↓

REFERENCE
"What was that command again?"
```

This is deliberately different from the organisation of a conventional reference manual.

Project XTC teaches first and provides lookup material afterwards.

---

# 34. Existing and New Chapter Summary

| Proposed chapter | Status |
|---|---|
| 01 Meet the X-Touch | Existing |
| 02 A Tour of the Hardware | Existing |
| 03 The Mental Model | Existing |
| 04 Banks and Channels | Existing — revise |
| 05 Modes | Existing — revise |
| 06 The SELECT Button | Existing — revise |
| 07 Displays and Feedback | Existing — revise |
| 08 V-Pots (Rotary Encoders) | Existing — revise |
| 09 Motor Faders | Existing — revise |
| 10 Transport Controls | Existing — substantial revision |
| 11 Device Mode | Existing — substantial revision |
| 12 Browser Mode | Existing — substantial revision |
| 13 Modifiers and Advanced Controls | New |
| 14 Mixer Edit Modes | New |
| 15 Markers and Advanced Navigation | New |
| 16 Automation | New |
| 17 Groups, Layers and Drum Pads | New |
| 18 Master and EQ Modes | New |
| 19 Advanced Recording and Overdub | New |
| 20 Towards a Mouse-Free (or Mouse-Lite) Workflow | Existing Chapter 13 — move/revise |
| 21 Configuring DrivenByMoss for the X-Touch | New |
| 22 Customisation and Expansion | New |
| Quick Reference | New reference section |

This produces:

- **12 existing chapters retained in their present positions;**
- **1 existing chapter moved from 13 to 20;**
- **9 new teaching/configuration chapters;**
- **1 new Quick Reference section.**

---

# 35. Proposed Contents as the Reader Would See It

```text
CONTENTS


PART I — UNDERSTANDING THE X-TOUCH

1.  Meet the X-Touch
2.  A Tour of the Hardware
3.  The Mental Model
4.  Banks and Channels
5.  Modes
6.  The SELECT Button
7.  Displays and Feedback


PART II — WORKING WITH THE X-TOUCH

8.  V-Pots (Rotary Encoders)
9.  Motor Faders
10. Transport Controls
11. Device Mode
12. Browser Mode


PART III — GOING DEEPER

13. Modifiers and Advanced Controls
14. Mixer Edit Modes
15. Markers and Advanced Navigation
16. Automation
17. Groups, Layers and Drum Pads
18. Master and EQ Modes
19. Advanced Recording and Overdub


PART IV — BUILDING THE WORKFLOW

20. Towards a Mouse-Free (or Mouse-Lite) Workflow


PART V — CONFIGURATION AND REFERENCE

21. Configuring DrivenByMoss for the X-Touch
22. Customisation and Expansion

Quick Reference
```

---

# 36. Filename Implications

If this structure is approved, the existing manuscript filenames 01–12 can remain unchanged.

The current:

```text
13_towards_a_mouse_free_or_mouse_lite_workflow.md
```

would eventually become:

```text
20_towards_a_mouse_free_or_mouse_lite_workflow.md
```

New files would then occupy:

```text
13_modifiers_and_advanced_controls.md
14_mixer_edit_modes.md
15_markers_and_advanced_navigation.md
16_automation.md
17_groups_layers_and_drum_pads.md
18_master_and_eq_modes.md
19_advanced_recording_and_overdub.md
21_configuring_drivenbymoss_for_the_xtouch.md
22_customisation_and_expansion.md
```

The Quick Reference filename should be decided only when its implementation is designed.

**Do not perform these renames yet.**

---

# 37. Contents Review Questions

Before this structure is adopted, the following editorial questions should be settled.

## Question 1 — Master and EQ together?

Is **Master and EQ Modes** a coherent chapter, or should they ultimately become two shorter chapters?

Current recommendation:

**Keep them together provisionally.**

Drafting will tell us whether the pairing works.

## Question 2 — Advanced Recording deserves a chapter?

The feature-assignment matrix suggests yes.

It now contains a coherent cluster:

- Arranger versus Launcher;
- overdub;
- clip creation;
- New Clip Length;
- OPTION + RECORD;
- Clip Based Looper links.

Current recommendation:

**Keep the chapter.**

## Question 3 — Configuration before or after Mouse-Lite?

A configuration chapter could logically appear near the beginning of the book.

However, detailed preferences make much more sense once the reader understands what they affect.

Current recommendation:

**Keep detailed configuration near the end.**

Only the minimum setup required to get the X-Touch working belongs near the beginning.

## Question 4 — Quick Reference as Chapter 23?

A Quick Reference is structurally different from a teaching chapter.

Current recommendation:

**Do not number it as Chapter 23.**

Treat it as reference material following Chapter 22.

---

# 38. Recommended Structure

Subject to review, the proposed structure is therefore:

```text
22 numbered chapters
        +
Quick Reference
        +
possible appendices
```

The teaching journey ends with Chapter 20.

Chapters 21–22 then explain configuration and expansion.

The Quick Reference sits at the back of the book for lookup.

---

# 39. Part 3 Status

The proposed revised Contents is now complete.

No manuscript has yet been changed.

The next task should be a **structure review**, checking:

1. whether any chapters are overloaded;
2. whether any two new chapters should be merged;
3. whether any chapter should be split;
4. whether the Part boundaries feel natural;
5. whether Chapter 20 remains the correct culmination of the teaching sequence;
6. whether configuration/reference material is placed appropriately.

Once that review is complete, the revised Contents can be approved.

Only then should:

- `00_contents.md` be replaced;
- Chapter 13 be renumbered;
- new manuscript files be created;
- existing chapters begin their targeted revisions.
