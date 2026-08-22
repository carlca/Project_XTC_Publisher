---
chapter: 22
title: "Customisation and Expansion"
status: draft
---

# Customisation and Expansion

We began Project XTC with a fixed piece of hardware.

Eight channel strips.

Eight V-Pots.

Motor faders.

Transport controls.

Mode buttons.

A Jog Wheel.

It would be easy to assume that this defines the limits of the system.

But DrivenByMoss provides another layer:

> **some parts of the X-Touch can be adapted to the way you work.**

And if one X-Touch is not enough, the Mackie MCU implementation can also support additional control surfaces.

So this final chapter is about two related ideas:

```text
Customisation
     │
     ▼
Make the existing surface suit you


Expansion
     │
     ▼
Make the physical surface larger
```

Neither is required.

A single X-Touch with its normal mappings is already a very capable controller.

But once the basic workflow is familiar, these options allow the system to become more personal.

---

## Customise After You Understand

There is a temptation to customise a new controller immediately.

Change the function buttons.

Reassign the footswitches.

Modify preferences.

Create the perfect setup before making any music.

That is usually backwards.

A better progression is:

```text
Use the standard workflow
        ↓
Notice repeated friction
        ↓
Identify the missing action
        ↓
Customise deliberately
```

In other words:

> **Solve problems you actually have.**

Do not solve theoretical problems merely because a configuration option exists.

---

## The Value of an Unused Button

A programmable button is valuable because it can shorten a repeated workflow.

Suppose you perform an operation twenty times during a session.

If that operation normally requires:

```text
open menu
   ↓
find command
   ↓
click
```

but can instead become:

```text
press button
```

that assignment may be worth making.

The best custom controls often feel surprisingly mundane.

They remove tiny interruptions.

And tiny interruptions repeated many times become significant.

---

# Function Buttons

The X-Touch provides a row of function buttons labelled:

```text
F1  F2  F3  F4  F5  F6  F7  F8
```

DrivenByMoss allows function-button behaviour to be assigned through its settings.

This makes the F-buttons a useful area for personal workflow commands.

Instead of asking:

> **What are F1–F8 supposed to do?**

a better question is:

> **What would I benefit from having one button away?**

---

## Choose Functions by Frequency

A useful assignment is normally something that is:

- performed frequently;
- slightly awkward to reach otherwise;
- unambiguous;
- safe to trigger accidentally;
- easy to remember.

Suppose you repeatedly use a particular Bitwig operation.

Giving it an F-button may turn:

```text
intention
   ↓
search
   ↓
mouse
   ↓
command
```

into:

```text
intention
   ↓
F-button
```

That is exactly the kind of compression a control surface is good at.

---

## Don't Fill Every Button

Eight labelled buttons can create a strange psychological pressure:

> **I must find eight things to assign.**

You don't.

An unused button is not wasted.

A button assigned to something you never remember is more useless than an intentionally empty one.

Start with one or two functions that genuinely improve the workflow.

Then let experience tell you whether more are needed.

---

## All Eight Function Buttons Are Assignable

The DrivenByMoss MCU documentation contains a small discrepancy.

Its general Functions section describes F1–F8 as assignable, while its Preferences section refers only to F1–F5.

The configuration interface in DrivenByMoss 26.6.3 resolves this discrepancy: all eight function buttons have independent assignment fields.

```text
F1  → Assignable
F2  → Assignable
F3  → Assignable
F4  → Assignable
F5  → Assignable
F6  → Assignable
F7  → Assignable
F8  → Assignable
```

In the default state verified for this guide, each button is configured as:

```text
Category  → Editing
Action    → Undo
```

So the reference to F1–F5 in the published Preferences section is outdated. For the current version covered here, the full F1–F8 row is available for independent assignment.

---

# Actions

One of the assignable function types in DrivenByMoss is an **Action**.

This allows an available Bitwig action to be selected and triggered from the controller.

Conceptually:

```text
Physical Button
      │
      ▼
DrivenByMoss
      │
      ▼
Selected Bitwig Action
```

This opens the door to a much more personal controller layout.

---

## Actions Turn Workflow into Hardware

Suppose Bitwig provides an action that you use constantly.

Without customisation:

```text
remember shortcut
       or
find command
```

With an assigned controller button:

```text
press
```

The software command has acquired a physical location.

And once an action has a physical location, muscle memory can develop around it.

This is one of the subtle advantages of programmable hardware.

---

## Pick Actions You Can Explain in One Sentence

A good custom assignment should normally have an obvious purpose.

For example:

> **This button does X.**

If you need a paragraph to remember why you assigned it, the mapping may be too clever.

Simple mappings survive.

Complicated mappings get forgotten.

A useful test is:

> **If I return to this project after a month, will I still know what this button does?**

If not, either simplify the assignment or document it.

---

## Label Your Customisations

The X-Touch's printed F-button labels obviously cannot change.

If you create important custom assignments, keep a record.

For example:

```text
F1   → [your chosen action]
F2   → [your chosen action]
F3   → unused
F4   → [your chosen action]
```

This record could live:

- in your Project XTC notes;
- beside the controller;
- in a small text file;
- in the project documentation.

The important thing is that a personal mapping should not become a personal mystery.

---

# Footswitches

DrivenByMoss exposes two MCU footswitch functions:

```text
Footswitch 1 — USER A

Footswitch 2 — USER B
```

Their functions can be selected in the DrivenByMoss settings.

This adds something fundamentally different from another button on the control surface.

A footswitch can be operated while **both hands are busy**.

---

## Why Feet Matter

Consider a recording situation.

Your left hand may be on an instrument.

Your right hand may also be on the instrument.

Reaching for the X-Touch interrupts the performance.

A footswitch gives us another input channel:

```text
Hands
  │
  └── perform music

Foot
  │
  └── control recording function
```

That separation can be extremely useful.

---

## Good Footswitch Jobs

A footswitch is particularly suitable for actions that are:

- performance-related;
- time-sensitive;
- simple;
- safe to trigger without looking.

The best assignments depend entirely on the workflow.

For one person, a footswitch may belong to recording.

For another, it may trigger a transport or navigation function.

For someone else, it may never be needed.

Again:

> **Customisation follows the work.**

---

# Clip Based Looper

One particularly interesting assignable function is **Clip Based Looper**.

This connects directly with the recording concepts from Chapter 19.

DrivenByMoss uses the currently selected MIDI clip slot.

If that slot is empty, a new clip is created using the configured **New Clip Length**, and playback begins.

The footswitch then controls overdub according to whether it is held.

Conceptually:

```text
Selected Clip Slot
        │
        ▼
Is there a clip?
   │           │
   │ no        │ yes
   ▼           ▼
Create Clip    Use Clip
   │           │
   └─────┬─────┘
         ▼
      Playback
         │
         ▼
Hold Footswitch
         │
         ▼
      Overdub
         │
         ▼
Release Footswitch
         │
         ▼
Stop Overdubbing
```

That is considerably more than a simple button assignment.

It creates a performance workflow.

---

## Hands-Free Loop Building

Imagine playing a MIDI keyboard.

Both hands are occupied.

The basic loop exists, and you want to add another layer.

With an appropriately assigned footswitch:

```text
Play
  ↓
Hold Footswitch
  ↓
Overdub
  ↓
Release
  ↓
Listen
```

The hands remain on the instrument.

The recording state is controlled by the foot.

This can feel much more natural than reaching away from the keyboard every time the loop changes state.

---

## New Clip Length Matters Here

Clip Based Looper also demonstrates why the configuration choices from Chapter 21 matter.

If the selected slot is empty, the new clip uses the configured New Clip Length.

So:

```text
Configuration
      │
      ▼
New Clip Length
      │
      ▼
Clip Based Looper
      │
      ▼
Performance behaviour
```

A setting made before the session affects what happens during the session.

This is exactly what we meant by:

> **Configure beforehand so that you have less to configure while making music.**

---

## A Simple Looper Workflow

Suppose New Clip Length is set to four bars.

A workflow might be:

### 1. Select the destination track and slot

Establish where the loop belongs.

### 2. Begin the Clip Based Looper operation

If necessary, the new four-bar clip is created.

### 3. Play the foundation

Record the basic musical idea.

### 4. Let it loop

Listen.

### 5. Hold the footswitch

Overdub becomes active.

### 6. Add another part

Continue playing.

### 7. Release the footswitch

Overdub stops.

### 8. Listen again

Decide whether the clip needs another layer.

This is the kind of workflow where hardware customisation becomes genuinely musical.

---

## Customisation Can Reduce Mode Switching

A useful custom control can sometimes avoid a journey through several other controls.

Without an assignment:

```text
leave current task
      ↓
find required function
      ↓
perform it
      ↓
return
```

With an assignment:

```text
press
```

This does not mean that modes are bad.

Modes are what make the X-Touch powerful.

But if one operation repeatedly forces you out of the mode where you actually want to work, a custom button may provide a useful shortcut.

---

# Expansion

Customisation changes what the existing hardware does.

Expansion changes how much physical hardware is available.

The Mackie MCU model was designed to support additional channel strips.

DrivenByMoss therefore supports multi-device configurations.

For the X-Touch family, the obvious companion is the **X-Touch Extender**.

---

## Why Add an Extender?

A single X-Touch gives us eight channel strips.

That has shaped much of this guide:

```text
Tracks 1–8
     ↓
BANK
     ↓
Tracks 9–16
```

An Extender gives us more physical strips simultaneously.

Conceptually:

```text
X-Touch

1   2   3   4   5   6   7   8


+

Extender

9  10  11  12  13  14  15  16
```

Now sixteen channels can be available without banking.

---

## Expansion Does Not Change the Mental Model

This is important.

An Extender does not invalidate everything we learned about banking and context.

It merely makes the visible window wider.

With one X-Touch:

```text
Project
──────────────────────────────────────

        ┌───────────────┐
        │   8 channels  │
        └───────────────┘
```

With an additional eight-channel surface:

```text
Project
──────────────────────────────────────

        ┌───────────────────────────────┐
        │          16 channels          │
        └───────────────────────────────┘
```

The idea remains:

> **The physical surface is a window onto the project.**

The window is simply larger.

---

## Main and Extender Roles

DrivenByMoss distinguishes between controller roles.

A device can be configured as:

- **Main**
- **Extender**
- **MCU Extender**

The Main device provides the full main-controller role, including controls such as the Master fader and transport functionality.

An Extender primarily contributes additional channel control.

Conceptually:

```text
MAIN
  │
  ├── Channel strips
  ├── Master
  ├── Transport
  └── Main commands


EXTENDER
  │
  └── Additional channel strips
```

This division reflects the physical design of MCU-style systems.

---

## MCU Extender

DrivenByMoss also distinguishes an **MCU Extender** role for devices that use the original Mackie MCU Extender protocol.

This matters because not every additional controller communicates in exactly the same way as the main MCU unit.

For a straightforward X-Touch plus X-Touch Extender setup, choose the role appropriate to the actual hardware and connection rather than assuming that every expansion device should be configured identically.

---

## Multiple Main Devices

DrivenByMoss also supports multiple devices configured as Main.

That is a more specialised configuration.

For most Project XTC readers, the simpler mental model is sufficient:

```text
Main X-Touch
     +
additional channel surface
```

More elaborate multi-device layouts should be configured only when there is a clear reason for them.

---

## Restart After Extender Changes

Changes to the Extender Setup require the DrivenByMoss extension to be restarted before the new configuration takes effect.

This is worth remembering because otherwise the settings may appear not to have worked.

A sensible workflow is:

```text
Change Extender Setup
        ↓
Restart extension
        ↓
Test banking and channel order
```

Do not repeatedly alter settings simply because the old state remains active before the required restart.

---

# What Does More Hardware Actually Buy Us?

It is easy to think:

> **Sixteen faders must be twice as good as eight.**

Not necessarily.

More physical channels offer some clear advantages.

---

## Less Banking

The obvious advantage is fewer bank changes.

For a sixteen-track project:

### One X-Touch

```text
Tracks 1–8
    ↓ BANK
Tracks 9–16
```

### X-Touch + eight-channel Extender

```text
Tracks 1–16
simultaneously
```

That can make broad mixing considerably more immediate.

---

## More Simultaneous Faders

Two hands can move several faders.

With more physical strips visible at once, more of the mix remains physically accessible.

This can be especially useful for:

- live mixing;
- automation passes;
- balancing Groups;
- performance-oriented work.

---

## More Immediate Mute and Solo

The advantage is not only faders.

Additional strips also mean more simultaneously available:

- MUTE buttons;
- SOLO buttons;
- SELECT buttons;
- ARM buttons;
- V-Pots;
- display information.

The physical representation of the mixer becomes broader.

---

## But More Hardware Also Means More Space

An Extender costs:

- money;
- desk space;
- another connection;
- more configuration;
- more physical reach.

The correct question is not:

> **Would sixteen faders be nice?**

Of course they would.

The better question is:

> **Does banking interrupt my workflow often enough that more physical channels are worth the cost and space?**

That is a much more useful decision.

---

# Expansion and the Dub Mixing Desk

Our Chapter 20 dub workflow gives an obvious example.

With eight strips:

```text
Drums
Bass
Skank
Organ
Percussion
Vocal
FX 1
FX 2
```

already fits rather neatly onto one X-Touch.

But a larger performance mix might contain:

```text
Drums
Bass
Skank
Organ
Piano
Percussion
Vocal 1
Vocal 2
FX Return 1
FX Return 2
FX Return 3
FX Return 4
...
```

An Extender could keep considerably more of that surface physically available at once.

For a performance-style mix, that may genuinely change how the controller feels.

You bank less.

You react more.

---

## More Controls Are Not Automatically Better

There is a useful parallel with custom buttons.

More functionality is only useful when it remains understandable.

A single well-learned X-Touch may be more effective than a huge surface whose layout you have not internalised.

Likewise:

```text
4 useful custom assignments
```

may be better than:

```text
20 assignments you cannot remember
```

The goal is not maximum capability.

It is **maximum fluency**.

---

# Build a Personal Layer on Top of the Standard One

Project XTC has spent most of its time describing a common baseline.

That matters.

If every user begins with a completely different control map, documentation becomes impossible and troubleshooting becomes much harder.

So think of customisation as a second layer:

```text
DrivenByMoss standard mapping
            │
            ▼
     Learn the system
            │
            ▼
   Personal customisation
```

Do not erase the standard mental model.

Build on it.

---

## Keep the Obvious Things Obvious

If a button labelled PLAY plays, that is easy to remember.

If a custom button labelled F2 performs some personal action, that is also manageable.

Problems arise when familiar controls are remapped so aggressively that the surface no longer makes visual sense.

The printed legends are useful.

Use them where possible.

Save custom assignments for places intended to be custom.

---

## Document Your Personal Setup

Once a controller becomes customised, your own documentation becomes valuable.

A simple file might record:

```text
Project XTC Personal Configuration

F1  → ...
F2  → ...
F3  → ...

Footswitch 1 → ...
Footswitch 2 → ...

New Clip Length → ...

Track Navigation → Hierarchical
```

If the system ever needs to be recreated, this turns a reconstruction exercise into a checklist.

---

## Customisation and Updates

DrivenByMoss evolves.

Bitwig evolves.

Available actions or configuration options may change.

After a major update, verify custom assignments just as you would verify normal controller behaviour.

A simple test might be:

```text
F-buttons
   ✓

Footswitches
   ✓

Clip Based Looper
   ✓

Extender
   ✓
```

If something has changed, consult the current DrivenByMoss documentation before rebuilding the setup from scratch.

---

# Leave Room for Discovery

One reason Project XTC grew from its original form was that the X-Touch could do more than we had initially realised.

An apparently obscure command such as:

```text
OPTION + MARKER
```

led us to audit the complete DrivenByMoss MCU feature set.

That audit uncovered:

- Marker Mode;
- deeper modifier functions;
- Mixer Edit Modes;
- Automation;
- layers and drum pads;
- Master Mode;
- advanced recording;
- assignable controls;
- Extenders.

There will probably be further discoveries.

That is not a flaw.

It is what happens when a flexible controller meets actively developed software.

---

## Don't Customise Away the Possibility of Learning

There is one subtle risk with customisation.

If we immediately assign a custom button to solve every unfamiliar task, we may never learn the standard DrivenByMoss workflow that already solves it.

So when you encounter friction:

```text
Problem
   ↓
Is there already a normal X-Touch method?
   │
   ├── yes → learn it
   │
   └── no / awkward
            ↓
        customise
```

This preserves the common vocabulary of the controller while still allowing personal refinement.

---

# A Sensible Customisation Process

A disciplined approach might be:

### 1. Use the normal setup

Work with it long enough to identify genuine friction.

### 2. Write the problem down

For example:

> I repeatedly need to perform X and the current route interrupts me.

### 3. Look for an existing X-Touch workflow

There may already be one.

### 4. If necessary, choose a custom control

Use an F-button, footswitch or assignable Action.

### 5. Test it in a real session

Does it actually help?

### 6. Keep or remove it

Do not preserve a customisation merely because you spent time creating it.

### 7. Document anything important

Future you will be grateful.

---

# Your X-Touch Does Not Have to Be My X-Touch

This guide needs a common baseline so that instructions remain meaningful.

But beyond that baseline, two users may reasonably develop different surfaces.

One might prioritise:

```text
Automation

Mixing

Device control
```

Another:

```text
Launcher recording

Clip Based Looper

Footswitch control
```

Another:

```text
Large mixer

Extender

Many simultaneous faders
```

Another may change almost nothing.

All of those are valid.

The controller serves the workflow.

Not the other way around.

---

# From Fixed Hardware to Adaptable Surface

When we first looked at the X-Touch, the hardware appeared fixed:

```text
buttons
faders
knobs
displays
```

Now we can see several dimensions of adaptability.

```text
Modes
   ↓
change what controls mean

Modifiers
   ↓
temporarily extend controls

Configuration
   ↓
change controller behaviour

Custom assignments
   ↓
add personal shortcuts

Extenders
   ↓
increase physical capacity
```

So although the hardware itself is fixed, the **surface as experienced by the user is not**.

---

## The Important Idea

Customisation is not about making the X-Touch more complicated.

It should do the opposite.

A good customisation removes friction.

A good assignment shortens a repeated path.

A good footswitch keeps your hands on the instrument.

A useful Extender keeps the channels you care about physically available.

The test is simple:

> **Does this make the work easier to perform and easier to understand?**

If yes, keep it.

If not, remove it.

---

# End of the Numbered Chapters

We began with a piece of hardware.

Eight motor faders.

Eight channel strips.

Eight V-Pots.

A collection of buttons whose labels came from the Mackie Control world.

At first, the surface could look almost overwhelming.

But the underlying ideas turned out to be much simpler.

```text
BANKS
   → move the window

SELECT
   → establish focus

MODES
   → change the view

MODIFIERS
   → temporarily extend a control

DISPLAYS
   → tell us what the controls mean

MOTOR FADERS
   → communicate in both directions

HIERARCHY
   → move between levels

CUSTOMISATION
   → adapt the surface to the work
```

Those ideas are more useful than memorising hundreds of commands.

Because when an unfamiliar function appears, we now have a way to understand it.

---

## From Controller to Companion

The title of this project is **X-Touch Companion**.

That word matters.

A useful companion does not demand constant attention.

It does not make you think about its internal machinery every moment.

It becomes familiar.

Predictable.

Available when needed.

The same should eventually be true of the X-Touch.

At first:

```text
Which button?

Which mode?

Which modifier?
```

Later:

```text
I want the chorus.

I want the delay.

I want that fader.

I want to record this.

I want the snare quieter.
```

And your hands know what to do.

---

## The Destination

The ultimate aim was never to become an expert in Mackie MCU button combinations.

It was never to avoid the mouse at all costs.

And it was never to use every feature simply because DrivenByMoss provides it.

The aim was to shorten the distance between:

```text
musical intention
       │
       ▼
physical action
       │
       ▼
musical result
```

When that distance becomes small enough, the controller itself begins to disappear from conscious attention.

You stop thinking:

> **I am operating the X-Touch.**

You think:

> **The vocal needs more delay.**

And then you do it.

That is where Project XTC has been heading all along.

---

# What Comes After the Chapters?

The numbered teaching chapters are now complete.

But a guide such as this also needs something different:

**a place to look things up.**

The next section of Project XTC will therefore be the **Quick Reference**.

It will organise the verified DrivenByMoss/X-Touch commands in two ways:

- by physical control;
- by task.

The teaching journey ends here.

The reference begins next.
