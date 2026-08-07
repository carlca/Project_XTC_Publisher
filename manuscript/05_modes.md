---
chapter: 5
title: Modes
revision: "1.1"
status: draft
---

The X-Touch is often described as having "lots of buttons". That is true, but it is only half the story.

The more important fact is that many of those buttons do **different jobs at different times**.

Understanding modes is the key to understanding the X-Touch.

Once this idea becomes familiar, the controller feels logical rather than mysterious.

## What Is a Mode?

A **mode** changes the meaning of one or more controls.

The physical hardware never changes.

Instead, the X-Touch changes how it interprets your button presses, encoder turns and fader movements.

Think of the controller as speaking several different "languages".

Each mode uses the same hardware to perform a different set of tasks.

::: field-note

A common mistake is to think that every button has exactly one purpose.

On the X-Touch, many controls are intentionally multifunctional.

:::

Figure 5.1 illustrates this idea. Although the hardware remains exactly the same, selecting a different mode changes the *role* of the controls rather than the controls themselves.

::: diagram mode-overview
caption: "Figure 5.1 — The X-Touch uses the same physical controls in many different operating modes."
:::

## The Current Mode Is Always Visible

Fortunately, the X-Touch rarely leaves you guessing.

The scribble strips, LEDs and button illumination usually indicate the current operating mode.

Before pressing a control, take a quick look at the feedback the controller is already providing.

Experienced users develop this habit very quickly.

## The Primary Modes

DrivenByMoss makes extensive use of the X-Touch's mode system.

The most frequently used modes include:

- TRACK
- SEND
- PAN/SURROUND
- PLUG-IN
- EQ
- INSTRUMENT
- USER

Each mode changes what the rotary encoders control and, in some cases, what appears on the scribble strips.

The important point is that these are **not different layouts of the controller**. They are simply different interpretations of the same hardware.

Throughout the remainder of this book we shall examine each of these modes in detail.

## TRACK Mode

TRACK mode is the mode most users spend the majority of their time in.

The controller focuses on the Bitwig tracks themselves.

Typical operations include:

- selecting tracks
- adjusting volume
- muting
- soloing
- recording
- automation

Think of TRACK mode as the controller's "home".

Whenever you become unsure where you are, returning to TRACK mode is often a sensible starting point.

## SEND Mode

SEND mode changes the rotary encoders so that they adjust send levels instead of pan.

Instead of controlling the stereo position of each track, the encoders now control how much of the signal is sent to an effects bus such as a reverb or delay.

Exactly which send is being adjusted depends upon the current Bitwig project and the selected send.

::: reality-check

If turning an encoder suddenly changes a reverb or delay send instead of the pan position, the controller is almost certainly in SEND mode.

:::

## PAN/SURROUND Mode

PAN/SURROUND mode returns the rotary encoders to controlling the stereo (or surround) position of each track.

For most stereo projects this simply means moving sounds left or right within the mix.

## PLUG-IN Mode

PLUG-IN mode is one of the X-Touch's most powerful capabilities.

Rather than controlling the mixer, the encoders are assigned to parameters exposed by the currently selected Bitwig device.

The scribble strips display parameter names, allowing the hardware to become a tactile extension of the software interface.

Later chapters explore this workflow in depth.

## INSTRUMENT Mode

INSTRUMENT mode provides direct access to software instrument parameters.

Depending upon the selected Bitwig device, the encoders may control filter cutoff, resonance, envelopes, oscillator settings or many other synthesis controls.

The exact assignments depend entirely upon the instrument currently in focus.

## USER Mode

USER mode deserves special attention.

Unlike the other operating modes, USER mode is not tied to a particular mixer function.

DrivenByMoss uses USER mode to expose additional Bitwig features.

For example, pressing **USER** immediately opens Bitwig's Browser. The scribble strips are repurposed to display browser information, allowing sounds and presets to be selected directly from the X-Touch.

::: field-note

Because USER mode is completely software-defined, it is capable of doing far more than its name might suggest.

Many users overlook it at first, yet it quickly becomes one of the most frequently used buttons on the controller.

:::

## Modes Are Temporary

Changing mode does not permanently alter the controller.

It simply changes what the controls do **at that moment**.

You are free to move between modes whenever your workflow requires.

The motor faders, scribble strips and LEDs update automatically to reflect the current context.

## Thinking in Modes

One of the biggest steps towards mastering the X-Touch is learning to ask a simple question:

> **"What mode am I in?"**

Many apparent "problems" disappear the moment you realise that the controller is behaving exactly as expected—it is simply operating in a different mode.

Once this becomes second nature, the X-Touch feels far less complicated than it first appears.

::: exercise

Open any Bitwig project.

Press each of the available mode buttons in turn and observe how the scribble strips, encoder assignments and button illumination change.

Do not try to memorise every function immediately.

Instead, become comfortable with the idea that the X-Touch continually adapts its controls to the task at hand.

Recognising the current mode is far more valuable than memorising individual button assignments.

:::
