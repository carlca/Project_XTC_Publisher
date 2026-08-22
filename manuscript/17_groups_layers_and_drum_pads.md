---
chapter: 17
title: "Groups, Layers and Drum Pads"
status: draft
---

# Groups, Layers and Drum Pads

So far, we have often treated the eight channel strips as a window onto a simple row of tracks.

Something like:

```text
Track 1   Track 2   Track 3   Track 4
Track 5   Track 6   Track 7   Track 8
```

Real Bitwig projects are rarely that simple.

A track may be a **Group** containing other tracks.

An instrument may contain **Layers**.

A Drum Machine may contain many **Drum Pads**.

So the project can have structure within structure:

```text
Project
   │
   ├── Drums
   │     ├── Kick
   │     ├── Snare
   │     └── Hats
   │
   ├── Bass
   │
   └── Synth
         │
         ├── Layer 1
         └── Layer 2
```

DrivenByMoss allows the X-Touch to move through these structures.

The eight channel strips do not merely move sideways through the project.

They can also move **deeper into it**.

---

## A Correction to an Easy Assumption

It would be natural to imagine hierarchical navigation working like this:

```text
SELECT
   ↓
ENTER
   ↓
work inside
   ↓
CANCEL
   ↓
go back
```

That is **not** how DrivenByMoss navigates Groups and Layers.

The actual mechanism is built primarily around the channel **SELECT** buttons.

For hierarchical Group navigation:

```text
SELECT Group
     ↓
Group becomes selected
     ↓
Press the same SELECT again
     ↓
Enter Group
     ↓
Long-press any SELECT
     ↓
Leave Group
```

For Layers and Drum Pads:

```text
SELECT Track
     ↓
Track becomes selected
     ↓
Press the same SELECT again
     ↓
Enter Layers / Drum Pads
     ↓
Long-press any SELECT
     ↓
Leave Layers / Drum Pads
```

This repeated-SELECT behaviour is central to understanding the chapter.

---

## Why ENTER and CANCEL Are Not Used Here

The X-Touch does have ENTER and CANCEL buttons.

They simply have different jobs.

When the Browser is active:

```text
ENTER
   → confirm Browser selection

CANCEL
   → discard Browser selection
```

Outside the Browser they behave like the computer keyboard's Enter and Escape keys.

They are therefore useful controls.

They are just **not the mechanism for entering and leaving Groups or Layers**.

For the structures in this chapter, think:

```text
SELECT
   → choose

SELECT again
   → go inside

Long-press SELECT
   → come back out
```

---

# Groups

A Bitwig Group is a track that contains other tracks.

For example:

```text
Drums
   │
   ├── Kick
   ├── Snare
   ├── Hats
   ├── Toms
   └── Percussion
```

At the top level of the project, the X-Touch may initially show:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

The individual drum tracks are not necessarily part of this top-level view.

They live inside the Drums Group.

---

## Hierarchical Track Navigation

DrivenByMoss provides a **Track navigation** preference.

When it is set to:

```text
Hierarchical
```

the controller presents the project according to its Group structure.

At the top level, that might look like:

```text
┌───────┬──────┬─────────┬──────┬────────┬─────┐
│ Drums │ Bass │ Guitars │ Keys │ Vocals │ FX  │
└───────┴──────┴─────────┴──────┴────────┴─────┘
```

The contents of the Drums Group do not have to consume channel strips until you actually enter that Group.

This allows a large project to remain manageable on an eight-channel surface.

---

## Entering a Group

Suppose the Drums Group is on Channel 1.

First press its SELECT button:

```text
Drums
  │
  ▼
SELECT
```

The Drums Group becomes the selected track.

Now press the **same SELECT button again**:

```text
Drums selected
      │
      ▼
SELECT again
      │
      ▼
Enter Drums Group
```

The eight channel strips now represent tracks inside the Group.

For example:

```text
Kick   Snare   Hats   Toms   Perc   Room
```

The physical hardware has not changed.

The **level of the project represented by it has changed**.

---

## Leaving a Group

To leave the current Group:

```text
Long-press any SELECT button
```

Conceptually:

```text
Kick   Snare   Hats   Toms   Perc
              │
              ▼
     long-press SELECT
              │
              ▼
Drums   Bass   Guitars   Keys   Vocals
```

This takes the controller back up to the parent level.

So the essential hierarchical movement is:

```text
SELECT
   ↓
select object

SELECT again
   ↓
enter object

long-press SELECT
   ↓
leave object
```

---

## SELECT Has Acquired a Second Dimension

Earlier in Project XTC, SELECT primarily meant:

> **This one.**

That remains true.

But in a hierarchical project, repeated SELECT can also mean:

> **Show me inside this one.**

So SELECT now has two related roles:

```text
First press
   → focus

Second press
   → descend, where appropriate
```

and:

```text
Long press
   → ascend
```

This is a compact navigation system built into buttons that already have an obvious relationship with the channel strips.

---

## Think of It as Zooming Into the Mixer

Another useful mental model is **magnification**.

At first:

```text
Drums   Bass   Guitars   Keys   Vocals
```

Then:

```text
SELECT Drums
SELECT Drums again
```

and the controller effectively zooms in:

```text
Kick   Snare   Hats   Toms   Percussion
```

Long-press SELECT and it zooms back out:

```text
Drums   Bass   Guitars   Keys   Vocals
```

Nothing has moved physically.

The X-Touch has changed the scale at which you are viewing the project.

---

## Nested Groups

Groups may themselves contain Groups.

Conceptually:

```text
Project
   │
   └── Drums
         │
         ├── Acoustic Kit
         │      ├── Kick
         │      ├── Snare
         │      └── Overheads
         │
         └── Percussion
                ├── Shaker
                └── Tambourine
```

The same principle can be applied repeatedly.

At the top level:

```text
Drums
```

Enter Drums:

```text
Acoustic Kit   Percussion
```

Enter Acoustic Kit:

```text
Kick   Snare   Overheads
```

Then long-press SELECT to move back towards the parent level.

The important point is not how many levels exist.

It is that the navigation rule remains understandable.

---

## The Eight Strips Are a Window

This gives us a more powerful version of the idea introduced in Chapter 4.

Originally:

```text
Large project
────────────────────────────────────────

       ┌───────────────────┐
       │ 8 visible tracks  │
       └───────────────────┘
```

Banking moved that window sideways.

Hierarchical navigation adds another direction:

```text
             Project
                │
                ▼
          ┌───────────┐
          │   Group   │
          └───────────┘
                │
                ▼
          Child Tracks
```

So the X-Touch can now move:

```text
← sideways through banks →

and

↓ deeper into structure
↑ back towards the parent
```

This is how eight physical channel strips can remain useful in a much larger project.

---

# Flat Track Navigation

Hierarchical navigation is not the only option.

DrivenByMoss also provides:

```text
Track navigation: Flat
```

In Flat mode, all tracks are presented in one flat track bank rather than using the Group structure as the controller's navigation hierarchy.

That changes what happens when an already-selected Group is selected again.

---

## Repeated SELECT in Flat Mode

With flat navigation:

```text
SELECT an already-selected Group
```

does **not** enter the Group as a new controller level.

Instead it toggles the Group's expanded state.

Conceptually:

```text
Drums ▶
```

becomes:

```text
Drums ▼
   Kick
   Snare
   Hats
```

and vice versa.

This is an important distinction.

The same physical gesture:

```text
SELECT again
```

has different Group behaviour depending on the Track navigation preference.

---

## Flat or Hierarchical?

Neither mode is universally correct.

They represent two different ways of thinking about a project.

### Flat

Think:

> **Show me the tracks as one long mixer.**

### Hierarchical

Think:

> **Show me the project structure, and let me enter the part I need.**

For a small project, Flat may be extremely convenient.

For a large project containing many Groups, Hierarchical navigation can make eight channel strips feel much less restrictive.

The choice is made in the DrivenByMoss settings, which we discuss in Chapter 21.

---

# Opening and Closing Groups Without Entering Them

DrivenByMoss provides another useful Group command:

```text
CONTROL + SELECT
```

If the selected channel is a Group, this opens or closes the Group folder.

So we should distinguish between two ideas:

```text
SELECT again
   → hierarchical navigation into the Group
     when Hierarchical navigation is configured
```

and:

```text
CONTROL + SELECT
   → open / close the Group folder
```

They are related, but they are not the same operation.

---

## Navigation Versus Presentation

This distinction is easier to understand if we think in terms of:

```text
Where am I?
```

versus:

```text
How is the Group displayed?
```

Hierarchical SELECT navigation changes the controller's current level.

CONTROL + SELECT changes the Group's open/closed state.

That gives us two different kinds of Group control without requiring a separate bank of dedicated Group buttons.

---

# Layers

Bitwig instruments can contain Layers.

For example:

```text
Instrument
   │
   ├── Layer 1
   ├── Layer 2
   ├── Layer 3
   └── Layer 4
```

DrivenByMoss allows the X-Touch channel strips to represent those Layers.

The mechanism is deliberately similar to Group navigation.

---

## Entering Layers Mode

First select the track containing the instrument.

If it is not already selected:

```text
SELECT Track
```

Once that track is selected, press its SELECT button again.

If the track contains an instrument with Layers or Drum Pads at the top level, DrivenByMoss enters Layers mode.

Conceptually:

```text
Synth Track
    │
    ▼
SELECT
    │
    ▼
Track selected
    │
    ▼
SELECT again
    │
    ▼
Layer 1   Layer 2   Layer 3   Layer 4
```

The channel strips now represent the instrument's internal elements rather than normal project tracks.

---

## Leaving Layers Mode

The exit mechanism is the same principle used for hierarchical Groups:

```text
Long-press any SELECT button
```

So:

```text
Layer 1   Layer 2   Layer 3   Layer 4
                   │
                   ▼
          long-press SELECT
                   │
                   ▼
              Synth Track
```

This consistency is useful.

Once the repeated-SELECT / long-press-SELECT model becomes familiar, it can be applied to more than one kind of hierarchy.

---

## Layer Mixing

Once Layers mode is active, the Layers can be edited using familiar mixer concepts.

DrivenByMoss supports Layer control for:

```text
Volume

Pan

Sends

Mute

Solo
```

So a layered instrument can effectively become a small mixer inside the larger project mixer.

For example:

```text
Layer A   Layer B   Layer C   Layer D
   │         │         │         │
 Volume    Volume    Volume    Volume
```

You can balance the Layers without needing to treat the instrument as one indivisible sound.

---

## Familiar Modes at a Different Level

The important point is that many of the controls you already know continue to make sense.

The context has changed.

Instead of:

```text
Track 1   Track 2   Track 3   Track 4
```

you may now have:

```text
Layer 1   Layer 2   Layer 3   Layer 4
```

But concepts such as:

```text
Volume
Pan
Send
Mute
Solo
```

remain familiar.

This is a recurring DrivenByMoss design idea:

> **Learn a small number of interaction patterns, then reuse them at different levels of the project.**

---

# Drum Pads

Drum Pads follow the same general model.

Suppose a Bitwig Drum Machine contains:

```text
Kick
Snare
Closed Hat
Open Hat
Clap
Rim
Shaker
Tambourine
```

The X-Touch can expose these through its channel strips when the containing track is entered in Layers/Drum Pad mode.

---

## Entering Drum Pad Mode

Select the track containing the Drum Machine.

Then press SELECT again:

```text
Drum Track
    │
    ▼
SELECT
    │
    ▼
Track selected
    │
    ▼
SELECT again
    │
    ▼
Kick   Snare   CHat   OHat   Clap   Rim   Shaker   Tamb
```

The eight physical channel strips are now a window onto the Drum Machine's pads.

---

## A Drum Machine Becomes a Mixer

This is where the idea becomes particularly useful.

Instead of treating the Drum Machine as one track:

```text
Drums
  │
  ▼
one volume
```

you can work with its internal sounds:

```text
Kick    Snare    Hats    Clap    Perc
 │        │        │       │       │
 ▼        ▼        ▼       ▼       ▼
level    level    level   level   level
```

That gives the X-Touch access to a level of detail that would otherwise require returning to Bitwig's graphical device interface.

---

## Drum Pad Mute and Solo

Mute and Solo become especially useful here.

Suppose you want to hear only the kick and snare.

You can use the familiar SOLO buttons at the Drum Pad level.

Or perhaps one percussion sound is getting in the way.

Use MUTE on that pad.

The physical controls have not changed.

Their targets have.

This is another example of why the current context matters so much on the X-Touch.

---

## Drum Pad Sends

Sends can also be useful at the Layer or Drum Pad level.

Imagine a Drum Machine where:

```text
Kick
   → mostly dry

Snare
   → some reverb

Clap
   → more reverb

Percussion
   → delay
```

Rather than processing the entire Drum Machine identically, individual elements can participate differently in the mix.

This can be particularly useful in electronic music and dub-style workflows.

---

# The Same Surface at Different Scales

We can now see several possible meanings for one physical channel strip.

At one moment it may represent:

```text
Track
```

At another:

```text
Group child
```

At another:

```text
Instrument Layer
```

At another:

```text
Drum Pad
```

Yet the controls remain recognisable:

```text
V-Pot

ARM

SOLO

MUTE

SELECT

Fader
```

The X-Touch is not changing physically.

DrivenByMoss is changing the **context** represented by the hardware.

---

## Context Is Everything

This is why the scribble strips and displays matter.

If Channel 3 represents:

```text
Bass
```

you need to know that.

If you enter a Group and Channel 3 now represents:

```text
Hi-Hat
```

you need to know that too.

If you then enter a layered instrument and Channel 3 represents:

```text
Noise Layer
```

the same physical controls have acquired yet another meaning.

The surface is contextual.

The feedback tells you what the current context is.

---

# A Complete Hierarchical Example

Imagine this project:

```text
Project
│
├── Drums
│   ├── Acoustic Kit
│   └── Drum Machine
│
├── Bass
│
├── Synths
│   ├── Pad
│   └── Lead
│
└── Vocals
```

Assume Track navigation is set to Hierarchical.

At the top level, the X-Touch might show:

```text
Drums   Bass   Synths   Vocals
```

You want the snare inside the Drum Machine.

---

## Step 1 — Select Drums

```text
SELECT Drums
```

Drums becomes the selected Group.

---

## Step 2 — Enter Drums

Press the same SELECT again:

```text
SELECT Drums again
```

The surface now shows:

```text
Acoustic Kit   Drum Machine
```

---

## Step 3 — Select Drum Machine

```text
SELECT Drum Machine
```

The Drum Machine track becomes selected.

---

## Step 4 — Enter its Drum Pads

Press the same SELECT again:

```text
SELECT Drum Machine again
```

Now the surface might show:

```text
Kick   Snare   CHat   OHat   Clap   Rim   Perc   Tamb
```

---

## Step 5 — Adjust the Snare

The Snare is now simply one of the visible channel-strip targets.

Use the appropriate edit mode to adjust:

```text
Volume

Pan

Send

Mute

Solo
```

---

## Step 6 — Leave Drum Pad Mode

Long-press any SELECT button.

You return from the Drum Pads to the containing track context.

---

## Step 7 — Leave the Drums Group

Long-press SELECT again as appropriate to return to the parent Group level.

Eventually:

```text
Drums   Bass   Synths   Vocals
```

is visible again.

We have moved:

```text
Project
   ↓
Drums Group
   ↓
Drum Machine
   ↓
Drum Pads
   ↓
Snare
```

and then back out again.

All without needing ENTER or CANCEL for the hierarchy.

---

# SELECT as Navigation

We can now refine the mental model of SELECT that began much earlier in this guide.

At its simplest:

```text
SELECT
   → this one
```

But in a hierarchical context:

```text
SELECT
   → focus this object

SELECT again
   → enter its internal level,
     where supported

long-press SELECT
   → leave the current internal level
```

And with a modifier:

```text
CONTROL + SELECT
   → open / close a Group folder
```

That is a remarkable amount of navigation built around one consistent row of buttons.

---

## Other Useful SELECT Modifiers

The channel SELECT buttons also have several other modifier combinations.

These are worth recognising even though they are not all specifically about hierarchy.

```text
SHIFT + SELECT
   → No assigned operation in Bitwig

OPTION + SELECT
   → Stop the playing clip
     on that track

CONTROL + SELECT
   → Open / close Group folder

ALT + SELECT
   → Set New Clip Length

SEND + SELECT
   → Select Send 1–8
```

With Bitwig Studio and DrivenByMoss 26.6.3, ALT + SELECT 1–8 chooses lengths from 1 beat to 32 bars. The selected length appears momentarily on the Track 1 scribble strip.

So SELECT is not merely a row of eight identical track-selection switches.

It is one of the most contextually useful parts of the surface.

---

# Hierarchy and Banking Work Together

Entering a Group does not mean that banking ceases to matter.

A Group may contain more than eight child tracks.

For example:

```text
Drums
│
├── Kick
├── Snare Top
├── Snare Bottom
├── Hi-Hat
├── Tom 1
├── Tom 2
├── Overheads
├── Room
├── Shaker
├── Tambourine
└── Claps
```

The first bank might expose:

```text
Kick   SnTop   SnBot   Hat   Tom1   Tom2   OH   Room
```

Then BANK can move the eight-channel window further through the Group.

So we now have two complementary navigation systems:

```text
Hierarchy
   → choose the level

Banking
   → choose the portion of that level
```

This is how the X-Touch scales.

---

## A Useful Mental Picture

Imagine the Bitwig project as a building.

Groups are rooms.

Tracks, Layers and Pads are things inside those rooms.

The X-Touch gives you a window.

BANK moves the window sideways:

```text
←          →
```

Hierarchical SELECT navigation moves you through the structure:

```text
↓ enter

↑ leave
```

The eight physical strips remain the same size.

But the space they can explore becomes much larger.

---

# Why Hierarchical Navigation Matters

Without hierarchy, a controller with eight channel strips can seem limited.

A project may contain:

```text
40 tracks
```

or:

```text
80 tracks
```

or more.

But a large project is often organised into meaningful structures:

```text
Drums

Bass

Guitars

Synths

Vocals

FX
```

Hierarchical navigation lets the controller work with those structures rather than treating the project as one enormous flat list.

At the top level, the project can remain comprehensible.

When detail is needed, you descend into it.

Then you come back out.

---

## The Controller Follows Your Attention

This leads to a useful way of thinking about the X-Touch.

Your attention may move like this:

```text
Whole Project
     ↓
Drums
     ↓
Drum Machine
     ↓
Snare
```

The X-Touch can follow that attention.

Then:

```text
Snare
  ↑
Drum Machine
  ↑
Drums
  ↑
Whole Project
```

The controller moves back out with you.

That is more useful than thinking merely in terms of button combinations.

The buttons are implementing a change in **attention**.

---

# Hierarchical Versus Flat Is a Workflow Choice

There is no requirement to use hierarchical navigation.

If you prefer:

```text
one long mixer
```

choose Flat.

If you prefer:

```text
top-level structure
       ↓
drill into detail
       ↓
return
```

choose Hierarchical.

This is a configuration choice, not a test of whether you are using the X-Touch correctly.

Chapter 21 discusses the DrivenByMoss settings in more detail.

---

# A Mouse-Lite Benefit

Groups, Layers and Drum Pads provide a good example of the Mouse-Lite idea.

Without hardware navigation, a common sequence might be:

```text
look at screen
     ↓
find Group
     ↓
open Group
     ↓
find track
     ↓
open device
     ↓
find Drum Machine
     ↓
find pad
     ↓
adjust control
```

With a familiar X-Touch workflow:

```text
SELECT
   ↓
SELECT again
   ↓
SELECT
   ↓
SELECT again
   ↓
adjust
```

That does not mean the graphical route is wrong.

Sometimes it will be clearer or faster.

But the physical route can allow your hands and ears to remain engaged with the mix.

---

## Don't Descend Further Than You Need

Hierarchy is useful, but there is no prize for navigating to the deepest possible level.

If the problem is:

> **The entire drum Group is too loud**

adjust the Group.

Do not enter it.

If the problem is:

> **The snare is too loud**

then descend far enough to reach the snare.

A useful rule is:

> **Work at the highest level that solves the problem.**

This keeps the workflow efficient.

---

# The Important Idea

The X-Touch's eight channel strips are not tied permanently to eight top-level tracks.

They can represent different levels of the Bitwig project.

With hierarchical Track navigation:

```text
SELECT
   → select

SELECT again
   → enter Group

long-press SELECT
   → leave Group
```

For a selected track containing top-level Layers or Drum Pads:

```text
SELECT again
   → enter Layers / Drum Pads

long-press SELECT
   → leave Layers / Drum Pads
```

With Flat Track navigation:

```text
SELECT an already-selected Group
   → toggle its expanded state
```

And independently:

```text
CONTROL + SELECT
   → open / close Group folder
```

Once inside Layers or Drum Pads, familiar mixer concepts continue to apply:

```text
Volume
Pan
Sends
Mute
Solo
```

So the controller can move from:

```text
Project
```

to:

```text
Group
```

to:

```text
Track
```

to:

```text
Layer / Drum Pad
```

and back again.

The physical surface stays the same.

**Its meaning changes with your attention.**

---

## Coming Next

Hierarchy lets us move downward into the details of a project.

But the X-Touch can also move in the opposite direction — upwards to the level of the project itself.

Touching the Master fader enters a special DrivenByMoss context where the V-Pots no longer represent ordinary track controls.

They can control the Master channel, the audio engine and even project navigation.

Next:

**Master Mode and Project Control.**
