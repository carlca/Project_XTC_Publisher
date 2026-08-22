---
chapter: 10
title: "Motor Faders"
status: draft
---

# Motor Faders

The eight channel faders are probably the most immediately impressive part of the X-Touch.

They are:

- touch-sensitive;
- motorised;
- capable of receiving position information from Bitwig;
- able to represent different tracks as the controller changes bank.

The Master fader provides the same physical style of control for the master channel.

But the motorisation is not merely a visual effect.

It solves one of the fundamental problems of a controller whose physical controls can represent many different things.

---

# A Fader Has Two Jobs

A normal MIDI fader sends information in one direction:

```text
Move Fader
    │
    ▼
Software Changes
```

A motor fader adds the return journey:

```text
Software Changes
      │
      ▼
Fader Moves
```

So the complete relationship becomes:

```text
Physical Fader
      ⇅
Bitwig Parameter
```

The fader is both:

```text
Input
```

and:

```text
Feedback
```

This is one of the defining features of the X-Touch.

---

# Why Motorisation Matters

Suppose Track 1 is at:

```text
-3 dB
```

and Track 9 is at:

```text
-14 dB
```

The first physical fader may represent Track 1.

Press:

```text
BANK >
```

and that same physical fader may now represent Track 9.

Without motorisation, its physical position would still show Track 1's old value.

With motorisation:

```text
BANK >
   │
   ▼
Track Assignment Changes
   │
   ▼
Bitwig Sends New Value
   │
   ▼
Fader Moves to -14 dB
```

The hardware immediately reflects the new context.

---

# The Faders Follow the Track Bank

In normal mixer operation:

```text
Fader 1  → Track 1
Fader 2  → Track 2
Fader 3  → Track 3
...
Fader 8  → Track 8
```

Change bank:

```text
BANK >
```

and the mapping becomes:

```text
Fader 1  → Track 9
Fader 2  → Track 10
Fader 3  → Track 11
...
Fader 8  → Track 16
```

The faders move automatically to the values of those newly represented tracks.

This is why eight physical faders can control a much larger project without losing positional feedback.

---

# CHANNEL Movement Also Updates the Faders

CHANNEL movement shifts the eight-track window by one track.

For example:

```text
Tracks 1–8
```

then:

```text
CHANNEL >
```

gives:

```text
Tracks 2–9
```

Each physical fader may therefore acquire a new track assignment.

Again, the motors move to reflect the new values.

The sequence is:

```text
Change Controller Window
        ↓
Assignments Change
        ↓
Faders Reposition
```

This should become so normal that you barely notice it happening.

---

# Do Not Fight the Motors

When changing banks or modes, the faders may move by themselves.

That is expected.

Do not hold them in place while they are repositioning.

Let the surface update.

Think:

```text
Motor Movement
   → Feedback
```

not:

```text
Motor Movement
   → Something has gone wrong
```

The movement is the controller telling you:

> **These are the current values for the things I now represent.**

---

# Touch Sensitivity

The faders know when you touch them.

This is different from merely detecting movement.

Conceptually:

```text
Finger Touches Fader
        ↓
Touch State
        ↓
DrivenByMoss / Bitwig
```

That touch information can be useful for:

- track-selection behaviour;
- automation;
- temporary controller-mode behaviour.

Exactly what happens on fader touch can depend on the DrivenByMoss preferences.

We will examine those options in Chapter 21.

---

# Fader Touch Can Select the Track

DrivenByMoss can be configured so that touching a fader selects its corresponding track.

With that preference enabled:

```text
Touch Fader
     ↓
Track Selected
```

This can make mixing very fluid.

Instead of:

```text
SELECT
   ↓
Move Fader
```

you may simply:

```text
Touch Fader
     ↓
Adjust
```

But this behaviour is configurable.

Do not assume that touching a fader must always change the selected track.

---

# Why Touch-to-Select Can Be Useful

Suppose you hear that the Vocal is too loud.

Your hand goes naturally to the Vocal fader.

With touch selection enabled:

```text
Touch Vocal Fader
        ↓
Vocal Selected
        ↓
Move Fader
```

The physical action of reaching for the channel also establishes controller focus.

That can be very efficient.

---

# Why Touch-to-Select Can Be Unwanted

Suppose the Synth track is selected because you are editing one of its devices.

At the same time, you want to reduce the Vocal level.

If touching the Vocal fader automatically selects Vocal:

```text
Synth Device Context
        ↓
Touch Vocal Fader
        ↓
Selection Changes
```

that may interrupt the workflow.

So DrivenByMoss makes this behaviour optional.

The important lesson is:

> **Fader touch is information. What DrivenByMoss does with that information can be configured.**

---

# The Master Fader

The Master fader is separate from the eight channel-strip faders.

In normal operation it provides direct access to the master level.

Conceptually:

```text
Channel Faders
   → Track Levels

Master Fader
   → Master Level
```

Unlike the eight channel faders, the Master fader does not normally move through the track bank.

It remains a stable physical destination for the overall output level.

That consistency makes it especially useful.

---

# SHIFT + Master Fader — Metronome Volume

DrivenByMoss also gives the Master fader a modified function.

Hold:

```text
SHIFT
```

while moving the Master fader.

The fader controls:

```text
Metronome Volume
```

So:

```text
Master Fader
   → Master Volume
```

while:

```text
SHIFT + Master Fader
   → Metronome Volume
```

This is a useful example of a modifier temporarily changing the meaning of an otherwise stable physical control.

---

# Why Metronome Volume Belongs on a Fader

Metronome level is the sort of value you may want to change quickly while recording.

You might think:

```text
I need the click louder.
```

or:

```text
The click is distracting me.
```

Instead of opening a software control:

```text
SHIFT
   +
Master Fader
```

provides an immediate physical adjustment.

Release SHIFT and the Master fader returns to its normal role.

---

# Faders and Automation

Touch sensitivity becomes especially important during automation.

Imagine writing a volume movement.

```text
Touch Fader
     ↓
Move Fader
     ↓
Automation Written
     ↓
Release Fader
```

The system knows not merely that the value changed, but also when your hand took control and when it released control.

This allows automation modes such as Touch and Latch to behave in musically useful ways.

We will explore those modes properly in Chapter 16.

---

# Motorised Automation Playback

Motorisation makes automation visible and physical.

Suppose a track contains volume automation.

During playback:

```text
Automation Data
      ↓
Bitwig Volume
      ↓
X-Touch Motor
      ↓
Fader Moves
```

You can literally watch the mix being performed.

This is not merely entertaining.

It tells you:

```text
where the automated value currently is
```

before you decide whether to touch the fader and intervene.

---

# The Fader Is a Moving Value Display

This leads to an important idea.

A motor fader is effectively a physical meter for a parameter.

For example:

```text
Low Position
   → Lower Value

High Position
   → Higher Value
```

When Bitwig changes the value, the display moves.

When you change the display, Bitwig changes the value.

So the distinction between:

```text
control
```

and:

```text
display
```

almost disappears.

---

# FLIP

The X-Touch includes a:

```text
FLIP
```

button.

FLIP exchanges or redirects assignments between the V-Pots and faders according to the current mode.

Conceptually:

```text
Before FLIP

V-Pots
   → Current Rotary Assignment

Faders
   → Track Volume
```

then:

```text
FLIP
```

and the current rotary assignment can move to the faders.

The exact result depends on the active controller context.

---

# Why FLIP Is Powerful

Some parameters are naturally comfortable on a rotary encoder.

Others benefit from the long physical travel of a fader.

Suppose a V-Pot currently controls:

```text
Send Level
```

FLIP can put that assignment onto the fader.

Instead of:

```text
Turn Encoder
```

you can use:

```text
Move Long-Throw Fader
```

This gives you:

- more physical travel;
- a visible position;
- touch sensitivity;
- motorised feedback.

---

# FLIP Does Not Mean One Fixed Assignment

It is important not to memorise FLIP as:

> **Faders become Sends.**

That may be what happens in one context.

In another context, the V-Pots may represent:

```text
Pan
```

or:

```text
Device Parameters
```

or another assignment.

The more useful rule is:

> **FLIP moves the current rotary-control relationship onto the faders.**

So always ask:

```text
What are the V-Pots controlling now?
```

before asking:

```text
What will FLIP do?
```

---

# FLIP in Send Mode

Suppose the V-Pots are controlling Send levels.

Normally:

```text
V-Pots
   → Sends

Faders
   → Track Volumes
```

Press:

```text
FLIP
```

and the Send assignments can be brought onto the faders.

Conceptually:

```text
Send 1
Send 2
Send 3
...
```

become physically performable with the motor faders.

This can be especially useful for effects-heavy mixing.

---

# FLIP in Device Mode

FLIP becomes even more interesting in Device Mode.

Suppose the eight V-Pots currently control:

```text
Cutoff
Resonance
Drive
Mix
Attack
Release
Feedback
Tone
```

Press:

```text
FLIP
```

and those assignments can be moved onto the faders.

A parameter such as:

```text
Filter Cutoff
```

can now be performed with a long physical gesture.

For some parameters this feels much more expressive than turning an encoder.

---

# FLIP Changes the Physical Character of a Parameter

This is worth emphasising.

FLIP does not merely move a parameter from one control to another.

It changes how that parameter feels.

Compare:

```text
Encoder
   → compact rotary gesture
```

with:

```text
Fader
   → long linear gesture
```

The software parameter may be identical.

The physical interaction is not.

That can matter when the controller is being used performatively.

---

# SHIFT + FLIP — Normal Tracks and Effect Tracks

FLIP itself changes the relationship between the V-Pots and faders.

DrivenByMoss also gives the FLIP button a second function when used with SHIFT.

Press:

```text
SHIFT + FLIP
```

to toggle the track bank between:

```text
Instrument / Audio / Hybrid Tracks
```

and:

```text
Effect Tracks
```

Conceptually:

```text
Instrument / Audio / Hybrid Tracks
              │
              │ SHIFT + FLIP
              ▼
         Effect Tracks
              │
              │ SHIFT + FLIP
              ▼
Instrument / Audio / Hybrid Tracks
```

This is not the same operation as FLIP by itself.

---

# FLIP and SHIFT + FLIP Do Different Jobs

The distinction is important.

Press:

```text
FLIP
```

and you change **which physical controls operate the current assignments**.

For example:

```text
V-Pot Assignment
       │
       ▼
     Fader
```

But press:

```text
SHIFT + FLIP
```

and you change **which kind of tracks appear in the track bank**.

So:

```text
FLIP
   → Change Control Assignment
```

while:

```text
SHIFT + FLIP
   → Change Track-Bank Type
```

The two operations share a button, but they work at completely different levels.

---

# Why Effect-Track Access Is Useful

Effect tracks often sit slightly outside the main flow of ordinary track navigation.

But when mixing, they can be extremely important.

A project might contain ordinary tracks such as:

```text
Kick
Snare
Bass
Keys
Vocal
Guitar
```

and separate Effect tracks such as:

```text
Room
Plate
Dub Delay
Long Reverb
```

Press:

```text
SHIFT + FLIP
```

and the X-Touch can move its attention from the Instrument / Audio / Hybrid track bank to the Effect tracks.

That gives you direct physical access to the returns that shape the mix.

---

# A Particularly Useful Mixing Workflow

Suppose the eight channel strips currently represent:

```text
Kick   Snare   Hats   Bass   Keys   Gtr   Vox   Perc
```

You are happy with their levels, but now want to adjust the Effect tracks themselves.

Press:

```text
SHIFT + FLIP
```

The track bank changes to the Effect tracks.

You can now work directly with controls such as:

```text
Room

Plate

Delay

Reverb
```

When finished:

```text
SHIFT + FLIP
```

returns to the Instrument / Audio / Hybrid track bank.

So the workflow becomes:

```text
Mix Source Tracks
       ↓
SHIFT + FLIP
       ↓
Mix Effect Tracks
       ↓
SHIFT + FLIP
       ↓
Return to Source Tracks
```

This can be considerably faster than navigating through a large project to find the Effect tracks manually.

---

# Don't Confuse This with Send Mode

There is an important distinction between:

```text
SEND
```

and:

```text
SHIFT + FLIP
```

SEND lets you control:

> **How much of a source track is being sent to an effect.**

SHIFT + FLIP lets you reach:

> **The Effect track receiving those sends.**

Conceptually:

```text
Source Track
     │
     │ SEND
     ▼
Send Amount
     │
     ▼
Effect Track
     │
     │ SHIFT + FLIP
     ▼
Effect Track Controls
```

These are two sides of the same signal-flow relationship.

---

# Source and Destination

Suppose a Vocal is feeding a Delay Effect track.

To change how much Vocal reaches the delay:

```text
Select Vocal
     ↓
SEND
     ↓
Adjust Send Level
```

To change the level or other track-level properties of the Delay Effect track itself:

```text
SHIFT + FLIP
      ↓
Find Delay Effect Track
      ↓
Adjust
```

Think:

```text
SEND
   → source side
```

```text
SHIFT + FLIP
   → destination side
```

That mental model makes the two workflows much easier to distinguish.

---

# Returning from FLIP

Press FLIP again to return the controls to their normal relationship.

Conceptually:

```text
Normal
   ↓
FLIP
   ↓
Flipped
   ↓
FLIP
   ↓
Normal
```

The faders then return to the values appropriate to their normal assignment.

Again, let the motors move.

Their movement is feedback.

---

# FLIP and Motor Recall

Motorisation is particularly important when using FLIP.

Suppose a fader normally represents:

```text
Track Volume = -8 dB
```

You press FLIP and it now represents:

```text
Send Level = -20 dB
```

The motor moves.

Press FLIP again.

The fader returns to:

```text
Track Volume = -8 dB
```

Without motorisation, the physical position would become meaningless every time the assignment changed.

With motorisation, the hardware follows the context.

---

# Do Not Assume the Fader Still Means Volume

This is one of the most important safety habits around FLIP.

After pressing FLIP:

> **Do not assume that moving a fader changes track volume.**

Read the display.

Check the active mode.

Then move the control.

The sequence should be:

```text
Change Context
      ↓
Read Feedback
      ↓
Understand Assignment
      ↓
Move Fader
```

This is the same principle we introduced in Chapter 7.

---

# Faders as Performance Controls

Motor faders become especially interesting when the X-Touch is treated as an instrument rather than merely a mixer.

Imagine several effect parameters assigned to the faders:

```text
Delay Send

Reverb Send

Filter Cutoff

Feedback

Effect Mix
```

Now several parameters can be moved simultaneously with multiple fingers.

That is difficult to reproduce with a mouse.

The controller becomes a performance surface.

---

# Multiple Faders at Once

One of the great advantages of physical controls is simultaneity.

A mouse generally manipulates one parameter at a time.

With faders you can:

```text
Raise Track 1
Lower Track 2
Increase Track 3
```

simultaneously.

Or, after FLIP:

```text
Increase Delay
Reduce Reverb
Open Filter
```

with several fingers.

This is one of the places where hardware control is not merely an alternative to the mouse.

It can enable a different style of interaction.

---

# Motor Faders and Muscle Memory

Because the faders always occupy the same physical positions, your hands begin to learn the surface.

For example:

```text
Channel 1
Channel 2
Channel 3
...
Channel 8
```

remain physically stable even though their track assignments change.

The scribble strips tell you what the channels represent.

The motors tell you their values.

Your hand learns where the controls are.

This combination of:

```text
Fixed Physical Position
        +
Dynamic Assignment
        +
Motor Feedback
```

is one of the X-Touch's strongest design ideas.

---

# A Practical Motor-Fader Exercise

Open a project containing more than eight tracks with noticeably different volume settings.

### 1. Observe the Faders

Do not touch anything.

Look at the eight physical positions.

### 2. Press BANK >

Watch all eight faders move to the values of the next bank.

### 3. Press BANK <

Watch the original positions return.

### 4. Move a Fader in Bitwig

Use the mouse to change one track's volume.

Watch the corresponding physical fader follow.

### 5. Move the Physical Fader

Confirm that Bitwig follows the hardware.

The purpose is to establish this relationship:

```text
Hardware
   ⇄
Software
```

---

# A Practical FLIP Exercise

Choose a mode in which the V-Pots have a clear assignment.

For example:

```text
SEND
```

Observe the V-Pot assignments.

Now press:

```text
FLIP
```

Watch the faders reposition.

Move one carefully and observe what changes in Bitwig.

Press:

```text
FLIP
```

again.

Watch the faders return.

The aim is to make this principle instinctive:

```text
FLIP
   → current rotary assignment
     moves to faders
```

---

# A Practical SHIFT + FLIP Exercise

Open a project containing both ordinary tracks and Effect tracks.

Begin with the normal Instrument / Audio / Hybrid track bank visible.

Press:

```text
SHIFT + FLIP
```

Observe the track names on the scribble strips.

The surface should now represent the Effect tracks.

Adjust an Effect-track level if appropriate.

Then press:

```text
SHIFT + FLIP
```

again.

Observe the normal track bank return.

The aim is to distinguish clearly between:

```text
FLIP
```

and:

```text
SHIFT + FLIP
```

They share a physical button.

They do **not** perform variations of the same operation.

---

# A Useful Mental Model

Think of the motor faders as:

```text
Eight Physical Value Displays
          +
Eight Touch-Sensitive Controls
```

Their meaning comes from the current context.

Normally:

```text
Faders
   → Track Volume
```

With another assignment flipped:

```text
Faders
   → Current V-Pot Function
```

And independently:

```text
SHIFT + FLIP
   → Normal Track Bank
     ↔ Effect Track Bank
```

So there are two distinct ideas:

```text
FLIP
   → What do the faders control?
```

and:

```text
SHIFT + FLIP
   → Which class of tracks
     does the bank contain?
```

---

# The Important Idea

The motor faders are one of the clearest examples of the X-Touch's two-way relationship with Bitwig.

They do not merely send values.

They receive them.

```text
You Move Fader
      ↓
Bitwig Changes
```

and:

```text
Bitwig Changes
      ↓
Fader Moves
```

That feedback allows the same eight physical controls to represent many different tracks and parameters without losing their current values.

FLIP extends this flexibility:

```text
FLIP
   → Move Current Rotary Assignment
     onto the Faders
```

while DrivenByMoss gives the same button a separate modified function:

```text
SHIFT + FLIP
   → Toggle
     Instrument / Audio / Hybrid Tracks
     ↔ Effect Tracks
```

This gives us an especially useful signal-flow relationship:

```text
SEND
   → Control how much signal
     goes to an Effect track

SHIFT + FLIP
   → Reach the Effect track itself
```

And throughout all of these context changes, the motors provide the same reassurance:

> **The physical position shows the current value of whatever the fader represents now.**

---

## Coming Next

The faders give us long-throw, touch-sensitive physical control.

The next part of the surface handles something different:

```text
Play

Stop

Record

Navigate

Loop

Scrub
```

Next:

**Transport Controls.**
