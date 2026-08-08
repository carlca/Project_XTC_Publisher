---
chapter: 11
title: Device Mode
revision: "1.0"
status: draft
---

So far, much of our attention has been focused on the mixer.

We have selected tracks, changed banks, adjusted levels, controlled pan and navigated through the project.

But a Bitwig track is much more than a channel in a mixer.

It may contain instruments, audio effects and other devices, each with parameters of its own.

**Device Mode** is where the X-Touch begins to reach inside the selected track and give you physical control over those devices.

## From Mixer to Device

In normal mixer operation, the eight channel strips represent tracks.

Conceptually, the controller looks something like this:

```text
X-Touch

   │
   ▼

Tracks

   │
   ├── Drums
   ├── Bass
   ├── Synth
   ├── Guitar
   └── Vocals
```

Device Mode takes us one level deeper.

A selected track might contain:

```text
Synth Track

   │
   ├── Instrument
   ├── EQ
   ├── Compressor
   └── Delay
```

Once a device is selected, we can go deeper again:

```text
Selected Device

   │
   ├── Parameter 1
   ├── Parameter 2
   ├── Parameter 3
   └── ...
```

This hierarchy is one of the most useful ways to understand Device Mode.

::: diagram device-hierarchy
caption: "Figure 11.1 — Device Mode moves the controller's focus from the selected track, through its devices, to the parameters of the selected device."
:::

## SELECT Comes First

Chapter 6 introduced the idea of **focus**.

Device Mode is where that idea becomes particularly important.

Before controlling a device, the X-Touch needs to know which track contains it.

The first step is therefore familiar:

> **Select the track.**

Once the track is selected, Device Mode can operate on the devices belonging to that track.

This gives us a simple hierarchy:

```text
SELECT
   │
   ▼
Track
   │
   ▼
Device
   │
   ▼
Parameters
```

If Device Mode appears to be showing the wrong instrument or effect, work backwards through that hierarchy.

Start by checking the selected track.

::: reality-check

When the X-Touch appears to be controlling the "wrong" device, do not immediately start pressing mode buttons.

First check which track is selected.

The controller may be doing exactly what it should — just on a different track.

:::

## A Track Can Contain Many Devices

A Bitwig track can contain an entire chain of devices.

For example:

```text
Polysynth → EQ+ → Compressor → Delay+
```

Each device has a different purpose and therefore exposes different parameters.

Selecting the Polysynth might give you controls relating to synthesis.

Selecting the EQ might give you frequency and gain controls.

Selecting the delay might expose delay time, feedback and mix.

The same eight V-Pots can control all of them.

The hardware remains unchanged.

The **context** changes.

## The Scribble Strips Become Essential

This is where the scribble strips really earn their keep.

In mixer operation, an encoder's purpose may be fairly predictable.

In Device Mode, it could represent almost anything.

One encoder might control:

- filter cutoff
- resonance
- attack
- release
- frequency
- gain
- feedback
- wet/dry mix

Trying to memorise those assignments would be hopeless.

Fortunately, you do not need to.

The scribble strips tell you what the controls currently represent.

This is precisely the behaviour we explored in Chapter 7.

> **Observe before you adjust.**

In Device Mode, that principle becomes essential.

## The V-Pots Become Parameter Controls

Chapter 8 introduced the V-Pots as context-sensitive rotary encoders.

Device Mode demonstrates why that design is so useful.

Suppose the currently selected device exposes eight parameters:

```text
Cutoff   Reso   Attack   Decay   Sustain   Release   Drive   Mix
```

The eight V-Pots can immediately become physical controls for those parameters.

Turn an encoder and the corresponding value changes in Bitwig.

The LED ring provides visual feedback.

The scribble strip tells you what the parameter is.

Suddenly, a software device begins to feel rather more like a piece of hardware.

## More Than Eight Parameters

Of course, most devices have considerably more than eight parameters.

The X-Touch only has eight V-Pots.

This creates a familiar problem.

Fortunately, we have already encountered the solution.

**Banking.**

Just as eight channel strips can provide access to many tracks, eight encoders can provide access to many parameters.

Think of the device parameters as pages:

```text
Page 1

P1   P2   P3   P4   P5   P6   P7   P8


Page 2

P9   P10  P11  P12  P13  P14  P15  P16


Page 3

P17  P18  P19  P20  P21  P22  P23  P24
```

Move to another parameter page and the V-Pots acquire new assignments.

The scribble strips update.

The LED rings update.

Once again, the controller reconfigures itself around the current context.

::: field-note

Parameter pages are really just another form of banking.

You already understand the underlying idea from Chapter 4.

Eight physical controls provide a window onto a much larger collection of software controls.

:::

## Devices, Parameters and Pages

It is useful to keep three separate concepts in mind:

```text
Device
   │
   ▼
Parameter Page
   │
   ▼
Eight Parameters
```

First you choose **what device** you want to control.

Then you choose **which page** of its parameters you want to see.

The eight V-Pots then control the parameters on that page.

This structure may sound complicated when described in words.

In use, it quickly becomes natural because the X-Touch continually updates its displays as you navigate.

## Follow the Feedback

Imagine moving from a synthesizer to a delay.

The controller may immediately change:

- parameter names on the scribble strips
- LED ring positions
- encoder functions

Nothing has physically moved except perhaps your hand.

Yet the entire row of V-Pots now represents a different piece of software.

This is exactly why Chapter 7 placed so much emphasis on feedback.

In Device Mode, the displays are not merely helpful.

They are part of the interface.

## Editing by Ear

One of the most enjoyable aspects of Device Mode is that it can change how you interact with plug-ins and instruments.

Consider adjusting a filter cutoff with a mouse.

Your attention naturally goes to the computer screen.

You locate the graphical control.

You watch the pointer.

You watch the value change.

With the X-Touch, you can instead:

1. Read the scribble strip.
2. Place your hand on the appropriate V-Pot.
3. Turn it.
4. Listen.

Once you know which control you are adjusting, there may be very little reason to keep watching the screen.

::: field-note

Device Mode is not necessarily about reproducing every control from a plug-in interface on the X-Touch.

Its real value is providing immediate physical access to the parameters you actually want to adjust.

:::

## Hardware Feel from Software Instruments

This becomes particularly interesting with software instruments.

A synthesizer may exist entirely inside the computer, but Device Mode gives some of its controls a physical presence.

Instead of dragging a virtual filter knob, you turn an encoder.

Instead of watching an envelope value, you adjust it while listening.

The software has not changed.

What has changed is your relationship with it.

This is one of the ways in which a control surface can make working with a DAW feel less like operating software and more like playing an instrument.

## Device Chains

As projects become more complex, tracks often contain several devices.

For example:

```text
Instrument
    │
    ▼
EQ
    │
    ▼
Compressor
    │
    ▼
Saturation
    │
    ▼
Delay
```

Device Mode allows you to move through that chain and concentrate on one device at a time.

The important thing is not to memorise where every device lives.

Instead, maintain the mental hierarchy:

> **Track → Device → Parameter Page → Parameter**

Whenever you become lost, move back up that hierarchy.

Which track?

Which device?

Which page?

Which parameter?

The displays provide the answers.

## Device Mode and Focus

We can now expand the idea introduced in Chapter 6.

SELECT establishes the track focus.

Device Mode establishes the device focus.

Parameter navigation establishes the parameter focus.

Conceptually:

```text
Project
   │
   ▼
Selected Track
   │
   ▼
Selected Device
   │
   ▼
Parameter Page
   │
   ▼
Parameter
```

This is not just a description of Device Mode.

It is a useful mental model for navigating Bitwig itself.

## Returning to the Mixer

Device Mode is temporary.

Entering it does not alter the structure of your project or permanently reassign the X-Touch.

When you have finished editing the device, you can return to normal mixer operation.

The V-Pots resume their mixer-related roles.

The scribble strips return to displaying the appropriate mixer information.

The controller has not changed identity.

It has simply changed context again.

## Device Mode and the Mouse

Device Mode also represents another significant step towards our Mouse-Free — or Mouse-Lite — workflow.

Without a control surface, editing a device often involves:

- locating the device on screen
- locating the required parameter
- moving the pointer to it
- dragging the control
- moving to the next parameter
- repeating the process

With the X-Touch, once the correct device and parameter page are selected, eight physical controls are immediately available.

That does not mean the graphical interface becomes useless.

Some devices contain complex visual information that is much easier to understand on screen.

The point is not to eliminate the screen or the mouse.

The point is to stop depending upon them when a physical control provides a better way to work.

::: field-note

Mouse-Lite does not mean "never touch the mouse".

It means:

**Use the mouse when it is the best tool — not simply because it is the only tool you know.**

:::

## The Bigger Picture

Device Mode brings together almost every concept we have encountered so far.

**Banks and Channels** taught us how a limited number of physical controls can represent a larger system.

**Modes** taught us that controls change meaning according to context.

**SELECT** taught us about focus.

**Displays and Feedback** taught us to read the controller.

**V-Pots** gave us context-sensitive parameter controls.

Device Mode combines all of those ideas.

That is why it can initially appear complicated.

It is also why, once the earlier concepts are understood, it becomes surprisingly logical.

You do not need to memorise the entire X-Touch.

You simply need to know where you are.

::: exercise

Open a Bitwig project containing a track with several devices.

Select that track using the X-Touch.

Enter Device Mode and observe the scribble strips before touching any controls.

Identify the currently selected device.

Now:

1. Locate a parameter shown on one of the scribble strips.
2. Adjust it with the corresponding V-Pot.
3. Watch the LED ring respond.
4. Listen to the result.
5. Move to another parameter page if one is available.
6. Observe how all eight encoder assignments change.
7. Select another device in the chain.
8. Observe how the scribble strips and LED rings change again.

Finally, select a completely different track.

Notice how the available devices change with it.

Throughout the exercise, keep the hierarchy in mind:

**Track → Device → Parameter Page → Parameter**

If you become lost, do not start pressing buttons at random.

Work backwards through the hierarchy and read the feedback the X-Touch is already providing.

:::
