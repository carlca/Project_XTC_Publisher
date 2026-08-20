---
chapter: 20
title: "Towards a Mouse-Free (or Mouse-Lite) Workflow"
status: draft
---

# Towards a Mouse-Free (or Mouse-Lite) Workflow

We now know that the X-Touch can do rather a lot.

It can:

- navigate tracks and banks;
- select and control devices;
- browse for devices and presets;
- control volume, panorama and Sends;
- navigate markers;
- enter Groups;
- work with layers and drum pads;
- control automation;
- record and overdub;
- operate at Master and project level.

It would therefore be tempting to turn all of this into a challenge:

> **Can we use Bitwig without touching the mouse at all?**

Perhaps.

But that is not really the most useful question.

A better one is:

> **When is the X-Touch a better way of expressing what I want to do?**

That leads us away from the idea of a strictly mouse-free workflow and towards something more practical:

**a Mouse-Lite workflow.**

---

## The Mouse Is Not the Enemy

There are things a mouse does extremely well.

If you need to:

- draw a detailed automation curve;
- edit individual MIDI notes;
- make a precise graphical selection;
- rearrange complicated regions;
- configure an unfamiliar device;
- perform detailed housekeeping;

Bitwig's graphical interface may be exactly the right tool.

There is no prize for refusing to use it.

The problem arises when reaching for the mouse becomes automatic.

```text
Want to change something
        │
        ▼
Reach for mouse
        │
        ▼
Find pointer
        │
        ▼
Find object
        │
        ▼
Click
```

Sometimes that is appropriate.

Sometimes the X-Touch already has the answer beneath your fingers.

---

## From Commands to Intentions

At the beginning of this guide, we learned individual operations.

```text
Move fader
Press SELECT
Turn V-Pot
Press PLAY
```

Then we learned modes and modifiers.

Now we can stop thinking primarily in terms of commands.

Instead, start with the intention:

> **What am I trying to accomplish?**

For example:

```text
"The vocal is too loud."
```

That intention may translate directly into:

```text
Find vocal channel
       ↓
Move fader
```

Or:

```text
"The delay needs more feedback."
```

may become:

```text
Select delay track/device
       ↓
Device Mode
       ↓
Find parameter
       ↓
Turn V-Pot
```

The controller becomes useful when the physical operation follows naturally from the musical thought.

---

## The Shortest Useful Path

A Mouse-Lite workflow is not necessarily the workflow with the fewest button presses.

It is the workflow with the least unnecessary interruption.

Compare:

```text
Hear problem
    ↓
Look at screen
    ↓
Find pointer
    ↓
Find track
    ↓
Find parameter
    ↓
Adjust
```

with:

```text
Hear problem
    ↓
Touch control
    ↓
Adjust
```

The second route may allow your attention to remain on the sound.

That is the real advantage.

---

## Learn Locations, Not Lists

One reason hardware becomes fast is that the body learns where things are.

After enough use, you do not think:

> The PLAY button is located at this coordinate on the controller.

Your hand simply goes there.

The same can become true of:

- MUTE;
- SOLO;
- SELECT;
- ARM;
- SEND;
- DEVICE;
- BANK;
- CHANNEL;
- modifiers;
- transport controls.

This is different from using a graphical interface, where controls may move, disappear, scroll out of view or belong to another window.

Physical controls have geography.

That geography can become muscle memory.

---

## Keep Your Eyes on the Feedback

Mouse-Lite does not mean screen-blind.

The X-Touch itself provides displays, LEDs, motor positions and V-Pot rings.

Bitwig provides additional feedback on the computer.

Use both.

The important change is that looking does not always have to be followed by pointing.

A useful pattern is:

```text
Look
  ↓
Understand context
  ↓
Operate physically
  ↓
Listen
```

rather than:

```text
Look
  ↓
Find pointer
  ↓
Point
  ↓
Click
  ↓
Look again
```

---

## Build Workflows from Small Habits

Trying to become "mouse-free" overnight would be frustrating.

Instead, identify operations that you perform repeatedly.

Perhaps:

```text
Play / Stop

Track selection

Volume

Pan

Mute / Solo

Banking
```

Use the X-Touch for those until they become automatic.

Then add:

```text
Sends

Device Mode

Markers

Automation

Browser
```

Eventually, several small habits connect into complete workflows.

---

# Workflow 1 — Navigating a Project

Suppose you want to listen to the chorus.

A screen-oriented workflow might involve finding the chorus visually and clicking the timeline.

But if the project has useful markers:

```text
OPTION + FORWARD
       ↓
Next Marker
       ↓
OPTION + FORWARD
       ↓
Chorus
       ↓
PLAY
```

You are navigating the **structure of the music**, not pixels on a timeline.

That distinction becomes increasingly valuable as projects grow.

---

## Add Markers While You Work

If you repeatedly visit a position, give it a marker.

For example:

```text
Intro
Verse
Chorus
Breakdown
Outro
```

or more task-specific landmarks:

```text
Vocal problem
Bass edit
Big transition
Mix check
```

The project gradually acquires a map that the X-Touch can navigate.

The mouse is not being eliminated.

The need to search visually is being reduced.

---

# Workflow 2 — Moving from the Mix into Detail

Suppose you are balancing the top-level project:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

Something is wrong with the snare.

Instead of opening the Group on screen:

```text
SELECT Drums
      ↓
ENTER
      ↓
Kick   Snare   Hats   Toms   Percussion
      ↓
Adjust Snare
      ↓
CANCEL
      ↓
Drums   Bass   Guitars   Keys   Vocals   FX
```

The X-Touch has effectively changed magnification.

You moved:

```text
Project
   ↓
Group
   ↓
Child Track
```

made the adjustment, and came back out.

This is hierarchical navigation becoming a workflow rather than an abstract feature.

---

# Workflow 3 — Working with a Device

Suppose a synth needs adjustment.

The process might be:

```text
SELECT Track
      ↓
DEVICE
      ↓
Choose Device
      ↓
Choose Parameter Page
      ↓
Turn V-Pot
```

If the parameter would be more naturally performed with a fader, FLIP may give you another physical approach.

The important thing is that the X-Touch can move from:

```text
Track
```

to:

```text
Device
```

to:

```text
Parameter
```

without requiring every stage to be performed graphically.

---

## Browser When You Need Something New

Sometimes the required device is not already there.

That is where Browser Mode enters the workflow.

Conceptually:

```text
Need something
     ↓
Browser Mode
     ↓
Navigate choices
     ↓
Select
     ↓
Return to work
```

Again, the goal is not to prove that the Bitwig Browser can be avoided.

It is to prevent the creative process from unnecessarily turning into a mouse-navigation exercise.

---

# Workflow 4 — Recording a Performance

A recording workflow can connect many of the controls we have already learned.

```text
Navigate to position
       ↓
SELECT Track
       ↓
ARM
       ↓
Set metronome if needed
       ↓
RECORD
       ↓
Perform
       ↓
STOP
       ↓
Listen
```

If the take is wrong:

```text
UNDO
  ↓
Try again
```

If it is nearly right, another pass or overdub may be more appropriate.

The controller begins to support the **cycle of recording**, rather than merely the moment when RECORD is pressed.

---

# Workflow 5 — Performing Automation

Suppose a track needs a level ride.

Rather than drawing the automation first:

```text
Choose automation mode
       ↓
PLAY
       ↓
Listen
       ↓
Touch fader
       ↓
Perform movement
       ↓
Release
       ↓
Listen again
```

The automation is created as a musical gesture.

If it needs correction, perform another pass.

This is one of the clearest examples of the X-Touch offering something fundamentally different from a mouse.

A mouse edits a line extremely well.

A fader performs a movement extremely well.

Use each where it makes sense.

---

# Workflow 6 — The X-Touch as a Dub Mixing Desk

Now for an example that brings many of these ideas together.

A traditional dub mix is not simply a set of static mixer settings.

The **mix itself becomes a performance**.

Faders move.

Channels disappear and return.

Sounds are thrown into delays.

Reverbs bloom and vanish.

Effects become rhythmic events.

That makes dub an unusually good demonstration of what a physical control surface can offer.

---

## Set Up the Project

Imagine a simplified arrangement containing:

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

And suppose the project has two Sends:

```text
Send 1 → Reverb

Send 2 → Delay
```

The exact effects do not matter.

The important point is that the tracks can be fed into them independently.

---

## Start with the Faders

In the normal mixer view, the eight motor faders give us:

```text
Drums   Bass   Skank   Organ   Perc   Vocal   FX 1   FX 2
  │       │      │       │      │      │       │      │
  ▼       ▼      ▼       ▼      ▼      ▼       ▼      ▼
█████   █████  █████   █████  █████  █████   █████  █████
```

Now the mix is physical.

You can ride several elements at once.

You can bring the organ forward.

Pull the vocal back.

Drop the percussion.

Return the drums.

These are not eight separate editing operations.

They can be part of one continuous performance.

---

## Mutes Become Musical Controls

MUTE does not have to be merely corrective.

In a dub mix it can become rhythmic.

For example:

```text
Full Mix
   ↓
Mute Drums
   ↓
Bass + Skank + Vocal
   ↓
Return Drums
   ↓
Mute Vocal
   ↓
Instrumental passage
```

The mixer becomes part of the arrangement.

You are deciding in real time what the listener hears.

---

## Move to the Reverb Send

Press SEND to expose the first Send.

Suppose Send 1 is the reverb.

Now the V-Pots provide something like:

```text
             REVERB

Drums   Bass   Skank   Organ   Perc   Vocal   FX 1   FX 2
  │       │      │       │      │      │       │      │
  ▼       ▼      ▼       ▼      ▼      ▼       ▼      ▼
 Send    Send   Send    Send   Send   Send    Send   Send
```

The controller is no longer primarily asking:

> **How loud is each track?**

It is asking:

> **How much of each track should enter the reverb?**

That is a completely different view of the same mix.

---

## Perform the Reverb

Perhaps the vocal reaches the end of a phrase.

Turn its Send up.

Let the phrase bloom into the reverb.

Then bring the Send back down.

Or send a snare hit heavily into the reverb while leaving the kick comparatively dry.

The effect is not merely configured.

It is **played**.

---

## Move to the Delay

Press SEND again to reach the delay Send.

Now the same eight V-Pots answer:

> **How much of each track should enter the delay?**

This is where things become particularly entertaining.

A vocal phrase ends:

```text
"...into the night"
          │
          ▼
Raise Vocal Send
          │
          ▼
"...night... night... night..."
```

Then pull the Send back.

The delay throw becomes a performance gesture.

---

## Send the Unexpected Things

Dub mixing becomes interesting when effects are not treated merely as polite ambience.

Try sending:

```text
Snare       → Delay

Organ stab  → Delay

Percussion  → Reverb

Vocal word  → Delay
```

then pulling the Send away again.

The effect becomes an event.

And because the X-Touch exposes several Send levels simultaneously, you can react to the music rather than repeatedly opening individual track controls.

---

## Faders + Mutes + Sends

Now combine the operations.

For example:

```text
Drop Organ fader
       ↓
Mute Vocal
       ↓
Throw Snare into Delay
       ↓
Bring Organ back
       ↓
Increase Percussion Reverb
       ↓
Return Vocal
       ↓
Drop Drums
       ↓
Bass continues alone
       ↓
Drums return
```

At this point you are no longer merely "operating Bitwig".

You are **performing the mix**.

---

## Use the Surface Like an Instrument

This is the important change of perspective.

A conventional editing mindset says:

```text
Set this value.

Now set that value.

Now change another value.
```

A performance mindset says:

```text
Listen.

Move.

React.

Anticipate.

Return.
```

The X-Touch is particularly good at the second kind of interaction because several controls are physically available at once.

You have two hands.

Use them.

---

## Capture the Dub Performance with Automation

There is another possibility.

The performance does not have to disappear when playback stops.

Enable the appropriate automation-writing mode and Bitwig can capture the movements.

Conceptually:

```text
PLAY
  ↓
Perform Mix
  │
  ├── Fader rides
  ├── Send movements
  └── other automated parameters
  ↓
STOP
  ↓
Bitwig remembers
```

Now play the section again.

The motor faders reproduce the movements you performed.

The live mix has become automation.

---

## Perform First, Edit Later

The first pass does not need to be perfect.

That is important.

Try:

```text
Perform
   ↓
Listen
   ↓
Keep what works
   ↓
Correct what doesn't
```

If one fader move is late, correct it.

If one Send stays open too long, fix it.

If a particular transition works brilliantly, leave it alone.

The control surface and graphical editor complement one another.

The surface captures the gesture.

The GUI can provide surgical correction afterwards.

That is Mouse-Lite working at its best.

---

## A Dub Pass Might Look Like This

Imagine an eight-bar passage.

### Bars 1–2

Full rhythm section.

Vocal present.

Moderate reverb.

### Bar 3

Mute vocal after the final word.

Throw that word into the delay.

### Bar 4

Drop drums.

Leave bass and delay repeats.

### Bar 5

Return drums.

Bring organ up.

### Bar 6

Push percussion into reverb.

### Bar 7

Drop organ and percussion.

Return vocal.

### Bar 8

Delay the final vocal phrase and pull several faders down into the transition.

None of this requires a complicated theoretical model.

It requires listening and reacting.

The X-Touch provides the physical controls.

---

## Why Dub Demonstrates the Point So Well

The lesson is not really about dub.

The same principles apply to:

- electronic music;
- ambient;
- techno;
- live remixing;
- soundtrack work;
- conventional mixing.

Dub simply makes the idea unusually obvious.

The mixer is not merely a place where levels are set.

It can be a **performance environment**.

And a physical control surface makes that idea tangible.

---

# Workflow 7 — From Broad Mix to Tiny Detail

Now imagine something happens during that mix.

A percussion sound is too loud.

The broad view is:

```text
Drums   Bass   Skank   Organ   Percussion   Vocal
```

But the percussion track contains a Drum Machine.

Navigate deeper:

```text
SELECT Percussion
       ↓
ENTER / appropriate Pad context
       ↓
Shaker   Conga   Rim   Bell   Tambourine   ...
```

Adjust the offending pad.

Then return.

This demonstrates something important.

A Mouse-Lite workflow does not mean remaining at one level of abstraction.

The X-Touch can move from:

```text
whole project
```

to:

```text
track
```

to:

```text
device
```

to:

```text
pad or layer
```

and back again.

---

# Workflow 8 — Moving Between Songs or Projects

At the other extreme, suppose you have finished working on the current project.

Touch the Master fader to enter the Master context.

Use the project-navigation controls to move to another project.

The same surface that moments ago was adjusting one drum pad can now operate at the level of:

```text
the entire project
```

That change in scale is one of the most remarkable aspects of the DrivenByMoss mapping.

---

## Think in Layers of Attention

A useful way to summarise the whole controller is by thinking about the level at which your attention currently sits.

```text
PROJECT
   │
   ▼
GROUP
   │
   ▼
TRACK
   │
   ▼
DEVICE
   │
   ▼
PARAMETER
```

or:

```text
TRACK
   │
   ▼
INSTRUMENT
   │
   ▼
LAYER / PAD
```

The X-Touch can move its focus through these levels.

The question becomes:

> **Where is my attention right now?**

Then put the controller there too.

---

## The Surface as a Moving Window

We began this guide with eight channel strips.

They looked fixed.

Now we know better.

Those eight strips can be a window onto:

```text
Tracks

Group contents

Layers

Drum pads

Sends

Parameters
```

The V-Pots can represent:

```text
Pan

Sends

Device parameters

Track parameters

Project controls
```

The faders can represent:

```text
Track volume

Other parameters through FLIP

Automation performances
```

The physical surface stays put.

Its meaning moves.

---

## Modes Are Views, Not Obstacles

When first encountering a controller like the X-Touch, modes can seem like a complication.

Why can't every control simply do one thing?

Because then we would need an enormous controller.

Instead, think:

> **A mode gives me the view appropriate to the job I am doing.**

If you want to mix:

```text
Mixer view
```

If you want to edit a device:

```text
Device view
```

If you want to browse:

```text
Browser view
```

If you want to navigate markers:

```text
Marker view
```

Modes are not hiding functionality from you.

They are organising it.

---

## Modifiers Are Temporary Questions

Likewise, modifiers become easier to remember when treated as questions.

Instead of thinking:

```text
I must memorise OPTION + this,
SHIFT + that,
CONTROL + something else...
```

think:

> **Is there a related operation available here?**

For example:

```text
MARKER
```

works with markers.

Then:

```text
OPTION + MARKER
```

provides a related marker operation: create one.

The combination makes sense because it belongs to the task.

---

## Let Repetition Build Muscle Memory

At first, you will still think:

> Which button was that?

That is normal.

Then you will think:

> Ah yes — OPTION + MARKER.

Eventually, your hand may simply do it.

The progression is:

```text
Remember
   ↓
Recognise
   ↓
Repeat
   ↓
Muscle memory
```

That is when a hardware controller begins to disappear from conscious attention.

You stop operating the X-Touch.

You simply use it.

---

## Don't Try to Use Everything

DrivenByMoss exposes a remarkable amount of functionality.

That does not mean every function needs to become part of your workflow.

If you never use a particular mode, that is fine.

If you prefer editing MIDI with the mouse, keep doing it.

If you love using the physical faders but prefer the Bitwig Browser on screen, that is also fine.

The goal is not completeness.

The goal is **fluency**.

A small set of operations that you can perform without thinking may be more valuable than fifty shortcuts you can barely remember.

---

## Build Your Own Core Workflow

A useful personal core might be:

```text
Transport

Track selection

Banking

Volume

Mute / Solo

Sends

Device control

Markers
```

Someone else might prioritise:

```text
Transport

Recording

Overdub

Browser

Drum pads

Automation
```

There is no universally correct set.

The X-Touch should adapt to the work rather than forcing the work to adapt to the controller.

---

## Know When to Reach for the Mouse

This may be the most important Mouse-Lite skill of all.

Do not turn a simple graphical operation into a twenty-button hardware puzzle merely because the controller technically permits it.

If the mouse is clearly faster:

**use the mouse.**

If the X-Touch keeps you closer to the music:

**use the X-Touch.**

If the keyboard shortcut is better than either:

**use the keyboard shortcut.**

The objective is not ideological purity.

It is a smoother path between:

```text
Intention
    ↓
Action
    ↓
Result
```

---

## Mouse-Free as an Experiment

There is still value in occasionally attempting a genuinely mouse-free session.

Not because it is necessarily the best way to work.

Because it reveals habits.

Try working for fifteen minutes without reaching for the mouse.

Every time you feel the urge, ask:

> **Can the X-Touch already do this?**

Sometimes the answer will be no.

Sometimes the answer will be yes, but awkwardly.

And sometimes you will discover:

> **Yes — and actually this is better.**

Those discoveries are how a personal Mouse-Lite workflow develops.

---

## From Control Surface to Musical Surface

At the beginning of Project XTC, the X-Touch could easily be seen as:

> **a box containing faders and buttons that remotely control Bitwig.**

That description is technically true.

But it misses something.

Once the surface becomes familiar, it can participate in the musical process.

You can:

```text
navigate by song structure;

reach into a Group;

balance a Drum Machine;

shape a device;

perform automation;

record a part;

build a clip;

ride a mix;

throw a vocal into delay.
```

Those are not merely software commands.

They are actions within a musical workflow.

---

## The Important Idea

A Mouse-Lite workflow does not begin by banning the mouse.

It begins by noticing where the X-Touch offers a more immediate relationship with the music.

The aim is not:

```text
NO MOUSE
```

It is:

```text
Hear intention
      ↓
Choose the most natural control
      ↓
Act
      ↓
Keep listening
```

Sometimes that control will be the mouse.

Sometimes the keyboard.

Very often, it can be the X-Touch.

And the more familiar the surface becomes, the less often you need to stop and think about the controller itself.

The modes stop feeling like modes.

The modifiers stop feeling like shortcuts.

The eight channel strips stop feeling like only eight channels.

They become a moving window onto the project.

And eventually the question changes from:

> **What can this button do?**

to:

> **What do I want to do?**

That is the point at which the X-Touch stops merely controlling the DAW.

It becomes part of the way you work.

---

# End of Part IV

We have now reached the end of the main workflow section of Project XTC.

The final part turns from **using** the system to **shaping** it.

DrivenByMoss provides configuration choices that determine how the X-Touch behaves, and some of the more advanced functions only make sense once those choices are understood.

Next:

# Part V — Configuration and Reference

**Chapter 21 — Configuring DrivenByMoss for the X-Touch**
