---
chapter: 8
title: V-Pots (Rotary Encoders)
revision: "1.0"
status: draft
---

The eight rotary encoders above the channel strips are among the most versatile controls on the X-Touch.

Behringer refers to them as **V-Pots**.

At first glance they look like ordinary rotary knobs. In reality, each V-Pot combines three useful features:

- a rotary encoder
- a push switch
- an LED ring

More importantly, their purpose changes according to the current mode.

A V-Pot might control pan in one moment, a send level in another, and a plug-in parameter a few seconds later.

This ability to adapt is what makes the V-Pots so powerful.

## Encoders Rather Than Pots

Despite the name **V-Pot**, these controls are not conventional potentiometers.

A traditional potentiometer has physical end stops. Turn it fully anticlockwise and eventually it can go no further. The physical position of the knob therefore represents the current value.

The X-Touch V-Pots work differently.

They are **endless rotary encoders**.

You can continue turning them in either direction indefinitely.

This matters because the same physical encoder can control many different parameters without its position becoming meaningless when you change from one parameter to another.

::: field-note

The word **V-Pot** is inherited from the Mackie Control terminology.

In practical terms, think of it as a **pushable endless rotary encoder surrounded by an LED display**.

:::

## Why Endless Encoders Matter

Imagine that an ordinary knob is controlling pan and is currently turned fully to the left.

You then switch modes and assign that same knob to a plug-in parameter whose current value is 80%.

What should happen?

With a conventional potentiometer there is an immediate disagreement between the physical position of the knob and the value in the software.

An endless encoder has no such problem.

The X-Touch simply changes the LED ring to show the new value.

The encoder is immediately ready to adjust it.

This is another example of the controller adapting itself to the current context.

## The LED Ring

Each V-Pot is surrounded by a ring of LEDs.

As we saw in the previous chapter, this is an important part of the X-Touch's feedback system.

The LEDs provide a visual indication of the value currently assigned to the encoder.

For a pan control, for example, the display can indicate whether the signal is positioned:

- left
- centre
- right

For other parameters the LEDs may instead represent a value progressing from minimum to maximum.

The important point is that the LED ring represents the **current software value**, not a permanent physical position of the encoder.

::: reality-check

When you change modes and the LED rings suddenly change, nothing has gone wrong.

The encoders are simply displaying the values of the parameters they now control.

:::

## Turning a V-Pot

Turning an encoder changes the currently assigned parameter.

Which parameter that happens to be depends upon context.

For example, the V-Pots may control:

- track pan
- send levels
- device parameters
- instrument parameters
- plug-in parameters
- browser navigation

You therefore cannot answer the question:

> **"What does this V-Pot control?"**

without first answering another question:

> **"What mode am I in?"**

This is exactly the mental model introduced earlier in the book.

The hardware remains the same.

Its meaning changes.

## Pressing a V-Pot

The V-Pots can also be pressed.

This is easy to overlook when first using the X-Touch because they look primarily like rotary controls.

The push action gives DrivenByMoss another command that can be associated with each encoder.

Its precise function depends upon the current context.

In one mode it may perform an action associated with the parameter being displayed; in another, it may be used for navigation or selection.

Do not assume that pressing an encoder always performs the same operation.

Instead, look at the current mode and the information displayed on the scribble strips.

::: field-note

The V-Pot's push action is one of the reasons it is useful to think of the encoder and the scribble strip beneath it as a pair.

The display tells you the context.

The V-Pot lets you interact with it.

:::

## V-Pots and Scribble Strips

The relationship between the V-Pots and the scribble strips is fundamental.

Each encoder sits directly above a display.

That physical arrangement is deliberate.

When a mode assigns parameters to the encoders, the corresponding scribble strips can tell you what those parameters are.

Conceptually, each channel becomes:

```text
        LED ring
           │
        V-Pot
           │
     Scribble Strip
           │
        Fader
```

The V-Pot provides the input.

The LED ring shows the value.

The scribble strip provides the context.

Together they form a small control surface within the larger controller.

## Pan Control

One of the simplest uses of the V-Pots is track panning.

When the controller is operating in the appropriate pan mode, each encoder controls the pan position of its corresponding channel.

Turn left and the signal moves towards the left.

Turn right and it moves towards the right.

The LED ring provides immediate visual feedback.

This is a good mode in which to become familiar with the physical feel of the encoders because the relationship between movement and result is easy to understand.

## Send Control

Switch to SEND mode and the same eight encoders take on a different role.

Instead of controlling pan, they can now adjust send levels.

The physical hardware has not changed.

Only the meaning assigned to it has changed.

This is precisely why endless encoders are so well suited to a controller such as the X-Touch.

The LED rings simply update to show the new values.

## Device and Plug-In Control

The real power of the V-Pots becomes apparent when controlling devices.

In Device or PLUG-IN mode, the encoders can be mapped to parameters belonging to the currently selected device.

Instead of:

```text
Pan   Pan   Pan   Pan   Pan   Pan   Pan   Pan
```

you might see parameters representing:

```text
Cutoff   Reso   Attack   Decay   Sustain   Release   Drive   Mix
```

The scribble strips identify the parameters.

The LED rings show their current values.

The V-Pots adjust them.

Suddenly the X-Touch becomes much more than a mixer.

It becomes a hands-on device editor.

## One Encoder, Many Jobs

This is worth emphasising.

The first V-Pot is not permanently:

> **Pan for Track 1**

Nor is it permanently:

> **Parameter 1**

It is simply the **first encoder in the current context**.

Change bank and it may control another track.

Change mode and it may control another type of parameter.

Select another device and it may acquire another purpose entirely.

Understanding this prevents one of the most common sources of confusion when learning a control surface.

## Turn, Look, Listen

When adjusting a V-Pot, you have several sources of information available at once.

You can:

- feel the encoder movement
- watch the LED ring
- read the scribble strip
- observe the corresponding change in Bitwig
- hear the result

That combination makes the V-Pots particularly effective for tasks such as sound design.

Instead of concentrating entirely on a graphical plug-in interface, you can begin to adjust parameters by ear.

::: field-note

Sometimes the best display in a music production system is no display at all.

Once you know which parameter a V-Pot controls, try listening to the result rather than watching the computer screen.

:::

## V-Pots and Focus

The previous chapters introduced two important questions:

> **"What mode am I in?"**

and:

> **"Which track is selected?"**

V-Pots add a third:

> **"What parameter is this encoder controlling?"**

Fortunately, you normally do not need to remember the answer.

The X-Touch tells you.

Read the scribble strip.

Look at the LED ring.

Then make the adjustment.

Once again:

> **Observe before you adjust.**

## The Bigger Picture

The V-Pots demonstrate almost everything that makes the X-Touch different from a simple MIDI controller.

They are:

- context-sensitive
- bidirectional
- multifunctional
- visually informative
- integrated with the current selection and mode

A single row of eight encoders can therefore control a remarkable amount of Bitwig.

The trick is not to memorise every possible assignment.

The trick is to understand the context.

Once you do that, the V-Pots become some of the most intuitive controls on the entire surface.

::: exercise

Open a Bitwig project containing several tracks and devices.

Begin with the V-Pots controlling pan.

Turn several encoders and observe both the LED rings and Bitwig.

Next, switch to SEND mode.

Notice how the LED rings immediately change to represent the send values.

Finally, select a track containing a device and enter the appropriate device or plug-in mode.

Read the parameter names shown on the scribble strips and adjust several of them using the V-Pots.

Throughout the exercise, keep asking three questions:

1. Which track is selected?
2. Which mode am I in?
3. What parameter does this V-Pot currently represent?

Do not try to memorise the assignments.

Instead, practise reading the controller until the answer becomes obvious from the feedback it provides.

:::
