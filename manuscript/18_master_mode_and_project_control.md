---
chapter: 18
title: "Master Mode and Project Control"
status: draft
---

# Master Mode and Project Control

Most of the X-Touch is organised around tracks.

The eight channel strips naturally encourage us to think in terms of:

```text
Track 1
Track 2
Track 3
...
Track 8
```

But not every useful operation belongs to an individual track.

Some controls affect:

```text
the Master channel

the whole project

Bitwig's editors

Bitwig's mixer

the metronome

the current project
```

DrivenByMoss therefore gives the X-Touch a collection of project-level controls.

These functions are less about:

> **Which track am I controlling?**

and more about:

> **What do I want Bitwig as a whole to do?**

---

# Master Mode

The X-Touch provides a dedicated motorised:

```text
MASTER FADER
```

Touching the Master fader selects the Master track and enters Master Mode.

Conceptually:

```text
Track-Oriented Control
        │
        │ Touch Master Fader
        ▼
    Master Mode
```

The eight V-Pots now provide a small collection of project-level controls rather than behaving as eight ordinary channel controls.

---

# The Master Mode V-Pots

For Bitwig Studio and DrivenByMoss 26.6.3, the verified Master Mode mapping is:

```text
V-Pot 1
   → Master Volume

V-Pot 2
   → Master Panorama

V-Pots 3–5
   → Unassigned

V-Pot 7
   → Previous Project

V-Pot 8
   → Next Project
```

This is an unusual mapping.

Unlike many X-Touch modes, the eight V-Pots do not form a simple sequence of eight similar parameters.

Instead they provide several different kinds of project-level operation.

---

# An Important Note About V-Pots 3–5

The published DrivenByMoss MCU documentation describes presses on V-Pots 3–5 as toggling the project's audio engine.

Hardware verification with Bitwig Studio and DrivenByMoss 26.6.3 found no observable response from pressing or turning any of these three V-Pots in Master Mode. Their display labels did not change either.

For the setup covered by this guide:

```text
V-Pots 3–5
   → Unassigned
```

This is a case where verified current behaviour takes precedence over an outdated documented mapping.

---

# V-Pot 1 — Master Volume

In Master Mode:

```text
V-Pot 1
   → Master Volume
```

This gives the rotary controls access to the project's overall output level.

Conceptually:

```text
Turn V-Pot 1
      ↓
Master Volume
```

Of course, the X-Touch also has a dedicated motorised Master fader.

The V-Pot assignment is therefore not the only way to control Master Volume.

It is part of the Master Mode parameter set.

---

# V-Pot 2 — Master Panorama

V-Pot 2 controls:

```text
Master Panorama
```

So:

```text
Turn V-Pot 2
      ↓
Master Panorama
```

Together, the first two V-Pots provide:

```text
V-Pot 1  → Level

V-Pot 2  → Panorama
```

for the Master channel.

---

# V-Pots 7 and 8 — Project Navigation

DrivenByMoss maps:

```text
V-Pot 7
   → Previous Project

V-Pot 8
   → Next Project
```

This is particularly useful when more than one Bitwig project is open.

Conceptually:

```text
Previous Project
      ▲
      │
   V-Pot 7
```

and:

```text
V-Pot 8
      │
      ▼
Next Project
```

The X-Touch can therefore move its focus between open projects without requiring the mouse.

---

# Project Navigation Changes the Whole Context

Changing project is much more significant than changing track.

If you move from:

```text
Project A
```

to:

```text
Project B
```

then almost everything represented by the X-Touch may change:

```text
Tracks

Devices

Fader Positions

Button States

Parameters

Markers

Transport Position
```

So after changing project:

> **Read the surface before acting.**

The motor faders and displays will update to reflect the newly focused project.

---

# Master Mode Is Not Just a Bigger Mixer Channel

It would be easy to assume that touching the Master fader simply turns the eight V-Pots into controls for the Master track.

But the documented mapping is broader than that.

It combines:

```text
Master Volume

Master Panorama

Project Navigation
```

So a better mental model is:

> **Master Mode is a small project-control panel.**

The Master channel is part of it.

The whole project is the larger context.

---

# Project-Level Utility Controls

DrivenByMoss also maps several other X-Touch buttons to operations that affect Bitwig's interface or the project as a whole.

These include:

```text
MIDI TRACKS

INPUTS

AUDIO TRACKS

AUDIO INSTRUMENT

CLICK

SOLO

OVR

SAVE

DROP
```

The labels are inherited from MCU hardware conventions.

In Bitwig, their DrivenByMoss meanings can be quite different.

This is another place where:

> **The printed label does not necessarily describe the Bitwig function.**

---

# MIDI TRACKS — Toggle the Note Editor Pane

DrivenByMoss maps:

```text
MIDI TRACKS
   → Toggle Note Editor Pane
```

So:

```text
MIDI TRACKS
      ↓
Note Editor
   On / Off
```

This provides direct hardware access to one of Bitwig's most important editing panes.

It can be useful when moving between:

```text
arrangement work
```

and:

```text
note editing
```

without reaching for the mouse.

---

# INPUTS — Toggle the Automation Editor Pane

DrivenByMoss maps:

```text
INPUTS
   → Toggle Automation Editor Pane
```

Conceptually:

```text
INPUTS
   ↓
Automation Editor
   On / Off
```

This complements the automation controls covered in Chapter 16.

Chapter 16 deals with:

```text
how automation is written
```

whereas INPUTS provides a quick way to change:

```text
whether the Automation Editor
is visible in Bitwig
```

Those are related but distinct operations.

---

# AUDIO TRACKS — Toggle the Plug-In Window

Press:

```text
AUDIO TRACKS
```

to toggle the plug-in window.

Conceptually:

```text
AUDIO TRACKS
      ↓
Plug-In Window
   Open / Closed
```

This can be useful when the X-Touch is controlling a plug-in or device but you occasionally want its graphical interface visible.

It supports a useful Mouse-Lite pattern:

```text
Control from Hardware
       ↓
Need Visual Detail
       ↓
AUDIO TRACKS
       ↓
Show Plug-In
```

---

# SHIFT + AUDIO TRACKS — Toggle Layouts

DrivenByMoss also maps:

```text
SHIFT + AUDIO TRACKS
   → Toggle Layouts
```

This provides another project-level view operation.

It should not be confused with the direct layout buttons covered in Chapter 7:

```text
AUX
   → Arrange

BUSSES
   → Mix

OUTPUTS
   → Edit
```

Those select specific Bitwig layouts.

By contrast:

```text
SHIFT + AUDIO TRACKS
   → Toggle Layouts
```

provides a switching operation.

So the distinction is:

```text
AUX / BUSSES / OUTPUTS
   → choose a particular layout
```

versus:

```text
SHIFT + AUDIO TRACKS
   → toggle layouts
```

---

# OPTION + AUDIO TRACKS — Toggle Device Expanded State

DrivenByMoss maps:

```text
OPTION + AUDIO TRACKS
   → Toggle Device Expanded State
```

This changes the way the current device is presented in Bitwig.

Conceptually:

```text
Device Collapsed
      │
      │ OPTION + AUDIO TRACKS
      ▼
Device Expanded
```

and back again.

This is another useful bridge between:

```text
hardware control
```

and:

```text
screen presentation
```

The X-Touch is not changing a device parameter.

It is changing how the device is displayed.

---

# AUDIO INSTRUMENT — Toggle the Mixer Pane

Press:

```text
AUDIO INSTRUMENT
```

to toggle Bitwig's Mixer pane.

Conceptually:

```text
AUDIO INSTRUMENT
        ↓
    Mixer Pane
      On / Off
```

Again, the printed MCU label is not an obvious description of the DrivenByMoss operation.

It is worth learning the Bitwig meaning rather than trying to infer it from:

```text
AUDIO INSTRUMENT
```

---

# Four Useful Bitwig Pane Controls

Taken together:

```text
MIDI TRACKS
   → Note Editor

INPUTS
   → Automation Editor

AUDIO TRACKS
   → Plug-In Window

AUDIO INSTRUMENT
   → Mixer Pane
```

give the X-Touch substantial control over what Bitwig shows on screen.

This is an important part of a Mouse-Lite workflow.

The controller is not only manipulating project parameters.

It can also reorganise the software workspace.

---

# CLICK — Metronome

DrivenByMoss maps:

```text
CLICK
   → Toggle Metronome
```

So:

```text
Metronome Off
      │
      │ CLICK
      ▼
Metronome On
```

and back again.

This is exactly the kind of operation that benefits from a dedicated physical control.

---

# SHIFT + CLICK — Metronome Ticks

The modified operation is:

```text
SHIFT + CLICK
   → Toggle Metronome Ticks
```

This controls the tick behaviour associated with the metronome.

So the pair is:

```text
CLICK
   → Metronome
```

```text
SHIFT + CLICK
   → Metronome Ticks
```

---

# SHIFT + Master Fader — Metronome Volume

We encountered another metronome control in Chapter 10:

```text
SHIFT + Master Fader
   → Metronome Volume
```

Together, the three operations form a useful hardware group:

```text
CLICK
   → Metronome On / Off

SHIFT + CLICK
   → Metronome Ticks

SHIFT + Master Fader
   → Metronome Volume
```

So the X-Touch can control not merely whether the click exists, but also aspects of how it behaves and how loudly it is heard.

---

# A Practical Metronome Workflow

Suppose you are about to record.

You can:

```text
CLICK
   ↓
Enable Metronome
```

then:

```text
SHIFT + Master Fader
   ↓
Set Comfortable Click Level
```

If necessary:

```text
SHIFT + CLICK
   ↓
Adjust Tick Behaviour
```

All of this can be done without opening a metronome control on screen.

---

# SOLO — Clear All Solos

The standalone SOLO utility control is mapped to:

```text
SOLO
   → Deactivate All Solos
```

This is different from the individual SOLO buttons in the eight channel strips.

Those act on particular tracks.

The project-level SOLO control answers:

> **How do I get out of the current solo state quickly?**

Press:

```text
SOLO
```

and all active solos are cleared.

---

# SHIFT + SOLO — Clear All Mutes

DrivenByMoss maps:

```text
SHIFT + SOLO
   → Deactivate All Mutes
```

So the pair becomes:

```text
SOLO
   → Clear All Solos

SHIFT + SOLO
   → Clear All Mutes
```

These are useful recovery controls.

If a complex project has several muted or soloed tracks and you simply want to return to an unrestricted listening state:

```text
SOLO
      +
SHIFT + SOLO
```

can clear those global conditions.

---

# Global Versus Channel-Strip Solo and Mute

Do not confuse the project-level utility controls with the channel-strip buttons.

For example:

```text
Channel SOLO
   → Change Solo State
     of One Track
```

whereas:

```text
SOLO Utility Button
   → Deactivate All Solos
```

Likewise, the modifier mappings associated with individual channel MUTE and SOLO buttons remain separate from this project-level operation.

The physical labels may look related.

The scope is different.

---

# OVR — Arranger Overdub

DrivenByMoss maps:

```text
REPLACE / OVR
   → Toggle Arranger Overdub
```

This controls whether recording into the Arranger uses overdub behaviour.

Conceptually:

```text
Arranger Overdub Off
        │
        │ OVR
        ▼
Arranger Overdub On
```

and back again.

Chapter 19 deals with recording and overdub workflows in more detail.

Here, the important point is that the X-Touch provides direct project-level access to the state.

---

# SHIFT + OVR — Launcher Overdub

The modified operation is:

```text
SHIFT + OVR
   → Toggle Launcher Overdub
```

So:

```text
OVR
   → Arranger Overdub
```

while:

```text
SHIFT + OVR
   → Launcher Overdub
```

This reflects Bitwig's two major performance/recording environments.

The modifier distinguishes:

```text
Arranger
```

from:

```text
Launcher
```

---

# Arranger and Launcher Overdub

A useful mental model is:

```text
OVR
   → timeline-oriented overdub
```

```text
SHIFT + OVR
   → clip-oriented overdub
```

The exact recording implications are explored in Chapter 19.

For now, remember the pairing:

```text
Unmodified
   → Arranger

SHIFT
   → Launcher
```

---

# SAVE — Save the Project

DrivenByMoss maps:

```text
SAVE
   → Save Project
```

This is refreshingly literal.

Press:

```text
SAVE
```

and Bitwig saves the current project.

This is one of the simplest project-level commands on the surface.

It is also one of the most useful.

---

# Saving from the Surface

A hardware SAVE button supports a good habit:

```text
Make Useful Change
      ↓
SAVE
```

without interrupting the current control-surface workflow.

There is no special Save Mode.

SAVE is an action:

```text
Press
   ↓
Project Saved
```

This is an example of the distinction introduced in Chapter 7 between:

```text
State
```

and:

```text
Action
```

SAVE performs an action and finishes.

---

# DROP — Duplicate the Selected Track

DrivenByMoss maps:

```text
DROP
   → Duplicate Selected Track
```

This is a powerful project-editing operation.

Conceptually:

```text
Selected Track
      │
      │ DROP
      ▼
Duplicate Track
```

Unlike changing a view or toggling a metronome, this modifies the project structure.

So check the selected track before pressing it.

---

# Why Duplicate Track Is Useful

Track duplication is common when building arrangements.

You might want to duplicate:

```text
an instrument setup

an effect chain

a vocal processing chain

a routing configuration

a sound-design starting point
```

Instead of recreating the track:

```text
SELECT Track
      ↓
DROP
```

provides a direct hardware route.

---

# DROP Is a Structural Command

Because DROP changes the project, it deserves the same caution as other structural operations.

Before pressing:

```text
DROP
```

ask:

```text
Which track is selected?
```

The operation acts on that selection.

This reinforces a recurring rule:

> **Selection establishes the target.**

The X-Touch can perform powerful operations quickly, but those operations depend on the current context being correct.

---

# Utility Controls Fall into Families

The collection becomes easier to remember if we organise it by purpose.

## Screen and Pane Control

```text
MIDI TRACKS
   → Note Editor

INPUTS
   → Automation Editor

AUDIO TRACKS
   → Plug-In Window

SHIFT + AUDIO TRACKS
   → Toggle Layouts

OPTION + AUDIO TRACKS
   → Device Expanded State

AUDIO INSTRUMENT
   → Mixer Pane
```

## Metronome

```text
CLICK
   → Metronome

SHIFT + CLICK
   → Metronome Ticks

SHIFT + Master Fader
   → Metronome Volume
```

## Global Mixer State

```text
SOLO
   → Clear All Solos

SHIFT + SOLO
   → Clear All Mutes
```

## Recording State

```text
OVR
   → Arranger Overdub

SHIFT + OVR
   → Launcher Overdub
```

## Project Actions

```text
SAVE
   → Save Project

DROP
   → Duplicate Selected Track
```

This is much easier to learn than treating them as a random collection of MCU mappings.

---

# The Printed Labels Are Historical, Not Explanatory

Some mappings make intuitive sense:

```text
SAVE
   → Save
```

Others do not:

```text
MIDI TRACKS
   → Note Editor Pane

INPUTS
   → Automation Editor Pane

AUDIO INSTRUMENT
   → Mixer Pane

DROP
   → Duplicate Track
```

This is a consequence of using an MCU-compatible hardware surface to control Bitwig.

DrivenByMoss has a fixed collection of physical buttons available.

It assigns useful Bitwig operations to them.

Therefore:

> **Learn the DrivenByMoss meaning, not the English meaning printed on the case.**

---

# Project Control and Mouse-Lite Operation

These utility mappings may initially seem less glamorous than motor faders or Device Mode.

But they solve a major practical problem.

Even after learning hardware mixing, you might otherwise keep reaching for the mouse to:

```text
open the Note Editor

show Automation

open a plug-in

show the Mixer

change layout

enable the metronome

clear solos

save

duplicate a track
```

The project-level controls bring many of those interruptions onto the X-Touch.

That makes them disproportionately valuable in everyday use.

---

# A Practical Master Mode Exercise

Open a Bitwig project.

Touch:

```text
MASTER FADER
```

Observe the scribble strips.

### 1. Master Volume

Turn:

```text
V-Pot 1
```

carefully.

Observe the Master Volume.

### 2. Master Panorama

Turn:

```text
V-Pot 2
```

carefully.

Observe Master Panorama.

### 3. Project Navigation

If more than one project is open, try:

```text
V-Pot 7
```

and:

```text
V-Pot 8
```

Observe the project focus change.

V-Pots 3–5 are unassigned in the verified setup, so they require no exercise.

The purpose of the exercise is to recognise that Master Mode combines **Master-channel parameters** with project navigation rather than presenting eight matching parameters.

---

# A Practical Pane-Control Exercise

Try the following one at a time:

```text
MIDI TRACKS
```

Observe the Note Editor.

Then:

```text
INPUTS
```

Observe the Automation Editor.

Then:

```text
AUDIO INSTRUMENT
```

Observe the Mixer pane.

Finally:

```text
AUDIO TRACKS
```

with an appropriate plug-in or device selected.

Observe the plug-in window.

The goal is to begin associating the physical buttons with their Bitwig meanings rather than their printed MCU labels.

---

# A Practical Layout Exercise

Chapter 7 introduced:

```text
AUX
   → Arrange

BUSSES
   → Mix

OUTPUTS
   → Edit
```

Now compare those with:

```text
SHIFT + AUDIO TRACKS
   → Toggle Layouts
```

The first group chooses specific layouts.

The second toggles between layouts.

Understanding that distinction helps prevent the mappings from feeling redundant.

---

# A Practical Global-State Exercise

In a test project, solo several tracks.

Press:

```text
SOLO
```

Observe all solos clear.

Now mute several tracks.

Press:

```text
SHIFT + SOLO
```

Observe all mutes clear.

The aim is to establish these controls as:

```text
global recovery commands
```

rather than individual channel operations.

---

# A Practical Save and Duplicate Exercise

Select a disposable test track.

Press:

```text
DROP
```

Confirm that the selected track is duplicated.

Then press:

```text
SAVE
```

The workflow demonstrates two different project-level action types:

```text
DROP
   → change project structure

SAVE
   → preserve project state
```

Both depend on understanding the current project context.

---

# If a Utility Button Does Something Unexpected

Ask:

```text
Am I using the correct physical button?

Is a modifier still held?

Which track is selected?

Which device is current?

Is Browser Mode active?

Am I in a specialised controller mode?

What does the X-Touch display show?
```

Many apparent mapping problems are actually context problems.

As throughout this guide:

```text
Read Feedback
      ↓
Confirm Context
      ↓
Act
```

---

# A Useful Mental Model

Think of Chapter 18 as moving upward through levels of scope.

At the narrowest level:

```text
Track Controls
```

Above that:

```text
Master Channel
```

Above that:

```text
Project
```

And alongside the project:

```text
Bitwig Workspace
```

The X-Touch can operate at all of these levels.

Master Mode provides:

```text
Master Volume

Master Panorama

Project Navigation
```

The utility buttons provide:

```text
Editor / Pane Control

Metronome Control

Global Solo / Mute Clearing

Overdub State

Save

Track Duplication
```

So the controller is no longer merely:

```text
a hardware mixer
```

It is becoming:

```text
a project-control surface
```

---

# The Important Idea

Master Mode expands the X-Touch's focus beyond ordinary tracks.

The verified Master Mode mapping is:

```text
V-Pot 1
   → Master Volume

V-Pot 2
   → Master Panorama

V-Pots 3–5
   → Unassigned

V-Pot 7
   → Previous Project

V-Pot 8
   → Next Project
```

The remaining project utilities form several useful groups:

```text
MIDI TRACKS
   → Note Editor Pane

INPUTS
   → Automation Editor Pane

AUDIO TRACKS
   → Plug-In Window

SHIFT + AUDIO TRACKS
   → Toggle Layouts

OPTION + AUDIO TRACKS
   → Toggle Device Expanded State

AUDIO INSTRUMENT
   → Mixer Pane
```

Metronome:

```text
CLICK
   → Metronome

SHIFT + CLICK
   → Metronome Ticks

SHIFT + Master Fader
   → Metronome Volume
```

Global state:

```text
SOLO
   → Deactivate All Solos

SHIFT + SOLO
   → Deactivate All Mutes
```

Recording:

```text
OVR
   → Arranger Overdub

SHIFT + OVR
   → Launcher Overdub
```

Project actions:

```text
SAVE
   → Save Project

DROP
   → Duplicate Selected Track
```

The printed labels can sometimes appear mysterious.

The underlying structure is much simpler:

```text
Control the Master
       +
Control the Project
       +
Control the Workspace
```

Once these mappings become familiar, many small operations that would otherwise interrupt a hardware workflow can remain on the X-Touch.

That is an important step toward treating it not simply as a mixer, but as a genuine Bitwig control surface.

---

## Coming Next

Chapter 18 has moved outward from individual tracks to the project as a whole.

Next we return to recording and look at the more advanced operations that build on transport, modifiers, automation and project state.

Next:

**Advanced Recording and Overdub.**
