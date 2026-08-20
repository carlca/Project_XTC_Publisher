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
