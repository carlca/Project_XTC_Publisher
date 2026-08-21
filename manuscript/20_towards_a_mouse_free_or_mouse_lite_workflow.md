---
chapter: 20
title: "Towards a Mouse-Free — or Mouse-Lite — Workflow"
status: draft
---

# Towards a Mouse-Free — or Mouse-Lite — Workflow

We now know a great many things the X-Touch can do.

We can:

- select tracks;
- move through banks;
- control volume, panorama and Sends;
- navigate devices and parameter pages;
- browse for devices and presets;
- work with markers;
- control automation;
- enter Groups, Layers and Drum Pads;
- record and overdub;
- navigate the project.

But knowing a collection of commands is not the same thing as having a **workflow**.

The real question is:

> **Can the X-Touch disappear into the process of making music?**

That is what this chapter is about.

---

# Mouse-Free Is Not the Goal

The phrase *mouse-free* sounds attractive.

It suggests complete command of the DAW from hardware.

But taken literally, it can become a trap.

You may find yourself performing six button presses merely to avoid one easy mouse click.

That is not efficiency.

That is ideology.

So Project XTC prefers another phrase:

> **Mouse-Lite.**

The aim is not to eliminate the mouse.

The aim is to stop reaching for it automatically.

---

## The Mouse Is Still Excellent at Some Things

A mouse or trackpad is extremely good for:

- detailed editing;
- drawing;
- dragging;
- arranging clips visually;
- inspecting complex interfaces;
- operations you perform rarely;
- tasks where the screen itself contains the useful information.

The X-Touch is extremely good for:

- repeated mixer operations;
- simultaneous controls;
- tactile adjustments;
- transport;
- navigation;
- performance;
- automation;
- operations that benefit from muscle memory.

So the useful question is not:

> **Can I do this without the mouse?**

It is:

> **Which tool gives me the shortest and clearest route to what I want?**

---

# Intention Before Control

Throughout this guide, we have gradually moved away from thinking in terms of buttons.

Instead of:

> Which button does what?

we can increasingly think:

> What am I trying to do?

For example:

```text id="e18e7a"
Intention
   │
   ▼
"The vocal needs more delay"
   │
   ▼
Find vocal
   │
   ▼
Select Send
   │
   ▼
Turn V-Pot
```

The hardware becomes a route from intention to result.

That is the real goal.

---

# A Working Vocabulary

By now, a relatively small set of concepts explains a large proportion of the controller.

```text id="wn4d3a"
SELECT
   → establish focus

BANK / CHANNEL
   → move the window

MODE
   → change what the controls represent

MODIFIER
   → temporarily extend a control

V-POT
   → adjust the current parameter

FADER
   → make a continuous physical adjustment

DISPLAY
   → tell us what the controls currently mean
```

And hierarchical navigation adds:

```text id="wz74xj"
SELECT again
   → enter, where appropriate

Long-press SELECT
   → leave
```

This vocabulary matters more than memorising hundreds of isolated commands.

---

# Observe Before You Adjust

The X-Touch is contextual.

A V-Pot may control:

```text id="6n7n7a"
Pan
```

then:

```text id="bd0lpo"
Send level
```

then:

```text id="npxo9q"
Device parameter
```

then:

```text id="opdqqv"
Drum Pad level
```

then:

```text id="sajc4u"
Master panorama
```

The physical control has not changed.

Its meaning has.

So before turning something:

> **Look at the feedback.**

This simple habit prevents a large proportion of control-surface mistakes.

---

# A Three-Step Habit

A useful general workflow is:

```text id="w4wdbe"
1. Establish focus

2. Establish mode

3. Adjust
```

For example:

```text id="4c8a3p"
Select Bass
    ↓
SEND
    ↓
Turn V-Pot
```

Or:

```text id="r3sk9d"
Select Synth
    ↓
DEVICE
    ↓
Turn parameter V-Pot
```

Or:

```text id="5t1kyd"
Select Drums
    ↓
SELECT again
    ↓
Work inside Group
```

Once that sequence becomes habitual, the X-Touch feels far less complicated.

---

# Navigation Without Losing the Plot

Large projects create a particular problem.

It is easy to lose track of:

> **Where am I?**

The X-Touch may currently represent:

- top-level tracks;
- tracks inside a Group;
- Layers;
- Drum Pads;
- Device parameters;
- Sends;
- Master controls.

So Mouse-Lite working depends on having a reliable mental route back.

---

## Hierarchical Navigation

With hierarchical Track navigation, the verified Group workflow is:

```text id="brpj55"
SELECT Group
      ↓
Group selected
      ↓
SELECT same Group again
      ↓
Enter Group
      ↓
Long-press any SELECT
      ↓
Leave Group
```

Layers and Drum Pads follow the same broad idea:

```text id="05r7hz"
SELECT containing track
       ↓
SELECT same track again
       ↓
Enter Layers / Drum Pads
       ↓
Long-press any SELECT
       ↓
Leave
```

This gives us a compact navigation vocabulary:

```text id="1l9xmf"
SELECT
   → focus

SELECT again
   → descend

Long SELECT
   → ascend
```

---

## Don't Use ENTER and CANCEL for Hierarchy

ENTER and CANCEL are useful X-Touch controls, but they are not the Group-navigation pair.

Their particularly important role is in Browser Mode:

```text id="35vv9o"
ENTER
   → confirm Browser selection

CANCEL
   → discard Browser selection
```

So when navigating project hierarchy, keep the mental model centred on SELECT.

When browsing, ENTER and CANCEL regain their obvious confirm/cancel roles.

This separation makes both workflows easier to remember.

---

# Work at the Highest Useful Level

Suppose the drums are too loud.

There are several possible responses.

You could enter the Drums Group, adjust the kick, snare, hats and percussion individually, then rebalance everything.

Or:

```text id="9sv6o6"
Drums Group
     │
     ▼
Lower Group fader
```

If that solves the problem, stop there.

A useful rule is:

> **Work at the highest level that solves the musical problem.**

Only descend into detail when the problem itself is detailed.

---

# Banks Are Not an Obstacle

An eight-channel controller cannot show a forty-track project simultaneously.

That does not mean it cannot control one efficiently.

Think of the X-Touch as a window:

```text id="y2e6qh"
Project
──────────────────────────────────────────

        ┌────────────────┐
        │ eight channels │
        └────────────────┘
```

BANK moves the window by eight.

CHANNEL moves it by one.

Hierarchy changes the level at which the window is looking.

Together:

```text id="m45zg9"
BANK
   → move widely

CHANNEL
   → move precisely

SELECT again
   → move deeper

Long SELECT
   → move outward
```

That is a surprisingly capable navigation system.

---

# Keep Related Tracks Together

The controller becomes easier to use when the Bitwig project itself has a sensible structure.

For example:

```text id="aqynk4"
Drums
Bass
Guitars
Keys
Vocals
FX
```

is easier to navigate than a project whose tracks are scattered arbitrarily.

Hardware workflow and project organisation reinforce one another.

A well-organised Bitwig project makes the X-Touch feel more intelligent.

A chaotic project makes the controller work harder.

---

# Use Groups as Navigation Landmarks

Groups are not only useful for audio routing.

They can become landmarks.

For example:

```text id="n7i7by"
Project
   │
   ├── Rhythm
   ├── Instruments
   ├── Vocals
   └── FX
```

With hierarchical navigation, those top-level Groups form a compact map of the project.

Enter only the area you currently need.

This can be much easier than continually banking through a long flat list of tracks.

---

# Device Work Without Hunting

Suppose you want to change a synthesizer parameter.

A screen-first workflow might be:

```text id="63sosx"
find track
   ↓
click track
   ↓
find device
   ↓
click device
   ↓
find parameter
   ↓
drag parameter
```

With a familiar X-Touch workflow:

```text id="k8l0t8"
SELECT track
    ↓
DEVICE
    ↓
choose device / page
    ↓
turn V-Pot
```

In Device Mode:

```text id="6m5z91"
BANK ← / →
   → previous / next device

CHANNEL ← / →
   → previous / next parameter page
```

And the modifiers give us faster direct selection:

```text id="e32y9j"
Hold CONTROL
   → display devices
   → press V-Pot to choose one

Hold OPTION
   → display parameter pages
   → press V-Pot to choose one
```

The aim is not to avoid looking at the device forever.

It is to make routine parameter work available physically.

---

# Pin What Matters

DrivenByMoss provides:

```text id="ut8mkg"
OPTION + TRACK
   → Pin cursor track

OPTION + DEVICE
   → Pin cursor device
```

Pinning can be useful when you want the controller's focus to remain attached to something while other activity happens in Bitwig.

This is another Mouse-Lite principle:

> **If the thing you care about keeps moving away, pin it rather than repeatedly finding it again.**

---

# Mixing by Ear

The X-Touch becomes particularly valuable when the screen is no longer the centre of attention.

Try balancing several tracks while deliberately looking away from Bitwig.

Use the faders.

Listen.

Then look back.

This exercise reveals something important.

With a mouse, mixing can easily become:

```text id="onh8i7"
look
  ↓
move
  ↓
look
  ↓
move
```

With physical faders:

```text id="27aaxc"
listen
   ↓
move
   ↓
listen
```

That is a different relationship with the music.

---

# More Than One Control at Once

A mouse pointer controls one thing at a time.

Your hands do not have that limitation.

For example:

```text id="pyqwyf"
Left hand
   → Vocal fader

Right hand
   → Delay return fader
```

or:

```text id="g9yr3s"
Finger 1
   → Kick

Finger 2
   → Bass
```

This is one of the strongest arguments for a physical mixing surface.

The advantage is not merely that a fader is nicer than a mouse.

It is that **several physical controls can be part of one gesture**.

---

# FLIP When the Fader Is the Better Instrument

Sometimes a parameter normally lives on a V-Pot but would be easier to perform with a fader.

That is where FLIP becomes useful.

Conceptually:

```text id="5n86mp"
Parameter on V-Pot
       │
       ▼
      FLIP
       │
       ▼
Parameter on Fader
```

The fader gives you:

- longer travel;
- touch sensitivity;
- motorised feedback;
- a different physical gesture.

For automation or expressive Send rides, this can be much more natural.

---

# Automation as Performance

With a mouse, automation often means drawing.

With the X-Touch it can mean performing.

```text id="oqk1iy"
Listen
  ↓
Touch fader
  ↓
Move
  ↓
Release
  ↓
Listen back
```

In TOUCH mode, the automation can return to the existing behaviour after you release the fader.

In LATCH, the new value continues.

So instead of thinking:

> **I need to edit the automation curve.**

you can sometimes think:

> **I need to play this movement.**

---

# Recording Without Breaking the Performance

Recording is another area where physical controls can preserve musical attention.

A normal recording workflow might be:

```text id="23cfpf"
SELECT track
     ↓
ARM
     ↓
RECORD
     ↓
perform
     ↓
STOP
```

For Launcher-oriented loop building:

```text id="5kzeyb"
Select track / slot
       ↓
Choose New Clip Length
       ↓
OPTION + RECORD
       ↓
New clip created
       ↓
Playback starts
       ↓
Overdub enabled
       ↓
Perform
```

The point is not that the X-Touch magically creates the performance.

It removes some of the software-management interruption surrounding it.

---

# Markers as Musical Landmarks

Markers are another powerful Mouse-Lite tool.

Instead of dragging the play cursor around a long arrangement, use meaningful locations.

For example:

```text id="90r5xv"
Intro

Verse

Chorus

Breakdown

Outro
```

DrivenByMoss provides:

```text id="d3l8oc"
OPTION + MARKER
   → Insert marker at current play position

OPTION + REWIND
   → Previous marker

OPTION + FORWARD
   → Next marker
```

And Marker Mode allows the V-Pots to start playback from marker positions.

Markers turn a long timeline into a set of named musical destinations.

---

# A Practical Mixing Session

Let's put several ideas together.

Imagine a project containing:

```text id="mmh9bm"
Drums
Bass
Skank Guitar
Organ
Percussion
Lead
Vocal
FX
```

You press PLAY.

The mix begins.

---

## The Bass Is Too Loud

Your hand goes directly to the Bass fader.

```text id="h4s8xy"
Bass too loud
    ↓
Bass fader
    ↓
lower
```

No menu.

No cursor.

No visual search.

---

## The Vocal Needs More Delay

Select the Vocal track.

Enter the appropriate Send context.

Turn the V-Pot.

```text id="q9w0ao"
SELECT Vocal
     ↓
SEND
     ↓
choose delay Send
     ↓
turn
```

Listen to the result.

---

## The Delay Needs a Performance Ride

Perhaps a simple static Send level is not enough.

You want the final word of the phrase to explode into delay.

Use FLIP if appropriate to place the Send on a fader.

Then perform the movement.

```text id="et1mkv"
phrase plays
    ↓
raise Send
    ↓
word hits delay
    ↓
pull Send back
```

That is not merely editing.

It is mixing as performance.

---

# A Dub-Oriented Example

This becomes especially interesting in dub.

A traditional dub mix treats the mixer almost like an instrument.

Channels disappear.

Echoes appear.

Reverb blooms.

Elements are dropped and returned.

The X-Touch is well suited to this because the physical controls encourage exactly that kind of interaction.

---

## Start with a Stable Mix

Imagine:

```text id="jpn3jg"
1   Drums
2   Bass
3   Skank
4   Organ
5   Percussion
6   Vocal
7   FX Return 1
8   FX Return 2
```

First establish a sensible balance.

The point is to have a stable place from which to perform.

---

## Drop the Vocal

At the end of a phrase:

```text id="kyq9p1"
Vocal
  ↓
MUTE
```

The space suddenly opens.

---

## Throw the Last Word into Delay

Before muting or dropping the vocal, increase its delay Send.

```text id="g40jhe"
Vocal Send
    ↑
last word
    ↓
delay repeats
```

Then bring the Send back.

The echo continues while the dry vocal disappears.

That is a classic dub gesture.

---

## Ride the Return

The effect return itself can be treated dynamically.

```text id="0q6b1e"
Delay Return
     │
     ├── raise
     ├── lower
     ├── mute
     └── return
```

The effect becomes part of the performance rather than a static processor.

---

## Work with Several Controls

One hand might ride the vocal Send.

The other might ride the effect return.

```text id="kefix0"
Left hand
   → Vocal Send

Right hand
   → Delay Return
```

That interaction is extremely awkward with one mouse pointer.

With physical controls it is natural.

---

# Groups Make Performance Mixes Manageable

Suppose the project is larger than eight tracks.

Create meaningful Groups:

```text id="8jlh0r"
Drums
Bass
Instruments
Vocals
FX
```

At the top level, those Groups become performance landmarks.

If the whole drum section needs changing:

```text id="9nd14m"
Drums Group fader
```

may be enough.

If the snare needs changing:

```text id="9slkbb"
SELECT Drums
     ↓
SELECT Drums again
     ↓
find Snare
     ↓
adjust
```

Then long-press SELECT to leave the Group.

The hierarchy follows the level of musical attention.

---

# Drum Machines Can Become Performance Mixers

A Drum Machine can itself become a physical submixer.

Select the containing track.

Press SELECT again to enter its Drum Pads.

Now the channel strips may represent:

```text id="71dskf"
Kick
Snare
Hat
Clap
Perc
Rim
Shaker
Tamb
```

You can now:

- mute individual elements;
- solo them;
- change levels;
- change panorama;
- adjust Sends.

This can turn a single Bitwig track into a surprisingly tactile performance environment.

---

# Don't Forget the Displays

In a fast performance workflow, the danger is assuming.

You think Channel 4 is still the Organ.

But perhaps you entered a Group.

Or changed bank.

Or switched mode.

Now Channel 4 means something else.

So develop a glance habit:

```text id="3z3jjo"
Intention
   ↓
quick glance
   ↓
physical action
```

Not:

```text id="3b87on"
physical action
   ↓
"Oh."
```

The displays are there to keep the contextual surface understandable.

---

# Use the Screen for Confirmation, Not Permission

A mature Mouse-Lite workflow often changes the role of the computer display.

Initially:

```text id="4id8ra"
Look at screen
     ↓
decide
     ↓
act
```

Later:

```text id="2wsovl"
hear / decide
     ↓
act physically
     ↓
glance if confirmation is useful
```

The screen remains important.

It simply stops being the starting point for every operation.

---

# Learn the Surface in Layers

Do not try to become Mouse-Lite by memorising the entire manual.

Build the workflow gradually.

A useful progression is:

```text id="otcttu"
Transport
    ↓
Volume
    ↓
Pan
    ↓
Mute / Solo
    ↓
Banks
    ↓
Sends
    ↓
Devices
    ↓
Modifiers
    ↓
Markers
    ↓
Hierarchy
    ↓
Automation
    ↓
Recording
```

At each stage, use the physical control until it becomes automatic.

Then add another layer.

---

# Muscle Memory Is the Real Upgrade

The X-Touch becomes faster not because its buttons change.

It becomes faster because **you stop thinking about them**.

At first:

```text id="b2gqkh"
I want Send 2
      ↓
Which button?
      ↓
Which mode?
      ↓
Which knob?
```

Later:

```text id="9n67mu"
I want more delay
      ↓
hand moves
```

That is the transition we are aiming for.

---

# Do Not Optimise Rare Tasks

Suppose you perform an operation once every six months.

You discover that it can technically be achieved through:

```text id="94azpz"
modifier
   +
mode
   +
three button presses
   +
V-Pot
```

but you cannot remember the sequence.

Use the mouse.

There is no failure in that.

Hardware shortcuts earn their value through repetition.

A useful rule is:

> **The more often you perform something, the more valuable a physical workflow becomes.**

---

# Use Customisation to Remove Repeated Friction

Later, Chapter 22 will look at assignable controls.

The principle is simple.

Do not customise because a button is available.

Customise because you repeatedly encounter this:

```text id="phbh29"
intention
   ↓
awkward route
   ↓
same awkward route
   ↓
same awkward route
```

Then a custom control can turn it into:

```text id="v8mykd"
intention
   ↓
button
```

Customisation should simplify an established workflow, not replace the process of learning one.

---

# A Mouse-Lite Test

Try working for ten minutes with one rule:

> **Do not reach for the mouse immediately.**

When you want to do something, ask:

```text id="xj6hde"
Do I know the X-Touch route?
       │
       ├── yes → use it
       │
       └── no
            │
            ▼
Would learning it be useful?
       │
       ├── yes → find out
       │
       └── no  → use mouse
```

This avoids both extremes.

You are neither mouse-dependent nor hardware-dogmatic.

---

# The Mouse-Lite Loop

Over time, the process becomes:

```text id="as0ry7"
Intention
    ↓
Do I know a direct physical route?
    │
    ├── Yes
    │    ↓
    │   X-Touch
    │
    └── No
         ↓
   Is this operation frequent?
         │
         ├── Yes → learn / customise
         │
         └── No  → mouse
```

That is a sustainable workflow.

---

# A Controller Should Reduce Thought

This may sound paradoxical after a guide containing twenty chapters.

But the purpose of learning the controller is eventually to think about it **less**.

At first:

```text id="pzg4po"
hardware
   ↓
thinking
   ↓
music
```

Eventually:

```text id="4jqf4n"
intention
   ↓
movement
   ↓
music
```

The hardware disappears from conscious attention.

That is when it becomes useful.

---

# What Should Stay on the Screen?

Even in a strongly hardware-oriented workflow, the screen remains excellent for information that is fundamentally visual.

For example:

- waveform editing;
- piano-roll editing;
- arrangement structure;
- automation detail;
- plugin interfaces;
- complex routing;
- naming;
- file management.

The X-Touch does not need to replace these things.

It complements them.

---

# What Should Move to the Surface?

Operations that benefit particularly from hardware include:

- transport;
- volume;
- panorama;
- Sends;
- Mute and Solo;
- track selection;
- bank navigation;
- device parameters;
- automation performance;
- marker navigation;
- recording;
- repeated performance actions.

These are operations where physical location and muscle memory can outperform pointing and clicking.

---

# The Screen and Surface Are Partners

The most productive model is therefore not:

```text id="tkc91p"
X-Touch
   VS
Mouse
```

It is:

```text id="a9qjdg"
            You
           /   \
          /     \
     X-Touch    Screen
          \     /
           \   /
           Bitwig
```

Each interface does the work it is best suited to.

The skill lies in moving naturally between them.

---

# A Complete Example

Imagine you are working on a song.

You want to:

1. move to the chorus;
2. lower the bass slightly;
3. add delay to the vocal;
4. adjust a synth parameter;
5. ride the vocal level;
6. record another percussion layer.

A Mouse-Lite workflow might be:

```text id="0k4mjc"
Marker navigation
      ↓
Chorus
      ↓
Bass fader
      ↓
SELECT Vocal
      ↓
SEND
      ↓
adjust delay
      ↓
SELECT Synth
      ↓
DEVICE
      ↓
adjust parameter
      ↓
SELECT Vocal
      ↓
TOUCH automation
      ↓
perform fader ride
      ↓
SELECT percussion track / slot
      ↓
OPTION + RECORD
      ↓
perform overdub
```

The mouse may not be needed.

But if you then decide to redraw one MIDI note:

```text id="s11uww"
use the mouse
```

That is exactly what Mouse-Lite means.

---

# Fluency Beats Purity

The best X-Touch workflow is not the one with the fewest mouse clicks.

It is the one with the least unnecessary friction.

Sometimes that means:

```text id="ykpx4d"
fader
```

Sometimes:

```text id="84opbi"
V-Pot
```

Sometimes:

```text id="d7pvbe"
button
```

Sometimes:

```text id="bhq3pd"
mouse
```

The important thing is that the choice becomes deliberate rather than habitual.

---

# The Important Idea

A control surface becomes powerful when you stop thinking of it as a collection of features.

Think instead in terms of musical intentions:

```text id="r40cye"
"That is too loud."

"That needs more delay."

"Take me to the chorus."

"Open the synth."

"Let me ride this level."

"Record another layer."

"Show me the snare."
```

Then let the X-Touch provide the physical route.

The recurring model is:

```text id="qfssy7"
Intention
    │
    ▼
Focus
    │
    ▼
Context / Mode
    │
    ▼
Physical Action
    │
    ▼
Musical Result
```

And when another interface is genuinely better:

```text id="a1r7c2"
use it
```

Mouse-Lite is not a restriction.

It is the freedom to choose the right interface without automatically defaulting to the mouse.

---

## Coming Next

The workflow is becoming increasingly physical.

But much of that fluency depends on how DrivenByMoss itself is configured.

Choices such as:

- Flat or Hierarchical track navigation;
- New Clip Length;
- fader-touch behaviour;
- startup mode;
- Arranger versus Launcher priority;
- knob sensitivity;

can change how the controller behaves.

So before customising individual buttons, we should make sure the underlying system is configured deliberately.

Next:

**Configuring DrivenByMoss for the X-Touch.**
