---
chapter: 11
title: "Transport Controls"
status: draft
---

# Transport Controls

The Transport section of the X-Touch is one of the most immediately familiar parts of the surface.

It contains controls for:

```text
REWIND

FORWARD

STOP

PLAY

RECORD
```

along with:

```text
Jog Wheel

Arrow Keys

ZOOM

SCRUB

NUDGE
```

At first, these look like ordinary tape-machine controls.

DrivenByMoss makes them considerably more capable.

The basic transport remains simple.

But modifiers and repeated presses add access to:

- Repeat;
- Punch In;
- Punch Out;
- marker navigation;
- tempo;
- loop start;
- loop length;
- fine adjustment;
- editing modes;
- zoom;
- Tap Tempo.

So the Transport area is not merely:

> **Play, Stop and Record.**

It is one of the X-Touch's principal navigation and timing surfaces.

---

# PLAY

Press PLAY to start playback.

DrivenByMoss documents the button as:

```text
PLAY
   → Start / Stop Playback
```

So PLAY behaves as a playback toggle.

If the project is stopped:

```text
PLAY
  ↓
Playback Starts
```

If it is already playing:

```text
PLAY
  ↓
Playback Stops
```

This makes PLAY useful even when your hand is already sitting over the transport area and you do not want to move to STOP.

---

# Double-Press PLAY

DrivenByMoss also documents:

```text
Double-press PLAY
   → Move Play Cursor to Start of Song
```

So PLAY contains two related operations:

```text
Single Press
   → Playback
```

```text
Double Press
   → Start of Song
```

This is useful when beginning another run-through from the very start.

---

# SHIFT + PLAY — Repeat

Hold SHIFT and press PLAY:

```text
SHIFT + PLAY
   → Toggle Repeat
```

This controls Bitwig's repeat state.

Conceptually:

```text
Repeat Off
    │
    │ SHIFT + PLAY
    ▼
Repeat On
```

and the same command toggles it back off.

This is one of the simpler modifier combinations because PLAY and Repeat are both closely related to playback.

---

# OPTION + PLAY — Punch In

DrivenByMoss documents:

```text
OPTION + PLAY
   → Toggle Punch In
```

Punch In determines whether recording begins automatically when playback reaches the configured punch-in boundary.

Conceptually:

```text
Playback
   │
   ▼
Punch-In Point
   │
   ▼
Recording Begins
```

OPTION + PLAY toggles that behaviour.

---

# OPTION + SHIFT + PLAY — Punch Out

Add SHIFT:

```text
OPTION + SHIFT + PLAY
   → Toggle Punch Out
```

Punch Out determines whether recording ends automatically at the configured punch-out boundary.

So the pair is:

```text
OPTION + PLAY
   → Punch In

OPTION + SHIFT + PLAY
   → Punch Out
```

This is a useful example of modifiers building a family of related transport operations.

---

# Punching as a Recording Workflow

Suppose only one phrase needs replacing.

Rather than manually pressing RECORD at exactly the right instant:

```text
Set Punch In
      ↓
Set Punch Out
      ↓
Begin Playback
      ↓
Bitwig Records Only
Inside the Punch Region
```

The X-Touch therefore participates not only in starting recording but in defining how recording interacts with playback.

Chapter 19 deals with recording in more detail.

---

# STOP

Press STOP:

```text
STOP
  ↓
Stop Playback
```

That is the obvious behaviour.

But repeated STOP presses add useful navigation.

DrivenByMoss documents:

```text
STOP
   → Stop Playback
```

then:

```text
Press STOP again
   → Move Play Cursor to Start of Song
```

So after stopping, another press gives you a quick return to the beginning.

---

# Double-Press STOP

There is another STOP gesture:

```text
Double-press STOP
   → Move Play Cursor to End of Song
```

So STOP has three useful roles:

```text
STOP
   → Stop
```

```text
STOP again
   → Start of Song
```

```text
Double STOP
   → End of Song
```

That gives surprisingly rich navigation from one familiar transport button.

---

# REWIND and FORWARD

The ordinary functions are straightforward.

```text
REWIND
   → Move Play Cursor Left
```

```text
FORWARD
   → Move Play Cursor Right
```

These controls move through the Arranger timeline.

Think:

```text
REWIND
   ← time

FORWARD
   time →
```

They provide coarse transport navigation without needing the mouse.

---

# OPTION + REWIND / FORWARD — Marker Navigation

Markers give REWIND and FORWARD another role.

DrivenByMoss documents:

```text
OPTION + REWIND
   → Move to closest marker
     before current position
```

and:

```text
OPTION + FORWARD
   → Move to closest marker
     after current position
```

So the same physical controls provide two kinds of navigation.

Without OPTION:

```text
REWIND / FORWARD
   → Move through Time
```

With OPTION:

```text
OPTION + REWIND / FORWARD
   → Move through Structure
```

That distinction becomes especially useful in large arrangements.

---

# Time Versus Structure

Imagine the timeline contains:

```text
Intro      Verse      Chorus      Breakdown      Outro
  │          │           │            │            │
  ▼          ▼           ▼            ▼            ▼
──●──────────●───────────●────────────●────────────●──
```

Ordinary REWIND and FORWARD ask:

> **How far through time should I move?**

OPTION + REWIND / FORWARD ask:

> **Which musical landmark should I move to?**

That is a very different way of navigating a song.

Chapter 15 explores Marker Mode in detail.

---

# RECORD

Press RECORD:

```text
RECORD
   → Start / Stop Recording
```

This is the main recording command.

But RECORD also has modifier functions:

```text
SHIFT + RECORD
   → Toggle Launcher Overdub
```

and:

```text
OPTION + RECORD
   → Create a new clip
     on selected track and slot,
     start playback,
     enable overdub
```

These are important commands, but Chapter 19 is their proper teaching home.

For now, remember that RECORD is another transport control whose modifiers change the recording context.

---

# The Jog Wheel

The large Jog Wheel is one of the most flexible controls in the Transport section.

Normally:

```text
Jog Wheel
   → Move Play Cursor
```

Turn left:

```text
← earlier
```

Turn right:

```text
later →
```

This is particularly useful for positioning the cursor without dragging the timeline with a mouse.

---

# SHIFT + Jog Wheel — Fine Position

Hold SHIFT:

```text
SHIFT + Jog Wheel
   → Fine Play-Cursor Adjustment
```

So:

```text
Jog Wheel
   → normal movement
```

while:

```text
SHIFT + Jog Wheel
   → finer movement
```

This follows the modifier pattern introduced in Chapter 8.

SHIFT often refines an existing continuous operation.

---

# OPTION + Jog Wheel — Tempo

Hold OPTION:

```text
OPTION + Jog Wheel
   → Change Tempo
```

Now the same wheel no longer moves through the song.

It changes the project's tempo.

Conceptually:

```text
Jog Wheel
   → Time Position
```

becomes:

```text
OPTION + Jog Wheel
   → Tempo
```

The physical gesture remains identical.

The modifier changes what is being controlled.

---

# Fine Tempo Adjustment

Add SHIFT:

```text
OPTION + SHIFT + Jog Wheel
   → Fine Tempo Adjustment
```

So:

```text
OPTION
   → choose Tempo
```

and:

```text
SHIFT
   → make the adjustment finer
```

This is a particularly clean example of two modifiers working together.

---

# CONTROL + Jog Wheel — Loop Start

Hold CONTROL:

```text
CONTROL + Jog Wheel
   → Change Loop Start
```

The wheel now moves the beginning of Bitwig's loop region.

Conceptually:

```text
Loop
┌──────────────────────────┐
│                          │
└──────────────────────────┘
▲
│
Loop Start
```

CONTROL + Jog Wheel moves that left boundary.

---

# Fine Loop-Start Adjustment

Add SHIFT:

```text
CONTROL + SHIFT + Jog Wheel
   → Fine Loop-Start Adjustment
```

Again:

```text
CONTROL
   → choose Loop Start

SHIFT
   → finer adjustment
```

---

# ALT + Jog Wheel — Loop Length

Hold ALT:

```text
ALT + Jog Wheel
   → Change Loop Length
```

Now the wheel changes the size of the loop.

Conceptually:

```text
Short Loop

┌──────┐
│      │
└──────┘
```

versus:

```text
Longer Loop

┌──────────────────────┐
│                      │
└──────────────────────┘
```

The Jog Wheel directly changes that length.

---

# Fine Loop-Length Adjustment

Add SHIFT:

```text
ALT + SHIFT + Jog Wheel
   → Fine Loop-Length Adjustment
```

So the full Jog Wheel map becomes:

```text
Jog Wheel
   → Play Position

SHIFT + Jog Wheel
   → Fine Play Position

OPTION + Jog Wheel
   → Tempo

OPTION + SHIFT + Jog Wheel
   → Fine Tempo

CONTROL + Jog Wheel
   → Loop Start

CONTROL + SHIFT + Jog Wheel
   → Fine Loop Start

ALT + Jog Wheel
   → Loop Length

ALT + SHIFT + Jog Wheel
   → Fine Loop Length
```

That is a great deal of control from one wheel.

---

# One Wheel, Four Dimensions

The Jog Wheel can therefore manipulate four distinct things:

```text
Position

Tempo

Loop Start

Loop Length
```

The modifiers choose the dimension.

SHIFT chooses precision.

Conceptually:

```text
             Jog Wheel
                 │
     ┌───────────┼───────────┐
     │           │           │
  OPTION      CONTROL       ALT
     │           │           │
   Tempo      Loop Start   Loop Length

No Modifier
     │
     ▼
  Position
```

This is one of the clearest demonstrations of DrivenByMoss's modifier design.

---

# The Arrow Keys

The X-Touch includes four directional arrow buttons.

DrivenByMoss documents them as behaving like the arrow keys on the computer keyboard:

```text
←   →   ↑   ↓
```

So they provide direct keyboard-style navigation from the surface.

Their exact effect depends on what currently has focus in Bitwig.

That is important.

The arrows do not necessarily represent one fixed DAW function.

They pass the familiar directional command into the current context.

---

# Why Keyboard-Style Arrows Are Useful

The arrow keys can help with tasks where Bitwig already has keyboard-navigation behaviour.

Conceptually:

```text
Current Bitwig Focus
        │
        ▼
Arrow Press
        │
        ▼
Move / Navigate
according to that focus
```

This is another example of the X-Touch complementing rather than replacing Bitwig's own interaction model.

---

# ZOOM

Press ZOOM to change the meaning of the arrow keys.

When ZOOM is active:

```text
← / →
   → Zoom Arranger Horizontally
```

The horizontal arrows control the timeline scale.

So:

```text
←
   → one horizontal zoom direction
```

```text
→
   → the opposite horizontal zoom direction
```

The precise visual result is shown immediately in Bitwig.

---

# ZOOM and Track Height

DrivenByMoss also documents:

```text
ZOOM active
   +
↑ / ↓
   → Toggle Track Height
```

Both vertical arrows toggle the track height.

So ZOOM changes the arrow-key context from ordinary navigation to display manipulation.

Conceptually:

```text
Arrow Keys
    │
    ├── normal
    │     → keyboard-style navigation
    │
    └── ZOOM active
          ├── left/right
          │     → horizontal zoom
          │
          └── up/down
                → track height
```

---

# Why This Matters

Zooming is a good example of a task that often sends your hand back to the mouse.

DrivenByMoss gives the X-Touch a physical alternative.

If you need to see a broader section of the arrangement:

```text
ZOOM
   ↓
Arrow
```

may be faster than finding and dragging a graphical zoom control.

As always, use whichever interface is more natural for the task.

---

# SCRUB

The X-Touch also has a SCRUB button.

DrivenByMoss documents:

```text
SCRUB
   → Toggle Between Editing Modes
```

This wording is important.

SCRUB is not documented here as simply enabling a traditional tape-style audio scrub mode.

Instead, DrivenByMoss uses the MCU SCRUB button to toggle Bitwig editing modes.

So once again:

> **Trust the DrivenByMoss mapping, not assumptions based only on the printed hardware label.**

---

# Hardware Labels Versus Bitwig Functions

The X-Touch inherits its labels from the Mackie Control design.

That means a button may be labelled:

```text
SCRUB
```

because that is the MCU control being transmitted.

DrivenByMoss is free to map that control to the most useful Bitwig function.

The same principle appears elsewhere with controls such as:

```text
TRIM

DROP

USER
```

So:

```text
Printed Label
      ≠
Guaranteed Literal Bitwig Function
```

The actual DrivenByMoss mapping is what matters.

---

# NUDGE — Tap Tempo

DrivenByMoss maps:

```text
NUDGE
   → Tap Tempo
```

This means repeated presses can establish the project tempo by tapping the beat.

Conceptually:

```text
Tap
Tap
Tap
Tap
```

gives Bitwig timing information from which it can derive tempo.

This can be particularly convenient when trying to match a project to something you are hearing or playing.

---

# Tap Tempo as a Musical Gesture

Instead of thinking:

> **What BPM number should this be?**

you can think:

> **This fast.**

Then tap:

```text
1     2     3     4
●     ●     ●     ●
```

NUDGE turns physical timing into tempo information.

That makes the control rather more musically intuitive than its printed name might suggest.

---

# The REPEAT Button

The dedicated MCU REPEAT control also toggles Repeat.

So DrivenByMoss provides:

```text
REPEAT
   → Toggle Repeat
```

and:

```text
SHIFT + PLAY
   → Toggle Repeat
```

These are two physical routes to the same state.

This kind of redundancy is not necessarily wasteful.

One route may make more sense depending on where your hand currently is.

---

# Multiple Routes Can Be Useful

Suppose your fingers are already around PLAY.

Then:

```text
SHIFT + PLAY
```

may be natural.

If your hand is near REPEAT:

```text
REPEAT
```

may be easier.

A control surface does not need to force every function through one unique route.

Sometimes a second route improves fluency.

---

# Transport Is More Than Playback

At this point, the Transport section can manipulate:

```text
Playback

Recording

Timeline Position

Markers

Repeat

Punch In

Punch Out

Tempo

Loop Start

Loop Length

Zoom

Track Height

Editing Mode

Tap Tempo
```

That is much broader than the word "Transport" initially suggests.

---

# A Navigation Workflow

Suppose you want to move to a chorus marked later in the project.

You could:

```text
OPTION + FORWARD
       ↓
Next Marker
```

If that is the Chorus marker:

```text
PLAY
```

and playback starts from there.

If the cursor needs a small correction:

```text
SHIFT + Jog Wheel
```

gives fine positioning.

The workflow becomes:

```text
Structural Navigation
       ↓
Fine Position
       ↓
Playback
```

all from the Transport area.

---

# A Loop-Editing Workflow

Suppose you want to work repeatedly on one section.

You can:

```text
CONTROL + Jog Wheel
       ↓
Set Loop Start
```

then:

```text
ALT + Jog Wheel
       ↓
Set Loop Length
```

then:

```text
SHIFT + PLAY
       ↓
Enable Repeat
```

Now the section loops.

If either boundary needs fine adjustment:

```text
SHIFT
```

can be added to the corresponding Jog Wheel modifier.

This gives the X-Touch a surprisingly complete loop-positioning workflow.

---

# A Punch-Recording Workflow

Suppose a short section needs rerecording.

Configure the punch region in Bitwig.

Then:

```text
OPTION + PLAY
   → Punch In
```

```text
OPTION + SHIFT + PLAY
   → Punch Out
```

Start playback before the region.

Bitwig can then enter and leave recording according to those boundaries.

This can reduce the need to manually time the RECORD button.

---

# A Tempo Workflow

Suppose you know roughly how fast the song should feel but do not know the BPM.

Start with:

```text
NUDGE
   → Tap Tempo
```

Tap the pulse.

Then use:

```text
OPTION + Jog Wheel
```

to refine the tempo.

If you need very small changes:

```text
OPTION + SHIFT + Jog Wheel
```

gives finer control.

So:

```text
Tap
   ↓
Approximate Tempo
   ↓
Jog
   ↓
Refine
```

is possible entirely from the X-Touch.

---

# Transport and Mouse-Lite Working

Transport is one of the easiest places to reduce dependence on the mouse.

Compare:

```text
Find play cursor
      ↓
Click timeline
      ↓
Find Play button
      ↓
Click
```

with:

```text
Jog Wheel
    ↓
PLAY
```

Or:

```text
Find marker visually
      ↓
Click marker
```

with:

```text
OPTION + FORWARD
```

The hardware route often maps more directly to the intention.

---

# The Transport Area Rewards Muscle Memory

Transport controls are particularly suitable for muscle memory because their physical positions do not change.

After enough use:

```text
PLAY
STOP
RECORD
REWIND
FORWARD
```

become locations rather than commands you have to search for.

The same can gradually become true of:

```text
SHIFT + PLAY

OPTION + PLAY

NUDGE

ZOOM
```

This is where a hardware transport can feel much faster than an on-screen equivalent.

---

# Do Not Learn Every Modifier Immediately

There is a lot in this chapter.

Start with the core:

```text
PLAY
STOP
REWIND
FORWARD
Jog Wheel
```

Then add:

```text
SHIFT + PLAY
   → Repeat
```

Then perhaps:

```text
OPTION + REWIND / FORWARD
   → Markers
```

Then:

```text
OPTION / CONTROL / ALT + Jog Wheel
```

Once the basic Transport area is automatic, the advanced functions have somewhere sensible to attach in memory.

---

# A Practical Transport Exercise

Open a project containing several minutes of material.

### 1. Use PLAY and STOP

Become comfortable starting and stopping without looking at the computer controls.

### 2. Press STOP again

Observe the play cursor return to the beginning.

### 3. Double-press STOP

Observe the play cursor move to the end.

### 4. Use REWIND and FORWARD

Move through the timeline.

### 5. Use the Jog Wheel

Position the cursor.

### 6. Add SHIFT

Make a finer movement.

The goal is to make the transport mechanics physically familiar.

---

# A Practical Jog Wheel Exercise

Now try the four Jog Wheel contexts:

```text
Normal
   → Position

OPTION
   → Tempo

CONTROL
   → Loop Start

ALT
   → Loop Length
```

For each one, add SHIFT and observe the finer adjustment.

This single exercise teaches one of the most reusable modifier patterns on the entire X-Touch.

---

# A Practical Marker Exercise

Add several markers to the project.

Then use:

```text
OPTION + REWIND
```

and:

```text
OPTION + FORWARD
```

to navigate between them.

Compare the experience with manually moving the cursor.

The aim is to feel the difference between:

```text
navigate by time
```

and:

```text
navigate by structure
```

---

# If Transport Behaviour Seems Unexpected

Check the current modifiers and modes.

For example:

```text
Jog Wheel moving tempo?
```

Perhaps OPTION is held.

```text
Arrow keys zooming?
```

Perhaps ZOOM is active.

```text
REWIND jumping to markers?
```

Perhaps OPTION is held.

The hardware is contextual.

Unexpected behaviour often means:

```text
different context
```

rather than:

```text
something is broken
```

---

# A Useful Mental Model

The Transport section can be understood in layers.

## Layer 1 — Basic Transport

```text
PLAY

STOP

REWIND

FORWARD

RECORD
```

## Layer 2 — Navigation

```text
Jog Wheel

Markers

Arrow Keys
```

## Layer 3 — Timing

```text
Repeat

Tempo

Loop Start

Loop Length

Tap Tempo
```

## Layer 4 — Recording Support

```text
Punch In

Punch Out

Overdub
```

## Layer 5 — View / Edit Control

```text
ZOOM

SCRUB
```

The hardware is easier to understand when these operations are grouped by purpose rather than memorised as one long button table.

---

# The Important Idea

The X-Touch Transport section begins with familiar controls:

```text
PLAY

STOP

REWIND

FORWARD

RECORD
```

But DrivenByMoss extends them considerably.

The verified mappings include:

```text
PLAY
   → Start / Stop Playback

Double PLAY
   → Start of Song

SHIFT + PLAY
   → Toggle Repeat

OPTION + PLAY
   → Toggle Punch In

OPTION + SHIFT + PLAY
   → Toggle Punch Out
```

```text
STOP
   → Stop

STOP again
   → Start of Song

Double STOP
   → End of Song
```

```text
REWIND / FORWARD
   → Move through timeline

OPTION + REWIND / FORWARD
   → Previous / Next Marker
```

The Jog Wheel provides:

```text
Normal
   → Position

OPTION
   → Tempo

CONTROL
   → Loop Start

ALT
   → Loop Length

SHIFT
   → Fine adjustment
```

And the remaining controls add:

```text
NUDGE
   → Tap Tempo

SCRUB
   → Toggle Editing Modes

ZOOM + ← / →
   → Horizontal Arranger Zoom

ZOOM + ↑ / ↓
   → Toggle Track Height

Arrow Keys
   → Keyboard-style directional navigation
```

So perhaps the most useful way to think about this area is:

> **Transport controls move not only through playback, but through time, structure and timing.**

Once these controls become familiar, a surprising amount of basic navigation can happen without the mouse.

---

## Coming Next

Transport lets us move around the project and control playback.

The next chapter moves from:

```text
Where are we?
```

to:

```text
What device are we controlling?
```

DrivenByMoss gives the X-Touch a particularly rich Device Mode, including device navigation, parameter pages, direct selection and pinning.

Next:

**Device Mode.**
