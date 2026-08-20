---
chapter: 21
title: "Configuring DrivenByMoss for the X-Touch"
status: draft
---

# Configuring DrivenByMoss for the X-Touch

For most of this guide, we have concentrated on the X-Touch itself.

Press this button.

Turn this V-Pot.

Move this fader.

Enter this mode.

But there is another part of the system that we have deliberately kept in the background:

**DrivenByMoss configuration.**

The X-Touch does not communicate with Bitwig in isolation.

The complete system is:

```text
X-Touch
   │
   ▼
Mackie Control protocol
   │
   ▼
DrivenByMoss
   │
   ▼
Bitwig Studio
```

DrivenByMoss sits between the hardware and the DAW.

Its configuration therefore determines some important aspects of how the surface behaves.

---

## Configuration Is Part of the Instrument

It is tempting to think of configuration as something separate from actually making music.

Open Settings.

Choose some options.

Close Settings.

Forget about them.

But configuration can have a direct effect on the musical workflow.

Consider New Clip Length.

If you regularly create four-bar clips, configuring that behaviour in advance removes a decision from the recording process.

Instead of:

```text
Create clip
    ↓
Choose length
    ↓
Confirm
    ↓
Record
```

you can move towards:

```text
Create
   ↓
Record
```

The configuration has become part of the workflow.

A useful principle is:

> **Configure beforehand so that you have less to configure while making music.**

---

## The Configuration Page

DrivenByMoss settings are accessed from Bitwig's controller configuration.

The precise appearance may vary slightly between Bitwig and DrivenByMoss versions, but the basic idea is the same.

The controller entry represents the connection between:

```text
Bitwig
   ↕
DrivenByMoss
   ↕
X-Touch
```

This is where the controller's MIDI ports and behaviour are configured.

---

## Choose the Correct Controller

The X-Touch should be configured using the appropriate **Mackie MCU** controller implementation supplied by DrivenByMoss.

This matters because the X-Touch can operate in several hardware protocols.

Project XTC assumes that the unit is operating in:

**MC — Mackie Control mode.**

If the X-Touch is operating in another protocol, the behaviour described throughout this guide should not be expected to match.

---

## Confirm MC Mode on the X-Touch

The X-Touch's operating mode is selected on the hardware.

For use with this guide, confirm:

```text
Mode
  ↓
MC
```

rather than one of the alternative controller protocols.

Once selected and confirmed, the X-Touch communicates using the Mackie Control protocol expected by DrivenByMoss.

This is the foundation on which everything else depends.

---

## MIDI Ports

The X-Touch exposes MIDI ports to the computer.

On a typical system these may include names such as:

```text
X-Touch INT

X-Touch EXT
```

The **INT** connection is the one associated with the main internal X-Touch control surface.

The **EXT** connection exists for expansion-related communication.

For a single X-Touch used as the main controller, make sure the DrivenByMoss controller entry is connected to the appropriate X-Touch MIDI input and output.

The important relationship is:

```text
X-Touch MIDI OUT
        │
        ▼
DrivenByMoss Input


DrivenByMoss Output
        │
        ▼
X-Touch MIDI IN
```

Communication must work in both directions.

---

## Why Both Directions Matter

The X-Touch is not merely sending commands to Bitwig.

Bitwig is also sending information back.

For example:

```text
Move fader
    ↓
Bitwig parameter changes
```

but also:

```text
Bitwig parameter changes
        ↓
Motor fader moves
```

Likewise, DrivenByMoss sends information for:

- displays;
- LEDs;
- V-Pot rings;
- motor faders.

So an apparently half-working controller can be a useful diagnostic clue.

If Bitwig responds to the X-Touch but the X-Touch does not update correctly, check the return path.

The control surface needs a **conversation**, not a monologue.

---

## A Simple Connection Test

After configuring the ports, perform a few basic tests.

### Test 1 — Fader to Bitwig

Move a channel fader.

Does the corresponding Bitwig value move?

### Test 2 — Bitwig to Fader

Change that value in Bitwig.

Does the physical fader move?

### Test 3 — Track Selection

Press SELECT.

Does Bitwig select the expected track?

### Test 4 — Display Feedback

Does the X-Touch display meaningful track or parameter information?

### Test 5 — Transport

Press PLAY and STOP.

Does Bitwig respond correctly?

If all five work, the basic two-way connection is in good shape.

---

## Don't Troubleshoot Advanced Features First

If Device Mode or Browser Mode appears not to work, it can be tempting to start changing advanced settings.

Before doing that, verify the basics.

A useful troubleshooting order is:

```text
Hardware mode
     ↓
MIDI ports
     ↓
Basic transport
     ↓
Track control
     ↓
Feedback
     ↓
Advanced modes
```

There is little value debugging an advanced feature while the underlying controller connection is incorrect.

---

# DrivenByMoss Behaviour Settings

Once the basic connection works, the more interesting configuration begins.

DrivenByMoss provides settings that influence how the MCU surface behaves.

Not every user will want the same choices.

That is intentional.

The controller should adapt to the workflow.

---

## Flat or Hierarchical Track Navigation

Chapter 17 introduced two ways of thinking about project tracks:

```text
Flat
```

and:

```text
Hierarchical
```

The choice affects how Groups are represented and navigated.

### Flat Navigation

A flatter approach prioritises moving through tracks as a sequence.

Conceptually:

```text
Track 1
Track 2
Track 3
Track 4
Track 5
...
```

This can be convenient if you mostly want rapid access to individual tracks regardless of Group structure.

### Hierarchical Navigation

A hierarchical approach preserves the structure of Groups.

Conceptually:

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
   └── Vocals
```

This allows the controller's view to move into and out of Groups.

Neither approach is inherently better.

They answer different needs.

---

## Choosing the Navigation Style

Ask how you think about large projects.

If your mental model is:

> **Give me a long mixer and let me move along it.**

a flatter approach may feel natural.

If your mental model is:

> **Let me see the broad structure and then drill into what I need.**

hierarchical navigation may be more useful.

The second approach fits particularly well with the workflow developed in Chapters 17 and 20:

```text
Project
   ↓
Group
   ↓
Track
   ↓
work
   ↓
back out
```

But the correct choice is the one that matches the way you actually work.

---

## New Clip Length

Chapter 19 introduced **New Clip Length**.

This determines the length used when the controller creates a new Launcher clip.

For example:

```text
1 bar

2 bars

4 bars

8 bars
```

The useful setting depends on the music.

If you frequently build four-bar patterns, a four-bar default may reduce unnecessary interaction.

If you normally work with longer phrases, another value may make more sense.

This is a good example of configuration serving muscle memory.

Once the setting matches your normal workflow, you stop thinking about it.

---

## Configure for the Common Case

A useful general principle is:

> **Set defaults for what you do most often, not for every theoretical possibility.**

Suppose:

```text
70% of new clips → 4 bars
20%              → 8 bars
10%              → something else
```

A four-bar default is probably sensible.

The fact that some clips require another length does not make the default wrong.

A good default reduces work **most of the time**.

---

## V-Pot Behaviour

Rotary encoders can behave differently depending on the type of parameter and the controller configuration.

DrivenByMoss translates the MCU encoder messages into Bitwig parameter changes and returns feedback to the V-Pot rings and displays.

The practical goal is simple:

```text
Turn
  ↓
Predictable change
  ↓
Useful visual feedback
```

If V-Pots seem excessively fast, slow or otherwise unintuitive, check the available DrivenByMoss configuration before assuming that the hardware itself is at fault.

---

## Touch Sensitivity and Motor Faders

The X-Touch's touch-sensitive motor faders are central to:

- automation;
- parameter feedback;
- FLIP;
- track volume control.

They depend on correct two-way communication.

A useful diagnostic distinction is:

### Fader sends values but does not move

Check the controller's output path back to the X-Touch.

### Fader moves but touch behaviour is unexpected

Check:

- the current automation mode;
- the current controller context;
- relevant DrivenByMoss behaviour.

Do not immediately assume a mechanical fault.

Context matters.

---

## Display Configuration

The scribble strips are not decoration.

As Chapter 7 established, they are part of the control system.

They tell you what the physical controls currently represent.

A useful configuration should therefore favour readable, meaningful feedback.

Remember the relationship:

```text
Mode changes
     ↓
Assignments change
     ↓
Displays change
     ↓
You know what the controls mean
```

Without the last step, a deeply contextual control surface becomes much harder to use.

---

## Parameter Names and Values

When Device Mode exposes parameters, the X-Touch has limited display space.

DrivenByMoss must compress information that Bitwig may normally display in a much larger graphical interface.

So do not expect the scribble strip to reproduce the entire Bitwig parameter description.

The aim is:

> **enough information to identify the control confidently.**

That is another reason familiarity matters.

A short parameter label that initially looks cryptic may become immediately recognisable after repeated use.

---

# Configuration for Particular Workflows

Rather than asking which settings are "best", it is often more useful to ask:

> **Best for what?**

---

## Configuration for Conventional Mixing

If the X-Touch is primarily being used as a mixer, priorities may include:

- predictable track banking;
- clear track names;
- immediate fader control;
- panorama access;
- Sends;
- Mute and Solo;
- automation.

The desired experience is:

```text
Select
   ↓
Mix
   ↓
Bank
   ↓
Continue mixing
```

Complex hierarchical navigation may be less important if the project structure is relatively simple.

---

## Configuration for Large Projects

For projects containing many Groups, hierarchical navigation becomes more attractive.

For example:

```text
Drums
Bass
Guitars
Keys
Vocals
FX
```

can provide a compact top-level view.

Then:

```text
SELECT Drums
      ↓
ENTER
      ↓
Kick
Snare
Hats
Toms
Percussion
```

gives access to detail only when needed.

The configuration is helping the eight channel strips scale to a much larger project.

---

## Configuration for Launcher-Based Work

For Launcher-oriented composition, priorities may include:

- New Clip Length;
- overdub behaviour;
- clip creation;
- navigation;
- Clip Based Looper options.

The goal is to reduce interruptions to the loop-building cycle:

```text
Create
   ↓
Record
   ↓
Loop
   ↓
Overdub
   ↓
Listen
```

A well-chosen default clip length can be more valuable here than an advanced option that is rarely touched.

---

## Configuration for Device-Heavy Work

If much of your work involves instruments and effects, Device Mode becomes especially important.

Priorities include:

- useful parameter feedback;
- predictable page navigation;
- easy device selection;
- effective V-Pot behaviour;
- FLIP where appropriate.

The desired path is:

```text
Track
   ↓
Device
   ↓
Parameter Page
   ↓
Parameter
```

with as little unnecessary navigation as possible.

---

## Configuration for Dub and Performance Mixing

Our Chapter 20 example suggests another set of priorities.

For performance-oriented mixing, useful behaviour includes:

- immediate fader access;
- fast Send selection;
- reliable Mute state;
- clear feedback;
- responsive automation;
- predictable banking.

The workflow might move rapidly between:

```text
Faders
   ↓
Mutes
   ↓
Send 1 — Reverb
   ↓
Send 2 — Delay
   ↓
Faders
```

Here, predictability matters more than novelty.

When performing a mix, you do not want to stop and wonder what the surface is going to do.

---

# The DrivenByMoss Settings Are Not a Test

There is a temptation with sophisticated software to assume that there must be one expert configuration.

There isn't.

A setting is not more advanced merely because it is more complicated.

The best configuration is the one that makes the controller behave predictably for **your work**.

That may be surprisingly simple.

---

## Change One Thing at a Time

When experimenting with configuration, avoid changing many settings simultaneously.

Use:

```text
Change one setting
      ↓
Test
      ↓
Understand the effect
      ↓
Keep or revert
```

rather than:

```text
Change six settings
      ↓
Something is different
      ↓
Which setting did that?
```

This is particularly important with a contextual controller where one configuration choice may affect several workflows.

---

## Test Changes Musically

A setting can look sensible in a preferences panel and still feel awkward in practice.

After changing something, use the controller for a real task.

If you change track navigation, navigate a real project.

If you change clip behaviour, create some clips.

If you change an encoder-related option, adjust real parameters.

The question is not:

> **Does the setting work?**

It is:

> **Does the setting improve the workflow?**

---

## Keep a Known-Good Configuration

Once the X-Touch is behaving reliably, it is worth knowing what that working configuration looks like.

If a future update changes behaviour, a known-good setup gives you something to compare against.

Useful things to record include:

```text
Bitwig version

DrivenByMoss version

X-Touch firmware version

X-Touch operating mode

MIDI port assignments

important DrivenByMoss options
```

This turns:

> Something has changed.

into the much more useful:

> **What changed between these two known configurations?**

---

## Version Matters

DrivenByMoss continues to develop.

Bitwig continues to develop.

Behaviour may therefore change after this guide is published.

Project XTC should always state the versions against which its instructions were verified.

That does not mean the guide instantly becomes useless when a new version appears.

It means the reader knows the reference point.

For example:

```text
Verified with:

Bitwig Studio 6.1 beta 4
DrivenByMoss 26.3.3
X-Touch firmware 1.22
```

A later version can then be compared with something concrete.

---

## Updates Can Add Functionality

This guide itself grew because we discovered functionality that had not yet been represented adequately.

Features such as:

```text
OPTION + MARKER
```

were easy to miss if we looked only at the most obvious controls.

DrivenByMoss development may introduce further capabilities.

So configuration and documentation should both be treated as living things.

The controller you know today may be able to do more tomorrow.

---

## After an Update

After updating Bitwig or DrivenByMoss, do not immediately assume that every existing workflow remains identical.

Perform a quick sanity check.

For example:

```text
Transport
   ✓

Faders
   ✓

SELECT
   ✓

Banking
   ✓

Displays
   ✓

Device Mode
   ✓

Sends
   ✓
```

If those fundamentals behave normally, continue to the more specialised functions you use.

This takes very little time and can prevent considerable confusion later.

---

## Troubleshooting by Layer

Remember the complete system:

```text
X-Touch Hardware
       │
       ▼
MC Protocol
       │
       ▼
MIDI Connection
       │
       ▼
DrivenByMoss
       │
       ▼
Bitwig
```

When something fails, work through those layers.

### Is the X-Touch in MC mode?

If not, fix that first.

### Are the MIDI ports correct?

If not, DrivenByMoss cannot communicate properly.

### Does basic transport work?

If not, the problem is probably more fundamental than Device Mode.

### Does feedback return to the X-Touch?

If commands work but displays or motors do not, investigate the return path.

### Does only one advanced feature fail?

Now look at the relevant mode or configuration.

Troubleshooting from the bottom upwards is much more efficient than randomly changing settings.

---

## Don't Forget the Obvious Things

Control-surface problems can sometimes have wonderfully uninteresting causes.

Before investigating obscure protocol behaviour, check:

- the X-Touch is powered on;
- the correct mode is selected;
- the correct MIDI ports are assigned;
- the controller entry is active;
- the expected track or mode is selected;
- the current project actually contains the object you are trying to control.

The more sophisticated the system becomes, the easier it is to overlook something simple.

---

# A Sensible Starting Configuration

Project XTC is not going to prescribe one mandatory configuration.

But for someone following the workflows in this guide, a sensible starting point is:

```text
X-Touch Mode
   → MC

MIDI
   → X-Touch internal ports

Track Navigation
   → choose deliberately:
      flat or hierarchical

New Clip Length
   → set to your most common loop length

Feedback
   → verify displays, LEDs,
      V-Pots and motor faders

Advanced options
   → leave at known defaults
      until you have a reason
      to change them
```

Then use the controller.

Let actual workflow problems tell you which configuration deserves attention.

---

## Configuration Should Eventually Disappear

This may sound strange in a chapter about configuration, but the goal of good configuration is to stop thinking about configuration.

When the system is set up well:

```text
Turn on X-Touch
      ↓
Open Bitwig
      ↓
Work
```

You should not need to reconsider the controller architecture every session.

The configuration has done its job when it becomes invisible.

---

## The Important Idea

DrivenByMoss configuration determines the environment in which all the controls described in this guide operate.

The aim is not to discover the most complicated setup.

It is to create a **predictable one**.

Configure:

- the correct MCU mode;
- the correct MIDI ports;
- the navigation style that suits your projects;
- useful defaults such as New Clip Length;
- the behaviour required by your normal workflow.

Then verify the two-way conversation:

```text
You
  ↓
X-Touch
  ↓
DrivenByMoss
  ↓
Bitwig

and

Bitwig
  ↓
DrivenByMoss
  ↓
X-Touch
  ↓
You
```

When that loop works reliably, the technology begins to recede.

And the controller becomes what we wanted from the beginning:

**a predictable physical route into the project.**

---

## Coming Next

We now have a working controller, a mental model for understanding it, and a configuration that supports the way we want to work.

But DrivenByMoss goes further.

There are specialised options and expansion possibilities that not every user will need immediately.

The final chapter looks beyond the core workflow at:

- customisation;
- specialised options;
- Clip Based Looper;
- expansion;
- extending the surface;
- adapting the system as DrivenByMoss evolves.

Next:

**Customisation and Expansion.**
