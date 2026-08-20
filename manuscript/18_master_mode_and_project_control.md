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

The Master channel belongs to the project as a whole.

DrivenByMoss gives the X-Touch a specialised Master Edit Mode for working at that level.

---

## The Master Fader Is More Than a Fader

The obvious job of the Master fader is to control the project's overall output level.

That is already useful.

But with DrivenByMoss, touching the Master fader also establishes a different context:

```text
Touch Master Fader
        │
        ▼
Select Master
        │
        ▼
Enter Master Edit Mode
```

So the Master fader performs two related jobs:

- it controls the Master level;
- it gives access to project-level controls.

This is another example of a familiar Project XTC principle:

> **An action can both change a value and establish focus.**

---

## From Track Focus to Project Focus

Earlier chapters concentrated on questions such as:

> Which track am I controlling?

Master Mode asks a different question:

> What if the thing I want to control belongs to the whole project?

Conceptually:

```text
Track Mode
   │
   ▼
Track-specific controls


Master Mode
   │
   ▼
Project-level controls
```

The physical V-Pots are the same.

What they represent has changed.

---

## Entering Master Edit Mode

Touch the Master fader.

DrivenByMoss selects the Master track and enters Master Edit Mode.

The V-Pots then acquire Master/project-related assignments.

At a high level:

```text
Master Edit Mode

V-Pot 1   → Master Volume
V-Pot 2   → Master Panorama
V-Pots 3–5 → Project / audio-engine controls
V-Pot 7   → Previous Project
V-Pot 8   → Next Project
```

The important point is not merely the list.

The important point is that the X-Touch has moved from:

```text
one track in the project
```

to:

```text
the project itself
```

---

## V-Pot 1 — Master Volume

V-Pot 1 controls the Master volume.

The Master fader already provides a large physical control for the same parameter, so this may seem redundant.

But redundancy is not necessarily wasteful on a control surface.

It gives the same parameter another form of access within the current mode.

Pressing V-Pot 1 resets the Master volume to its default value.

Conceptually:

```text
Turn V-Pot 1
      ↓
Master Volume

Press V-Pot 1
      ↓
Reset Master Volume
```

This follows the V-Pot press behaviour introduced earlier in the guide.

---

## V-Pot 2 — Master Panorama

V-Pot 2 controls the Master panorama.

Pressing it resets the panorama to its default position.

So:

```text
Turn V-Pot 2
      ↓
Master Panorama

Press V-Pot 2
      ↓
Reset Panorama
```

This gives the Master channel the same sort of direct physical access we have already used on ordinary tracks.

---

## Master Control and Caution

Master controls deserve a little more care than ordinary track controls.

Changing a single track affects one element of the mix.

Changing the Master affects **everything downstream of it**.

That means accidental adjustments can have much wider consequences.

A good habit is therefore:

> **Know that you are in Master Mode before turning controls.**

The displays and current feedback should make that clear.

Again:

> **Observe before you adjust.**

---

## V-Pots 3–5 — Project-Level Controls

DrivenByMoss assigns V-Pots 3–5 to project-level audio-engine control functions.

These are operated by pressing the V-Pots rather than turning them.

The important conceptual point is that these controls affect the **state of the project/audio engine**, not an individual channel parameter.

So the surface now contains several different kinds of control at once:

```text
V-Pot 1
   → continuous Master parameter

V-Pot 2
   → continuous Master parameter

V-Pots 3–5
   → project/audio-engine actions
```

This is another example of the controller being organised around context rather than around one fixed type of control.

---

## Why Project-Level Controls Matter

At first glance, project-level operations may seem less important than faders or device parameters.

But they become useful precisely because they save another trip to the computer interface.

Instead of thinking:

```text
find project control on screen
       ↓
move mouse
       ↓
click
```

the X-Touch can expose the relevant action directly when Master Mode is active.

That is a small but useful step towards a Mouse-Lite workflow.

---

## V-Pot 7 — Previous Project

Press V-Pot 7 to move to the previous project.

Conceptually:

```text
Current Project
      │
      │ press V-Pot 7
      ▼
Previous Project
```

This is a surprisingly powerful operation to have on the control surface.

It means project navigation itself can become part of the hardware workflow.

---

## V-Pot 8 — Next Project

Press V-Pot 8 to move to the next project.

So V-Pots 7 and 8 form a natural pair:

```text
V-Pot 7
   ← Previous Project

V-Pot 8
   Next Project →
```

This is easy to remember because the spatial relationship mirrors the navigation.

Left control: previous.

Right control: next.

---

## Project Switching from the Surface

Imagine working through several related Bitwig projects.

Perhaps they are:

- different songs in a set;
- alternative versions;
- works in progress;
- test projects.

Instead of opening project-selection controls with the mouse, Master Mode can provide direct navigation.

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

That is a good example of a command that is not musically glamorous but can make the overall workflow feel much more continuous.

---

## The Master Fader and Metronome Volume

We have already encountered another useful Master-fader modifier:

```text
SHIFT + Master Fader
```

controls metronome volume.

That is not part of Master Edit Mode itself, but it is worth remembering because it demonstrates how many roles the Master area can acquire:

```text
Master Fader
     │
     ├── normal
     │      Master volume
     │
     ├── touch
     │      Master focus / Master Mode
     │
     └── SHIFT
            Metronome volume
```

One physical fader participates in several related workflows.

---

## Master Mode and Context

Suppose you were just working in Device Mode.

The V-Pots represented device parameters.

Then you touch the Master fader.

Now those same V-Pots represent project-level functions.

Conceptually:

```text
Device Mode
   │
   ▼
V-Pots = Device Parameters

Touch Master Fader

   │
   ▼

Master Mode
   │
   ▼
V-Pots = Master / Project Controls
```

Nothing about the hardware has changed.

The current focus has changed.

This is precisely the mental model Project XTC has been building throughout the guide.

---

## The Master Channel Is a Different Scale

There is a useful way to think about this.

Ordinary track control is local:

```text
Track
   ↓
its level
its pan
its sends
its devices
```

Master control is global:

```text
Project
   ↓
overall output
overall panorama
project state
project navigation
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
the entire project
```

without changing control surfaces.

---

## Working from the Top Down

Master Mode is particularly useful when you want to start from the project level and then descend.

For example:

```text
Master level
     ↓
Group balance
     ↓
Track balance
     ↓
Device parameter
```

Earlier chapters showed how the X-Touch can move deeper into a project.

Master Mode reminds us that we can also move **upwards**.

The controller's point of view can operate at several levels.

---

## The Hierarchy Keeps Expanding

At this point, our project hierarchy looks something like:

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

Instead, it exposes the level that is currently useful.

That is what keeps the surface manageable.

---

## Project Control Is Still Feedback-Driven

Master Mode is another context where displays matter.

When the V-Pots no longer represent ordinary mixer or device parameters, the feedback tells you what they now mean.

That is especially important for project-level actions.

Do not assume that a V-Pot is still doing what it did moments ago.

Read the controller.

Check the context.

Then act.

The same rule continues to pay off:

> **Observe before you adjust.**

---

## A Practical Master Workflow

A simple Master Mode workflow might look like this.

### 1. Touch the Master fader

This establishes Master focus and enters Master Edit Mode.

### 2. Check the displays

Confirm that the controller is showing the Master/project context.

### 3. Adjust Master level if required

Use the Master fader or the appropriate V-Pot.

### 4. Adjust Master panorama if required

Use V-Pot 2.

### 5. Use project-level actions only deliberately

Treat V-Pots 3–5 as actions rather than ordinary continuous controls.

### 6. Navigate projects if required

Use V-Pots 7 and 8.

### 7. Return to normal track work

Select the required track or mode and continue.

The important thing is the shift in scale.

You temporarily step out of the track-level view, work at the project level, then return.

---

## Project Navigation and Mouse-Lite Working

Project switching is another good example of Mouse-Lite philosophy.

The goal is not:

> Never use Bitwig's project interface.

The goal is:

> If you already know you want the previous or next project, why should that necessarily require the mouse?

The X-Touch gives you a direct physical route.

That is the recurring theme of this guide:

**use the physical surface when it shortens the path between intention and action.**

---

## A Note on Verification

Some project-level assignments are less obvious than ordinary mixer functions.

For that reason, Project XTC should verify the exact current DrivenByMoss behaviour of the Master Mode action controls before final publication.

In particular, the functions assigned to V-Pots 3–5 should be confirmed against the current DrivenByMoss version rather than inferred from the labels alone.

The general Master Mode structure is clear.

The final reference tables should contain only verified current behaviour.

---

## The Important Idea

Master Mode changes the X-Touch's point of view from:

> **one part of the project**

to:

> **the project as a whole.**

Touching the Master fader establishes that context.

The surface can then provide access to:

- Master volume;
- Master panorama;
- project/audio-engine controls;
- previous project;
- next project.

So our mental model expands once more:

```text
Physical Control
      +
Current Focus
      +
Current Mode
      =
Current Function
```

At track level, the focus is a track.

At Device level, it is a device.

Inside a Group, it may be a child track.

In Master Mode, it is the project-level Master context.

The same surface moves between all of them.

---

## Coming Next

So far, we have looked at how to navigate, mix, automate and control increasingly complex structures.

The next chapter turns to another fundamental workflow:

**recording.**

DrivenByMoss gives the X-Touch several ways to work with:

- Arranger recording;
- Launcher overdub;
- clip creation;
- New Clip Length;
- overdub controls.

Next:

**Advanced Recording and Overdub.**
