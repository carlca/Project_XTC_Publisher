---
chapter: 11
title: Transport Controls
revision: "1.0"
status: draft
---

After learning about modes, selection, V-Pots and motor faders, the Transport section of the X-Touch may come as something of a relief.

Most of it does exactly what you expect.

The familiar **REWIND**, **FAST FORWARD**, **STOP**, **PLAY** and **RECORD** buttons provide immediate control over Bitwig's transport.

But the Transport section is more than a convenient replacement for clicking Play on the computer screen.

Combined with the jog wheel and navigation controls, it allows you to move around a project, locate a position and control playback without repeatedly reaching for the mouse.

## The Five Transport Buttons

At the bottom-right of the X-Touch are five large transport buttons:

- REWIND
- FAST FORWARD
- STOP
- PLAY
- RECORD

Their layout deliberately resembles the transport controls found on tape machines, hardware recorders and traditional mixing systems.

If you have used almost any audio equipment before, they should feel immediately familiar.

## PLAY

Press **PLAY** to start playback from the current position.

Pressing PLAY is one of the simplest examples of the two-way relationship between the X-Touch and Bitwig.

The controller sends the command.

Bitwig begins playback.

The X-Touch then reflects the resulting transport state through its illuminated controls and displays.

Even here, the controller is both issuing a command and providing feedback.

## STOP

Press **STOP** to stop playback.

Simple as this sounds, having a large physical STOP button becomes surprisingly valuable.

There is no need to locate a small transport control on the computer screen.

Your hand quickly learns where STOP is, and after a while you may find yourself using it without looking at the controller at all.

::: field-note

Transport controls are particularly good candidates for developing muscle memory.

Unlike context-sensitive controls, their basic purpose remains predictable.

Once your hand knows where PLAY and STOP are, controlling playback becomes almost unconscious.

:::

## RECORD

The **RECORD** button controls Bitwig's recording transport.

Recording involves more than simply pressing one button — tracks must be armed correctly and Bitwig must be ready to record — but once those conditions are satisfied, RECORD gives you direct physical control over the process.

This becomes especially useful when recording instruments or automation.

Instead of preparing everything and then reaching for the mouse, you can remain focused on the performance.

::: reality-check

Pressing RECORD does not automatically make every track record.

Track arming and the transport's recording state are separate concepts.

Always check that the intended track is correctly armed before beginning a take.

:::

## REWIND and FAST FORWARD

The **REWIND** and **FAST FORWARD** buttons allow you to move backwards and forwards through the project.

Their exact behaviour is governed by the integration between the X-Touch, DrivenByMoss and Bitwig, but their purpose is straightforward:

> **Move the current playback position.**

For coarse navigation they provide a quick way of moving through the project without touching the mouse.

For more deliberate positioning, however, another control becomes particularly useful.

## The Jog Wheel

The large wheel above the transport buttons is the **jog wheel**.

It provides a physical way of moving through the project timeline.

Turn it one way to move backwards.

Turn it the other way to move forwards.

Unlike clicking somewhere on a graphical timeline, the jog wheel encourages you to think in terms of movement from the current position.

This can feel much more natural when searching for the beginning of a phrase, a transition or a particular point in a recording.

## Coarse and Fine Navigation

The transport buttons and jog wheel complement each other.

Think of them broadly as two approaches to navigation:

```text
REWIND / FAST FORWARD
          │
          ▼
     Move quickly

       Jog Wheel
          │
          ▼
   Position precisely
```

You do not need to choose one method exclusively.

A typical workflow might involve moving rapidly towards the required part of the project and then using the jog wheel to refine the position.

::: field-note

The most useful navigation method is usually the one that requires the least thought.

Use the transport buttons when you want to move.

Use the jog wheel when you want to arrive somewhere specific.

:::

## The Time Display

Navigation becomes much more useful when you can see where you are.

The X-Touch's main display provides positional information that helps you keep track of the current location within the project.

As you move through the timeline, the display updates accordingly.

Once again, input and feedback work together:

```text
Turn jog wheel
      │
      ▼
Bitwig position changes
      │
      ▼
Display updates
```

You move.

The controller tells you where you have arrived.

## Transport and the Computer Screen

It is worth noticing how many routine mouse movements disappear once the transport controls become familiar.

Without a control surface, a typical editing or recording session may involve repeatedly moving the pointer between:

- the arrangement
- the mixer
- device controls
- the transport
- the timeline

With the X-Touch, many transport operations remain permanently beneath your hand.

You can keep the computer screen focused on the information that actually needs a graphical display.

## Transport While Mixing

Physical transport controls are especially useful while mixing.

Imagine adjusting several faders during playback.

You hear something you want to investigate.

Instead of moving your hand away from the controller and locating Bitwig's transport:

1. Press STOP.
2. Navigate backwards.
3. Press PLAY.
4. Listen again.
5. Continue adjusting the mix.

Your attention remains on the sound and the controller rather than shifting repeatedly between hardware and screen.

This may seem like a small improvement.

Repeated hundreds of times during a session, it becomes a substantial one.

## Transport While Recording

The same principle applies when recording.

A typical sequence might be:

1. Select the required track.
2. Arm it for recording.
3. Navigate to the starting position.
4. Press RECORD.
5. Perform the part.
6. Press STOP.
7. Return to the beginning of the take.
8. Press PLAY to review it.

The computer is still doing all the recording.

The X-Touch simply allows the routine operations surrounding that recording to happen physically.

That keeps your attention where it belongs: on the performance.

## Visual Feedback

The transport section also reinforces the principle introduced in Chapter 7:

> **Observe before you adjust.**

Illuminated transport buttons tell you about the current state.

The position display tells you where you are.

Bitwig's own interface provides further confirmation.

Do not treat the physical controls and the software interface as two independent systems.

They are two views of the same transport state.

## Developing Muscle Memory

Transport is one of the best places to begin operating the X-Touch without constantly looking at it.

The five transport buttons are large, consistently positioned and easy to distinguish by location.

With practice, your hand begins to find them automatically.

The jog wheel is equally unmistakable.

This is an important step towards a more tactile workflow.

You stop thinking:

> **"Where is the Play button?"**

and simply press it.

That small change is one of the reasons a control surface can make a DAW feel more like an instrument and less like a computer application.

## A Step Towards Mouse-Lite

The Transport section gives us an early glimpse of the workflow we shall explore more fully in Chapter 13.

The aim is not necessarily to eliminate the mouse.

There are many tasks for which a mouse remains an excellent tool.

The aim is to stop reaching for it when a physical control is faster, clearer or more natural.

Starting playback is a perfect example.

You *could* move the pointer to Bitwig's PLAY button and click it.

But when a large physical PLAY button is already beneath your hand, why would you?

::: field-note

A Mouse-Lite workflow is not about refusing to use the mouse.

It is about using the most appropriate tool for each job.

For transport operations, that tool is very often the X-Touch.

:::

## The Bigger Picture

The Transport section may be one of the least mysterious parts of the X-Touch, but it plays an important role in the overall workflow.

The faders allow you to mix.

The V-Pots allow you to adjust parameters.

SELECT establishes focus.

The displays tell you what is happening.

And the Transport section lets you control **when** it happens.

Together, these controls begin to form a complete working environment.

You are no longer simply controlling individual Bitwig parameters.

You are operating the session.

::: exercise

Open an existing Bitwig project.

For the duration of this exercise, avoid using the mouse for transport operations.

Using only the X-Touch:

1. Start playback.
2. Stop playback.
3. Move backwards through the project.
4. Move forwards through the project.
5. Use the jog wheel to locate a particular section.
6. Start playback from that position.
7. Stop again.

Now choose a short section of the project and practise repeatedly navigating to it and playing it.

Do not concentrate on speed.

Instead, concentrate on allowing your hand to learn where the transport controls are.

The goal is to reach the point where PLAY, STOP and basic navigation no longer require conscious thought.

That is one more step towards a **Mouse-Free — or Mouse-Lite — workflow**.

:::
