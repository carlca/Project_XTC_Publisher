---
chapter: 18
title: "Master Mode and Project Control"
status: draft
---

# Master Mode and Project Control

Most of the X-Touch is concerned with the tracks that make up a project.

We select them.

We bank through them.

We mix them.

We control their devices and parameters.

But Bitwig also has a level **above** the individual tracks.

The Master track belongs to the project as a whole.

DrivenByMoss gives the X-Touch a specialised **Master Edit Mode** for working at that level.

---

## The Master Fader Is More Than a Fader

The obvious job of the Master fader is to control the project's overall output level.

That is already useful.

But with DrivenByMoss, touching the Master fader also changes the controller's context:

```text
Touch Master Fader
        │
        ▼
Select Master Track
        │
        ▼
Enter Master Edit Mode
```

So the Master fader performs two related jobs:

- it controls the Master level;
- touching it establishes the Master context.

This is another example of a familiar Project XTC principle:

> **An action can both control a value and establish focus.**

---

## From Track Focus to Project Focus

Earlier chapters concentrated on questions such as:

> **Which track am I controlling?**

Master Mode asks a different question:

> **What if the thing I want to control belongs to the whole project?**

Conceptually:

```text
Track Context
     │
     ▼
Track-specific controls


Master Context
     │
     ▼
Master and project-level controls
```

The physical V-Pots are the same.

What they represent has changed.

---

## Entering Master Edit Mode

Touch the Master fader.

DrivenByMoss selects the Master track and enters Master Edit Mode.

The V-Pots then acquire these assignments:

```text
Master Edit Mode

V-Pot 1      → Master Volume

V-Pot 2      → Master Panorama

V-Pots 3–5   → Press to toggle
                the project's audio engine

V-Pot 7      → Press for Previous Project

V-Pot 8      → Press for Next Project
```

V-Pot 6 has no Master Mode function documented in the current DrivenByMoss MCU reference.

The important point is not merely the list.

The important point is that the X-Touch has moved from:

```text
one track in the project
```

to:

```text
the project-level Master context
```

---

## V-Pot 1 — Master Volume

V-Pot 1 controls the Master volume.

The Master fader already provides a large physical control for the same parameter, so this may initially seem redundant.

But redundancy is not necessarily wasteful on a control surface.

It means the current mode remains internally consistent: the V-Pots themselves expose the parameters belonging to the Master context.

Turn V-Pot 1:

```text
V-Pot 1
   │
   ▼
Master Volume
```

Press V-Pot 1:

```text
V-Pot 1 Press
      │
      ▼
Reset Master Volume
```

The press behaviour follows the general V-Pot principle we met earlier:

> **Pressing a parameter knob resets it to its default value.**

---

## V-Pot 2 — Master Panorama

V-Pot 2 controls the Master panorama.

Turn it:

```text
V-Pot 2
   │
   ▼
Master Panorama
```

Press it:

```text
V-Pot 2 Press
      │
      ▼
Reset Master Panorama
```

So the first two V-Pots form a straightforward pair:

```text
V-Pot 1   Master Volume

V-Pot 2   Master Panorama
```

Both can be pressed to reset their parameter.

---

## V-Pots 3–5 — Audio Engine Control

V-Pots 3, 4 and 5 have a different kind of assignment.

They are not continuous parameter controls.

Pressing any of them toggles the audio engine on or off for the current project.

Conceptually:

```text
Press V-Pot 3, 4 or 5
          │
          ▼
Toggle Project Audio Engine
```

This is an important distinction.

With V-Pots 1 and 2:

```text
TURN
   → change a value
```

With V-Pots 3–5:

```text
PRESS
   → perform an action
```

The same physical row therefore contains both parameter controls and project-level commands.

---

## Why Three Knobs?

The current DrivenByMoss documentation assigns the same audio-engine toggle behaviour to V-Pots 3, 4 and 5.

Project XTC should describe that behaviour exactly as documented rather than inventing separate meanings for the three controls.

So the useful fact to remember is simply:

```text
V-Pots 3–5
   │
   ▼
Press
   │
   ▼
Toggle Audio Engine
```

There is no need to assign a different conceptual role to each one.

---

## What Does Toggling the Audio Engine Mean?

This is a project-level action.

It affects Bitwig's audio engine for the current project rather than a single track, device or parameter.

That makes it qualitatively different from most of the controls we have used so far.

The hierarchy is roughly:

```text
Parameter
   ↓
Device
   ↓
Track
   ↓
Group
   ↓
Project
   ↓
Audio Engine
```

Master Edit Mode is one of the places where the X-Touch reaches that upper level.

---

## Use Project-Level Actions Deliberately

Because the audio-engine control affects the project as a whole, it deserves more care than changing one track parameter.

A good habit is:

> **Check that you are in Master Mode before pressing project-level controls.**

The displays and current context should confirm what the V-Pots represent.

As throughout this guide:

> **Observe before you adjust.**

---

## V-Pot 7 — Previous Project

Press V-Pot 7 to switch to the previous project.

Conceptually:

```text
Current Project
      │
      │ press V-Pot 7
      ▼
Previous Project
```

This is a surprisingly powerful operation to have on the control surface.

Project navigation itself becomes part of the hardware workflow.

---

## V-Pot 8 — Next Project

Press V-Pot 8 to switch to the next project.

So V-Pots 7 and 8 form a natural pair:

```text
V-Pot 7
   ← Previous Project


V-Pot 8
   Next Project →
```

The spatial relationship is easy to remember.

Left means previous.

Right means next.

---

## Moving Between Projects from the Surface

Imagine working through several related Bitwig projects.

Perhaps they are:

- different songs in a set;
- alternative versions;
- works in progress;
- test projects.

Instead of returning to project-selection controls with the mouse, Master Mode can provide direct navigation.

The workflow becomes:

```text
Finish with Project A
        │
        ▼
Touch Master Fader
        │
        ▼
Master Edit Mode
        │
        ▼
Press V-Pot 8
        │
        ▼
Project B
```

This is not a glamorous function.

But it can make the overall workflow feel much more continuous.

---

## The Master Fader and Metronome Volume

The Master fader also participates in another useful command:

```text
SHIFT + Master Fader
```

changes the Metronome volume.

This is **not** part of Master Edit Mode itself.

It is a modifier operation on the Master fader.

So the Master area now illustrates three different kinds of context:

```text
Master Fader
     │
     ├── move normally
     │      → Master Volume
     │
     ├── touch
     │      → Select Master
     │        and enter Master Edit Mode
     │
     └── SHIFT + move
            → Metronome Volume
```

One physical fader participates in several related workflows.

---

## Master Mode and Context

Suppose you were just working in Device Mode.

The V-Pots represented device parameters.

Then you touch the Master fader.

Now those same V-Pots represent Master and project-level functions.

Conceptually:

```text
Device Mode
   │
   ▼
V-Pots = Device Parameters

Touch Master Fader

   │
   ▼

Master Edit Mode
   │
   ▼
V-Pots = Master / Project Controls
```

Nothing about the hardware has changed.

The current focus has changed.

This is precisely the mental model Project XTC has been building throughout the guide.

---

## The Master Track Is a Different Scale

There is a useful way to think about this.

Ordinary track control is local:

```text
Track
   │
   ├── Volume
   ├── Panorama
   ├── Sends
   └── Devices
```

Master control is global:

```text
Project
   │
   ├── Master Volume
   ├── Master Panorama
   ├── Audio Engine
   └── Project Navigation
```

The X-Touch lets you change scale.

You can work on:

```text
one parameter
```

then:

```text
one track
```

then:

```text
one Group
```

then:

```text
the project as a whole
```

without changing control surfaces.

---

## Moving Up and Down the Project

Chapter 17 showed how the controller can descend:

```text
Project
   ↓
Group
   ↓
Track
   ↓
Layer / Drum Pad
```

Master Mode reminds us that the controller can also move in the other direction.

From a detailed track or device context:

```text
Parameter
   ↑
Device
   ↑
Track
   ↑
Project
```

Touching the Master fader gives us a direct route to that project-level view.

---

## The Hierarchy Keeps Expanding

At this point, our conceptual model looks something like:

```text
Project
   │
   ├── Master
   │
   ├── Groups
   │     └── Tracks
   │
   ├── Tracks
   │     └── Devices
   │           └── Parameters
   │
   └── Instruments
         └── Layers / Drum Pads
```

The X-Touch does not expose all of this at once.

It exposes the level that is currently useful.

That is what keeps the surface manageable.

---

## Project Control Is Still Feedback-Driven

Master Mode is another context where displays matter.

When the V-Pots no longer represent ordinary mixer or device parameters, the feedback tells you what they now mean.

That is especially important when some V-Pots are controlling values while others perform project-level actions.

Do not assume that a V-Pot still does what it did moments ago.

Read the controller.

Check the context.

Then act.

The same rule continues to pay off:

> **Observe before you adjust.**

---

## A Practical Master Workflow

A simple Master Mode workflow might look like this.

### 1. Touch the Master fader

This selects the Master track and enters Master Edit Mode.

### 2. Check the displays

Confirm that the controller is showing the Master/project context.

### 3. Adjust Master level if required

Use the Master fader or V-Pot 1.

### 4. Adjust Master panorama if required

Use V-Pot 2.

### 5. Toggle the audio engine only deliberately

Press V-Pot 3, 4 or 5 when you actually intend to change the project's audio-engine state.

### 6. Navigate projects if required

Use:

```text
V-Pot 7
   → Previous Project

V-Pot 8
   → Next Project
```

### 7. Return to ordinary work

Select the required track or mode and continue.

The important thing is the shift in scale.

You temporarily step out of the track-level view, work at the project level, then return.

---

## Project Navigation and Mouse-Lite Working

Project switching is another good example of Mouse-Lite philosophy.

The goal is not:

> **Never use Bitwig's project interface.**

The goal is:

> **If you already know you want the previous or next project, why should that necessarily require the mouse?**

The X-Touch gives you a direct physical route.

That is the recurring theme of this guide:

**use the physical surface when it shortens the path between intention and action.**

---

## One Surface, Several Scales

By this point, the same X-Touch may have represented:

```text
Project Tracks

Group Contents

Instrument Layers

Drum Pads

Device Parameters

Mixer Dimensions

Master / Project Controls
```

The hardware has not become larger.

The conceptual surface has.

That is the power of context.

---

## The Important Idea

Master Mode changes the X-Touch's point of view from:

> **one part of the project**

to:

> **the project-level Master context.**

Touching the Master fader enters that mode.

The verified Master Edit Mode assignments are:

```text
V-Pot 1
   → Master Volume
   → Press to reset

V-Pot 2
   → Master Panorama
   → Press to reset

V-Pots 3–5
   → Press to toggle
     the project's audio engine

V-Pot 7
   → Previous Project

V-Pot 8
   → Next Project
```

And independently:

```text
SHIFT + Master Fader
   → Metronome Volume
```

So our mental model expands once more:

```text
Physical Control
      +
Current Focus
      +
Current Mode
      +
Modifier, if any
      =
Current Function
```

At track level, the focus is a track.

At Device level, it is a device.

Inside a Group, it may be a child track.

In Master Edit Mode, it is the Master and project context.

The same surface moves between all of them.

---

## Coming Next

So far, we have looked at how to navigate, mix, automate and control increasingly complex structures.

The next chapter turns to another fundamental workflow:

**recording.**

DrivenByMoss gives the X-Touch explicit operations for:

- normal recording;
- Launcher overdub;
- Arranger overdub;
- clip creation;
- New Clip Length.

Next:

**Advanced Recording and Overdub.**
