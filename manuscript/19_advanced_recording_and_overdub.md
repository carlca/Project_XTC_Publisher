---
chapter: 19
title: "Advanced Recording and Overdub"
status: draft
---

# Advanced Recording and Overdub

The RECORD button looks simple enough.

Press it, and Bitwig records.

But Bitwig has more than one recording environment.

It has the linear **Arranger**.

It has the clip-based **Launcher**.

It can record new material.

It can overdub onto existing material.

And DrivenByMoss gives the X-Touch access to several of these operations without requiring us to reach for the mouse.

The important question is therefore not simply:

> **How do I record?**

It is:

> **What do I want Bitwig to record, and where?**

---

## Two Recording Worlds

Bitwig gives us two related but distinct ways of organising music.

### The Arranger

The Arranger is based around a linear timeline:

```text
Time ─────────────────────────────────────►

Track 1  ████████████████████████████████
Track 2       ███████████████████████
Track 3            █████████████
```

Music has a position in time.

Recording into the Arranger creates material along that timeline.

### The Launcher

The Launcher is based around clips that can be triggered independently:

```text
          Scene 1    Scene 2    Scene 3

Track 1   [ Clip ]   [ Clip ]   [ Clip ]
Track 2   [ Clip ]   [ Clip ]   [ Clip ]
Track 3   [ Clip ]   [ Clip ]   [ Clip ]
```

Here the important object is not merely a timeline position.

It is a **clip**.

That difference matters when we start talking about recording and overdubbing.

---

## The RECORD Button

The X-Touch's **RECORD** button provides the main recording operation.

At its simplest:

```text
RECORD
   ↓
Recording
```

But, as with so many X-Touch controls, modifiers give the button additional meanings.

DrivenByMoss can use the same physical control for related recording operations.

The button therefore belongs to a family of actions rather than one isolated command.

---

## Recording Starts with Track ARM

Before recording musical input, the appropriate track normally needs to be armed.

The channel-strip **ARM** buttons provide direct access to that state.

Conceptually:

```text
Choose track
    ↓
ARM
    ↓
Track ready to record
    ↓
RECORD
```

This is an important distinction.

**ARM** answers:

> Which track should receive the input?

**RECORD** answers:

> Should Bitwig record now?

Keeping those two ideas separate makes recording behaviour much easier to understand.

---

## Arranger Recording

For conventional linear recording, the workflow is straightforward.

### 1. Select the track

Establish focus on the track you want to record.

### 2. Arm it

Press the corresponding ARM button.

### 3. Position the transport

Use the transport controls, Jog Wheel or markers.

### 4. Start recording

Press RECORD.

### 5. Perform

Bitwig records into the Arranger.

Conceptually:

```text
Position
   ↓
ARM
   ↓
RECORD
   ↓
Perform
   ↓
Arranger material
```

The X-Touch therefore provides the essential physical controls for a conventional recording pass.

---

## Recording and Playback Are Related

Recording does not exist separately from transport.

Before recording, we may need to:

- locate the start position;
- set the loop;
- enable the metronome;
- configure a count-in;
- arm a track.

During recording, we may need to:

- monitor the transport;
- adjust a performance;
- stop;
- restart.

Afterwards, we need to:

- return;
- listen;
- record another pass.

So the recording workflow combines several ideas we have already learned:

```text
Navigation
    +
Transport
    +
Track focus
    +
ARM
    +
RECORD
    =
Recording workflow
```

This is why learning the controller as a system is more useful than memorising individual buttons.

---

## Overdub Is Not the Same as Record

The word **overdub** means that existing material remains while new material is added.

Conceptually:

```text
Existing material
       +
New performance
       =
Combined material
```

That is different from simply recording a new passage.

The distinction becomes especially important with MIDI and Launcher clips.

---

## Arranger Overdub

Bitwig can overdub note data into existing Arranger material.

Instead of replacing the existing notes, the new performance is added.

For example, suppose a MIDI clip already contains:

```text
Kick       ●       ●       ●       ●
Snare          ●               ●
```

An overdub pass might add:

```text
Hat        x   x   x   x   x   x   x   x
```

giving:

```text
Kick       ●       ●       ●       ●
Snare          ●               ●
Hat        x   x   x   x   x   x   x   x
```

The original performance remains.

The new one becomes part of it.

---

## Why Overdub Is Useful

Overdub encourages a layered way of working.

A drum pattern might be built as:

```text
Pass 1
   ↓
Kick and Snare

Pass 2
   ↓
Hi-Hats

Pass 3
   ↓
Percussion

Pass 4
   ↓
Extra hits
```

Likewise, a MIDI instrument performance might begin with chords and later acquire additional notes.

The controller allows recording to become an iterative process rather than a one-shot operation.

---

## Launcher Overdub

The Launcher introduces its own overdub workflow.

Instead of thinking about the Arranger timeline, we are working with a clip.

Conceptually:

```text
Launcher Clip
      │
      ▼
Existing Notes
      │
      │ overdub
      ▼
Existing Notes
      +
New Notes
```

This is particularly useful for loop-based composition.

Start with a simple idea.

Let it repeat.

Add another part.

Let it repeat again.

Add another.

The clip develops while playback continues.

---

## OVR

The X-Touch's **OVR** control participates in the overdub workflow.

DrivenByMoss maps the MCU controls onto Bitwig's available recording and overdub functions.

As elsewhere in this guide, the printed MCU label should not be treated as a guarantee that Bitwig has an identically named internal function.

The useful question is always:

> **What Bitwig recording state is this control changing?**

The final Quick Reference will give the verified mapping for the DrivenByMoss version covered by Project XTC.

---

## Arranger and Launcher Overdub Are Different States

It is worth keeping these conceptually separate.

```text
Arranger Overdub
       │
       ▼
Add material to existing
Arranger note content
```

versus:

```text
Launcher Overdub
       │
       ▼
Add material to an
existing Launcher clip
```

Both involve adding rather than replacing.

But they act in different recording environments.

When something appears not to be overdubbing as expected, one of the first questions should therefore be:

> **Am I working in the Arranger or the Launcher?**

---

## OPTION + RECORD

DrivenByMoss gives **OPTION + RECORD** an additional recording-related function.

This is one of the advanced combinations identified during the MCU feature audit.

Rather than treating it as an isolated shortcut, place it in the broader model:

```text
RECORD
    │
    ├── normal
    │      primary recording operation
    │
    └── OPTION
           related advanced
           recording operation
```

The exact current behaviour should be verified against the DrivenByMoss version used for final publication before it is placed in the Quick Reference.

This is preferable to inferring behaviour merely from older MCU conventions or the label printed on the controller.

---

## Creating a New Clip

Launcher recording introduces another practical problem.

What happens if there is no clip yet?

Before we can overdub into a clip, there needs to be a clip to receive the material.

DrivenByMoss provides control-surface operations for creating clips.

Conceptually:

```text
Empty slot
    │
    ▼
Create Clip
    │
    ▼
New empty clip
    │
    ▼
Record / Overdub
```

This allows the Launcher workflow to begin from the X-Touch rather than requiring the initial clip to be created with the mouse.

---

## New Clip Length

If the controller creates a new clip, another question immediately appears:

> **How long should it be?**

DrivenByMoss provides a **New Clip Length** setting.

For example, a new clip might be:

```text
1 bar
2 bars
4 bars
8 bars
```

depending on the chosen configuration.

Conceptually:

```text
New Clip Length
       │
       ▼
Create Clip
       │
       ▼
Clip of configured length
```

This is an important example of the relationship between **configuration** and **performance**.

During a session, you want clip creation to be immediate.

Before the session, you decide what behaviour will usually be most useful.

---

## Configuration Removes Decisions from Performance

Suppose you normally build four-bar loops.

If New Clip Length is already configured appropriately, the creative workflow can become:

```text
Create
   ↓
Record
   ↓
Loop
   ↓
Overdub
```

rather than:

```text
Create
   ↓
Specify length
   ↓
Confirm
   ↓
Record
```

A good configuration removes repetitive decisions from the musical moment.

We will return to this principle in Chapter 21.

---

## Building a Clip in Layers

A Launcher workflow might look like this:

### Pass 1 — Foundation

Record the basic idea.

```text
Kick + Snare
```

### Pass 2 — Add movement

Enable the appropriate overdub state and add:

```text
Hi-Hats
```

### Pass 3 — Add detail

Add:

```text
Percussion
```

### Pass 4 — Listen

Let the clip repeat without playing.

### Pass 5 — Correct or extend

Add only what the pattern needs.

This turns recording into a conversation with the loop.

---

## Recording Without Stopping the Idea

One of the attractions of overdub-based working is continuity.

Instead of:

```text
record
  ↓
stop
  ↓
edit
  ↓
record
  ↓
stop
```

the process can become:

```text
play
  ↓
record
  ↓
overdub
  ↓
listen
  ↓
overdub
  ↓
listen
```

The musical idea keeps moving.

For some styles of composition, that can be much more productive.

---

## Looping and Recording

The loop controls introduced earlier become especially useful during recording.

Set a region.

Let it repeat.

Perform another pass.

Conceptually:

```text
Loop Region
┌────────────────────┐
│                    │
└────────────────────┘
        ▲
        │
    repeats

Pass 1 → Pass 2 → Pass 3 → ...
```

Combined with overdub, the X-Touch can support a workflow in which a section develops over successive repetitions.

---

## Recording by Ear

There is a recurring theme here.

A screen-based recording workflow can easily become:

```text
find control
    ↓
click
    ↓
watch cursor
    ↓
find another control
```

A well-configured control surface allows more of the process to become:

```text
listen
   ↓
ARM
   ↓
RECORD
   ↓
perform
   ↓
listen
```

The screen remains useful.

But it does not have to mediate every decision.

---

## Recording and Markers

Markers from Chapter 15 can also become part of the recording workflow.

Suppose a vocal needs replacing in the second chorus.

Instead of searching visually for the section:

```text
OPTION + FORWARD
       ↓
Second Chorus marker
       ↓
ARM
       ↓
RECORD
```

Navigation and recording now form one physical workflow.

This is where apparently separate controller features begin to reinforce one another.

---

## Recording and Groups

The hierarchy from Chapter 17 can also matter.

A large project may contain a Group of recording tracks.

You can navigate into the Group, select the required track, arm it and record.

Conceptually:

```text
Project
   ↓
Recording Group
   ↓
Track
   ↓
ARM
   ↓
RECORD
```

Again, the individual commands matter less than the fact that they connect into a sequence.

---

## Recording and the Metronome

The Master fader also participates in the recording environment.

As noted earlier:

```text
SHIFT + Master Fader
```

controls metronome volume.

This is a particularly good example of a control-surface feature whose usefulness becomes obvious in context.

During recording you may want the click:

- loud enough to perform accurately;
- quiet enough not to dominate;
- changed without opening another Bitwig panel.

The modified Master fader gives you a direct physical control.

---

## Undo Is Part of Recording

Not every take is worth keeping.

That is not a failure of the workflow.

It is part of recording.

A practical control-surface workflow should therefore include the ability to:

```text
Record
   ↓
Listen
   ↓
No
   ↓
UNDO
   ↓
Try again
```

Undo is not merely an editing command.

During performance-oriented recording, it can become part of the creative cycle.

---

## The Value of Immediate Recovery

The faster you can recover from a bad take, the less disruptive the mistake becomes.

Compare:

```text
bad take
   ↓
stop
   ↓
reach for mouse
   ↓
find edit
   ↓
undo
   ↓
reposition
   ↓
start again
```

with:

```text
bad take
   ↓
stop
   ↓
UNDO
   ↓
start again
```

That difference may amount to only a few seconds.

Musically, it can be much larger.

The second workflow is more likely to preserve momentum.

---

## Clip Based Looper

DrivenByMoss also includes **Clip Based Looper** functionality.

This extends the idea of creating and building clips from the control surface into a more specialised looping workflow.

It is worth knowing that the functionality exists.

However, it should not be confused with the basic recording and overdub concepts in this chapter.

The core progression remains:

```text
Create Clip
    ↓
Record
    ↓
Loop
    ↓
Overdub
```

Clip Based Looper builds a more specialised workflow on top of those ideas.

Because it is configurable and goes beyond the normal everyday MCU workflow, we will return to it in Chapter 22.

---

## Don't Learn Recording as a Button Table

The X-Touch provides several recording-related controls.

It would be possible to summarise them immediately as a table of button combinations.

But that would hide the important distinctions.

Instead, ask:

### Where am I recording?

```text
Arranger
or
Launcher?
```

### What am I doing?

```text
New recording
or
Overdub?
```

### What is the destination?

```text
Timeline
or
Clip?
```

### Does the destination already exist?

```text
Existing clip
or
New clip?
```

Once those questions are answered, the relevant control becomes much easier to understand.

---

## A Recording Decision Tree

A useful mental model is:

```text
              RECORD SOMETHING
                     │
          ┌──────────┴──────────┐
          │                     │
      Arranger               Launcher
          │                     │
     ┌────┴────┐           ┌────┴────┐
     │         │           │         │
    New     Overdub      New Clip  Existing Clip
                               │         │
                               ▼         ▼
                            Record    Overdub
```

You do not need to consciously follow this diagram every time you press RECORD.

Its purpose is to separate several operations that otherwise all look like "recording".

---

## A Practical Arranger Workflow

Suppose you want to record a guitar part.

### 1. Navigate to the section

Use transport or markers.

### 2. Select the guitar track

Establish focus.

### 3. Arm the track

Press ARM.

### 4. Set the metronome level if necessary

Use the available X-Touch control.

### 5. Press RECORD

Perform the part.

### 6. Stop and listen

Use the transport controls.

### 7. Undo if necessary

Then try again.

This is conventional recording, but most of the mechanical process can remain on the control surface.

---

## A Practical Launcher Workflow

Suppose instead that you are building a rhythmic idea in the Launcher.

### 1. Choose the track

Select and arm it.

### 2. Create or select the destination clip

Use the appropriate clip workflow.

### 3. Record the first layer

Establish the foundation.

### 4. Enable the appropriate overdub state

Keep the existing material.

### 5. Add another layer

Let the clip continue looping.

### 6. Listen

Do nothing for a pass if necessary.

### 7. Add only what is needed

The controller becomes part of an iterative composition process.

---

## A Practical Dub-Oriented Example

There is another interesting possibility.

Imagine building a rhythmic foundation in the Launcher:

```text
Drums
Bass
Skank
Percussion
```

Once the clips are established, the X-Touch can move naturally from **recording surface** to **mixing surface**.

The same hardware that helped create the material can then provide:

- fader rides;
- mutes;
- Send levels;
- delay throws;
- reverb changes.

In other words:

```text
Build the material
        ↓
Arrange the controls
        ↓
Perform the mix
```

We are going to return to this idea properly in Chapter 20.

There, the X-Touch gets to behave rather more like a traditional dub mixing desk.

---

## The Important Idea

Advanced recording becomes much easier to understand once we stop treating RECORD as one universal operation.

Ask four questions:

```text
WHERE?
   Arranger or Launcher?

WHAT?
   New recording or overdub?

INTO WHAT?
   Timeline or clip?

WHAT ALREADY EXISTS?
   Nothing or existing material?
```

Then the X-Touch controls fit into a meaningful workflow.

The important concepts are:

```text
ARM
   → choose what receives input

RECORD
   → perform the primary recording operation

Overdub
   → add to existing material

New Clip Length
   → determine the size of newly created clips

Clip creation
   → establish a Launcher destination

OPTION + RECORD
   → advanced recording-related operation
     to be verified for the target version
```

The aim is not to memorise a larger collection of recording commands.

It is to make recording from the X-Touch feel like a connected process:

```text
Navigate
   ↓
Arm
   ↓
Record
   ↓
Perform
   ↓
Listen
   ↓
Overdub or Undo
   ↓
Continue
```

The less machinery you have to think about, the more attention remains available for the performance.

---

## End of Part III

We have now gone considerably deeper into what DrivenByMoss makes possible on the X-Touch.

We have explored:

- Mixer Edit Modes;
- Markers and structural navigation;
- Automation;
- Groups and hierarchical navigation;
- Instrument Layers;
- Drum Pads;
- Master Mode;
- project-level control;
- advanced recording;
- overdubbing.

Individually, these are useful features.

But Project XTC was never intended to become merely a better-organised list of features.

The real question is:

> **What happens when we put them together?**

That is the purpose of Part IV.

---

# Part IV — Building the Workflow

The next chapter brings together everything we have learned so far.

Transport.

Faders.

V-Pots.

Modes.

Modifiers.

Devices.

Browser.

Markers.

Automation.

Recording.

And, yes, Sends.

It is time to stop thinking about what each individual control can do and start thinking about what **we can do with the whole surface**.

Next:

**Towards a Mouse-Free (or Mouse-Lite) Workflow.**
