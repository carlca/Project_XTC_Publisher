---
chapter: 12
title: Browser Mode
revision: "1.0"
status: draft
---

Up to this point, most of our work with the X-Touch has involved controlling things that already exist in the project.

We have selected tracks.

We have adjusted levels.

We have navigated devices and changed their parameters.

But sooner or later we need something new.

Perhaps we want to add an instrument.

Perhaps we need an audio effect.

Perhaps we want to replace a preset or search for a particular sound.

This is where **Browser Mode** becomes particularly interesting.

Instead of reaching immediately for the mouse, we can begin exploring Bitwig's Browser directly from the X-Touch.

## From Control to Creation

Device Mode allows us to move down through a hierarchy:

```text
Track
   │
   ▼
Device
   │
   ▼
Parameter Page
   │
   ▼
Parameter
```

Browser Mode performs a different job.

It allows us to choose something that is not yet part of that hierarchy.

Conceptually:

```text
Selected Track
      │
      ▼
    Browser
      │
      ▼
Search / Navigate
      │
      ▼
Choose an Item
      │
      ▼
Add to Project
```

This is an important change.

The X-Touch is no longer merely editing the project.

It is helping us build it.

::: diagram browser-workflow
caption: "Figure 12.1 — Browser Mode extends the workflow from selecting a destination to finding and adding new material."
:::

## SELECT Still Comes First

Once again, the SELECT button plays a central role.

Before opening the Browser, ask:

> **"Where do I want the new item to go?"**

The selected track establishes the context in which browsing takes place.

This is the same idea introduced in Chapter 6.

Selection is not simply about highlighting something.

It establishes **focus**.

A useful working sequence is therefore:

```text
SELECT
   │
   ▼
Destination
   │
   ▼
Open Browser
   │
   ▼
Choose
```

That first step prevents a surprising amount of confusion.

::: reality-check

Before browsing for a new device or sound, check the selected track.

Finding exactly what you wanted and then discovering that you were working in the wrong place is considerably less entertaining than it sounds.

:::

## Opening the Browser

With DrivenByMoss, the X-Touch provides access to Bitwig's Browser without requiring you to begin the operation with the mouse.

When Browser Mode is entered, the role of the controller changes.

Controls that previously represented mixer or device parameters can now become navigation and selection controls.

The scribble strips change accordingly.

This should already feel familiar.

The hardware has not changed.

The **context** has.

## Read the Scribble Strips

Browser Mode is another excellent demonstration of why the scribble strips matter.

When browsing, they may present information relating to the available choices rather than track or device parameters.

The labels on the controller therefore become your guide.

Do not assume that an encoder still performs the function it had a few seconds earlier.

Read first.

Then turn or press.

The principle remains:

> **Observe before you adjust.**

Although in Browser Mode we might reasonably amend that to:

> **Observe before you choose.**

## Navigation Rather Than Parameter Control

In Device Mode, turning a V-Pot normally changes a value.

Browser Mode can give those same controls a different purpose.

Now an encoder may be involved in navigating choices rather than adjusting a continuous parameter.

This distinction is important.

In one context:

```text
Turn V-Pot
     │
     ▼
Change Parameter
```

In another:

```text
Turn V-Pot
     │
     ▼
Navigate Choices
```

The physical action is identical.

Its meaning is determined by the current mode.

This is precisely the mental model we established much earlier in the book.

## Narrowing the Search

Bitwig's Browser can contain a huge amount of material.

Depending upon your installation, that may include:

- instruments
- audio effects
- note effects
- presets
- samples
- plug-ins
- other device content

Browsing everything at once would quickly become unwieldy.

The useful approach is to narrow the available choices until the required item becomes easy to locate.

Think of browsing as a funnel:

```text
Everything
    │
    ▼
Category
    │
    ▼
Filtered Results
    │
    ▼
Selection
```

Each decision reduces the number of possibilities.

This is much more effective than treating the Browser as one enormous list.

## Browsing Is Contextual

The contents of the Browser depend upon what you are doing.

If you are adding an instrument, the useful choices are different from those involved in adding an audio effect.

If you are choosing a preset, the available material depends upon the device.

If you are looking for a sample, you are dealing with another type of content again.

This means Browser Mode should not be thought of as:

> **"A list of everything Bitwig contains."**

It is better understood as:

> **"A way of choosing something appropriate for the current context."**

That makes the Browser much less intimidating.

## Choosing an Item

Eventually, browsing leads to a choice.

Once the required item has been located, it can be selected and inserted or loaded in the appropriate context.

At this point the Browser has done its job.

The new item becomes part of the project.

Conceptually:

```text
Browser
   │
   ▼
Choose
   │
   ▼
Insert
   │
   ▼
New Device
```

And something rather satisfying can happen next.

The workflow can move naturally back into Device Mode.

## Browser Mode Meets Device Mode

Suppose you want to add a delay to a track.

The workflow might be:

1. SELECT the destination track.
2. Open the Browser.
3. Navigate to an appropriate delay.
4. Choose it.
5. Return to Device Mode.
6. Adjust its parameters with the V-Pots.

Notice what has happened.

You have gone from:

> **"I want a delay."**

to:

> **"I am adjusting the delay."**

without the mouse necessarily being the centre of the operation.

This is where the individual chapters of the book begin joining together into complete workflows.

::: field-note

Browser Mode becomes much more powerful when you stop thinking of it as an isolated feature.

It is the bridge between deciding that you need something and then controlling what you have added.

:::

## Browsing for Instruments

The same principle applies when building an instrument track.

Imagine starting with an appropriate empty track.

You can:

1. Select the track.
2. Enter the Browser.
3. Locate an instrument.
4. Choose it.
5. Enter Device Mode.
6. Begin adjusting its parameters.

The Browser finds the instrument.

Device Mode controls it.

SELECT establishes where the whole operation takes place.

Three apparently separate features become a single workflow.

## Browsing for Presets

Browser Mode is equally useful when searching for sounds rather than devices.

Suppose you already have a synthesizer loaded but want another preset.

Instead of thinking:

> **"I need to operate the Browser."**

think:

> **"I want another sound for this device."**

The Browser is simply the mechanism that helps you find it.

This distinction matters because it keeps your attention on the musical task rather than the software operation.

## Browsing with Your Ears

Browsing sounds presents an interesting opportunity.

Computer-based browsing naturally encourages us to look.

We read names.

We study categories.

We watch lists move up and down the screen.

But ultimately, when choosing a sound, the important question is usually:

> **"Does this sound right?"**

The more navigation you can perform from the controller, the easier it becomes to keep your attention on listening rather than pointing and clicking.

::: field-note

Names and categories help you find sounds.

Your ears decide whether they belong in the music.

:::

## The Screen Still Matters

A Mouse-Lite workflow does not mean pretending the computer display has suddenly become useless.

Bitwig's Browser can present detailed information that simply cannot fit onto the X-Touch's scribble strips.

There will be occasions when looking at the screen is clearly the most efficient way to understand what is available.

That is perfectly fine.

The aim is not:

> **"Never look at Bitwig."**

The aim is:

> **"Do not reach for the mouse automatically."**

If the X-Touch can perform the operation comfortably, use it.

If the graphical Browser is better suited to the task, use that.

The two approaches complement each other.

## Do Not Memorise the Browser

As with Device Mode, there is little value in trying to memorise every possible Browser state.

The available choices will change.

Your installed devices may change.

Your plug-ins may change.

Your presets and samples may change.

The useful skill is not remembering where everything lives.

It is understanding how to navigate what is currently in front of you.

Read the feedback.

Make a choice.

Observe the result.

Continue.

## When You Become Lost

Browser Mode can initially feel more complicated than the mixer because the controls are being used in a less familiar way.

If you become unsure what is happening, return to the questions we have used throughout the book:

- Which track is selected?
- Which mode am I in?
- What are the scribble strips showing?
- What does the current control represent?

Do not press controls randomly in an attempt to escape.

Read the controller first.

The information you need is often already there.

::: reality-check

When a control appears to have stopped doing its usual job, check whether you are still in Browser Mode.

A V-Pot that normally adjusts pan cannot adjust pan while it is busy helping you navigate the Browser.

:::

## Building a Workflow

We can now combine much of what we have learned into a single sequence.

Imagine adding and adjusting a new effect:

```text
SELECT Track
      │
      ▼
Open Browser
      │
      ▼
Find Effect
      │
      ▼
Choose Effect
      │
      ▼
Device Mode
      │
      ▼
Choose Parameter Page
      │
      ▼
Adjust with V-Pots
      │
      ▼
Listen
```

This is more than a collection of X-Touch features.

It is a **workflow**.

That distinction is important.

The purpose of learning the controller is not to become good at pressing its buttons.

The purpose is to make the controller disappear into the process of making music.

## Another Step Towards Mouse-Lite

Browser Mode brings us very close to the subject of the final chapter.

Earlier we used the X-Touch to manipulate a project.

Now we can also begin adding things to it.

That removes another common reason for immediately reaching for the mouse.

Again, the goal is not mouse avoidance for its own sake.

A mouse remains extremely useful for detailed editing, graphical operations and many other tasks.

But opening a Browser, finding something, selecting it and then adjusting it are operations that can increasingly take place from the control surface.

The mouse becomes an option rather than a reflex.

## The Bigger Picture

Browser Mode completes an important chain of ideas.

**SELECT** establishes where we are working.

**Browser Mode** helps us find something to add.

**Device Mode** lets us control what we have added.

**V-Pots** provide the physical controls.

**Displays and Feedback** tell us what those controls currently mean.

**Motor Faders and Transport** allow the rest of the session to continue around us.

The individual features of the X-Touch are beginning to disappear.

In their place we are developing workflows.

And that brings us naturally to the final chapter.

::: exercise

Open a Bitwig project containing a suitable track.

For this exercise, resist the temptation to begin with the mouse.

First:

1. Select the destination track from the X-Touch.
2. Enter Browser Mode.
3. Observe the scribble strips before touching anything else.
4. Navigate through the available choices.
5. Choose an instrument, effect or other suitable item.
6. Confirm that it has been added in the intended location.

Now move directly into Device Mode.

7. Identify the newly added device.
8. Locate a useful parameter.
9. Adjust it using a V-Pot.
10. Listen to the result.

Finally, return to normal mixer operation.

The purpose of this exercise is not to prove that every operation can be performed without a mouse.

It is to experience the complete sequence:

**Select → Browse → Choose → Control → Listen**

When that sequence begins to feel like a single operation rather than five separate features, the X-Touch is becoming part of your workflow.

:::
