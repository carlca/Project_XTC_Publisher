---
chapter: 9
title: "V-Pots (Rotary Encoders)"
status: draft
---

# V-Pots (Rotary Encoders)

Across the top of the eight X-Touch channel strips is a row of rotary encoders.

These are usually called:

> **V-Pots**

They may look like ordinary knobs.

They are not.

Each V-Pot combines three important things:

```text
Turn
   +
Press
   +
LED Ring
```

DrivenByMoss makes extensive use of all three.

More importantly, the parameter controlled by a V-Pot changes according to the current edit mode.

So a better mental model is not:

```text
V-Pot = Pan Knob
```

but:

```text
V-Pot
   │
   ▼
Current Parameter
```

The V-Pots are eight general-purpose parameter controls whose meaning changes with context.

---

# Three Parts of a V-Pot

Each V-Pot gives us:

```text
        Turn
         ↕
      ┌─────┐
      │     │
      │  ●  │  ← Press
      │     │
      └─────┘
       ◜───◝
      LED Ring
```

The three parts have different jobs.

Turning changes a value.

Pressing performs an action associated with that value.

The LED ring provides feedback.

This combination makes a V-Pot considerably more capable than a conventional rotary knob.

---

# Why Encoders Rather Than Ordinary Knobs?

An ordinary potentiometer has a fixed physical position.

For example:

```text
minimum        centre        maximum
   │              │              │
   ▼              ▼              ▼
   7 o'clock    12 o'clock     5 o'clock
```

That works well when the knob always controls the same parameter.

But the X-Touch constantly changes context.

A single V-Pot might control:

```text
Pan
```

then:

```text
Send Level
```

then:

```text
Device Parameter
```

then:

```text
Track Volume
```

An endless rotary encoder has no fixed physical position.

So it can inherit whatever value belongs to the parameter it currently represents.

That is exactly what a contextual controller needs.

---

# The LED Ring Shows the Current Value

Because the V-Pot itself has no fixed pointer position, the LED ring provides visual feedback.

Conceptually:

```text
V-Pot
  │
  ├── Turn
  │     ↓
  │   Change value
  │
  └── LED ring
        ↓
      Show value
```

When the assignment changes, the ring can immediately represent the new parameter.

You do not need to physically reposition the knob.

---

# The Meaning Comes from the Current Mode

The most important thing to understand about the V-Pots is:

> **Their function is contextual.**

For example, in Panorama Mode:

```text
V-Pot 1
   → Pan Track 1

V-Pot 2
   → Pan Track 2

...

V-Pot 8
   → Pan Track 8
```

In Send Mode:

```text
V-Pot 1
   → Send level Track 1

V-Pot 2
   → Send level Track 2

...

V-Pot 8
   → Send level Track 8
```

In Device Mode:

```text
V-Pot 1
   → Device Parameter 1

V-Pot 2
   → Device Parameter 2

...

V-Pot 8
   → Device Parameter 8
```

The hardware remains unchanged.

Its assignment changes.

---

# Turn to Change the Value

The most obvious V-Pot gesture is:

```text
Turn V-Pot
      │
      ▼
Change Current Parameter
```

Exactly which parameter changes depends on the current mode.

For example:

```text
Pan Mode
   → Panorama
```

```text
Send Mode
   → Send Level
```

```text
Device Mode
   → Device Parameter
```

The scribble strip and LED ring help tell you what the V-Pot currently represents.

---

# SHIFT for Fine Adjustment

DrivenByMoss supports fine adjustment of V-Pot-controlled parameters with SHIFT.

So:

```text
Turn V-Pot
      │
      ▼
Normal Adjustment
```

while:

```text
SHIFT + Turn V-Pot
          │
          ▼
Fine Adjustment
```

This is especially useful when a small parameter change matters.

For example:

```text
Send Level
   → broad adjustment
```

then:

```text
SHIFT + V-Pot
   → precise adjustment
```

Rather than trying to make an extremely small movement with the encoder, hold SHIFT and make the same physical gesture.

---

# Press to Reset

The V-Pots are also push switches.

DrivenByMoss gives the normal press a particularly useful function:

```text
Press V-Pot
      │
      ▼
Reset Parameter
to Default Value
```

This applies to the current parameter.

So if a Pan value has been changed:

```text
Pan = 37% Right
```

pressing the V-Pot can restore its default value.

Likewise, a changed device parameter can be returned to its default.

This makes experimentation much less intimidating.

You can change something and quickly return it to its normal value.

---

# Press Is Not the Same as Turn

It is useful to treat these as two distinct gestures:

```text
TURN
   → edit
```

```text
PRESS
   → reset
```

That distinction becomes even more useful once modifiers are added.

---

# SHIFT + Press — Centre

DrivenByMoss documents:

```text
SHIFT + Press V-Pot
          │
          ▼
Set Parameter to Centre
```

This differs subtly from resetting to default.

The parameter's **default** value and its **centre** value are not necessarily the same thing.

So:

```text
Press
   → default
```

while:

```text
SHIFT + Press
   → centre
```

For a bipolar parameter such as Panorama, centre is immediately meaningful.

For other parameter types, the usefulness depends on the parameter.

---

# CONTROL + Press — Minimum

CONTROL provides another direct-value gesture:

```text
CONTROL + Press V-Pot
            │
            ▼
Set Parameter to Minimum
```

Instead of turning the encoder all the way down:

```text
turn
turn
turn
turn
turn
...
```

you can jump directly to the minimum.

Conceptually:

```text
Current Value
     │
     │ CONTROL + Press
     ▼
   Minimum
```

---

# ALT + Press — Maximum

ALT provides the opposite operation:

```text
ALT + Press V-Pot
         │
         ▼
Set Parameter to Maximum
```

So the four press gestures form a useful family:

```text
Press
   → Default

SHIFT + Press
   → Centre

CONTROL + Press
   → Minimum

ALT + Press
   → Maximum
```

This is one of the cleanest modifier patterns on the X-Touch.

---

# Four Useful Destinations

Think of the parameter range as:

```text
MINIMUM -------- CENTRE -------- MAXIMUM
                    │
                 DEFAULT?
```

Depending on the parameter, its default may be at the centre.

But it does not have to be.

The V-Pot press gestures therefore provide four conceptually different destinations:

```text
Default
Centre
Minimum
Maximum
```

without requiring precise turning.

---

# OPTION + Press in Send Mode

OPTION has a special role when the V-Pot controls a Send level.

DrivenByMoss documents:

```text
OPTION + Press V-Pot
          │
          ▼
Toggle Send On / Off
```

This is particularly useful because Send level and Send state are related but distinct things.

Turning controls:

```text
How much?
```

while OPTION + Press controls:

```text
On or off?
```

So one V-Pot gives direct access to both aspects of the Send.

---

# A Send V-Pot as a Complete Control

In Send Mode:

```text
Turn
   → Send Level
```

```text
SHIFT + Turn
   → Fine Send Level
```

```text
Press
   → Reset Send Level
```

```text
OPTION + Press
   → Toggle Send On / Off
```

This is an excellent example of how much functionality can be packed into a single physical encoder.

For dub-style mixing, this is particularly useful.

You can treat the V-Pot not simply as a level control but as a compact performance control for the Send itself.

---

# Track Edit Mode

Track Edit Mode gives the eight V-Pots a different arrangement.

DrivenByMoss assigns them to properties of the **selected track**.

The available controls are:

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

So rather than:

```text
8 V-Pots
   → same parameter
     across 8 tracks
```

Track Edit Mode gives us:

```text
8 V-Pots
   → different parameters
     for 1 selected track
```

This is a fundamental change in perspective.

---

# Across Tracks Versus Across Parameters

Compare Panorama Mode:

```text
          Track
V-Pot     Target

  1         1
  2         2
  3         3
  4         4
  5         5
  6         6
  7         7
  8         8
```

All eight knobs perform the same kind of operation.

Now compare Track Edit Mode:

```text
V-Pot     Parameter

  1       Volume
  2       Panorama
  3       Crossfader
  4       Send 1
  5       Send 2
  6       Send 3
  7       Send 4
  8       Send 5
```

All eight knobs refer to the same selected track, but control different things.

This gives us two important V-Pot layouts:

```text
one parameter
across many tracks
```

and:

```text
many parameters
on one track
```

Recognising which layout you are currently using is crucial.

---

# Track Mode Can Expose Six Sends

DrivenByMoss provides a preference that can hide the Crossfader parameter from Track Edit Mode.

With that option enabled, the freed V-Pot is used for another Send.

So instead of:

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

you can have:

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

This can be particularly attractive in a Send-heavy workflow.

We will return to configuration choices in Chapter 21.

---

# Volume Edit Mode

Press TRACK twice to enter Volume Edit Mode.

Here the relationship is simple:

```text
V-Pot 1
   → Volume Track 1

V-Pot 2
   → Volume Track 2

...

V-Pot 8
   → Volume Track 8
```

This may initially seem redundant because the X-Touch already has motor faders.

But it demonstrates an important principle:

> **The V-Pots are general-purpose controls, not permanently assigned Pan knobs.**

And depending on how the surface is configured or how you are working, alternative physical access to a parameter can be useful.

---

# Panorama Edit Mode

Press PAN to enter Panorama Edit Mode.

Now:

```text
V-Pot 1
   → Panorama Track 1

V-Pot 2
   → Panorama Track 2

...

V-Pot 8
   → Panorama Track 8
```

This is probably the role most people instinctively associate with the rotary controls on a mixing surface.

But on the X-Touch it is only one of many assignments.

---

# Send Edit Mode

Press SEND to enter Send Edit Mode.

The V-Pots now control a Send across the current bank of tracks.

For example, with Send 1 selected:

```text
Track       1     2     3     4     5     6     7     8
            │     │     │     │     │     │     │     │
            ▼     ▼     ▼     ▼     ▼     ▼     ▼     ▼
V-Pot       1     2     3     4     5     6     7     8

            Send 1 levels
```

This is an extremely useful mixer-oriented arrangement.

Rather than visiting each track and finding its Send individually, the entire Send appears across the physical surface.

---

# Think Across the Mix

Suppose Send 1 feeds a delay.

In Send Mode:

```text
Kick    Snare   Hats    Bass    Keys    Lead    Vox     FX
 │        │       │       │       │       │       │       │
 ▼        ▼       ▼       ▼       ▼       ▼       ▼       ▼
Delay Send Amount
```

Now you can shape:

> **How much of the entire mix is feeding this delay?**

using one row of knobs.

That is a very different way of thinking from:

> **What are all the parameters on this track?**

Both are useful.

The mode determines which viewpoint the hardware gives you.

---

# Selecting Sends

Repeated presses of SEND step forward through Sends 1–8.

Conceptually:

```text
SEND
  ↓
Send 1
  ↓
SEND
  ↓
Send 2
  ↓
SEND
  ↓
Send 3
```

and so on.

SHIFT + SEND moves backwards.

You can also use:

```text
SEND + SELECT 1–8
```

to choose a Send directly.

Once the desired Send is selected, the V-Pots control its level across the tracks.

---

# Device Mode

Device Mode is where the general-purpose nature of the V-Pots becomes particularly powerful.

Press DEVICE.

The eight V-Pots now control the currently selected eight device parameters.

Conceptually:

```text
Selected Device

Parameter 1   Parameter 2   Parameter 3   Parameter 4
     │             │             │             │
     ▼             ▼             ▼             ▼
  V-Pot 1       V-Pot 2       V-Pot 3       V-Pot 4


Parameter 5   Parameter 6   Parameter 7   Parameter 8
     │             │             │             │
     ▼             ▼             ▼             ▼
  V-Pot 5       V-Pot 6       V-Pot 7       V-Pot 8
```

The X-Touch has effectively become a hardware parameter editor.

---

# Parameter Pages

A device may expose far more than eight parameters.

The X-Touch only has eight V-Pots.

So DrivenByMoss organises device parameters into pages.

For example:

```text
Page 1
Parameters 1–8

Page 2
Parameters 9–16

Page 3
Parameters 17–24
```

In Device Mode:

```text
CHANNEL <
   → Previous Parameter Page

CHANNEL >
   → Next Parameter Page
```

Each page repopulates the eight V-Pots with another group of parameters.

Again, the eight knobs form a movable window.

---

# Direct Parameter-Page Selection

DrivenByMoss provides a faster way to choose parameter pages.

Hold OPTION in Device Mode.

The V-Pots show the available parameter pages.

Then:

```text
Press V-Pot
      │
      ▼
Select that Parameter Page
```

Conceptually:

```text
Hold OPTION

Page 1   Page 2   Page 3   Page 4   ...
  │        │        │        │
  ▼        ▼        ▼        ▼
Pot 1    Pot 2    Pot 3    Pot 4
```

Press the V-Pot corresponding to the page you want.

This avoids stepping through pages one at a time.

---

# Direct Device Selection

CONTROL provides a corresponding shortcut for devices.

Hold CONTROL in Device Mode.

DrivenByMoss shows the devices on the selected track across the V-Pots.

Then:

```text
Press V-Pot
      │
      ▼
Select that Device
```

For example:

```text
Selected Track

EQ     Comp    Saturator    Chorus    Delay    Reverb
│       │          │          │         │         │
▼       ▼          ▼          ▼         ▼         ▼
1       2          3          4         5         6
```

If you want the Delay:

```text
Hold CONTROL
      ↓
Press V-Pot 5
      ↓
Delay Selected
```

This can be much faster than repeatedly pressing BANK to move through devices.

---

# Device Navigation Has Two Speeds

So Device Mode gives us two navigation methods.

Sequential:

```text
BANK <
BANK >
   → Previous / Next Device
```

Direct:

```text
Hold CONTROL
      ↓
Press Device V-Pot
```

Likewise for parameter pages:

Sequential:

```text
CHANNEL <
CHANNEL >
   → Previous / Next Page
```

Direct:

```text
Hold OPTION
      ↓
Press Page V-Pot
```

This gives the workflow both precision and speed.

---

# EQ Mode

EQ Mode works like Device Mode, but targets the track's equalizer device.

DrivenByMoss specifically supports Bitwig's EQ+ in this mode.

An especially interesting behaviour is:

> If EQ Mode is activated on a track that does not yet contain an equalizer device, DrivenByMoss automatically adds one.

The V-Pots then control the EQ device parameters in the same general manner as Device Mode.

So the workflow can become:

```text
Select Track
     ↓
EQ
     ↓
EQ+ available
     ↓
V-Pots edit EQ
```

This makes the hardware feel less like a remote control for an existing screen layout and more like an active part of the mixing workflow.

---

# Instrument Mode

The INSTRUMENT assignment selects the instrument device edit mode.

Like the other device-oriented contexts, the V-Pots become parameter controls for the relevant device.

The underlying mental model remains:

```text
Select context
      ↓
Eight parameters appear
      ↓
Turn V-Pots
      ↓
Edit
```

The particular parameters depend on the device and its mappings.

---

# Project and Track Parameters

Pressing DEVICE again enters the Project/Track Parameter edit mode.

DrivenByMoss labels these contexts:

```text
PP
```

or:

```text
tP
```

depending on the active parameter context.

The eight device knobs control the currently selected eight parameters.

Again:

```text
8 physical V-Pots
       │
       ▼
8 current parameters
```

The mechanism is the same even though the target has changed.

---

# Layers and Drum Pads

The V-Pots also participate in Layer and Drum Pad editing.

Once you enter Layers or Drum Pads using the SELECT behaviour described earlier, the mode buttons can select different Layer edit modes.

The V-Pots can then edit:

```text
Volume
Pan
Sends
```

for the Layers or Drum Pads.

The channel-strip MUTE and SOLO buttons also follow the Layer or Drum Pad context.

So a row that previously represented:

```text
eight tracks
```

can now represent:

```text
eight layers
```

or:

```text
eight drum pads
```

while the V-Pots retain the same broad role:

> **Edit the current parameter across the eight current targets.**

---

# Master Mode

Touching the Master fader selects the Master track and enters Master Edit Mode.

The V-Pots acquire a very different set of functions.

DrivenByMoss documents:

```text
V-Pot 1
   → Master Volume

V-Pot 2
   → Master Panorama
```

Pressing either resets its parameter.

The published DrivenByMoss MCU documentation describes presses on V-Pots 3–5 as toggling the project's audio engine.

With Bitwig Studio and DrivenByMoss 26.6.3, pressing or turning V-Pots 3–5 in Master Mode produces no observable response. They should therefore be treated as unassigned in the setup covered by this guide.

V-Pots 7 and 8 provide project-level actions:

```text
Press V-Pot 7
   → Previous Project
```

and:

```text
Press V-Pot 8
   → Next Project
```

This is another reminder that a V-Pot press is not universally a parameter reset.

Its meaning can be overridden by the current mode.

---

# Context Comes Before the Gesture

Earlier we learned:

```text
Press V-Pot
   → reset parameter
```

That is the **common** behaviour for parameter controls.

But Master Mode shows why we must always remember the complete model:

```text
Current Mode
      +
Current Assignment
      +
Gesture
      =
Function
```

For V-Pot 8 in Master Mode:

```text
Master Mode
      +
V-Pot 8
      +
Press
      =
Next Project
```

The context wins.

---

# Browser Mode

The V-Pots take on another role in Browser Mode.

Here they are used for navigating Browser columns.

DrivenByMoss documents:

```text
Turn V-Pot
   → Navigate Browser column
```

and:

```text
Press V-Pot
   → Enter filter or result
```

Pressing again confirms the selection at that level.

So the same gesture that normally edits a numeric parameter can now navigate a list.

---

# From Continuous Values to Choices

This is an important conceptual shift.

Normally:

```text
Turn V-Pot
      │
      ▼
Continuous Value
```

For example:

```text
0% ─────────────── 100%
```

But in Browser Mode:

```text
Turn V-Pot
      │
      ▼
Discrete Choices
```

For example:

```text
Bass
Keys
Lead
Pad
Pluck
Strings
```

The encoder is equally comfortable doing both because it has no fixed physical endpoint.

---

# Marker Mode

V-Pots also participate in Marker Mode.

Press MARKER to enter Marker Mode.

DrivenByMoss documents:

```text
Press V-Pot
      │
      ▼
Start Playback
from Marker Position
```

So the V-Pot row becomes a set of marker destinations.

Conceptually:

```text
Intro   Verse   Chorus   Break   Drop   Outro
  │       │       │       │       │      │
  ▼       ▼       ▼       ▼       ▼      ▼
Pot 1   Pot 2   Pot 3   Pot 4   Pot 5  Pot 6
```

Pressing a V-Pot chooses the corresponding marker position for playback.

This is another excellent example of the V-Pots acting as:

> **eight contextual choices**

rather than simply eight knobs.

---

# The V-Pots Have Two Broad Personalities

After seeing these modes, we can identify two broad V-Pot roles.

## Parameter Controls

```text
Turn
   → change value

Press
   → parameter action
```

Examples:

```text
Pan
Volume
Send Level
Device Parameter
EQ Parameter
```

## Choice Controls

```text
Turn
   → navigate choices

Press
   → choose
```

or simply:

```text
Press
   → select item
```

Examples:

```text
Browser columns
Devices
Parameter Pages
Markers
Projects
```

This is a useful distinction.

---

# Eight Knobs Can Mean Eight Tracks

In modes such as Panorama or Send:

```text
V-Pot 1  → Track 1
V-Pot 2  → Track 2
V-Pot 3  → Track 3
...
V-Pot 8  → Track 8
```

The parameter is common.

The targets differ.

---

# Eight Knobs Can Mean Eight Parameters

In Device Mode:

```text
V-Pot 1  → Parameter 1
V-Pot 2  → Parameter 2
V-Pot 3  → Parameter 3
...
V-Pot 8  → Parameter 8
```

The target device is common.

The parameters differ.

---

# Eight Knobs Can Mean Eight Choices

While holding CONTROL in Device Mode:

```text
V-Pot 1  → Device 1
V-Pot 2  → Device 2
V-Pot 3  → Device 3
...
V-Pot 8  → Device 8
```

While holding OPTION:

```text
V-Pot 1  → Page 1
V-Pot 2  → Page 2
V-Pot 3  → Page 3
...
V-Pot 8  → Page 8
```

The same physical row therefore supports three different mental layouts:

```text
one parameter across eight targets
```

```text
eight parameters on one target
```

```text
eight choices
```

That is one of the keys to understanding the X-Touch.

---

# Read Before You Turn

Because the V-Pots are so contextual, it is especially important not to assume what a knob currently controls.

Before turning one:

```text
Look
  ↓
Identify Context
  ↓
Confirm Assignment
  ↓
Turn
```

The scribble strips, mode indicators and LED rings are all part of the interaction.

A useful habit is:

> **Read before you turn.**

This becomes increasingly important as you use more advanced modes.

---

# Why This Matters in a Mouse-Lite Workflow

With a mouse, you often work like this:

```text
Find parameter visually
      ↓
Move pointer
      ↓
Click
      ↓
Drag
```

With the X-Touch:

```text
Choose context
      ↓
Parameter appears on V-Pot
      ↓
Turn
```

The second approach becomes fast when you stop thinking primarily in terms of screen coordinates.

Instead of:

> **Where is the control on the screen?**

you think:

> **Which controller context exposes the control?**

That is a fundamental shift towards a hardware-centred workflow.

---

# V-Pots and Dub-Style Mixing

Send Mode provides a particularly good example.

Suppose:

```text
Send 1 → Delay

Send 2 → Reverb
```

Select Send 1.

Now the eight V-Pots represent:

```text
Delay amount
across eight tracks
```

Instead of opening eight mixer channels and adjusting their Sends individually, you have eight physical controls side by side.

You can think:

```text
Kick delay
Snare delay
Hat delay
Bass delay
Keys delay
Lead delay
Vocal delay
FX delay
```

as one physical performance surface.

Switch to Send 2 and the same knobs become the Reverb sends.

That is a much more musical way to approach effects than thinking of each Send as a tiny control buried inside an individual mixer strip.

---

# A Practical Pan Exercise

Start in Panorama Mode.

Use the eight V-Pots to change the Pan positions of several tracks.

Then try:

```text
SHIFT + Turn
```

and notice the finer adjustment.

Now deliberately change one Pan value and press its V-Pot:

```text
Press
   → Default
```

Then try:

```text
SHIFT + Press
   → Centre
```

Try:

```text
CONTROL + Press
   → Minimum
```

and:

```text
ALT + Press
   → Maximum
```

Watch Bitwig while doing this.

The aim is to make the press-modifier family physically memorable.

---

# A Practical Send Exercise

Create or use a project with a Delay effect track.

Enter Send Mode and select the corresponding Send.

The V-Pots should now represent the Send amount across the current bank.

Try:

```text
Turn
```

to change Send level.

Then:

```text
SHIFT + Turn
```

for finer adjustment.

Finally try:

```text
OPTION + Press
```

to toggle the Send on or off.

This is worth practising because it turns a fairly abstract modifier combination into an obvious musical action.

---

# A Practical Device Exercise

Select a track containing several devices.

Press DEVICE.

Turn the V-Pots and watch the corresponding parameters in Bitwig.

Then use:

```text
CHANNEL >
```

to move to another parameter page.

Next hold:

```text
OPTION
```

and observe how the V-Pot assignments change.

Press one of the V-Pots to select a parameter page directly.

Then hold:

```text
CONTROL
```

and observe the device choices.

Press the V-Pot corresponding to another device.

The sequence demonstrates three different uses of exactly the same hardware:

```text
Normal Device Mode
   → edit parameters

OPTION held
   → choose parameter page

CONTROL held
   → choose device
```

---

# Do Not Fight the Context

If a V-Pot appears to be controlling the wrong thing, resist the temptation to keep turning it until the result makes sense.

Instead ask:

```text
Which mode am I in?

Which track is selected?

Which device is selected?

Which parameter page is active?

Is a modifier being held?
```

Usually the V-Pot is doing exactly what its current context tells it to do.

The challenge is understanding that context.

---

# A Useful Mental Model

The complete V-Pot model is now:

```text
              Current Mode
                   │
                   ▼
Current Target → V-Pot ← Modifier
                   │
                   ▼
              Current Action
```

Or more simply:

```text
V-Pot
  +
Context
  +
Gesture
  =
Function
```

The gesture may be:

```text
Turn
Press
SHIFT + Turn
SHIFT + Press
CONTROL + Press
ALT + Press
OPTION + Press
```

The context decides what that gesture acts upon.

---

# The Important Idea

A V-Pot is not simply a knob.

It is a:

```text
Rotary Encoder
      +
Push Button
      +
LED Display
```

and DrivenByMoss uses it as a general-purpose contextual control.

Its common parameter gestures are:

```text
Turn
   → Change value

SHIFT + Turn
   → Fine adjustment

Press
   → Reset to default

SHIFT + Press
   → Centre

CONTROL + Press
   → Minimum

ALT + Press
   → Maximum
```

For Sends:

```text
OPTION + Press
   → Toggle Send on / off
```

But the V-Pot row can also become:

```text
8 track controls
```

or:

```text
8 device parameters
```

or:

```text
8 device choices
```

or:

```text
8 parameter-page choices
```

or:

```text
Browser navigation
```

or:

```text
Marker destinations
```

The important question is therefore never merely:

> **What does this knob do?**

It is:

> **What does this knob do in the context I am in now?**

Once that becomes instinctive, the V-Pots stop feeling like eight mysterious multifunction controls.

They become one of the most flexible parts of the X-Touch.

---

## Coming Next

The V-Pots provide flexible contextual control.

The motor faders provide something different:

> **a physical control that can move itself to reflect Bitwig's current state.**

That creates a particularly strong connection between software and hardware.

Next:

**Motor Faders.**
