---
chapter: 8
title: "Modifiers: SHIFT, OPTION, CONTROL and ALT"
status: draft
---

# Modifiers: SHIFT, OPTION, CONTROL and ALT

By now, an important pattern should be becoming familiar.

The X-Touch does not have enough physical controls for every possible function to exist as a dedicated button.

Instead, DrivenByMoss reuses controls according to context.

One of the main ways it does this is through four modifier buttons:

```text
SHIFT

OPTION

CONTROL

ALT
```

Hold one of these while pressing, turning or moving another control, and the meaning of that control may change.

The underlying idea is simple:

> **A modifier temporarily changes the context of another control.**

---

# A Modifier Is a Temporary Context

Suppose a control normally does this:

```text
Control
   │
   ▼
Primary Function
```

Hold a modifier:

```text
Modifier + Control
       │
       ▼
Alternative Function
```

Release the modifier:

```text
Control
   │
   ▼
Primary Function again
```

So modifiers behave rather like temporary modes.

They extend the controller without requiring more hardware.

---

# Why Modifiers Matter

Imagine the X-Touch without modifiers.

Every secondary function would require:

- another physical button;
- another mode;
- another menu;
- or another trip to the mouse.

Modifiers allow one control to support several related operations.

For example:

```text
MARKER
   → enter Marker Mode
```

while:

```text
OPTION + MARKER
   → create a marker
```

The same physical button participates in two related tasks.

That is exactly what modifiers are for.

---

# SHIFT

SHIFT is one of the most frequently used modifiers.

It often provides:

- finer adjustment;
- a related secondary function;
- reverse movement;
- access to a Launcher-oriented variant;
- or another function closely related to the unmodified control.

For example:

```text
Jog Wheel
   → move play position
```

while:

```text
SHIFT + Jog Wheel
   → finer movement
```

Likewise:

```text
SEND
   → next Send
```

while:

```text
SHIFT + SEND
   → previous Send
```

So SHIFT often means:

> **Do the same kind of thing, but differently.**

---

# SHIFT and Precision

One recurring SHIFT pattern is fine adjustment.

For example:

```text
Turn parameter control
      │
      ▼
Normal movement
```

with SHIFT:

```text
SHIFT + Turn
      │
      ▼
Finer movement
```

The exact control depends on the mode.

But once you recognise the pattern, SHIFT becomes easier to remember.

---

# SHIFT and Transport

SHIFT also modifies several transport controls.

Verified DrivenByMoss examples include:

```text
SHIFT + PLAY
   → Toggle Repeat
```

and:

```text
SHIFT + RECORD
   → Toggle Launcher overdub
```

and:

```text
SHIFT + OVR
   → Toggle Launcher overdub
```

So SHIFT does not always mean precision.

Its actual meaning remains contextual.

---

# SHIFT and REDO

The UNDO button also follows a familiar modifier pattern:

```text
UNDO
   → Undo
```

while:

```text
SHIFT + UNDO
   → Redo
```

This is a particularly easy combination to remember because the two actions form an obvious pair.

---

# SHIFT and the Metronome

DrivenByMoss also provides:

```text
SHIFT + METRONOME
   → Toggle metronome ticks
```

and:

```text
SHIFT + Master Fader
   → Metronome volume
```

These two controls belong to the same general recording and timing workflow.

---

# OPTION

OPTION frequently gives a control an **alternative action**.

Examples include:

```text
OPTION + MARKER
   → Create marker
```

```text
OPTION + REWIND
   → Previous marker
```

```text
OPTION + FORWARD
   → Next marker
```

```text
OPTION + TRACK
   → Pin cursor track
```

```text
OPTION + DEVICE
   → Pin cursor device
```

OPTION often changes not merely the degree of an operation, but **what the operation does**.

A useful shorthand is:

> **OPTION often means: give me the alternative operation.**

---

# OPTION + BANK and CHANNEL

Chapter 4 introduced an especially important distinction.

Normally:

```text
BANK
   → move through track bank by 8

CHANNEL
   → move through track bank by 1
```

With OPTION:

```text
OPTION + BANK
   → move selected device left / right
```

and:

```text
OPTION + CHANNEL
   → move selected track left / right
```

This is a major change in meaning.

Without OPTION:

```text
I move my view
```

With OPTION:

```text
I move an object in the project
```

That is exactly the kind of difference worth recognising before pressing the modifier casually.

---

# OPTION and the Jog Wheel

DrivenByMoss also gives OPTION a clear Jog Wheel role:

```text
OPTION + Jog Wheel
   → Change Tempo
```

Add SHIFT:

```text
OPTION + SHIFT + Jog Wheel
   → Fine Tempo adjustment
```

This illustrates how modifiers can combine.

OPTION determines **what** is being controlled.

SHIFT modifies **how precisely** it is being controlled.

---

# CONTROL

CONTROL often exposes another structural or specialised function.

For example:

```text
CONTROL + Jog Wheel
   → Change Loop Start
```

and:

```text
CONTROL + SHIFT + Jog Wheel
   → Fine Loop Start adjustment
```

Again:

```text
CONTROL
   → choose the parameter

SHIFT
   → refine the movement
```

---

# CONTROL and Devices

In Device Mode, CONTROL becomes especially useful.

Hold CONTROL and DrivenByMoss exposes the devices on the selected track.

Conceptually:

```text
Hold CONTROL
      │
      ▼
Devices shown on V-Pots
      │
      ▼
Press V-Pot
      │
      ▼
Select Device
```

So CONTROL can act as a temporary direct-selection context.

This is much faster than stepping device-by-device when you already know which one you want.

---

# CONTROL + SELECT

CONTROL also modifies the channel SELECT buttons.

DrivenByMoss documents:

```text
CONTROL + SELECT
   → Open / Close Group folder
```

This is distinct from hierarchical Group navigation.

Hierarchical navigation uses:

```text
SELECT again
   → enter Group
```

whereas:

```text
CONTROL + SELECT
   → open / close Group folder
```

changes the Group's expanded state.

---

# ALT

ALT is another modifier used for specialised parameter operations.

A clear example is the Jog Wheel:

```text
ALT + Jog Wheel
   → Change Loop Length
```

and:

```text
ALT + SHIFT + Jog Wheel
   → Fine Loop Length adjustment
```

So the Jog Wheel now has several modifier layers:

```text
Jog Wheel
   → Position

SHIFT + Jog Wheel
   → Fine Position

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

This is one of the clearest examples of the modifier system.

---

# One Control, Several Parameters

Without modifiers:

```text
Jog Wheel
   → Position
```

With modifiers:

```text
OPTION
   → Tempo

CONTROL
   → Loop Start

ALT
   → Loop Length
```

and then:

```text
SHIFT
   → finer movement
```

The Jog Wheel has not changed.

Its context has.

---

# V-Pot Press Modifiers

The V-Pots provide another excellent modifier pattern.

DrivenByMoss documents these general press behaviours:

```text
Press V-Pot
   → Reset parameter to default
```

```text
SHIFT + Press V-Pot
   → Centre value
```

```text
CONTROL + Press V-Pot
   → Minimum value
```

```text
ALT + Press V-Pot
   → Maximum value
```

And when the V-Pot controls a Send:

```text
OPTION + Press V-Pot
   → Toggle Send on / off
```

This gives the V-Pot press a compact family of related functions.

---

# A Useful V-Pot Mental Model

Think:

```text
PRESS
   → default
```

then:

```text
SHIFT
   → centre
```

```text
CONTROL
   → minimum
```

```text
ALT
   → maximum
```

```text
OPTION
   → context-specific alternate action
```

This pattern is especially useful because it gives physical access to values that might otherwise require precise mouse work.

---

# OPTION + V-Pot Is Contextual

OPTION + V-Pot press is particularly important because its meaning depends on the current assignment.

For a Send:

```text
OPTION + Press
   → toggle Send on / off
```

In other contexts, OPTION can provide another context-specific action.

So do not learn OPTION as:

> **OPTION always means X.**

Instead:

> **OPTION asks for the alternative action appropriate to the current context.**

---

# SELECT Modifiers

The SELECT row is one of the most heavily modified parts of the X-Touch.

Verified DrivenByMoss uses include:

```text
SHIFT + SELECT
   → Multi-select tracks
```

```text
OPTION + SELECT
   → Stop playing clip on that track
```

```text
CONTROL + SELECT
   → Open / Close Group folder
```

```text
ALT + SELECT
   → Set New Clip Length
```

and:

```text
SEND + SELECT
   → Select Send 1–8
```

We looked at these in Chapter 6.

The important point here is that the modifiers do not merely change a button's label.

They change the **question the button answers**.

---

# The Same SELECT Button, Different Questions

Normal:

```text
SELECT
   → Which track do I want?
```

OPTION:

```text
OPTION + SELECT
   → Which track's playing clip
     do I want to stop?
```

CONTROL:

```text
CONTROL + SELECT
   → Which Group do I want
     to open or close?
```

ALT:

```text
ALT + SELECT
   → Which New Clip Length
     do I want?
```

SEND:

```text
SEND + SELECT
   → Which Send do I want?
```

The physical row remains the same.

The context changes the meaning.

---

# Modifiers Can Be Combined

Modifiers do not necessarily operate one at a time.

For example:

```text
OPTION + SHIFT + PLAY
   → Toggle Punch Out
```

while:

```text
OPTION + PLAY
   → Toggle Punch In
```

Likewise:

```text
OPTION + SHIFT + Jog Wheel
```

combines OPTION's Tempo context with SHIFT's fine-adjustment behaviour.

So the pattern can be:

```text
Modifier 1
   → choose alternate function

Modifier 2
   → refine that function
```

This is one reason the X-Touch can expose so much functionality without becoming physically enormous.

---

# Order of Pressing

When this guide writes:

```text
OPTION + MARKER
```

it means:

1. hold OPTION;
2. press MARKER;
3. release the buttons.

Likewise:

```text
CONTROL + SHIFT + Jog Wheel
```

means:

1. hold CONTROL;
2. hold SHIFT;
3. turn the Jog Wheel;
4. release the modifiers.

The `+` symbol means:

> **Use these controls together.**

It does not mean you should perform them as a rapid sequential shortcut.

---

# Modifier Buttons and Modes Work Together

Modifiers do not replace modes.

They operate **inside** them.

For example, Device Mode already changes what the V-Pots mean.

Then CONTROL can temporarily change that Device Mode context again:

```text
DEVICE Mode
     │
     ▼
V-Pots = Device Parameters
```

then:

```text
Hold CONTROL
     │
     ▼
V-Pots = Device Choices
```

Similarly:

```text
Hold OPTION
     │
     ▼
V-Pots = Parameter Page Choices
```

So the complete meaning of a control can depend on:

```text
Physical Control
      +
Current Mode
      +
Current Focus
      +
Held Modifier
      =
Current Function
```

This is the core architecture of the X-Touch + DrivenByMoss workflow.

---

# Modifiers Often Change Scale

Another useful pattern is that modifiers can change the **scale** of an operation.

For example:

```text
ARM
   → this track
```

while:

```text
SHIFT + ARM
   → record-arm across the active bank
```

Likewise:

```text
CHANNEL
   → move the view
```

while:

```text
OPTION + CHANNEL
   → move the track itself
```

The modifier can therefore make an operation broader, deeper or more consequential.

---

# Some Modified Commands Are Consequential

Not every modifier command is harmless.

For example:

```text
OPTION + CHANNEL
   → move selected track
```

and:

```text
OPTION + BANK
   → move selected device
```

actually change the Bitwig project structure.

Likewise:

```text
OPTION + RECORD
```

creates a clip and enables overdub.

So one good habit is:

> **Know whether a modified command changes the view, changes a value, or changes the project itself.**

That distinction helps prevent surprises.

---

# Modifiers Are Easier to Learn in Context

It would be possible to create an enormous table containing:

```text
SHIFT + every control

OPTION + every control

CONTROL + every control

ALT + every control
```

That would be complete.

It would also be difficult to learn.

A better approach is:

> **Learn each modified command with the job it performs.**

So:

```text
OPTION + MARKER
```

belongs with markers.

```text
OPTION + RECORD
```

belongs with recording.

```text
CONTROL + V-Pot
```

belongs with device selection.

```text
ALT + Jog Wheel
```

belongs with loop manipulation.

This reduces the feeling that the controller contains hundreds of unrelated shortcuts.

---

# Modifier Patterns Are Tendencies, Not Rules

There are some useful patterns:

```text
SHIFT
   → fine / secondary / reverse
```

```text
OPTION
   → alternate operation
```

```text
CONTROL
   → structural / direct-selection operation
```

```text
ALT
   → specialised parameter or maximum-type operation
```

But these are **not universal rules**.

For example:

```text
OPTION + MARKER
   → create marker
```

cannot be derived mechanically from a universal definition of OPTION.

You simply learn it as part of the Marker workflow.

Patterns reduce memory load.

They do not replace actual mappings.

---

# The Displays Are Part of the Modifier System

Because modifiers can change what controls mean, feedback becomes especially important.

Suppose a V-Pot normally controls:

```text
Pan
```

but after changing mode and holding a modifier it now represents:

```text
Device 4
```

The hardware did not physically move.

Without feedback, that would be confusing.

So when using modifiers:

> **Look at what the controller tells you.**

A useful cycle is:

```text
Hold Modifier
      ↓
Assignments change
      ↓
Displays / LEDs update
      ↓
Confirm context
      ↓
Act
```

The X-Touch is meant to be read as well as touched.

---

# SHIFT and Launcher-Oriented Work

DrivenByMoss contains a preference called:

```text
Flip arranger and clip record / automation
```

This can reverse the normal-versus-SHIFT relationship for certain Arranger and Clip recording/automation functions.

That means commands such as:

```text
RECORD
```

and:

```text
SHIFT + RECORD
```

may behave differently for users who have deliberately enabled that preference.

This is an important reminder:

> **A modifier mapping can be affected by configuration.**

Project XTC describes the normal mapping unless otherwise stated.

Chapter 21 discusses the configuration option itself.

---

# Don't Memorise Everything at Once

This chapter contains a lot of examples.

You do not need to learn all of them now.

Start with a small core:

```text
SHIFT + control
   → related / fine function
```

```text
OPTION + control
   → alternative function
```

Then add practical combinations as you encounter them.

For example:

```text
SHIFT + UNDO
   → Redo
```

```text
OPTION + MARKER
   → Create marker
```

```text
OPTION + REWIND / FORWARD
   → Marker navigation
```

```text
OPTION + DEVICE
   → Pin device
```

The repeated use will turn them into muscle memory.

---

# A Practical Jog Wheel Exercise

The Jog Wheel is an excellent way to experience the modifier system.

Start with:

```text
Jog Wheel
   → change position
```

Then try:

```text
SHIFT + Jog Wheel
   → fine position
```

Then:

```text
OPTION + Jog Wheel
   → tempo
```

Then:

```text
CONTROL + Jog Wheel
   → loop start
```

Then:

```text
ALT + Jog Wheel
   → loop length
```

Finally add SHIFT to those modifier combinations for finer adjustment.

The point of the exercise is not merely to manipulate the transport.

It is to feel one physical control becoming several different controls through context.

---

# A Practical V-Pot Exercise

Choose a parameter controlled by a V-Pot.

Try:

```text
Press
```

to reset it to default.

Then:

```text
SHIFT + Press
```

for centre.

Then:

```text
CONTROL + Press
```

for minimum.

Then:

```text
ALT + Press
```

for maximum.

If the current V-Pot is controlling a Send, try:

```text
OPTION + Press
```

to toggle the Send.

Again, the aim is to feel the pattern physically rather than memorise a table.

---

# A Useful Mental Model

Earlier we had:

```text
Physical Control
      │
      ▼
Current Function
```

Then modes added:

```text
Physical Control
      +
Current Mode
      =
Current Function
```

Now modifiers extend the model:

```text
Physical Control
      +
Current Focus
      +
Current Mode
      +
Modifier, if held
      =
Current Function
```

This explains how one V-Pot, button or wheel can participate in so many workflows without the surface becoming physically enormous.

---

# The Important Idea

Modifiers do not create a second controller hidden underneath the first.

They temporarily reshape the controller you already know.

The four main modifiers are:

```text
SHIFT
OPTION
CONTROL
ALT
```

Some useful recurring patterns are:

```text
SHIFT
   → finer / related / reverse
```

```text
OPTION
   → alternate operation
```

```text
CONTROL
   → structural or direct-selection operation
```

```text
ALT
   → specialised parameter operation
```

But always remember:

> **The exact meaning depends on context.**

The most useful approach is not to memorise every possible combination.

Learn the modifier vocabulary.

Then learn individual combinations as part of real tasks.

That way:

```text
OPTION + MARKER
```

is not an arbitrary shortcut.

It belongs to the Marker workflow.

```text
OPTION + RECORD
```

belongs to recording.

```text
CONTROL + Jog Wheel
```

belongs to loop editing.

```text
ALT + Press V-Pot
```

belongs to parameter control.

The job gives the shortcut meaning.

---

## Coming Next

Now that we understand the modifier vocabulary, we can apply it to one of the most important physical controls on the X-Touch:

**the V-Pots.**

Their rotary movement, push action, LED rings and modifier behaviours make them far more capable than a simple row of knobs.

Next:

**V-Pots (Rotary Encoders).**
