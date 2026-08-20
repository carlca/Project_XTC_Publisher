---
chapter: 10
title: Motor Faders
revision: "1.0"
status: draft
---

The nine motorised faders are probably the first thing most people notice about the X-Touch.

Eight belong to the channel strips, while the ninth sits separately as the master fader.

Move a fader and Bitwig responds.

Change a value in Bitwig and the fader moves by itself.

Switch banks and all eight channel faders can spring into new positions almost simultaneously.

It is impressive to watch, but the motors are not there simply for show.

They solve one of the fundamental problems of using physical controls with software.

## The Problem with Ordinary Faders

Imagine a simple MIDI controller with eight conventional faders.

The first fader is controlling Track 1, whose volume is currently fairly high.

Now switch to another bank.

That same physical fader might now control Track 9, whose volume is much lower.

The hardware fader is still sitting near the top of its travel, while the software value it represents is somewhere near the bottom.

The two disagree.

Different controllers solve this problem in different ways, often using techniques such as value pickup or soft takeover.

The X-Touch takes a much more direct approach.

It simply moves the fader.

::: field-note

Motorisation means that the physical position of a fader can always reflect the value currently held by Bitwig.

The hardware adapts to the software rather than asking you to compensate for the difference.

:::

## Faders as Input and Output

It is tempting to think of a fader purely as an input device.

You move it.

Bitwig receives a new value.

But an X-Touch motor fader works in both directions.

```text
You move the fader
        │
        ▼
      Bitwig

      Bitwig
        │
        ▼
The fader moves
```

This makes the fader both a **control** and a **display**.

Its position is information.

::: diagram fader-feedback
caption: "Figure 9.1 — The motor fader is both an input control and a physical display of Bitwig's current value."
:::

## Eight Channel Faders

The eight main faders correspond to the eight channels in the current bank.

In a simple project this might mean:

```text
Fader       1      2      3      4      5      6      7      8
Track       1      2      3      4      5      6      7      8
```

Move to the next bank and those same physical faders might represent:

```text
Fader       1      2      3      4      5      6      7      8
Track       9     10     11     12     13     14     15     16
```

As soon as the bank changes, the motors reposition the faders to show the values belonging to the new tracks.

This is the physical manifestation of the banking system introduced in Chapter 4.

## Banking Makes Sense of the Motors

Without motorisation, changing banks would create an immediate mismatch between the physical faders and the newly displayed tracks.

With motorised faders, the transition is obvious.

Press a bank control and three things happen together:

- the visible tracks change
- the scribble strips update
- the faders move to their new positions

The X-Touch has physically reconfigured itself for the new bank.

::: reality-check

If several faders suddenly move when you change banks, nothing unexpected has happened.

They are simply taking up the positions belonging to the newly displayed tracks.

:::

## Touch-Sensitive Faders

The X-Touch faders are not merely motorised.

They are also **touch-sensitive**.

The controller can detect when your finger is resting on a fader.

This is particularly important when working with automation.

There is a significant difference between:

> **"The fader is at this position."**

and:

> **"The user is currently touching the fader."**

Knowing when you have physically taken control allows Bitwig and the controller to behave appropriately during automation operations.

We will encounter this distinction again when we look at automation in more detail.

## Do Not Fight the Motors

When a motor fader moves by itself, let it move.

Do not hold it in position or deliberately push against the motor.

The movement is feedback from Bitwig.

The fader is trying to show you the value that currently exists in the project.

If you want to change that value, wait for the fader to settle and then move it normally.

::: field-note

A moving fader is not the X-Touch doing something *to* your mix.

It is the X-Touch showing you something that has already happened in Bitwig.

That distinction is important.

:::

## Automation Comes Alive

Motor faders become particularly valuable when automation is playing.

A track's volume may change continuously during a song.

On a conventional controller, the physical fader would remain stationary while the software value moved.

On the X-Touch, the motor fader can follow those changes.

You can therefore **see the automation physically happening**.

A vocal may rise slightly during a chorus.

A pad may fade away.

An effects return may increase during a transition.

The corresponding faders can move as those changes occur.

This is one of the moments when the distinction between software and hardware begins to disappear.

## Writing Automation

Touch sensitivity and motorisation become especially useful when writing automation.

You can grab a fader and perform a level change naturally with your hand rather than drawing an automation curve with a mouse.

Bitwig records the movement.

When the automation is played back, the fader can reproduce it.

The physical gesture has become part of the project.

For many users this feels much closer to working on a traditional mixing console.

## The Master Fader

To the right of the eight channel faders is a ninth motorised fader.

This is the **master fader**.

Unlike the channel faders, it is not part of the eight-channel banking system.

Its role is associated with the master output rather than whichever eight tracks happen to be visible.

This separation is useful because the master remains available while you move through the project's channel banks.

## Faders and SELECT

Remember the distinction introduced in Chapter 6.

A fader represents a track within the current bank.

The SELECT button identifies the track that currently has your attention.

Moving a fader does not mean that you have changed the controller's focus.

Likewise, selecting a track does not mean that its fader must move.

These are different concepts:

```text
Fader position  →  Track level

SELECT          →  Current focus
```

Keeping those two ideas separate prevents a surprising amount of confusion.

## Faders as Feedback

Chapter 7 described the various ways in which the X-Touch communicates with you.

Motor faders are perhaps its most physical form of feedback.

You do not have to read a number to know roughly where a track's level is.

You can simply look at the fader.

In fact, you can often see the overall shape of a mix by looking across all eight faders at once.

That is something a row of numerical values on a computer screen does not communicate nearly as naturally.

## Mixing with Your Hands

This is where the X-Touch begins to change the experience of using a DAW.

With a mouse, adjusting several track levels usually means moving one virtual fader at a time.

With the X-Touch you have eight physical faders beneath your fingers.

You can bring one track down while raising another.

You can balance several channels together.

You can make small changes without repeatedly pointing at different objects on the screen.

Mixing becomes a physical activity again.

::: field-note

The advantage of physical faders is not simply that they replace virtual ones.

The real advantage is that you can control **several things at once**.

That is something a mouse is fundamentally bad at doing.

:::

## Trust the Position

A useful habit is to trust what the faders are showing you.

When you change banks, allow them to settle.

When automation is playing, watch them move.

When you open an existing project, notice how the X-Touch reconstructs the mix physically in front of you.

The faders are not approximations of the software state.

They are part of the feedback system that keeps the controller and Bitwig synchronised.

## The Bigger Picture

The motor faders demonstrate the same principle we encountered with the V-Pots.

The X-Touch does not expect its physical controls to have one permanent meaning.

Instead, the hardware adapts itself to the current context.

The V-Pots achieve this by having no fixed physical position and using LED rings to display their values.

The faders achieve it differently.

They physically move.

Two different engineering solutions serve the same underlying idea:

> **The controller should reflect the current state of the software.**

That principle lies at the heart of the X-Touch.

::: exercise

Open a Bitwig project containing more than eight tracks.

First, look at the positions of the eight channel faders.

Change to the next bank and watch what happens.

Notice how the scribble strips and faders update together.

Move several faders and confirm that the corresponding Bitwig levels follow them.

Now change those same levels using Bitwig's mixer and watch the X-Touch faders respond.

If the project contains volume automation, play a section containing that automation and observe the appropriate fader.

Finally, return to the first bank.

The faders should return to the positions belonging to those tracks.

The aim of this exercise is not simply to practise moving faders.

It is to experience the central idea of this chapter:

**The motor faders are both controls and physical displays.**

:::
