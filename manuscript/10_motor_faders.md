---
chapter: 10
title: "Motor Faders"
status: draft
---

# Motor Faders

The X-Touch has nine motorised faders:

```text
8 Channel Faders
       +
1 Master Fader
```

At first glance, they look like the faders on any conventional mixing console.

But the word **motorised** changes everything.

A normal fader tells the software:

> **This is where I want the level to be.**

A motor fader can also let the software tell the hardware:

> **This is where the level already is.**

That two-way relationship is one of the most important features of the X-Touch.

---

# The Fader Is Both Input and Feedback

Move a fader:

```text
Your Hand
    │
    ▼
X-Touch Fader
    │
    ▼
Bitwig
```

But Bitwig can also move the fader:

```text
Bitwig
   │
   ▼
X-Touch Motor
   │
   ▼
Physical Fader
```

So the fader is simultaneously:

```text
Control
   +
Display
```

That is fundamentally different from using an ordinary MIDI controller.

---

# Why Motorisation Matters

Imagine Track 1 is at:

```text
-18 dB
```

and Track 2 is at:

```text
-4 dB
```

If the same ordinary physical fader were reassigned from Track 1 to Track 2, its position could not represent both values.

You would have a mismatch:

```text
Physical Fader
     │
     ▼
   -18 dB

Software Value
     │
     ▼
    -4 dB
```

With a motor fader, reassignment can physically move the control:

```text
Track changes
     │
     ▼
New value received
     │
     ▼
Motor moves fader
     │
     ▼
Hardware matches software
```

This is what allows the X-Touch's eight channel strips to act as a movable window onto a much larger project.

---

# Banking Demonstrates the Motors

Suppose the current bank contains:

```text
Kick    Snare   Hats    Bass    Pad     Lead    Vox     FX
```

with different volume levels.

The eight faders physically show those values.

Now press:

```text
BANK >
```

and the controller moves to another group:

```text
Perc    Room    Piano   Gtr 1   Gtr 2   BVox    Verb    Delay
```

The faders move automatically to the volume values of the new tracks.

That movement is not decoration.

It is feedback.

The surface is telling you:

> **These are the values for the tracks you are now controlling.**

---

# Never Fight a Moving Fader

When changing banks, modes or tracks, the faders may move.

Let them.

Do not hold a fader in place while its motor is trying to reposition it.

A good habit is:

```text
Change Context
      ↓
Let Faders Settle
      ↓
Read Surface
      ↓
Touch Fader
      ↓
Adjust
```

The movement is part of the controller's communication with you.

---

# Touch Sensitivity

The X-Touch faders are touch-sensitive.

The controller can therefore distinguish between:

```text
Fader is merely sitting here
```

and:

```text
A person is touching the fader
```

That distinction is particularly important for automation.

Conceptually:

```text
Touch
  ↓
"I have taken control."

Release
  ↓
"I have finished."
```

The exact result depends on Bitwig's current automation mode, but touch detection gives the DAW information that an ordinary MIDI fader cannot provide.

---

# Fader Touch Can Select the Track

DrivenByMoss provides a preference allowing a touched fader to select its corresponding track.

With that option enabled:

```text
Touch Channel Fader
        │
        ▼
Select that Track
```

This creates a very natural workflow.

Instead of:

```text
SELECT Track
      ↓
Move Fader
```

you can simply:

```text
Touch Fader
      ↓
Track Selected
      ↓
Adjust Level
```

The physical act of reaching for the channel establishes focus.

---

# Why Touch-to-Select Can Be Useful

Suppose you are mixing and decide the Vocal needs attention.

With touch selection enabled:

```text
Touch Vocal Fader
       │
       ▼
Vocal becomes selected
```

You can then move into another context:

```text
DEVICE
```

or:

```text
SEND
```

knowing that Vocal is already the selected track.

The workflow becomes:

```text
Touch
  ↓
Focus
  ↓
Choose Context
  ↓
Edit
```

This can significantly reduce explicit SELECT-button presses during mixing.

---

# Touch-to-Select Is a Preference

Not everyone wants touching a fader to change track selection.

For some workflows, you may want to adjust levels while leaving another track selected.

DrivenByMoss therefore makes this behaviour configurable.

The important point is:

> **If touching a fader unexpectedly changes the selected track, that may be a DrivenByMoss preference rather than a fault.**

We will look at configuration in Chapter 21.

---

# The Normal Channel-Fader Role

In the standard mixer context, the eight channel faders control the volume of the eight tracks currently represented by the surface.

Conceptually:

```text
Track       1     2     3     4     5     6     7     8
            │     │     │     │     │     │     │     │
            ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼
Fader       1     2     3     4     5     6     7     8
```

Move Fader 4:

```text
Fader 4
   │
   ▼
Volume of current Track 4
```

Remember that "Track 4" here means:

> **the fourth track in the current controller bank**

not necessarily Bitwig Track 4.

---

# The Faders Follow the Current Bank

This follows directly from the movable-window model introduced in Chapter 4.

Bank 1:

```text
Fader     1   2   3   4   5   6   7   8

Track     1   2   3   4   5   6   7   8
```

After BANK >:

```text
Fader     1   2   3   4   5   6   7   8

Track     9  10  11  12  13  14  15  16
```

The hardware does not belong permanently to particular tracks.

The motors make that reassignment practical because each fader can immediately move to the correct value.

---

# FLIP Changes the Fader Assignment

One of the most important advanced fader functions is:

```text
FLIP
```

FLIP exchanges the assignments of the V-Pots and the faders.

Conceptually, before FLIP:

```text
V-Pot
   → Parameter A

Fader
   → Parameter B
```

After FLIP:

```text
V-Pot
   → Parameter B

Fader
   → Parameter A
```

This allows a parameter normally controlled by a rotary encoder to be placed on a long-throw motor fader.

---

# Why FLIP Is Useful

Suppose the V-Pots currently control Send levels.

Normally:

```text
V-Pots
   → Send Levels

Faders
   → Track Volumes
```

Press FLIP:

```text
V-Pots
   → Track Volumes

Faders
   → Send Levels
```

Now you can ride Send levels using the motor faders.

This can be extremely useful when you want more physical precision or a more performance-oriented gesture.

---

# FLIP Is More Than a Convenience

A V-Pot and a fader feel very different.

A V-Pot is excellent for:

```text
quick rotary adjustment
```

A fader is excellent for:

```text
long, visible movement
```

So FLIP lets you choose not only:

> **Which parameter do I want to control?**

but also:

> **Which physical control would I prefer to use for it?**

That can have a surprisingly large effect on workflow.

---

# Send Levels on Faders

Send Mode provides a particularly useful example.

Normally:

```text
V-Pots
   → Send Levels

Faders
   → Track Volumes
```

After FLIP:

```text
Faders
   → Send Levels
```

Imagine Send 1 feeds a delay.

The eight faders can now become:

```text
Kick Delay
Snare Delay
Hat Delay
Bass Delay
Keys Delay
Lead Delay
Vocal Delay
FX Delay
```

This turns the X-Touch into a very different kind of performance surface.

---

# Riding Effects

With Send levels on the faders, you can perform effects dynamically.

For example:

```text
Vocal phrase
     │
     ▼
Raise Delay Send
     │
     ▼
Phrase enters delay
     │
     ▼
Lower Send
```

The long fader throw makes this feel more like conventional console mixing than turning a small encoder.

For dub-oriented work, FLIP can therefore be particularly interesting.

---

# Device Parameters on Faders

FLIP is not limited to Sends.

In contexts where the V-Pots are controlling device parameters, FLIP can place those parameters on the faders.

Conceptually:

```text
Device Mode

V-Pots
   → Parameters 1–8
```

then:

```text
FLIP

Faders
   → Parameters 1–8
```

The motor faders now physically represent the current device parameter values.

---

# Why Motorisation Becomes Especially Valuable Here

Suppose a device parameter is at:

```text
23%
```

and another is at:

```text
81%
```

When those parameters are assigned to motor faders, the hardware physically shows their relative values.

Change device or parameter page:

```text
New Parameters
      ↓
New Values
      ↓
Faders Move
```

So FLIP does not merely make a parameter controllable by a fader.

It makes that parameter **physically visible**.

---

# FLIP Is Contextual

The meaning of FLIP depends on what the V-Pots currently control.

If the V-Pots control:

```text
Pan
```

FLIP places that assignment on the faders.

If they control:

```text
Sends
```

FLIP places Sends on the faders.

If they control:

```text
Device Parameters
```

FLIP places those parameters on the faders.

So:

```text
FLIP
   │
   ▼
Exchange current
V-Pot / Fader assignments
```

The context determines what is actually exchanged.

---

# Returning to Normal

Press FLIP again to return the assignments.

Conceptually:

```text
Normal
   │
   │ FLIP
   ▼
Flipped
   │
   │ FLIP
   ▼
Normal
```

If the faders appear to be controlling something unexpected, check whether FLIP is active.

This is another example of the general rule:

> **When hardware behaviour surprises you, check the current context before assuming something is wrong.**

---

# Automation and Motor Faders

Motor faders become particularly valuable when automation is involved.

Suppose Bitwig contains volume automation:

```text
Volume
  │
  │       ╭──────
  │   ╭───╯
  │───╯
  └──────────────── Time
```

During playback, the software value changes.

The X-Touch fader can follow it:

```text
Automation
    │
    ▼
Bitwig Volume
    │
    ▼
Motor Fader Moves
```

You can therefore watch the automation physically happen.

---

# Automation Becomes Tangible

On screen, automation is a line.

On the X-Touch, automation can become:

```text
a fader moving under your fingers
```

This provides a strong physical connection to the mix.

Instead of merely seeing:

```text
volume increasing
```

you can see and feel the control itself move.

That is one of the major reasons motorised surfaces remain useful even in a software-based studio.

---

# Touch and Automation

Touch sensitivity allows Bitwig to know when you intervene.

Conceptually:

```text
Automation playing
      │
      ▼
Fader moving
      │
      ▼
You touch fader
      │
      ▼
DAW knows:
"User has taken control"
```

What happens next depends on the active automation mode.

The important point for this chapter is that the X-Touch can communicate both:

```text
fader position
```

and:

```text
fader touch state
```

to the DAW.

Chapter 16 covers the automation workflow itself.

---

# Do Not Chase an Automated Fader

If a fader is moving because automation is playing, you do not need to follow it with your hand.

Let the motor reproduce the existing automation.

Touch it only when you actually intend to intervene.

Think:

```text
Motor movement
   → information

My movement
   → intention
```

That distinction makes automated mixing much easier to understand.

---

# The Master Fader

The ninth fader is physically separated from the eight channel strips.

This is the Master fader.

In normal use it represents the Master track.

Unlike the eight channel faders, it does not participate in the ordinary eight-track banking system.

Conceptually:

```text
Channel Faders
      │
      ▼
Current Bank

Master Fader
      │
      ▼
Master Track
```

This gives the project output a permanent physical control.

---

# Touching the Master Fader

DrivenByMoss gives the Master fader another important role.

Touching it selects the Master track and enters the Master editing context.

Conceptually:

```text
Touch Master Fader
        │
        ▼
Select Master Track
        │
        ▼
Master Edit Context
```

The V-Pots can then expose Master and project-level functions.

We saw some of those functions in Chapter 9.

---

# SHIFT + Master Fader

DrivenByMoss also gives the Master fader a modified function:

```text
SHIFT + Master Fader
        │
        ▼
Metronome Volume
```

This is a useful example of a fader being temporarily repurposed.

Normally:

```text
Master Fader
   → Master Volume
```

with SHIFT:

```text
SHIFT + Master Fader
   → Metronome Volume
```

Release SHIFT and the normal Master assignment returns.

---

# A Physical Metronome Level

This can be particularly convenient while recording.

Instead of opening a software control to change click level:

```text
Hold SHIFT
     ↓
Move Master Fader
     ↓
Adjust Metronome Volume
```

The same large physical control is temporarily borrowed for another level-setting task.

Again, the modifier changes the context.

---

# Faders and Layer / Drum Pad Modes

When the controller enters Layer or Drum Pad contexts, the channel strips can represent those objects rather than ordinary project tracks.

The faders follow that context.

So the eight physical faders may represent:

```text
8 Tracks
```

or:

```text
8 Layers
```

or:

```text
8 Drum Pads
```

depending on the current mode.

The principle remains the same:

> **The fader controls the level of whatever the current channel strip represents.**

This is more useful than memorising a separate rule for every context.

---

# The Fader Belongs to the Channel Strip

A useful way to think about the surface is:

```text
Channel Strip
     │
     ├── Scribble Strip
     ├── V-Pot
     ├── REC
     ├── SOLO
     ├── MUTE
     ├── SELECT
     └── Fader
```

When the identity of the channel strip changes, all of these controls follow it.

If Channel Strip 3 represents:

```text
Bass
```

then Fader 3 controls Bass.

If the context changes and Channel Strip 3 now represents:

```text
Snare Layer
```

then Fader 3 controls that Layer.

The fader does not need a separate mental identity.

It belongs to the current channel strip.

---

# Motor Movement Is Feedback

It is worth returning to this idea because it changes how the surface should be used.

When a fader moves by itself, it is not merely performing a mechanical trick.

It is telling you something.

For example:

```text
BANK >
   ↓
Faders move
   ↓
"These are the new track levels."
```

or:

```text
Select another device
   ↓
FLIP active
   ↓
Faders move
   ↓
"These are the new parameter values."
```

or:

```text
Playback
   ↓
Automation runs
   ↓
Fader moves
   ↓
"This value is changing over time."
```

So:

> **Motor movement is part of the X-Touch's display system.**

---

# Faders Are Visual Displays

This gives us an unusual but useful idea.

A fader is not merely something you manipulate.

Its physical position is also something you **read**.

```text
Low
 │
 ▼

│
│
●
│
│
│
│
```

versus:

```text
High
 │
 ▼

│
│
│
│
│
●
│
```

At a glance, eight faders provide a physical picture of the current mix.

That picture changes automatically when the controller context changes.

---

# Read Before You Move

Chapter 9 gave us:

> **Read before you turn.**

For the faders, the equivalent is:

> **Look before you move.**

When changing bank or context:

```text
Let Motors Move
      ↓
Observe Positions
      ↓
Understand Current State
      ↓
Make Adjustment
```

The existing fader position is useful information.

Do not discard it mentally just because you are about to change it.

---

# Faders and the Scribble Strips Work Together

A fader position alone tells you:

```text
how much
```

The scribble strip tells you:

```text
what
```

Together:

```text
Scribble Strip
      │
      ▼
   "Vocal"

Fader Position
      │
      ▼
    -6 dB
```

This combination is much more informative than either element alone.

It is another reason the X-Touch should be treated as a complete surface rather than a collection of independent controls.

---

# A Practical Banking Exercise

Open a project with at least twelve tracks and give the tracks noticeably different volume levels.

Start with Tracks 1–8 visible.

Look at the fader positions.

Then press:

```text
BANK >
```

Do not touch anything immediately.

Watch the faders move.

Now press:

```text
BANK <
```

and watch them return.

Repeat several times.

The aim is to establish the instinct:

```text
Bank changes
     ↓
Faders show new state
```

rather than:

```text
Why are the faders moving?
```

---

# A Practical FLIP Exercise

Enter Panorama or Send Mode.

Observe what the V-Pots currently control.

Now press:

```text
FLIP
```

Move one of the faders and watch the corresponding parameter in Bitwig.

Press FLIP again.

The exercise should make this relationship obvious:

```text
Before FLIP

V-Pots = A
Faders = B
```

```text
After FLIP

V-Pots = B
Faders = A
```

Try it in more than one edit mode.

The point is to understand FLIP as a general mechanism rather than memorising separate FLIP behaviours.

---

# A Send Performance Exercise

Create two effect tracks:

```text
Delay

Reverb
```

Enter Send Mode and select the Delay Send.

Press FLIP.

The faders should now give you physical control over Delay Send levels across the current tracks.

Play the project.

Try raising a Send briefly for a particular musical event and then lowering it again.

For example:

```text
Snare Hit
    │
    ▼
Raise Delay Send
    │
    ▼
Delay catches hit
    │
    ▼
Lower Send
```

This demonstrates why putting Send levels on faders can be musically useful rather than merely technically interesting.

---

# An Automation Observation Exercise

Use a project containing existing volume automation.

Play the automated section without touching the fader.

Watch the motor follow the automation.

Then stop playback.

The important observation is simply:

```text
Software automation
       │
       ▼
Physical movement
```

Chapter 16 will deal with writing and editing automation.

For now, become comfortable with the idea that a moving fader can be **output from Bitwig**, not input from you.

---

# If a Fader Seems Wrong

If a fader appears to control the wrong thing, check the current context.

Ask:

```text
Which bank am I in?

Which mode am I in?

Is FLIP active?

Am I inside a Group?

Am I editing Layers or Drum Pads?

Is automation currently playing?

Am I holding SHIFT?

What does the scribble strip say?
```

A surprising fader assignment is usually a context issue.

The controller is contextual by design.

---

# A Useful Mental Model

The motor fader can be understood as:

```text
            Bitwig
              ▲
              │
              │ value feedback
              │
              ▼
        ┌───────────┐
        │   Fader   │
        └───────────┘
              ▲
              │
              │ your movement
              │
              ▼
             You
```

Information flows in both directions.

That is the essential difference between a motor fader and a simple MIDI slider.

---

# The Important Idea

The X-Touch's motor faders are not merely volume controls.

They are:

```text
Physical Controls
       +
Touch Sensors
       +
Motorised Displays
```

Normally, the eight channel faders control the current channel-strip levels.

But their assignments can change with context.

FLIP can exchange the current V-Pot and fader assignments:

```text
V-Pot Parameter
      ↕
    FLIP
      ↕
Fader Parameter
```

Touch sensitivity allows the controller to know when you take hold of a fader.

With the appropriate DrivenByMoss preference:

```text
Touch Fader
   → Select Track
```

The Master fader provides permanent access to the Master track and can also be repurposed:

```text
SHIFT + Master Fader
   → Metronome Volume
```

And when Bitwig changes a controlled value:

```text
Bitwig
   ↓
Motor
   ↓
Fader moves
```

So perhaps the most important idea in this chapter is:

> **A motor fader is something you both operate and observe.**

It lets your hand change Bitwig.

And it lets Bitwig physically show its state back to you.

---

## Coming Next

We now understand the X-Touch's two principal continuous-control systems:

```text
V-Pots
   → flexible contextual rotary control

Motor Faders
   → physical control plus motorised feedback
```

Next we move to another part of the surface that looks familiar but becomes considerably more capable through DrivenByMoss modifiers:

**the Transport Controls.**
