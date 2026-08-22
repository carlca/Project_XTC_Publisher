---
chapter: 7
title: "Displays and Feedback"
status: draft
---

# Displays and Feedback

The X-Touch does not merely send commands to Bitwig.

Bitwig also sends information back.

That two-way communication is one of the most important differences between the X-Touch and a simple MIDI controller.

A basic MIDI controller might work like this:

```text
Turn Knob
    │
    ▼
Bitwig Changes
```

The X-Touch can work like this:

```text
Turn Knob
    │
    ▼
Bitwig Changes
    │
    ▼
X-Touch Updates
```

The controller therefore becomes part of the user interface.

It does not merely control Bitwig.

It also tells you what Bitwig is doing.

---

# Feedback Is Part of the Control Surface

The X-Touch provides several forms of feedback:

```text
Scribble Strips

V-Pot LED Rings

Button LEDs

Motor Faders

VU Meters

Assignment Display

Segment Display
```

Each communicates a different kind of information.

Together they answer questions such as:

```text
What am I controlling?

Which track is selected?

What mode am I in?

What is the current value?

Is this function active?

What is the current level?

Where is the play cursor?
```

This is why learning to **read** the X-Touch is just as important as learning to operate it.

---

# The Scribble Strips

Above the eight channel strips are the scribble-strip displays.

These are among the most useful parts of the X-Touch.

In a normal mixer context they may show track information such as:

```text
Kick    Snare   Hats    Bass    Keys    Lead    Vocal   FX
```

Change bank:

```text
BANK >
```

and the displays change with the faders:

```text
Perc    Room    Piano   Gtr1    Gtr2    BVox    Verb    Delay
```

The scribble strips tell you what the eight physical channel strips currently represent.

---

# The Displays Follow Context

The same display can mean different things in different modes.

In a mixer context:

```text
Track Name
```

In Send Mode:

```text
Send Information
```

In Device Mode:

```text
Parameter Name
Parameter Value
```

In Browser Mode:

```text
Browser Choice
```

In Marker Mode:

```text
Marker Information
```

So the displays are contextual.

They should not be thought of as permanent track-name labels.

They are the X-Touch's way of answering:

> **What do these controls mean right now?**

---

# Read Before You Touch

This gives us one of the most useful habits for working with the X-Touch:

> **Read before you touch.**

Before turning a V-Pot:

```text
Look at Display
      ↓
Identify Parameter
      ↓
Turn V-Pot
```

Before moving a fader after changing context:

```text
Look at Display
      ↓
Identify Channel
      ↓
Move Fader
```

This becomes increasingly important as the controller moves beyond simple mixing.

---

# Abbreviated Names

The displays have limited width.

Long track or parameter names may therefore be shortened.

For example:

```text
Supermassive Reverb
```

cannot appear in full.

You may see something more like:

```text
SupRvrb
```

The exact abbreviation depends on what Bitwig and DrivenByMoss send.

This is normal.

Over time, frequently used names become surprisingly easy to recognise.

---

# Naming Tracks for Hardware

Because the scribble strips have limited space, sensible track naming helps.

A track named:

```text
Main Lead Vocal Double Processed
```

may not communicate very much on a small display.

A shorter name such as:

```text
Ld Vox
```

may be much more useful.

Likewise:

```text
Kick
Snare
Hat
Bass
Pad
Lead
Vox
Delay
```

work particularly well on a control surface.

You do not have to rename an entire project for the X-Touch.

But concise names can make hardware navigation much easier.

---

# Display Colours

The X-Touch supports coloured scribble-strip backgrounds.

DrivenByMoss can use these as another layer of feedback.

Colour can help distinguish tracks or contexts without requiring you to read every label.

For example, a project might visually separate:

```text
Drums

Bass

Instruments

Vocals

Effects
```

through colour.

The exact colour behaviour depends on the DrivenByMoss hardware and display configuration.

Chapter 21 covers that configuration.

---

# Display Mode

The X-Touch includes a:

```text
DISPLAY MODE
```

control.

DrivenByMoss maps this to:

```text
DISPLAY MODE
   → Toggle Track Names
     in the First Display
```

This changes what the first display row presents.

It gives you a choice between different kinds of contextual information.

Conceptually:

```text
Current Display Information
          │
          │ DISPLAY MODE
          ▼
Track Names
```

and back again.

---

# Why Display Mode Is Useful

There are two questions the surface frequently needs to answer:

```text
What tracks am I controlling?
```

and:

```text
What mode or parameters am I controlling?
```

Those needs can compete for limited display space.

DISPLAY MODE gives you a way to change the emphasis.

If you momentarily lose track of which channels are represented:

```text
DISPLAY MODE
      ↓
Track Names
```

can restore that orientation.

This is especially useful after changing banks or moving into a more specialised controller context.

---

# The Assignment Display

The X-Touch also contains a small assignment display.

DrivenByMoss can use this to show the current controller mode.

For example, the surface may be operating in a context such as:

```text
Panorama

Send

Device

EQ

Browser
```

The assignment display provides another clue to the controller's current state.

This matters because the same physical V-Pot may perform very different jobs in those contexts.

---

# The Segment Display

The large segment display in the Transport area can show transport-related information.

DrivenByMoss can use it to display the play position.

Depending on configuration, this can be represented in forms such as:

```text
Time
```

or:

```text
Measures / Beats
```

The final digits can also display additional information.

---

# TEMPO / TICKS

DrivenByMoss maps the MCU:

```text
TEMPO / TICKS
```

control to toggling the final part of the segment display between:

```text
Tempo
```

and:

```text
Ticks
```

Conceptually:

```text
Segment Display
      │
      ├── Main Position
      │
      └── Final Digits
              │
              │ TEMPO / TICKS
              ▼
        Tempo ↔ Ticks
```

This lets the same limited display area provide two different kinds of timing information.

---

# Which Display Is More Useful?

There is no universally correct choice.

Tempo may be useful when:

```text
setting project speed

matching another piece of music

making fine tempo adjustments
```

Ticks may be more useful when:

```text
working with precise musical position
```

The important point is that the hardware display is configurable rather than fixed.

---

# V-Pot LED Rings

Each V-Pot is surrounded by LEDs.

These provide visual feedback about the current parameter value.

For example, a Pan control might appear approximately as:

```text
Left      Centre      Right

●●○○○      ○○●○○      ○○○●●
```

A level-style parameter may instead appear more like:

```text
Low

●○○○○○○○○○○
```

versus:

```text
High

●●●●●●●●●○○
```

The exact LED-ring representation depends on the parameter.

The important point is:

> **The encoder has no fixed physical position, so the LEDs provide the position information.**

---

# Why Endless Encoders Need Feedback

A normal knob has a physical endpoint.

You can look at it and see:

```text
about 2 o'clock
```

An endless encoder has no such permanent position.

It can rotate forever.

So its meaning has to come from elsewhere:

```text
Display
   +
LED Ring
```

This makes the combination much more flexible.

The same encoder can represent:

```text
Pan

Send Level

Device Parameter

Browser Choice

Master Parameter
```

without needing to physically jump to a new position.

---

# Button LEDs

Many X-Touch buttons illuminate.

These LEDs often indicate whether a function is active.

For example:

```text
MUTE
SOLO
REC
SELECT
REPEAT
```

may provide immediate visual confirmation of state.

This gives us another useful pattern:

```text
Press Button
     ↓
Bitwig State Changes
     ↓
LED Reflects State
```

The light is not merely decoration.

It is confirmation.

---

# State Versus Action

Some buttons represent an ongoing state.

For example:

```text
MUTE
```

can be:

```text
On
```

or:

```text
Off
```

An illuminated button is therefore useful.

Other controls represent an action rather than a persistent state.

For example:

```text
SAVE
```

performs something and finishes.

There is no long-term "Save Mode" that needs to remain illuminated.

Understanding whether a control represents:

```text
State
```

or:

```text
Action
```

helps explain the feedback you should expect.

---

# VU Meters

The channel strips include level-meter feedback.

This lets you see signal activity without relying entirely on Bitwig's mixer.

Conceptually:

```text
Audio Signal
     │
     ▼
Bitwig Level
     │
     ▼
DrivenByMoss
     │
     ▼
X-Touch VU Meter
```

The meter is another example of information travelling **from the DAW back to the hardware**.

---

# EDIT / GLOBAL VIEW — Toggle VU Meters

DrivenByMoss maps the MCU Global View / EDIT control to:

```text
EDIT / GLOBAL VIEW
   → Toggle VU Meters
```

This lets you switch the meter display on or off from the surface.

Conceptually:

```text
VU Meters Off
     │
     │ EDIT
     ▼
VU Meters On
```

and:

```text
VU Meters On
     │
     │ EDIT
     ▼
VU Meters Off
```

If the channel displays appear different after pressing EDIT, remember that this control may have changed the meter feedback rather than the mixer itself.

---

# Why Toggle the VU Meters?

Meters are useful when you want to see:

```text
Signal Presence

Relative Level

Activity Across Tracks
```

But display space is limited.

There may be times when other feedback is more useful than continuous level information.

The toggle lets the surface adapt to the current task.

---

# Motor Faders Are Displays Too

A motor fader is not merely an input control.

Its physical position is also feedback.

Suppose Bitwig reports:

```text
Track Volume = -6 dB
```

The fader moves to the corresponding position.

So:

```text
Bitwig Value
     │
     ▼
Motor
     │
     ▼
Physical Position
```

The fader itself has become a display.

---

# Changing Banks Demonstrates Feedback

Banking makes this particularly obvious.

Suppose the first bank contains:

```text
Kick    Snare   Hats    Bass    Pad     Lead    Vox     FX
```

with eight different volume settings.

Press:

```text
BANK >
```

The controller now represents another set of tracks.

The scribble strips change.

The faders move.

The button LEDs change.

Possibly the VU activity changes.

In other words:

```text
BANK >
   │
   ▼
New Controller Context
   │
   ├── New Names
   ├── New Fader Positions
   ├── New Button States
   └── New Meter Activity
```

The whole surface updates as one system.

---

# Layout Controls

DrivenByMoss also maps three MCU controls to Bitwig's main application layouts:

```text
AUX
   → Arrange Layout

BUSSES
   → Mix Layout

OUTPUTS
   → Edit Layout
```

These controls do not merely change the X-Touch.

They change the layout shown by Bitwig itself.

---

# AUX — Arrange Layout

Press:

```text
AUX
```

to switch Bitwig to:

```text
Arrange Layout
```

This is useful when the main task is working with the timeline and the overall song arrangement.

Conceptually:

```text
AUX
  ↓
Arrange
```

---

# BUSSES — Mix Layout

Press:

```text
BUSSES
```

to switch Bitwig to:

```text
Mix Layout
```

This gives the mixer greater visual emphasis.

Conceptually:

```text
BUSSES
   ↓
Mix
```

This is a good example of a hardware label inherited from MCU being repurposed for a Bitwig-specific operation.

---

# OUTPUTS — Edit Layout

Press:

```text
OUTPUTS
```

to switch Bitwig to:

```text
Edit Layout
```

Conceptually:

```text
OUTPUTS
    ↓
Edit
```

Again, the printed hardware label is less important than the DrivenByMoss assignment.

---

# Three Physical Routes into Bitwig's Main Views

Together:

```text
AUX
   → Arrange

BUSSES
   → Mix

OUTPUTS
   → Edit
```

give the X-Touch direct access to three major Bitwig working layouts.

A useful mental model is:

```text
             Bitwig
                │
      ┌─────────┼─────────┐
      │         │         │
   Arrange     Mix       Edit
      ▲         ▲         ▲
      │         │         │
     AUX      BUSSES    OUTPUTS
```

This can reduce another common reason for reaching for the mouse.

---

# Hardware Labels Can Be Misleading

The layout controls provide an excellent example of why Project XTC concentrates on the **DrivenByMoss mapping**, not simply the text printed on the X-Touch.

A new user seeing:

```text
AUX

BUSSES

OUTPUTS
```

might reasonably assume that these buttons navigate mixer channel types.

In DrivenByMoss they instead mean:

```text
Arrange

Mix

Edit
```

So once again:

> **Do not assume that the printed MCU label describes the Bitwig operation.**

The X-Touch supplies the physical controls.

DrivenByMoss supplies their Bitwig meaning.

---

# Feedback and Layout Work Together

The layout buttons reveal an important distinction.

Some X-Touch controls change:

```text
what the hardware controls
```

Others change:

```text
what Bitwig displays
```

And some operations cause both interfaces to update.

This gives us two related but distinct ideas:

```text
Controller Context
```

and:

```text
Bitwig Layout
```

Do not assume that changing one necessarily changes the other.

---

# The Screen Is Still Useful

Project XTC aims toward a Mouse-Lite workflow.

That does not mean:

> **Never look at the computer.**

The screen remains extremely useful for:

- detailed waveform editing;
- device interfaces;
- Browser exploration;
- arrangement overview;
- visual automation;
- complex modulation.

The X-Touch's feedback complements the screen.

It does not need to reproduce it.

---

# Hardware Feedback Reduces Screen Checking

The benefit is that many simple questions can be answered without looking away from the controller.

Instead of asking the screen:

```text
Which track is this?

Is it muted?

What is its level?

What parameter is this?

What mode am I in?
```

the X-Touch can often answer directly.

That keeps your attention closer to the controls you are physically using.

---

# Feedback Makes Context Safe

A contextual controller would be dangerous without feedback.

Imagine one V-Pot controlling:

```text
Pan
```

then:

```text
Send
```

then:

```text
Filter Cutoff
```

with no indication of which one was active.

That would be unusable.

Feedback makes context practical:

```text
Context Changes
      ↓
Display Changes
      ↓
You Read
      ↓
You Act
```

This is the basic interaction loop of the X-Touch.

---

# Trust the Surface — But Read It

Once the controller is configured correctly, the hardware feedback is there to help you.

If the faders suddenly move after a bank change:

```text
That is information.
```

If the scribble strips change after entering Device Mode:

```text
That is information.
```

If a button lights:

```text
That is information.
```

If the assignment display changes:

```text
That is information.
```

The controller is continually telling you what state it is in.

---

# A Practical Display Exercise

Open a project containing at least eight tracks.

### 1. Read the Scribble Strips

Without looking at Bitwig's mixer, identify the tracks represented by the eight channel strips.

### 2. Press BANK >

Watch:

```text
Track Names

Fader Positions

Button LEDs

VU Activity
```

change.

### 3. Press BANK <

Watch the previous state return.

### 4. Press DISPLAY MODE

Observe how the first display changes.

Press it again and compare the information shown.

The aim is to start treating the displays as an active part of navigation rather than passive decoration.

---

# A Practical VU Exercise

Play a section containing several active tracks.

Watch the channel meters.

Now press:

```text
EDIT / GLOBAL VIEW
```

Observe the change in VU-meter display.

Press it again.

The important relationship is:

```text
EDIT / GLOBAL VIEW
      ↓
VU Feedback Toggle
```

not whatever the printed label might initially suggest.

---

# A Practical Layout Exercise

With a project open, try:

```text
AUX
```

then:

```text
BUSSES
```

then:

```text
OUTPUTS
```

Observe Bitwig move between:

```text
Arrange

Mix

Edit
```

Repeat the sequence several times.

The goal is to associate the **physical button position** with the Bitwig layout rather than relying on the printed MCU name.

---

# A Practical Segment-Display Exercise

Watch the Transport segment display.

Press:

```text
TEMPO / TICKS
```

Observe the final digits.

Press it again.

The aim is simply to recognise that this part of the display is switchable and to learn which representation is most useful for your normal workflow.

---

# If the Feedback Looks Wrong

If the X-Touch displays or LEDs do not seem to match Bitwig, ask:

```text
Am I in the mode I think I am?

Did I change bank?

Did I change track?

Did I change device?

Is FLIP active?

Is DISPLAY MODE showing the view I expect?

Are VU meters enabled?

Is the controller receiving MIDI feedback?

Is the correct DrivenByMoss profile configured?
```

Feedback problems are not always display problems.

Sometimes the controller is correctly showing a context you did not realise you had entered.

---

# Configuration Matters

Several aspects of feedback can be configured in DrivenByMoss.

These include things such as:

```text
Display Setup

Display Colours

VU Behaviour

Segment Display

Track Names

Startup Mode
```

We will deal with those settings in Chapter 21.

For now, the important principle is:

> **If the X-Touch's feedback differs from what you expect, configuration may be part of the explanation.**

---

# A Useful Mental Model

Think of the X-Touch as having two directions of communication.

```text
                YOUR ACTIONS

                    │
                    ▼

                 X-Touch
                    │
                    ▼

                  Bitwig
```

and:

```text
                 BITWIG

                    │
                    ▼

                 X-Touch
                    │
          ┌─────────┼─────────┐
          │         │         │
          ▼         ▼         ▼
       Displays   Motors     LEDs
```

The first direction is control.

The second is feedback.

A good control surface requires both.

---

# The Important Idea

The X-Touch is not simply a collection of physical inputs.

It is a two-way interface.

Its feedback systems include:

```text
Scribble Strips

V-Pot LED Rings

Button LEDs

VU Meters

Motor Faders

Assignment Display

Segment Display
```

DrivenByMoss also gives several physical controls direct display or view functions:

```text
DISPLAY MODE
   → Toggle Track Names
     in First Display

TEMPO / TICKS
   → Toggle Tempo / Ticks

EDIT / GLOBAL VIEW
   → Toggle VU Meters
```

and direct access to Bitwig's main layouts:

```text
AUX
   → Arrange

BUSSES
   → Mix

OUTPUTS
   → Edit
```

The central habit is:

```text
Context Changes
      ↓
Read Feedback
      ↓
Understand State
      ↓
Act
```

So perhaps the most important rule in this chapter is:

> **Do not merely operate the X-Touch. Read it.**

The surface is continually telling you what it represents.

Learning to notice that information is what makes the controller's increasingly complex contextual behaviour manageable.

---

## Coming Next

Feedback tells us what the controller is doing.

But DrivenByMoss can dramatically change what a control does when a modifier is held.

The same button, encoder or Jog Wheel may acquire an entirely different role through:

```text
SHIFT

OPTION

CONTROL

ALT
```

Next:

**Modifiers.**
