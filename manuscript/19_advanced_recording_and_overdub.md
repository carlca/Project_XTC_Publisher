---
chapter: 19
title: "Advanced Recording and Overdub"
status: draft
---

# Advanced Recording and Overdub

Recording sounds simple.

Press RECORD.

Play something.

Press STOP.

And for straightforward Arranger recording, that may be all you need.

But Bitwig has more than one recording environment.

It has the linear **Arranger**.

It has the performance-oriented **Clip Launcher**.

And it has **overdub**, where new material is added without replacing what is already there.

DrivenByMoss gives the X-Touch direct access to these different recording workflows.

The important thing is knowing **which kind of recording you are asking Bitwig to perform**.

---

## The Basic RECORD Button

The normal RECORD button performs the most obvious function:

```text id="m8t47f"
RECORD
   │
   ▼
Start / Stop Recording
```

This is the standard recording command.

For a conventional linear recording workflow:

```text id="y8v04q"
Arm Track
    ↓
Position Play Cursor
    ↓
RECORD
    ↓
Perform
    ↓
STOP
```

there is nothing mysterious about it.

But RECORD also participates in two important modifier combinations.

---

# Three RECORD Operations

DrivenByMoss documents these three RECORD commands:

```text id="x2tq1p"
RECORD
   → Start / Stop recording


SHIFT + RECORD
   → Toggle Launcher overdub


OPTION + RECORD
   → Create a new clip on the selected
     track and slot,
     start playback,
     and enable overdub
```

These are not three variations of the same operation.

They represent three different recording intentions.

---

## RECORD — Record Normally

Think:

> **Record.**

```text id="g2t5qo"
RECORD
   ↓
Normal recording
```

This is the direct transport operation.

It is the appropriate starting point when your intention is simply to record in the normal Bitwig workflow.

---

## SHIFT + RECORD — Launcher Overdub

Hold SHIFT and press RECORD:

```text id="j31pqd"
SHIFT + RECORD
       │
       ▼
Toggle Launcher Overdub
```

This does **not** merely start another ordinary recording pass.

It changes the Launcher overdub state.

Think:

> **When working with Launcher clips, allow new material to be added to what is already there.**

---

## OPTION + RECORD — Create, Play and Overdub

This is the more specialised command:

```text id="p3v38r"
OPTION + RECORD
       │
       ▼
Create new clip
on selected track and slot
       │
       ▼
Start playback
       │
       ▼
Enable overdub
```

That combination is particularly interesting because one physical command establishes an entire clip-recording state.

It does not merely toggle an existing setting.

It creates something and gets it ready for performance.

---

# Arranger and Launcher

To understand these commands, we need to distinguish Bitwig's two principal working environments.

Conceptually:

```text id="xx6b0m"
Bitwig
  │
  ├── Arranger
  │      │
  │      └── linear timeline
  │
  └── Launcher
         │
         └── clips / scenes
```

Both can contain musical material.

Both can participate in recording.

But they encourage different ways of working.

---

## Arranger Thinking

The Arranger is fundamentally linear.

Think:

```text id="j2v0bz"
START ─────────────────────────────► END
```

A song develops through time.

Recording naturally fits a model such as:

```text id="e13qai"
Bar 1
  ↓
Bar 2
  ↓
Bar 3
  ↓
Bar 4
  ↓
...
```

This is familiar tape-machine-style thinking.

---

## Launcher Thinking

The Launcher is more modular.

Think:

```text id="n9x68m"
Clip A    Clip B    Clip C

Clip D    Clip E    Clip F

Clip G    Clip H    Clip I
```

A clip can repeat.

Another clip can be launched.

Material can be built incrementally.

That makes **overdub** particularly important.

---

# What Is Overdub?

Suppose a MIDI clip already contains:

```text id="emg1ki"
Kick
Kick
Kick
Kick
```

You want to add a hi-hat pattern without losing the kicks.

Ordinary replacement recording would be the wrong idea.

Overdub means:

```text id="d2zcga"
Existing material
      +
New performance
      =
Combined clip
```

So:

```text id="wp83hf"
Pass 1
Kick     Kick     Kick     Kick

Pass 2
  Hat Hat   Hat Hat   Hat Hat   Hat Hat

Result
Kick+Hat  Kick+Hat  Kick+Hat  Kick+Hat
```

The second pass adds to the first.

---

## Overdub Is Layering in Time

A useful mental model is:

```text id="w6zq0x"
First pass
    ↓
Listen
    ↓
Second pass
    ↓
Add
    ↓
Third pass
    ↓
Add
```

The clip grows through repeated performances.

This is especially useful for:

- drum programming;
- percussion;
- layered MIDI parts;
- loop-based composition;
- performance-oriented workflows.

---

# The OVR Button

The X-Touch has an OVR button.

In DrivenByMoss:

```text id="5hwd6t"
OVR
   → Toggle Arranger Overdub
```

and:

```text id="0drf6v"
SHIFT + OVR
   → Toggle Launcher Overdub
```

This gives us a very useful pair:

```text id="zgg4at"
OVR
   → Arranger overdub

SHIFT + OVR
   → Launcher overdub
```

The modifier changes the target environment.

---

## RECORD and OVR Are Related but Different

It is worth separating two concepts.

RECORD answers:

> **Should recording run?**

OVR answers:

> **When recording, should new material be added to existing material?**

Conceptually:

```text id="5m43vl"
RECORD
   │
   ▼
Recording state


OVR
   │
   ▼
Overdub behaviour
```

They interact, but they are not interchangeable.

---

# A Useful Recording Map

The verified normal mapping can be summarised as:

```text id="l2l7x0"
RECORD
   → Start / Stop recording

SHIFT + RECORD
   → Toggle Launcher overdub

OPTION + RECORD
   → Create new clip
     + start playback
     + enable overdub

OVR
   → Toggle Arranger overdub

SHIFT + OVR
   → Toggle Launcher overdub
```

Notice something interesting:

```text id="f00v2e"
SHIFT + RECORD
```

and:

```text id="8jhlje"
SHIFT + OVR
```

both give access to Launcher overdub.

That is not a documentation mistake.

DrivenByMoss provides more than one physical route to the same state.

---

## Why Provide Two Routes?

The two routes make sense in different contexts.

If your hand is already around the transport controls:

```text id="2n6ws9"
SHIFT + RECORD
```

may feel natural.

If you are thinking specifically in terms of overdub state:

```text id="6n70gp"
SHIFT + OVR
```

may be easier to remember.

A control surface does not always need one and only one route to every function.

Sometimes redundancy makes a workflow easier.

---

# OPTION + RECORD Is Different

OPTION + RECORD deserves special attention because it does more than toggle Launcher overdub.

It performs a sequence:

```text id="3ykpqa"
Selected Track
      +
Selected Slot
      │
      ▼
OPTION + RECORD
      │
      ▼
Create Clip
      │
      ▼
Start Playback
      │
      ▼
Enable Overdub
```

This is a **workflow command**.

One button combination prepares the selected Launcher location for loop-oriented recording.

---

## Selected Track and Selected Slot Matter

OPTION + RECORD operates on:

```text id="lqgoyx"
Selected Track
      +
Selected Slot
```

So before invoking it, establish the destination.

The command is powerful because it acts immediately.

That means focus matters.

A useful habit is:

```text id="k10zll"
Select destination
      ↓
Check destination
      ↓
OPTION + RECORD
```

As always:

> **Establish focus before performing an action that creates something.**

---

# New Clip Length

When creating clips from the controller, another setting becomes important:

```text id="o9g8pe"
New Clip Length
```

DrivenByMoss allows the default length for newly created clips to be configured.

This means the recording workflow can be prepared before the performance begins.

For example:

```text id="x2sqqx"
New Clip Length
      │
      ▼
4 bars
      │
      ▼
Create new clip
      │
      ▼
Four-bar working structure
```

The exact choice depends on the music.

---

## Setting New Clip Length from the Surface

DrivenByMoss also lets the X-Touch choose a new clip length using the track SELECT buttons with a modifier.

The eight choices are:

```text id="evz8fm"
SHIFT + SELECT 1   → 16 bars

SHIFT + SELECT 2   → 8 bars

SHIFT + SELECT 3   → 4 bars

SHIFT + SELECT 4   → 2 bars

SHIFT + SELECT 5   → 1 bar

SHIFT + SELECT 6   → 2 beats

SHIFT + SELECT 7   → 1 beat

SHIFT + SELECT 8   → 32 bars
```

So New Clip Length does not necessarily require a trip to the DrivenByMoss preferences.

It can be changed directly from the surface.

---

## The Order Is Worth Learning

The sequence is not simply shortest-to-longest or longest-to-shortest.

It is:

```text id="m6ukdq"
SELECT 1     16 bars
SELECT 2      8 bars
SELECT 3      4 bars
SELECT 4      2 bars
SELECT 5      1 bar
SELECT 6      2 beats
SELECT 7      1 beat
SELECT 8     32 bars
```

That final 32-bar assignment means it is worth learning the mapping rather than assuming the buttons form a perfectly linear progression.

This is exactly the sort of detail that will belong in the Quick Reference later.

---

# ALT + SELECT and New Clip Length

DrivenByMoss's common edit-mode functions also document:

```text id="ryj64m"
ALT + Track SELECT
   → Set the length of a new clip
```

The important conceptual point is that the channel SELECT row can participate in clip-length selection as well as track selection.

This is another example of modifiers turning familiar controls into a temporary command surface.

The exact controller feedback should always be observed when using these modified functions.

---

# A Four-Bar Loop Workflow

Suppose you want to build a four-bar MIDI percussion loop.

A controller-oriented workflow could be:

### 1. Select four bars

Use the appropriate New Clip Length selection:

```text id="b7id1q"
SHIFT + SELECT 3
```

### 2. Select the destination track and slot

Establish where the new clip should be created.

### 3. Press OPTION + RECORD

DrivenByMoss creates the clip, starts playback and enables overdub.

### 4. Play the first layer

For example:

```text id="p73nwc"
Kick
```

### 5. Let the clip repeat

Listen to what you recorded.

### 6. Add another layer

For example:

```text id="53v5aw"
Snare
```

### 7. Add another

Perhaps:

```text id="d98t72"
Hi-Hat
```

The clip grows while playback continues.

---

# Building Rather Than Recording

This workflow changes the meaning of the word *recording*.

Instead of:

```text id="7jhj65"
Record complete performance
          ↓
Stop
```

we have:

```text id="7iqi6v"
Create loop
    ↓
Add idea
    ↓
Listen
    ↓
Add idea
    ↓
Listen
    ↓
Add idea
```

That is closer to **building** than traditional recording.

The X-Touch can participate in both approaches.

---

# Arranger Overdub

Now consider the Arranger.

Suppose a MIDI passage already exists and you want to add notes without replacing the existing performance.

Enable:

```text id="jkd1fq"
OVR
```

DrivenByMoss toggles Arranger overdub.

Conceptually:

```text id="7q9ogf"
Existing Arranger material
          +
New recorded material
          │
          ▼
Combined result
```

This is the linear-timeline counterpart to Launcher overdub.

---

# Launcher Overdub

For Launcher clips:

```text id="9gh42f"
SHIFT + OVR
```

toggles Launcher overdub.

Or:

```text id="59xsk7"
SHIFT + RECORD
```

can toggle the same Launcher overdub state.

So the conceptual distinction remains simple:

```text id="72b7yk"
OVR
   → Arranger

SHIFT + OVR
   → Launcher
```

even though Launcher overdub also has the SHIFT + RECORD route.

---

# A Note About Audio and MIDI

Overdub is particularly easy to understand with MIDI because new notes can be added to an existing clip.

For example:

```text id="ngrzgb"
Pass 1   Kick

Pass 2   Snare

Pass 3   Hats
```

produces one increasingly complete MIDI performance.

Do not assume that every audio-recording situation behaves identically.

Bitwig's recording behaviour depends on the type of track, clip and recording context.

Project XTC's concern here is the **X-Touch command mapping**:

```text id="l8r3wv"
which recording state
or overdub state
does the controller request?
```

The detailed editing consequences remain Bitwig behaviour.

---

# Recording Is a State Machine

It can help to think of the recording controls as changing states.

For example:

```text id="2qeh67"
Stopped
   │
   │ RECORD
   ▼
Recording
   │
   │ RECORD / STOP
   ▼
Stopped
```

Then overdub adds another dimension:

```text id="4mkbnf"
Recording
   │
   ├── Arranger overdub OFF
   │
   └── Arranger overdub ON
```

And Launcher operation has its own overdub state:

```text id="2l73yd"
Launcher
   │
   ├── Overdub OFF
   │
   └── Overdub ON
```

Thinking in terms of states helps explain why several buttons can appear to affect “recording” while actually controlling different aspects of it.

---

# Check the State Before Performing

Recording commands are consequential.

A mistaken Pan value is easy to undo.

Recording into the wrong clip or changing the wrong overdub state can be more disruptive.

So before beginning:

```text id="0tw5m7"
Check Track
     ↓
Check Slot
     ↓
Check Clip Length
     ↓
Check Overdub State
     ↓
Perform
```

The more fluent you become, the faster this check becomes.

Eventually it is no more cumbersome than glancing at a mixer before moving a fader.

---

# Arm Is Still Important

The channel-strip ARM buttons remain the obvious way to establish recording targets.

Press the ARM button for the appropriate track:

```text id="y1b1uw"
ARM
 │
 ▼
Track armed
```

DrivenByMoss also provides:

```text id="apn4o4"
SHIFT + ARM
```

to toggle the record-arm state across all tracks in the active Bitwig bank page.

That can be powerful, so use it deliberately.

---

## One Track Versus the Bank

The distinction is:

```text id="t02xpa"
ARM
   → specific track
```

versus:

```text id="k4kef9"
SHIFT + ARM
   → toggle record-arm state
     across tracks in active bank page
```

Again, the modifier changes the scale of the command.

This is a pattern we have seen throughout the X-Touch.

---

# Monitoring from the Surface

DrivenByMoss also provides channel-strip monitoring commands:

```text id="i90zqp"
SHIFT + MUTE
   → Toggle monitor

SHIFT + SOLO
   → Toggle auto monitor
```

These functions belong naturally to a recording workflow.

Before recording, you may need to determine how the armed track is monitored.

The X-Touch can therefore participate not only in:

```text id="6yd9f6"
recording
```

but also:

```text id="3cty9u"
arming
monitoring
overdubbing
```

---

# Recording Without Constant Screen Attention

A hardware-oriented recording workflow might become:

```text id="i37syj"
SELECT track
     ↓
ARM
     ↓
Set monitoring if needed
     ↓
Choose recording / overdub state
     ↓
RECORD
     ↓
Perform
     ↓
STOP
```

For Launcher loop building:

```text id="vp9zgl"
Choose clip length
     ↓
Select track / slot
     ↓
OPTION + RECORD
     ↓
Perform
     ↓
Overdub
     ↓
Listen
```

The computer screen remains available.

It simply does not have to mediate every step.

---

# Recording and Musical Attention

This matters because recording is one of the moments when you least want to be thinking about software.

You may be:

- playing a keyboard;
- holding a guitar;
- singing;
- programming drums;
- manipulating another controller.

Every unnecessary mouse operation interrupts that activity.

A control surface can move routine recording operations into physical memory.

Eventually:

```text id="cq9m11"
I want another pass
```

becomes:

```text id="avc6ga"
hand moves
button pressed
continue playing
```

without requiring a menu search.

---

# Launcher-Oriented Users

There is an important DrivenByMoss preference that affects the recording controls:

```text id="d2igpy"
Flip arranger and clip record / automation
```

When enabled, the normal and SHIFT functions of the Record and Automation buttons are flipped between Arranger-oriented and Clip-oriented behaviour.

This exists for users who spend more time in the Clip Launcher than the Arranger.

Conceptually:

```text id="mctf4s"
Default configuration

Normal
   → Arranger-oriented function

SHIFT
   → Launcher-oriented function
```

can become:

```text id="ue2x7v"
Flipped configuration

Normal
   → Launcher-oriented function

SHIFT
   → Arranger-oriented function
```

We will discuss this preference properly in Chapter 21.

---

## Why the Flip Preference Matters

Without knowing about this preference, two people can press the same physical buttons and report apparently contradictory behaviour.

One says:

> **RECORD does this.**

Another says:

> **No, SHIFT + RECORD does that.**

Both controllers may be behaving correctly.

Their DrivenByMoss configuration may simply differ.

This reinforces an important documentation rule:

> **When behaviour can be configured, describe the default and identify the preference that can change it.**

---

# Recording and Automation Are Parallel Ideas

Recording musical notes and recording automation are conceptually related.

In both cases:

```text id="fjh1un"
You perform something
        ↓
Bitwig captures it
        ↓
Bitwig reproduces it later
```

For notes:

```text id="u8s7w9"
play notes
   ↓
record MIDI
```

For automation:

```text id="q7i1wp"
move fader
   ↓
record automation
```

This is one reason the X-Touch can feel so natural in both roles.

It turns software recording into a physical act.

---

# Overdub as a Performance Tool

Overdub is not merely a technical recording option.

It can become part of a performance.

Imagine building a rhythmic clip:

```text id="4dxby9"
Loop 1
   → kick

Loop 2
   → add snare

Loop 3
   → add hats

Loop 4
   → add percussion
```

The arrangement develops through physical performance rather than through drawing notes.

The X-Touch's role is not to create the musical material.

Its role is to make the **recording state** accessible while the musical material is being created.

---

# A Practical Launcher Workflow

A useful practice exercise is:

### 1. Create an empty MIDI track

Load an instrument.

### 2. Select a four-bar New Clip Length

Use:

```text id="rqj6o4"
SHIFT + SELECT 3
```

### 3. Select an empty Launcher slot

Make sure the intended track and slot are selected.

### 4. Press OPTION + RECORD

The clip is created, playback starts and overdub is enabled.

### 5. Play a simple pattern

Do not try to make it complicated.

### 6. Let it loop

Listen.

### 7. Add another part

Use the active overdub state to layer another performance.

### 8. Toggle Launcher overdub if required

Use:

```text id="e8clpp"
SHIFT + RECORD
```

or:

```text id="a14aob"
SHIFT + OVR
```

### 9. Listen again

The aim of the exercise is not the music.

It is learning the physical relationship between:

```text id="wbih5w"
Clip
   +
Recording
   +
Overdub
   +
X-Touch
```

---

# A Practical Arranger Workflow

For comparison:

### 1. Select and arm the track

Use the channel-strip controls.

### 2. Position the play cursor

Use the transport controls or Jog Wheel.

### 3. Decide whether Arranger overdub is required

If yes:

```text id="6x3bhd"
OVR
```

### 4. Press RECORD

Begin recording.

### 5. Perform

Concentrate on the music.

### 6. Press STOP

Finish the pass.

### 7. Listen

Decide whether another pass is required.

This is much closer to a traditional linear recording workflow.

The same hardware supports both models.

---

# Do Not Memorise Everything at Once

There are several commands in this chapter.

You do not need to learn all of them simultaneously.

Start with:

```text id="50wkr6"
RECORD
   → Record

OVR
   → Arranger overdub
```

Then add:

```text id="kmmvmw"
SHIFT + RECORD
   → Launcher overdub
```

Then:

```text id="a51pr3"
OPTION + RECORD
   → New clip + play + overdub
```

Once those are familiar, the rest becomes easier to place around them.

This is the same learning strategy we have used throughout Project XTC:

> **Build a mental model first. Add commands to it gradually.**

---

# The Important Idea

The X-Touch does not have one generic concept called “recording”.

DrivenByMoss exposes several related states and operations.

The verified normal mappings are:

```text id="j1d0cf"
RECORD
   → Start / Stop recording

SHIFT + RECORD
   → Toggle Launcher overdub

OPTION + RECORD
   → Create a new clip on the
     selected track and slot,
     start playback,
     enable overdub

OVR
   → Toggle Arranger overdub

SHIFT + OVR
   → Toggle Launcher overdub
```

And the channel strips contribute:

```text id="bpl7wo"
ARM
   → Arm specific track

SHIFT + ARM
   → Toggle record-arm state
     across the active bank

SHIFT + MUTE
   → Toggle monitor

SHIFT + SOLO
   → Toggle auto monitor
```

The important question is therefore not simply:

> **How do I record?**

It is:

> **What am I recording, where am I recording it, and do I want to replace or add to what is already there?**

Once that intention is clear, the X-Touch command becomes much easier to choose.

---

## Coming Next

We now have most of the pieces.

We can:

- navigate tracks and banks;
- control devices;
- browse;
- mix;
- use modifiers;
- work with markers;
- perform automation;
- enter Groups, Layers and Drum Pads;
- control the Master context;
- record and overdub.

The next question is:

> **What does all of this feel like when we stop thinking about individual features and actually use the X-Touch to make music?**

Next:

**Towards a Mouse-Free — or Mouse-Lite — Workflow.**
