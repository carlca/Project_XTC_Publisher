---
chapter: 4
title: "Banks and Channels"
status: draft
---

# Banks and Channels

The X-Touch has eight channel strips.

A Bitwig project can have far more than eight tracks.

So one of the first important ideas to understand is this:

> **The eight channel strips are a window onto the project.**

They do not permanently belong to Tracks 1–8.

They represent whichever eight tracks are currently visible to the controller.

---

## The Eight-Channel Window

Imagine a Bitwig project containing 24 tracks:

```text
Project

 1   2   3   4   5   6   7   8
 9  10  11  12  13  14  15  16
17  18  19  20  21  22  23  24
```

The X-Touch can physically show eight of them at once.

Initially, that might be:

```text
Bitwig Project
──────────────────────────────────────────────

┌──────────────────────────────┐
│  1   2   3   4   5   6   7   8  │
└──────────────────────────────┘
              X-Touch
```

The faders, V-Pots, MUTE, SOLO, ARM and SELECT buttons all refer to those eight tracks.

But the window can move.

---

# BANK — Move Eight Tracks at a Time

The BANK buttons move the track-bank focus by eight tracks.

Press:

```text
BANK >
```

and the controller moves to the next group of eight.

So:

```text
Before

┌──────────────────────────────┐
│  1   2   3   4   5   6   7   8  │
└──────────────────────────────┘
```

becomes:

```text
After BANK >

┌──────────────────────────────┐
│  9  10  11  12  13  14  15  16 │
└──────────────────────────────┘
```

Press BANK > again:

```text
┌──────────────────────────────┐
│ 17  18  19  20  21  22  23  24 │
└──────────────────────────────┘
```

BANK < moves in the opposite direction.

---

## BANK Is the Large Movement

A useful mental model is:

```text
BANK
  │
  ▼
move by one whole surface
```

Because the X-Touch has eight channel strips:

```text
BANK
  │
  ▼
8 tracks
```

This is the fastest way to move through a large project.

---

# CHANNEL — Move One Track at a Time

The CHANNEL buttons move the track-bank focus by one track.

Suppose the controller currently shows:

```text
1   2   3   4   5   6   7   8
```

Press:

```text
CHANNEL >
```

and the window moves by one:

```text
2   3   4   5   6   7   8   9
```

Press it again:

```text
3   4   5   6   7   8   9  10
```

CHANNEL < moves the window back one track.

---

## CHANNEL Is the Small Movement

So the simplest distinction is:

```text
BANK
   → move 8

CHANNEL
   → move 1
```

Or:

```text
BANK
   → coarse navigation

CHANNEL
   → fine navigation
```

That is the fundamental relationship between the two pairs of buttons.

---

# BANK and CHANNEL Work Together

Suppose you have 40 tracks and want to reach Track 19.

You could press CHANNEL > eighteen times.

That would work.

But it would be tedious.

Instead:

```text
Tracks 1–8
    │
    │ BANK >
    ▼
Tracks 9–16
    │
    │ BANK >
    ▼
Tracks 17–24
```

Now Track 19 is visible.

BANK gets you into the right area.

CHANNEL lets you make smaller adjustments when necessary.

A useful rule is:

> **BANK for distance. CHANNEL for precision.**

---

# The Hardware Does Not Belong to Particular Tracks

This is worth emphasising.

Physical Channel Strip 1 is not:

> **Track 1.**

It means:

> **The first track in the controller's current bank.**

Likewise, Physical Channel Strip 8 means:

> **The eighth track in the current bank.**

So:

```text
Bank 1

Strip     1   2   3   4   5   6   7   8
Track     1   2   3   4   5   6   7   8
```

then:

```text
Bank 2

Strip     1   2   3   4   5   6   7   8
Track     9  10  11  12  13  14  15  16
```

The physical strips remain where they are.

Their targets change.

---

# Watch the Scribble Strips

This is why the scribble strips are so important.

After changing bank, do not continue thinking:

```text
Fader 1 = previous Track 1
```

Look at the display.

It tells you what Fader 1 represents **now**.

For example:

```text
Before BANK >

Kick   Snare   Hats   Bass   Pad   Lead   Vox   FX
```

then:

```text
After BANK >

Room   Perc   Piano   Gtr1   Gtr2   BVox   Verb   Delay
```

The controls have not moved.

Their context has.

This gives us one of the most important habits in Project XTC:

> **Observe before you adjust.**

---

# Banking Does Not Select a Track

Moving the bank and selecting a track are different ideas.

BANK and CHANNEL change:

> **Which tracks are available on the eight channel strips?**

SELECT changes:

> **Which particular track has focus?**

So:

```text
BANK / CHANNEL
      │
      ▼
move the window
```

whereas:

```text
SELECT
   │
   ▼
choose something inside the window
```

This distinction becomes increasingly important later.

---

# Selection Can Move with the Window

Suppose Track 6 is selected.

Your current bank is:

```text
1   2   3   4   5  [6]  7   8
```

You then move to:

```text
9  10  11  12  13  14  15  16
```

Track 6 still exists in the project.

It is simply no longer represented by one of the eight visible channel strips.

This distinction between:

```text
selected track
```

and:

```text
tracks currently exposed by the bank
```

is useful when understanding more advanced controller behaviour.

---

# The Window Can Overlap

CHANNEL navigation shows us that banks are not necessarily isolated blocks.

For example:

```text
1  2  3  4  5  6  7  8
```

followed by CHANNEL > gives:

```text
2  3  4  5  6  7  8  9
```

So the controller window can overlap its previous position.

This is why it is better to think in terms of a **movable eight-track window** than a set of fixed pages.

---

# A Visual Model

Imagine a long strip of tracks:

```text
01 02 03 04 05 06 07 08 09 10 11 12 13 14 15 16 17 18 19 20
```

The X-Touch window begins here:

```text
[01 02 03 04 05 06 07 08] 09 10 11 12 13 14 15 16 17 18 19 20
```

BANK >:

```text
01 02 03 04 05 06 07 08 [09 10 11 12 13 14 15 16] 17 18 19 20
```

CHANNEL >:

```text
01 02 03 04 05 06 07 08 09 [10 11 12 13 14 15 16 17] 18 19 20
```

BANK changes the window dramatically.

CHANNEL nudges it.

---

# Banking and Large Projects

Suppose a project contains:

```text
Drums
Bass
Guitar
Piano
Pad
Lead
Vocal
Backing Vocal
Percussion
Strings
FX 1
FX 2
...
```

With a mouse, you might scroll horizontally through the mixer.

With the X-Touch:

```text
BANK >
```

is the equivalent large-scale movement.

The eight physical strips remain a stable workspace while the project moves through them.

This can become much faster than visually hunting for a track.

---

# Track Order Matters

Because BANK and CHANNEL follow the Bitwig track bank, the order of tracks in the project affects the physical workflow.

For example, this:

```text
Kick
Snare
Hats
Percussion
Bass
Guitar
Keys
Vocal
```

may make more physical sense than:

```text
Kick
Vocal
Keys
Snare
Guitar
Hats
Bass
Percussion
```

if the first arrangement reflects how you naturally think about the mix.

This is not an X-Touch rule.

It is a workflow observation:

> **A logically organised Bitwig project is easier to navigate from hardware.**

---

# OPTION Changes BANK and CHANNEL

BANK and CHANNEL have another set of functions when used with OPTION.

These are important because they do **not** navigate the track bank.

Instead, they physically reorganise things in the Bitwig project.

The verified DrivenByMoss mappings are:

```text
OPTION + BANK <
   → Move selected device left

OPTION + BANK >
   → Move selected device right
```

and:

```text
OPTION + CHANNEL <
   → Move selected track left

OPTION + CHANNEL >
   → Move selected track right
```

This is a significant distinction.

Without OPTION:

```text
BANK / CHANNEL
   → navigate
```

With OPTION:

```text
BANK / CHANNEL
   → move project objects
```

---

# OPTION + CHANNEL — Move the Selected Track

Suppose the project order is:

```text
Drums   Bass   Guitar   Vocal
```

and Guitar is selected:

```text
Drums   Bass  [Guitar]  Vocal
```

Use:

```text
OPTION + CHANNEL <
```

and the selected track moves to the left.

Conceptually:

```text
Before

Drums   Bass  [Guitar]  Vocal


OPTION + CHANNEL <


After

Drums  [Guitar]  Bass   Vocal
```

Likewise:

```text
OPTION + CHANNEL >
```

moves the selected track to the right.

This is not scrolling.

It is **reordering the project**.

---

## Navigation Versus Reorganisation

This difference deserves a clear mental separation:

```text
CHANNEL >
   → show the next track position
```

but:

```text
OPTION + CHANNEL >
   → move the selected track
     to the right
```

One changes your view.

The other changes the project.

Because moving tracks is consequential, use the modified command deliberately.

---

# OPTION + BANK — Move the Selected Device

OPTION + BANK performs the corresponding operation at device level.

Suppose a track contains:

```text
EQ  →  Compressor  →  Delay
```

and Compressor is selected.

Use:

```text
OPTION + BANK <
```

to move the selected device left.

Conceptually:

```text
Before

EQ  →  [Compressor]  →  Delay


OPTION + BANK <


After

[Compressor]  →  EQ  →  Delay
```

And:

```text
OPTION + BANK >
```

moves the selected device to the right.

Again, this is not controller navigation.

The device itself is being moved within the Bitwig device chain.

---

# Why BANK for Devices and CHANNEL for Tracks?

At first, this may seem slightly odd:

```text
OPTION + BANK
   → move device

OPTION + CHANNEL
   → move track
```

But it becomes easier to remember once Device Mode is introduced.

BANK already acquires a strong relationship with **devices** there.

CHANNEL remains associated with movement at a finer level.

For now, it is enough to learn the verified mapping rather than trying to force every command into a perfect analogy.

---

# Device Mode Is the Important Exception

So far we have said:

```text
BANK
   → move 8 tracks

CHANNEL
   → move 1 track
```

That is correct during normal track-oriented operation.

But DrivenByMoss explicitly makes **Device Mode an exception**.

In Device Mode:

```text
BANK <
   → Previous Device

BANK >
   → Next Device
```

while:

```text
CHANNEL <
   → Previous Parameter Page

CHANNEL >
   → Next Parameter Page
```

So the same buttons change meaning according to context.

---

## Normal Context Versus Device Context

Outside Device Mode:

```text
BANK
   → 8 tracks

CHANNEL
   → 1 track
```

Inside Device Mode:

```text
BANK
   → devices

CHANNEL
   → parameter pages
```

This is not an inconsistency.

It is an example of the X-Touch's contextual design.

The controls are reused for the kind of navigation appropriate to the current mode.

---

# BANK Means "Larger Step"

There is a useful conceptual pattern here.

In ordinary track navigation:

```text
BANK
   → large movement through tracks
```

In Device Mode:

```text
BANK
   → movement between whole devices
```

Meanwhile:

```text
CHANNEL
```

handles the finer-grained movement:

```text
Normal
   → individual tracks

Device Mode
   → individual parameter pages
```

So even though the literal targets change, the broad relationship remains:

> **BANK moves at the larger structural level; CHANNEL moves at the finer level.**

That is a useful idea to carry into later chapters.

---

# Context Determines Meaning

This gives us an early example of one of the most important ideas in the entire guide.

A physical button does not necessarily have one permanent function.

Its meaning depends on context.

For BANK >:

```text
Normal track context
       │
       ▼
move track bank by 8
```

but:

```text
Device Mode
       │
       ▼
select next device
```

and:

```text
OPTION + BANK >
       │
       ▼
move selected device right
```

One physical button.

Three related but distinct operations.

---

# Do Not Memorise All Three at Once

At this stage of the guide, the most important pair is still:

```text
BANK
   → 8 tracks

CHANNEL
   → 1 track
```

Learn that first.

The other meanings will become easier when we reach the relevant chapters.

For now, simply remember:

> **BANK and CHANNEL are contextual navigation controls, and modifiers can turn navigation into editing.**

---

# Banks and Hierarchy

Later we will introduce another dimension: hierarchical navigation.

A project might contain:

```text
Project
   │
   ├── Drums
   │     ├── Kick
   │     ├── Snare
   │     └── Hats
   │
   ├── Bass
   └── Synths
```

When working hierarchically, entering the Drums Group changes the level represented by the controller.

BANK and CHANNEL then navigate the tracks available at that level.

So we eventually gain two kinds of movement:

```text
BANK / CHANNEL
      → across the current level

SELECT navigation
      → between levels
```

This becomes extremely powerful in large projects.

We will explore it properly in Chapter 17.

---

# The Window Model Still Holds

Even after adding Device Mode, Groups, Layers and other contexts, the original window idea remains useful.

The X-Touch has a limited number of physical controls.

DrivenByMoss decides what part of Bitwig those controls currently expose.

Conceptually:

```text
Large Bitwig world
────────────────────────────────────

          ┌──────────────┐
          │   X-Touch    │
          │    window    │
          └──────────────┘
```

Sometimes that window contains tracks.

Sometimes devices.

Sometimes parameters.

Sometimes Layers or Drum Pads.

The hardware stays finite.

The thing it can explore does not.

---

# A Practical Exercise

Create or open a Bitwig project with at least twelve tracks.

Start with the first eight visible on the X-Touch.

### 1. Press BANK >

Watch the scribble strips.

You should see the track bank move by eight positions.

### 2. Press BANK <

Return to the original area.

### 3. Press CHANNEL >

Watch the window move by one track.

### 4. Press CHANNEL > several more times

Notice that the eight-strip window overlaps its previous position.

### 5. Press CHANNEL <

Move back one track at a time.

Do this without touching the mouse.

The aim is to make:

```text
BANK = large move

CHANNEL = small move
```

feel obvious rather than remembered.

---

# A Second Exercise

Once the basic navigation is comfortable, select a track and try:

```text
OPTION + CHANNEL <
```

and:

```text
OPTION + CHANNEL >
```

Watch Bitwig carefully.

The selected track itself should move.

Then compare that with plain CHANNEL.

The distinction should become very clear:

```text
CHANNEL
   → I move my view

OPTION + CHANNEL
   → I move the track
```

This is an excellent example of why modifiers deserve deliberate use.

---

# The Important Idea

The X-Touch does not have eight permanent tracks.

It has an **eight-channel window** onto Bitwig.

In normal track-oriented operation:

```text
BANK <
BANK >
   → move track-bank focus by 8

CHANNEL <
CHANNEL >
   → move track-bank focus by 1
```

With OPTION:

```text
OPTION + BANK
   → move selected device left / right

OPTION + CHANNEL
   → move selected track left / right
```

And in Device Mode:

```text
BANK
   → previous / next device

CHANNEL
   → previous / next parameter page
```

So the deeper mental model is:

```text
Physical Control
       +
Current Context
       +
Modifier, if any
       =
Current Function
```

For now, though, remember the simplest version:

> **BANK for distance. CHANNEL for precision.**

---

## Coming Next

We now know how eight physical channel strips can move through a project containing many more than eight tracks.

But navigation alone does not tell us what the controls **mean** at any particular moment.

The X-Touch can change the role of its V-Pots and other controls depending on what we are trying to edit.

Next:

**Modes.**
