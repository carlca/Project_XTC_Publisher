---
chapter: 6
title: "The SELECT Button"
status: draft
---

# The SELECT Button

Every X-Touch channel strip has a SELECT button.

At first glance, its purpose seems obvious:

```text
SELECT
   │
   ▼
Select Track
```

And that is indeed its most basic function.

But in DrivenByMoss, SELECT is considerably more important than that.

It can:

- select a track;
- enter a Group;
- leave a Group;
- enter Layers or Drum Pads;
- expand or collapse a Group;
- participate in multi-selection;
- stop a playing clip;
- open or close a Group folder;
- choose a new clip length;
- select a Send.

So SELECT is not merely:

> **Which track do I want?**

It is one of the X-Touch's principal **navigation and context controls**.

---

# Basic Selection

Suppose the X-Touch currently represents:

```text
1       2       3       4       5       6       7       8

Kick   Snare   Hats    Bass    Pad     Lead    Vox     FX
```

Press SELECT beneath Bass:

```text
Kick   Snare   Hats   [Bass]   Pad     Lead    Vox     FX
```

Bass becomes the selected track in Bitwig.

That selection matters because many other X-Touch operations act on:

> **the currently selected track**

For example, Device Mode needs to know which track's devices you want to edit.

---

# SELECT Establishes Focus

A useful mental model is:

```text
Many Tracks
     │
     ▼
   SELECT
     │
     ▼
One Track Has Focus
```

The SELECT button answers:

> **Which track am I interested in right now?**

This makes it different from BANK and CHANNEL.

BANK and CHANNEL move the eight-channel window.

SELECT chooses something within that window.

```text
BANK / CHANNEL
      │
      ▼
Where am I looking?


SELECT
   │
   ▼
What am I working on?
```

That distinction is fundamental.

---

# Selection and the Eight-Channel Window

Imagine the controller currently shows:

```text
Kick   Snare   Hats   Bass   Pad   Lead   Vox   FX
```

You press SELECT beneath Vocal:

```text
Kick   Snare   Hats   Bass   Pad   Lead  [Vox]  FX
```

The X-Touch now has a selected track.

If you subsequently move the bank, Vocal may disappear from the eight visible strips.

But that does not necessarily mean the selection itself has disappeared.

This is why it is useful to distinguish:

```text
controller bank
```

from:

```text
selected track
```

The bank determines what the surface currently exposes.

SELECT determines what has focus.

---

# SELECT Has a Second Role

When hierarchical track navigation is enabled in DrivenByMoss, pressing SELECT on an already selected Group does something different.

It enters that Group.

The sequence is:

```text
SELECT Group
      │
      ▼
Group becomes selected
      │
      ▼
SELECT same Group again
      │
      ▼
Enter Group
```

This is one of the most important navigation patterns on the X-Touch.

---

# Selecting Versus Entering

Suppose the top level of the project contains:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

and Drums is a Group.

The first press:

```text
SELECT Drums
```

means:

> **Select the Drums Group.**

The second press:

```text
SELECT Drums again
```

means:

> **Enter the Drums Group.**

The controller might then show:

```text
Kick   Snare   Hats   Toms   Perc   Room
```

The same physical channel strips now represent tracks **inside** the Group.

---

# SELECT Creates Hierarchical Navigation

Conceptually:

```text
Project
   │
   ├── Drums
   │     │
   │     ├── Kick
   │     ├── Snare
   │     ├── Hats
   │     └── Percussion
   │
   ├── Bass
   ├── Guitar
   └── Vocal
```

At the top level:

```text
Drums   Bass   Guitar   Vocal
```

Select Drums:

```text
[Drums]   Bass   Guitar   Vocal
```

Select Drums again:

```text
Kick   Snare   Hats   Percussion
```

The X-Touch has moved **down one level** in the project hierarchy.

---

# Leaving a Group

To leave the current Group in hierarchical navigation:

> **Long-press any track SELECT button.**

Conceptually:

```text
Inside Drums

Kick   Snare   Hats   Perc
             │
             │ long-press SELECT
             ▼

Project Level

Drums   Bass   Guitar   Vocal
```

Notice the wording:

> **any SELECT button**

You do not need to find a special Back button.

The long press itself means:

> **Leave this level.**

---

# A Compact Navigation Vocabulary

This gives us a remarkably small set of gestures:

```text
SELECT
   │
   ▼
Focus
```

```text
SELECT again
   │
   ▼
Enter
```

```text
Long-press SELECT
   │
   ▼
Leave
```

Or, even more compactly:

```text
SELECT
   → focus

SELECT again
   → descend

Long SELECT
   → ascend
```

This pattern becomes extremely useful later.

---

# SELECT and Flat Navigation

DrivenByMoss also supports **Flat** track navigation.

In Flat mode, the controller does not use Groups as hierarchical levels in the same way.

Instead, all tracks are presented in a flat navigation structure.

That changes what happens when an already selected Group track is selected again.

In Flat mode:

```text
SELECT selected Group again
          │
          ▼
Toggle Group expanded state
```

So the same gesture has two related meanings depending on the Track Navigation preference.

---

## Hierarchical Versus Flat

In **Hierarchical** navigation:

```text
SELECT Group
      ↓
SELECT Group again
      ↓
Enter Group
```

In **Flat** navigation:

```text
SELECT Group
      ↓
SELECT Group again
      ↓
Expand / Collapse Group
```

This is an important example of configuration changing controller behaviour.

If two X-Touch users describe different results from pressing SELECT twice on a Group, both may be correct.

Their DrivenByMoss Track Navigation setting may differ.

---

# SELECT Also Enters Layers and Drum Pads

Groups are not the only structures that SELECT can enter.

If the selected track contains an instrument with Layers or Drum Pads, pressing its SELECT button again can enter the corresponding Layer / Drum Pad mode.

Conceptually:

```text
Instrument Track
      │
      │ SELECT
      ▼
Selected
      │
      │ SELECT again
      ▼
Layers / Drum Pads
```

The eight channel strips can then represent the contents of the instrument.

For example:

```text
Kick   Snare   Hat   Clap   Rim   Tom   Shaker   Perc
```

rather than eight ordinary project tracks.

---

# Leaving Layers or Drum Pads

The exit gesture remains the same:

```text
Long-press any SELECT
          │
          ▼
Leave Layer / Drum Pad mode
```

So the hierarchical vocabulary remains consistent:

```text
SELECT again
   → enter

Long SELECT
   → leave
```

This consistency is one reason SELECT is worth understanding early in the guide.

---

# SELECT Is Contextual

We can now see that a normal SELECT press does not have only one possible effect.

Its meaning depends on what is currently selected and what that track contains.

For example:

```text
Ordinary Track
      │
      ▼
SELECT
      │
      ▼
Select Track
```

but:

```text
Selected Group
      │
      ▼
SELECT again
      │
      ▼
Enter Group
```

and:

```text
Selected Track
containing Layers
      │
      ▼
SELECT again
      │
      ▼
Enter Layers
```

and similarly for Drum Pads.

The physical button stays the same.

The context determines what the action means.

---

# SHIFT + SELECT — Multi-Selection

SELECT also participates in modifier combinations.

DrivenByMoss documents:

```text
SHIFT + SELECT
      │
      ▼
Multi-select Tracks
```

where multi-selection is supported by the DAW.

So normal SELECT says:

> **Work with this track.**

SHIFT + SELECT says:

> **Add this track to, or otherwise participate in, a multiple-track selection.**

Conceptually:

```text
SELECT Track 2

Track 2
   │
   ▼
selected
```

then:

```text
SHIFT + SELECT Track 4
```

allows a multi-track selection rather than simply replacing the original selection.

---

# SHIFT + SELECT Has Another Important Context

There is another documented use of SHIFT + the Track SELECT buttons:

> **Selecting the New Clip Length.**

The eight SELECT buttons correspond to:

```text
SHIFT + SELECT 1   → 16 bars

SHIFT + SELECT 2   → 8 bars

SHIFT + SELECT 3   → 4 bars

SHIFT + SELECT 4   → 2 bars

SHIFT + SELECT 5   → 1 bar

SHIFT + SELECT 6   → 2 beats

SHIFT + SELECT 7   → 1 beat

SHIFT + SELECT 8   → 32 bars
```

This means SHIFT + SELECT is another contextual combination.

In an appropriate selection context it participates in track multi-selection.

It is also used by DrivenByMoss to choose the length used when creating new clips.

We will return to New Clip Length in the recording chapters.

---

# OPTION + SELECT — Stop a Clip

OPTION gives SELECT a very different purpose.

DrivenByMoss documents:

```text
OPTION + SELECT
       │
       ▼
Stop the playing clip
on that track
```

Suppose several Launcher clips are playing:

```text
Drums    Bass    Keys    Vocal
  ▶        ▶       ▶       ▶
```

Use:

```text
OPTION + SELECT
```

on Keys.

The command targets the playing clip on that specific track.

This is a performance-oriented function rather than a selection function.

---

## The Modifier Changes the Question

Without OPTION:

```text
SELECT
   │
   ▼
Which track do I want?
```

With OPTION:

```text
OPTION + SELECT
       │
       ▼
Which track's playing clip
do I want to stop?
```

This is a useful example of the modifier system.

The physical location still identifies the track.

The modifier changes the action performed on it.

---

# CONTROL + SELECT — Open or Close a Group

CONTROL gives SELECT another Group-related function.

DrivenByMoss documents:

```text
CONTROL + SELECT
        │
        ▼
Open / Close Group Folder
```

when the corresponding track is a Group.

This should not be confused with hierarchical entry.

---

## Entering and Opening Are Different

With hierarchical navigation:

```text
SELECT selected Group again
          │
          ▼
Enter Group
```

means:

> **Make the Group's contents the controller's current navigation level.**

Whereas:

```text
CONTROL + SELECT
```

means:

> **Open or close the Group folder in Bitwig.**

Conceptually:

```text
SELECT again
   → controller navigation

CONTROL + SELECT
   → Group folder state
```

These are related ideas, but they are not the same operation.

---

# ALT + SELECT — Set New Clip Length

DrivenByMoss also documents:

```text
ALT + SELECT
     │
     ▼
Set the length of a new clip
```

This associates the eight SELECT buttons with clip-length choices.

The exact clip-length choices documented for the Track SELECT row are:

```text
1   → 16 bars

2   → 8 bars

3   → 4 bars

4   → 2 bars

5   → 1 bar

6   → 2 beats

7   → 1 beat

8   → 32 bars
```

This is particularly useful for Launcher-oriented recording.

Instead of opening a settings dialog before creating a clip, the surface can participate directly in choosing its length.

---

# SEND + SELECT — Choose the Send

SELECT also works with the SEND mode button.

DrivenByMoss documents:

```text
SEND + SELECT 1
   → Send 1

SEND + SELECT 2
   → Send 2

...

SEND + SELECT 8
   → Send 8
```

So the SELECT row becomes a direct Send selector.

This is an important pattern.

Normally the eight SELECT buttons correspond to eight tracks.

But when SEND is held:

```text
SELECT row
     │
     ▼
Send choices 1–8
```

The same physical row is temporarily repurposed.

---

# A Row of Eight Choices

This gives us a broader way to think about the SELECT buttons.

Sometimes they mean:

```text
Track 1
Track 2
Track 3
...
Track 8
```

But with another control held, the same row can become:

```text
Choice 1
Choice 2
Choice 3
...
Choice 8
```

For example:

```text
SEND + SELECT
      │
      ▼
Send 1–8
```

or when setting clip length:

```text
modifier + SELECT
       │
       ▼
one of eight clip lengths
```

The SELECT row is therefore not merely eight copies of a Track Select command.

It is also an **eight-choice command surface**.

---

# Why SELECT Is So Powerful

The X-Touch has eight identical channel strips.

That gives DrivenByMoss a ready-made row of eight physical targets.

SELECT naturally identifies:

```text
this one
```

So the software can reuse that gesture in many contexts.

For example:

```text
SELECT
   → this track

OPTION + SELECT
   → stop clip on this track

CONTROL + SELECT
   → open/close this Group

SEND + SELECT
   → choose this Send number

clip-length modifier + SELECT
   → choose this clip length
```

The physical position provides the number or target.

The context provides the meaning.

---

# SELECT and Fader Touch

There is another relationship worth understanding.

DrivenByMoss can be configured so that touching a motor fader automatically selects its track.

With that preference enabled:

```text
Touch Fader
     │
     ▼
Select Track
```

So there are two physical ways of establishing track focus:

```text
SELECT button
```

or:

```text
touch fader
```

The SELECT button remains the explicit choice.

Fader-touch selection can make mixing workflows faster because simply reaching for a channel can establish its focus.

We will discuss the preference itself in Chapter 21.

---

# The Master Fader Can Select Too

The same principle applies to the Master fader.

DrivenByMoss documents that touching the Master fader selects the Master track.

Conceptually:

```text
Touch Master Fader
        │
        ▼
Master Track Selected
```

That selection can then place the controller into the Master editing context.

So selection is not limited strictly to the eight channel SELECT buttons.

But those eight buttons remain the controller's primary explicit selection mechanism.

---

# SELECT Before Acting

A useful X-Touch habit is:

> **Establish focus before performing a contextual action.**

For example:

```text
SELECT Synth
     ↓
DEVICE
     ↓
edit synth
```

or:

```text
SELECT Vocal
     ↓
SEND
     ↓
adjust delay
```

or:

```text
SELECT Drum Group
     ↓
SELECT again
     ↓
work inside Drums
```

The sequence is often:

```text
Focus
   ↓
Context
   ↓
Action
```

SELECT frequently performs the first step.

---

# Avoid Accidental Second Presses

Because SELECT can have a second-stage meaning, it is worth being deliberate when pressing an already selected track.

On an ordinary track, another press may have little consequence.

But on a Group, Layer-capable instrument or Drum Machine, a second press may change the controller's navigation context.

So:

```text
first SELECT
   → select
```

and:

```text
second SELECT
   → potentially enter
```

are worth thinking of as separate gestures.

---

# If the Surface Suddenly Changes

Suppose you press SELECT and the scribble strips unexpectedly change from:

```text
Drums   Bass   Guitar   Keys   Vocal
```

to:

```text
Kick   Snare   Hats   Perc   Room
```

The controller has probably not malfunctioned.

You may simply have entered a Group or Layer/Drum Pad context.

The recovery gesture is:

```text
Long-press any SELECT
```

to leave that context.

This is worth remembering because it gives you a simple escape route when learning hierarchical navigation.

---

# ENTER and CANCEL Are Not Hierarchy Controls

It is particularly important to clarify one thing.

The X-Touch has ENTER and CANCEL buttons.

It might seem natural to assume:

```text
ENTER
   → go into Group

CANCEL
   → go back
```

But that is **not** how DrivenByMoss documents hierarchical Track navigation.

Hierarchy uses:

```text
SELECT again
   → enter

Long SELECT
   → leave
```

ENTER and CANCEL have other roles.

For example, in Browser Mode:

```text
ENTER
   → confirm Browser selection

CANCEL
   → discard Browser selection
```

Outside the Browser they behave like the corresponding computer keyboard keys.

Keeping these concepts separate prevents a great deal of confusion.

---

# Hierarchical Navigation as a Tree

The SELECT behaviour becomes particularly intuitive if you imagine the project as a tree.

```text
Project
   │
   ├── Drums
   │     │
   │     ├── Kick
   │     ├── Snare
   │     └── Hats
   │
   ├── Bass
   │
   └── Synths
         │
         ├── Pad
         └── Lead
```

BANK and CHANNEL move:

```text
across
```

the current level.

SELECT again moves:

```text
down
```

into a level.

Long SELECT moves:

```text
up
```

out of it.

So:

```text
BANK / CHANNEL
      → horizontal navigation

SELECT / Long SELECT
      → vertical navigation
```

This is a powerful mental model for large projects.

---

# SELECT as Navigation

We can therefore expand our original definition.

At first:

```text
SELECT
   → choose a track
```

Now:

```text
SELECT
   → establish focus

SELECT again
   → enter available structure

Long SELECT
   → leave structure
```

And with modifiers:

```text
SHIFT + SELECT
   → additional selection / clip-length function

OPTION + SELECT
   → stop playing clip on track

CONTROL + SELECT
   → open / close Group folder

ALT + SELECT
   → set new clip length

SEND + SELECT
   → select Send 1–8
```

That is a great deal of functionality from one row of buttons.

---

# Do Not Memorise the Modifier Table Yet

At this point, you do not need to memorise every SELECT combination.

The most important behaviour to learn is:

```text
SELECT
   → focus
```

followed by:

```text
SELECT again
   → enter
```

and:

```text
Long SELECT
   → leave
```

Once that is comfortable, the modifier functions can be added gradually.

The dedicated Modifiers chapter will give them a more systematic treatment.

---

# A Practical Exercise

Create or open a project containing several ordinary tracks and at least one Group.

For example:

```text
Drums
Bass
Guitar
Keys
Vocal
```

with Drums containing:

```text
Kick
Snare
Hats
Percussion
```

Make sure DrivenByMoss Track Navigation is set to **Hierarchical**.

### 1. Select Bass

Press its SELECT button.

Watch Bitwig and the X-Touch feedback.

### 2. Select Drums

Press SELECT beneath the Drums Group.

The Group should become selected.

### 3. Press Drums SELECT again

The controller should enter the Group.

The scribble strips should now represent its contents.

### 4. Long-press a SELECT button

The controller should leave the Group.

### 5. Repeat the process

Do it several times until:

```text
SELECT
SELECT again
Long SELECT
```

feels like:

```text
focus
enter
leave
```

rather than three commands you have to remember.

---

# A Modifier Exercise

Once normal hierarchical navigation is comfortable, try a few modified SELECT operations separately.

For example:

```text
OPTION + SELECT
```

on a track with a playing Launcher clip.

Then try:

```text
CONTROL + SELECT
```

on a Group.

Finally, enter Send Mode and try:

```text
SEND + SELECT
```

to select different Send channels.

The purpose is not to memorise everything.

It is to notice the recurring pattern:

> **The SELECT button identifies a position; the modifier or current mode determines what that position means.**

---

# The Important Idea

SELECT is one of the most important controls on the X-Touch.

Its basic function is:

```text
SELECT
   → select track
```

But it also provides hierarchical navigation:

```text
SELECT selected Group again
   → enter Group

Long-press any SELECT
   → leave Group
```

and access to Layers and Drum Pads:

```text
SELECT selected containing track again
   → enter Layers / Drum Pads

Long-press any SELECT
   → leave
```

Its modifier functions include:

```text
SHIFT + SELECT
   → multi-selection
     / New Clip Length context

OPTION + SELECT
   → stop playing clip on track

CONTROL + SELECT
   → open / close Group folder

ALT + SELECT
   → set New Clip Length

SEND + SELECT
   → choose Send 1–8
```

So SELECT is much more than a track-selection button.

A useful mental model is:

```text
SELECT
   │
   ▼
"This one."
```

The current mode, modifier and context determine what **“this one”** means.

---

## Coming Next

We now know how to move the X-Touch's eight-channel window through the project and how SELECT establishes focus within it.

But the controller still needs to tell us what those physical controls currently represent.

That feedback comes from several places:

- the scribble strips;
- the assignment display;
- LEDs;
- motorised faders;
- V-Pot rings.

Next:

**Displays and Feedback.**
