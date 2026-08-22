---
chapter: 14
title: "Mixer Edit Modes"
status: draft
---

# Mixer Edit Modes

The X-Touch has eight V-Pots.

In some contexts, each V-Pot controls the same kind of parameter across eight tracks.

For example:

```text
Pan Mode

V-Pot 1  → Pan Track 1
V-Pot 2  → Pan Track 2
V-Pot 3  → Pan Track 3
...
V-Pot 8  → Pan Track 8
```

But DrivenByMoss also provides another way of using the same eight controls.

Instead of:

```text
one parameter
across eight tracks
```

the V-Pots can become:

```text
eight different parameters
for one selected track
```

This is the idea behind the Mixer Edit Modes.

---

# Two Ways to Look at the Mixer

The X-Touch can organise its eight V-Pots in two broad ways.

## Across Tracks

```text
Track 1   Track 2   Track 3   Track 4   ...
   │         │         │         │
   ▼         ▼         ▼         ▼
Same Parameter
```

For example:

```text
Pan
```

or:

```text
Send 1
```

across several tracks.

## Across Parameters

```text
Selected Track
      │
      ├── Volume
      ├── Panorama
      ├── Crossfader
      ├── Send 1
      ├── Send 2
      ├── Send 3
      ├── Send 4
      └── Send 5
```

The eight V-Pots now represent different aspects of one track.

These two viewpoints are both useful.

---

# TRACK — Track Edit Mode

Press:

```text
TRACK
```

to enter Track Edit Mode.

The V-Pots now control parameters belonging to the currently selected track.

The normal DrivenByMoss layout is:

```text
V-Pot 1  → Volume

V-Pot 2  → Panorama

V-Pot 3  → Crossfader

V-Pot 4  → Send 1

V-Pot 5  → Send 2

V-Pot 6  → Send 3

V-Pot 7  → Send 4

V-Pot 8  → Send 5
```

So the entire row becomes a compact mixer strip for one selected track.

---

# One Track, Eight Mixer Controls

Suppose Vocal is selected.

Track Edit Mode gives you something conceptually like:

```text
Vocal

Volume
Pan
Crossfader
Send 1
Send 2
Send 3
Send 4
Send 5
```

across the eight V-Pots.

Instead of moving sideways through the project, you are moving **deeper into one track**.

This is the opposite perspective from ordinary Pan or Send Mode.

---

# Why Track Edit Mode Is Useful

Suppose you want to adjust several related properties of the Vocal track.

Without Track Edit Mode, you might move through several controller contexts:

```text
Volume
   ↓
Pan
   ↓
Send 1
   ↓
Send 2
```

Track Edit Mode brings them together:

```text
Selected Track
      │
      ▼
Eight Mixer Parameters
```

This can be much faster when the work is centred on one particular track.

---

# The Crossfader Control

By default, V-Pot 3 controls the selected track's Crossfader assignment or position.

That gives the normal Track Edit layout:

```text
Volume

Panorama

Crossfader

Send 1

Send 2

Send 3

Send 4

Send 5
```

The important point is that the Crossfader occupies one of the eight available V-Pot positions.

That leaves room for five Sends.

---

# Crossfader Versus Send 6

DrivenByMoss provides a preference that can hide the Crossfader control from Track Edit Mode.

When that preference is enabled, the freed V-Pot is used for:

```text
Send 6
```

So the layout changes from:

```text
V-Pot 1  → Volume

V-Pot 2  → Panorama

V-Pot 3  → Crossfader

V-Pot 4  → Send 1

V-Pot 5  → Send 2

V-Pot 6  → Send 3

V-Pot 7  → Send 4

V-Pot 8  → Send 5
```

to:

```text
V-Pot 1  → Volume

V-Pot 2  → Panorama

V-Pot 3  → Send 1

V-Pot 4  → Send 2

V-Pot 5  → Send 3

V-Pot 6  → Send 4

V-Pot 7  → Send 5

V-Pot 8  → Send 6
```

The trade-off is therefore very simple:

```text
Crossfader
    versus
Sixth Send
```

---

# Which Layout Is Better?

Neither is universally better.

If you use Bitwig's Crossfader regularly:

```text
keep Crossfader
```

If you rarely use it but frequently work with many Sends:

```text
hide Crossfader
      ↓
gain Send 6
```

This is a good example of a preference that should follow the actual workflow.

The question is not:

> **Which configuration exposes more features?**

It is:

> **Which eight controls are most useful to me on this track?**

---

# A Send-Heavy Workflow

Suppose a project uses:

```text
Send 1  → Short Reverb

Send 2  → Long Reverb

Send 3  → Delay

Send 4  → Dub Echo

Send 5  → Chorus

Send 6  → Special FX
```

For that project, the six-Send Track Edit layout can be extremely useful.

Select a track:

```text
SELECT Vocal
```

then:

```text
TRACK
```

and you immediately have:

```text
Volume
Pan
Send 1
Send 2
Send 3
Send 4
Send 5
Send 6
```

on one row.

That is a very compact mixing environment.

---

# A Crossfader-Oriented Workflow

In another project, the Crossfader may be central to the performance.

Perhaps tracks are being assigned between:

```text
A
```

and:

```text
B
```

for live transitions or performance mixing.

Then the normal Track Edit layout makes more sense:

```text
Volume
Pan
Crossfader
Send 1
Send 2
Send 3
Send 4
Send 5
```

The preference lets the controller reflect the way the project is actually being used.

---

# TRACK Pressed Again — Volume Edit Mode

DrivenByMoss also uses repeated presses of some assignment buttons to reach related modes.

Press TRACK again:

```text
TRACK
   ↓
Track Edit Mode

TRACK again
   ↓
Volume Edit Mode
```

In Volume Edit Mode:

```text
V-Pot 1  → Volume Track 1

V-Pot 2  → Volume Track 2

...

V-Pot 8  → Volume Track 8
```

The viewpoint changes from:

```text
many parameters
on one track
```

to:

```text
one parameter
across many tracks
```

---

# Track Edit Mode Versus Volume Edit Mode

Compare:

```text
TRACK

Selected Track
   │
   ├── Volume
   ├── Panorama
   ├── Crossfader / Send 1
   ├── Sends
   └── ...
```

with:

```text
TRACK again

Track 1  → Volume
Track 2  → Volume
Track 3  → Volume
...
Track 8  → Volume
```

The same physical button therefore provides two related mixer perspectives.

---

# PAN — Panorama Edit Mode

Press:

```text
PAN
```

and the V-Pots control Panorama across the current bank.

```text
V-Pot 1  → Pan Track 1

V-Pot 2  → Pan Track 2

...

V-Pot 8  → Pan Track 8
```

This is the classic mixer-style rotary layout.

All eight controls perform the same kind of operation.

Their targets differ.

---

# SEND — Send Edit Mode

Press:

```text
SEND
```

to enter Send Edit Mode.

Now the V-Pots control one selected Send across the current bank of tracks.

For example:

```text
Send 1 Selected

Track 1  → V-Pot 1
Track 2  → V-Pot 2
Track 3  → V-Pot 3
...
Track 8  → V-Pot 8
```

All eight V-Pots now answer:

> **How much of this track goes to this Send?**

---

# SEND Pressed Again

Repeated presses of SEND move forward through the available Sends.

Conceptually:

```text
SEND
  ↓
Send 1

SEND
  ↓
Send 2

SEND
  ↓
Send 3
```

and so on.

SHIFT + SEND moves backwards.

So:

```text
SEND
   → Next Send

SHIFT + SEND
   → Previous Send
```

This allows the same eight V-Pots to move through multiple Send destinations.

---

# Direct Send Selection

DrivenByMoss also provides:

```text
SEND + SELECT 1–8
```

to choose a Send directly.

Conceptually:

```text
SEND + SELECT 1
   → Send 1

SEND + SELECT 2
   → Send 2

...

SEND + SELECT 8
   → Send 8
```

This avoids stepping through several Sends when you already know which one you want.

---

# Across Tracks Versus One Track

Mixer Edit Modes become much easier to understand when grouped into two families.

## One Parameter Across Many Tracks

```text
Volume Mode

Panorama Mode

Send Mode
```

Conceptually:

```text
Track 1   Track 2   Track 3   Track 4   ...
   │         │         │         │
   ▼         ▼         ▼         ▼
Same Parameter
```

## Many Parameters on One Track

```text
Track Edit Mode
```

Conceptually:

```text
Selected Track
      │
      ├── Volume
      ├── Panorama
      ├── Crossfader / Send
      ├── Send
      ├── Send
      └── ...
```

Once you recognise which of those two viewpoints is active, the V-Pot row becomes much easier to understand.

---

# Mixer Edit Mode Is About Perspective

The difference is not merely which button you pressed.

It is the question you are asking.

Track Edit Mode asks:

> **What can I change about this one track?**

Panorama Mode asks:

> **How are these eight tracks positioned across the stereo field?**

Send Mode asks:

> **How much are these eight tracks feeding this one destination?**

Volume Mode asks:

> **How loud are these eight tracks?**

The mode changes the perspective.

---

# Track Edit Mode and the Selected Track

Track Edit Mode depends on track selection.

If the selected track changes:

```text
Track Edit Parameters
        ↓
Change Target
```

The same eight V-Pots now represent the corresponding parameters of the newly selected track.

For example:

```text
SELECT Vocal
     ↓
TRACK
     ↓
Vocal Parameters
```

then:

```text
SELECT Guitar
     ↓
Guitar Parameters
```

The V-Pot layout remains conceptually stable.

The target track changes.

---

# Fader Touch and Track Edit Mode

If:

```text
Select Channel on Fader Touch
```

is enabled in DrivenByMoss, touching a fader can change the selected track.

That means Track Edit Mode can follow your physical attention.

Conceptually:

```text
Track Edit Mode
      ↓
Touch Vocal Fader
      ↓
Vocal Selected
      ↓
V-Pots = Vocal Parameters
```

then:

```text
Touch Guitar Fader
      ↓
Guitar Selected
      ↓
V-Pots = Guitar Parameters
```

This can create a very fluid workflow.

But remember that fader-touch selection is configurable.

---

# V-Pot Press Modifiers Still Apply

The general V-Pot behaviours from Chapter 9 remain useful in Mixer Edit Modes.

For a parameter control:

```text
Press
   → Default
```

```text
SHIFT + Press
   → Centre
```

```text
CONTROL + Press
   → Minimum
```

```text
ALT + Press
   → Maximum
```

And when controlling a Send:

```text
OPTION + Press
   → Toggle Send On / Off
```

So Mixer Edit Modes determine:

```text
what parameter
```

the V-Pot represents.

The gestures determine:

```text
what you do to that parameter
```

---

# FLIP and Mixer Edit Modes

FLIP can exchange the current V-Pot assignment with the faders.

For example, in Send Mode:

```text
V-Pots
   → Send Levels
```

Press:

```text
FLIP
```

and those Send levels can be controlled from the motor faders.

This can be useful for more expressive or precise physical control.

Chapter 10 explains FLIP itself in detail.

Here the important point is simply:

> **Mixer Edit Modes define the current rotary assignment; FLIP can move that assignment onto the faders.**

---

# Track Edit Mode and Mouse-Lite Mixing

Suppose the Vocal needs several adjustments:

```text
slightly quieter

a little left

more delay

less long reverb
```

A screen-oriented workflow may involve moving between several mixer controls.

Track Edit Mode can gather those operations around one physical row.

```text
SELECT Vocal
      ↓
TRACK
      ↓
Volume
Pan
Sends
```

The work becomes centred on the selected track rather than scattered across the screen.

---

# Send Mode and Mix-Wide Thinking

Suppose Send 3 feeds a dub delay.

Select Send 3.

The V-Pots now show:

```text
Kick Delay
Snare Delay
Hat Delay
Bass Delay
Keys Delay
Lead Delay
Vocal Delay
Perc Delay
```

This changes the musical question.

Instead of:

> **How much delay does the Vocal have?**

you can think:

> **How is delay distributed across the whole mix?**

That is one of the strongest reasons for using edit modes that organise the surface by task.

---

# A Practical Track Edit Exercise

Select a track.

Press:

```text
TRACK
```

Observe the eight V-Pot assignments.

With the normal Crossfader configuration, identify:

```text
Volume

Panorama

Crossfader

Send 1

Send 2

Send 3

Send 4

Send 5
```

Turn the controls carefully and watch Bitwig.

Then select another track.

Observe the same physical layout follow the newly selected track.

The aim is to understand:

```text
same parameters
      ↓
different selected track
```

---

# A Practical Six-Send Exercise

If you do not use Bitwig's Crossfader regularly, enable the DrivenByMoss preference that hides the Crossfader from Track Edit Mode.

Return to:

```text
TRACK
```

Observe the changed layout.

You should now have access to:

```text
Volume

Panorama

Send 1

Send 2

Send 3

Send 4

Send 5

Send 6
```

Compare this with the normal layout.

The point is not to decide that one is objectively better.

It is to decide which arrangement better matches your actual projects.

---

# A Practical Send Exercise

Choose a project containing at least one Effect track.

Press:

```text
SEND
```

Use repeated SEND presses or:

```text
SEND + SELECT
```

to choose the desired Send.

Now adjust the Send across several tracks.

Try:

```text
OPTION + Press V-Pot
```

on one of the Send controls.

Observe the Send toggle.

This demonstrates how the edit mode and the V-Pot modifier system work together.

---

# A Practical Perspective Exercise

Try these three modes in sequence:

```text
TRACK

PAN

SEND
```

Ask yourself what question each one makes the surface answer.

For TRACK:

```text
What can I change
about this track?
```

For PAN:

```text
Where are these tracks
in the stereo field?
```

For SEND:

```text
How much are these tracks
feeding this effect?
```

Learning the **question** behind the mode is more useful than memorising the button sequence alone.

---

# The Important Idea

Mixer Edit Modes reorganise the eight V-Pots around different mixing questions.

Track Edit Mode provides multiple controls for one selected track:

```text
Volume

Panorama

Crossfader

Send 1

Send 2

Send 3

Send 4

Send 5
```

DrivenByMoss can optionally hide the Crossfader, changing that layout to:

```text
Volume

Panorama

Send 1

Send 2

Send 3

Send 4

Send 5

Send 6
```

So the configuration choice is:

```text
Crossfader
    versus
Sixth Send
```

The other major mixer perspectives are:

```text
Volume Mode
   → Volume across tracks

Panorama Mode
   → Panorama across tracks

Send Mode
   → One Send across tracks
```

The deeper idea is:

```text
Same Eight V-Pots
       │
       ▼
Different View
of the Mixer
```

Track Edit Mode asks:

> **What can I change about this one track?**

The other edit modes ask:

> **How does one parameter vary across these tracks?**

Once that distinction becomes clear, the mode buttons stop feeling like unrelated mappings.

They become different ways of organising the same physical surface around the task at hand.

---

## Coming Next

Mixer Edit Modes give us different views of track and mixer parameters.

The next chapter moves from mixer state to musical structure.

DrivenByMoss lets the X-Touch work with markers as named destinations in the Arranger, including direct creation and navigation.

Next:

**Markers and Advanced Navigation.**
