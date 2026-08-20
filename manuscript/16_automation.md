---
chapter: 16
title: "Automation"
status: draft
---

# Automation

The motor faders on the X-Touch do something rather special.

Move a fader and Bitwig responds.

Change the same parameter in Bitwig and the physical fader moves.

We saw this two-way relationship earlier:

```text
You move the fader
        │
        ▼
      Bitwig

      Bitwig
        │
        ▼
The fader moves
```

Automation adds another dimension.

Bitwig can **remember the movement**.

Instead of a fader representing one fixed value, it can become part of a performance that changes over time.

---

## From Position to Movement

Suppose a track begins quietly and gradually becomes louder.

Without automation, we might set the fader to one compromise level.

With automation, we can perform the change:

```text
quiet                           loud
  │                               │
  ▼                               ▼
  ────────╱────────────────────────
         ╱
        ╱
```

Bitwig records the changing value.

When the project plays again, that movement can be reproduced.

And because the X-Touch has motorised faders, the physical fader can move with it.

That is one of the moments when a control surface stops feeling like a remote control and starts feeling like part of the DAW.

---

## Automation Is About Behaviour

The X-Touch provides buttons for several automation modes:

- READ/OFF
- WRITE
- TOUCH
- LATCH
- TRIM

The names can look like a list that needs to be memorised.

A more useful way to understand them is to ask three questions:

```text
What happens before I touch the control?

What happens while I move it?

What happens when I release it?
```

For a touch-sensitive motor fader, that gives us a simple model:

```text
Touch
  ↓
Move
  ↓
Release
  ↓
What happens now?
```

The answer depends on the automation mode.

---

## READ/OFF

The **READ/OFF** button controls automation playback.

In normal automation reading, Bitwig follows automation that has already been recorded.

Conceptually:

```text
Recorded automation
        │
        ▼
      Bitwig
        │
        ▼
   Motor fader
```

The physical fader follows the changing automated value.

This is useful feedback.

You can see and feel the automation happening rather than merely watching a line move on the screen.

---

## Automation Playback

Imagine that a track contains this volume automation:

```text
Volume

high          ──────
             ╱
            ╱
low  ──────
     ───────────────────► time
```

During playback, the X-Touch fader follows it:

```text
Bitwig automation
       │
       ▼
Motor position
       │
       ▼
Fader moves
```

Do not fight the fader while simply reading automation.

Its movement is information.

The controller is showing you what the project is doing.

---

## WRITE

**WRITE** is the most direct automation-writing mode.

When Write is active, movements of an automated parameter are written into the project.

Conceptually:

```text
WRITE active
     │
     ▼
Move fader
     │
     ▼
New value written
     │
     ▼
Automation continues to be written
```

Write is powerful precisely because it is direct.

It also deserves care.

If you leave Write active while playing through a section, you may overwrite automation that you intended to keep.

Think of WRITE as:

> **Keep writing the current control state into the automation.**

That makes it useful when deliberately replacing an automation passage.

---

## TOUCH

**TOUCH** makes particular sense with the X-Touch because the faders are touch-sensitive.

The important event is not merely moving the fader.

It is **touching it**.

Conceptually:

```text
Existing automation plays
          │
          ▼
     Touch fader
          │
          ▼
You take control
          │
          ▼
      Move fader
          │
          ▼
New movement is written
          │
          ▼
    Release fader
          │
          ▼
Existing automation resumes
```

This is one of the most natural ways to make corrections to an existing automation pass.

You can listen to the automated mix, reach for the fader when something needs changing, make the adjustment, and let go.

Bitwig then resumes control.

---

## Touch as an Override

The relationship can be thought of as a temporary handover:

```text
Bitwig
  │
  │ automation playing
  ▼
Fader
  │
  │ you touch it
  ▼
 YOU
  │
  │ you release it
  ▼
Bitwig
```

This is where touch sensitivity becomes much more than a hardware specification.

The fader knows when you have deliberately put your hand on it.

That lets Bitwig distinguish between:

> **The motor is moving the fader**

and:

> **The user is moving the fader.**

That distinction is fundamental to touch automation.

---

## LATCH

**LATCH** begins similarly to Touch.

Existing automation can play until you touch and move the control.

The important difference appears when you release it.

Conceptually:

```text
Existing automation
        │
        ▼
   Touch fader
        │
        ▼
   Take control
        │
        ▼
    Move fader
        │
        ▼
  Release fader
        │
        ▼
New value remains latched
```

Instead of immediately returning to the previously recorded automation, the new value continues.

That makes Latch useful when you want to establish a new level and keep it there.

---

## TOUCH and LATCH Compared

These two modes are easier to understand side by side.

### TOUCH

```text
automation
    │
    ▼
  touch
    │
    ▼
your movement
    │
    ▼
 release
    │
    ▼
automation resumes
```

### LATCH

```text
automation
    │
    ▼
  touch
    │
    ▼
your movement
    │
    ▼
 release
    │
    ▼
new value continues
```

The key difference is therefore not what happens while you are holding the fader.

It is what happens **after you let go**.

---

## Choosing Between TOUCH and LATCH

Suppose a vocal is slightly too loud for one phrase.

TOUCH is a natural choice:

```text
normal level
    ↓
phrase arrives
    ↓
touch fader
    ↓
pull it down
    ↓
phrase ends
    ↓
release
    ↓
previous automation resumes
```

Now suppose a synth needs to become quieter from the second chorus onwards.

LATCH may make more sense:

```text
second chorus
    ↓
touch fader
    ↓
lower level
    ↓
release
    ↓
new level continues
```

The mode follows the musical intention.

---

## TRIM

TRIM is associated with automation adjustment rather than simply replacing the existing automation shape.

The useful concept is **relative change**.

Imagine that you already have a detailed automation performance:

```text
       ╱╲
  ╱───╯  ╲──╮
─╯          ╰────
```

You like its movement, but the whole passage needs to sit a little lower.

Conceptually, trimming means:

```text
existing shape
      +
relative adjustment
      =
same general shape at a new level
```

In the current DrivenByMoss MCU mapping, the TRIM control maps to Bitwig's available automation behaviour rather than providing a separate traditional console-style trim system.

For that reason, it is best to think of the X-Touch's automation buttons as controls over the automation modes Bitwig actually provides, rather than assuming that every label on the MCU surface corresponds to an identically named DAW function.

---

## The Labels Belong to the MCU

This is an important general point.

The X-Touch follows the Mackie Control layout.

Its buttons therefore carry labels such as:

```text
READ/OFF
WRITE
TRIM
TOUCH
LATCH
```

But the controller is being used with **Bitwig through DrivenByMoss**.

The printed label tells us where the control came from.

DrivenByMoss determines what that control does in Bitwig.

So:

> **Trust the current DrivenByMoss mapping, not assumptions based solely on the button legend.**

This principle applies elsewhere on the X-Touch too.

---

## Resetting Automation Overrides

DrivenByMoss also provides a way to reset automation overrides.

Use:

```text
OPTION + READ/OFF
```

to reset overrides.

This is useful when manual intervention has left parameters overriding their normal automated state.

Conceptually:

```text
Automation
    │
    ▼
Manual override
    │
    ▼
OPTION + READ/OFF
    │
    ▼
Reset override
```

It gives you a quick route back to the automation-controlled state.

---

## Performing Automation

Automation does not have to be drawn.

It can be **performed**.

That distinction is especially important with a control surface.

Suppose you want a delay return to rise dramatically into the end of a phrase.

With a mouse, you might create automation points and draw a curve.

With the X-Touch, you can approach the same problem musically:

```text
Play
  ↓
Listen
  ↓
Touch control
  ↓
Ride the level
  ↓
Release
```

The automation becomes a recorded gesture.

That is much closer to the way levels were traditionally ridden on a mixing console.

---

## The First Pass Does Not Have to Be Perfect

One advantage of automation modes such as Touch is that automation can be refined.

A workflow might be:

```text
First pass
   │
   ▼
Capture the broad movement
   │
   ▼
Listen again
   │
   ▼
Touch only where needed
   │
   ▼
Correct the problem area
```

This is often more natural than trying to perform an entire complicated automation move perfectly in one pass.

Automation can be treated like any other performance:

record it, listen, and improve it.

---

## Automation and the Motor Fader

The motor fader gives us a particularly clear feedback loop:

```text
             You
              │
              ▼
         Motor Fader
              │
              ▼
            Bitwig
              │
              ▼
         Automation
              │
              ▼
            Bitwig
              │
              ▼
         Motor Fader
```

Information travels both ways.

When you perform a move, the X-Touch sends control information to Bitwig.

When Bitwig plays the automation back, it sends the resulting state back to the X-Touch.

The fader therefore becomes both:

- an **input device**;
- an **output display**.

That is one of the defining advantages of a motorised control surface.

---

## Don't Grab a Moving Fader Casually

A moving motor fader is telling you that Bitwig is controlling that parameter.

Touching it may have meaning depending on the current automation mode.

So before grabbing a moving fader, know which automation mode is active.

In READ, you may simply be inspecting playback.

In TOUCH, touching the fader may deliberately hand control to you.

In WRITE, your actions may replace automation.

The same physical gesture can therefore have very different consequences.

The current mode matters.

---

## Automation Is Not Just Volume

Faders make volume automation particularly obvious, but automation in Bitwig is much broader.

Parameters throughout the project can change over time.

The X-Touch may expose those parameters through:

- faders;
- V-Pots;
- Device Mode;
- mixer edit modes;
- FLIP.

So the same general automation ideas apply beyond channel volume.

Conceptually:

```text
Physical control
      │
      ▼
Bitwig parameter
      │
      ▼
Automation
```

If the parameter is automatable and the current X-Touch context gives you control over it, the surface can become part of the automation workflow.

---

## FLIP and Automation

FLIP becomes particularly interesting here.

Suppose a parameter is normally assigned to a V-Pot.

FLIP may allow that parameter to be placed on a fader.

That gives the parameter:

- longer physical travel;
- touch sensitivity;
- motorised position feedback.

So FLIP is not merely a convenience for mixing.

It can change the **physical way in which an automation performance is made**.

For expressive automation, that can be significant.

---

## Watching Automation Come Back

There is something worth doing at least once simply to understand the system.

Record a deliberate fader movement.

Then:

1. stop;
2. return to a point before the movement;
3. enable the appropriate automation playback;
4. press PLAY;
5. take your hand away.

Watch the fader reproduce what you performed.

The movement you made has become part of the project.

That simple demonstration makes the feedback loop tangible:

```text
You moved it
     ↓
Bitwig remembered it
     ↓
Bitwig plays it
     ↓
The X-Touch moves it
```

---

## A Practical Automation Workflow

A straightforward automation pass might look like this.

### 1. Choose the parameter

For example, track volume.

### 2. Choose the automation mode

For an existing automated mix that needs correction, TOUCH may be appropriate.

### 3. Start playback

Listen rather than watching the screen.

### 4. Touch the fader

Take control when the musical moment arrives.

### 5. Perform the movement

Ride the level by ear.

### 6. Release

In TOUCH, Bitwig can return to the existing automation behaviour.

### 7. Play the section again

Listen to the result while the motor fader reproduces the automation.

### 8. Correct it if necessary

Automation is editable and repeatable.

You are not committing to a one-take performance.

---

## Automation and Mouse-Lite Working

Automation provides another example of why a control surface can change the relationship with a DAW.

With a mouse, automation often encourages this:

```text
Look
  ↓
Point
  ↓
Click
  ↓
Draw
  ↓
Adjust
```

With a touch-sensitive fader:

```text
Listen
  ↓
Touch
  ↓
Move
  ↓
Release
```

Neither approach is universally better.

Drawing automation is invaluable when exact editing is required.

But for a musical gesture, the physical approach can be far more immediate.

The aim of Project XTC is not to prohibit the mouse.

It is to make reaching for it **a choice rather than a reflex**.

---

## Automation as Performance

This leads to perhaps the most useful way to think about automation with the X-Touch.

Do not think only:

> **I am programming a parameter change.**

Think:

> **I am performing a parameter change and asking Bitwig to remember it.**

That shift in perspective matters.

A fade becomes something you play.

A send ride becomes something you play.

A filter movement becomes something you play.

And because the X-Touch can reproduce the resulting movement, the surface remains connected to that performance afterwards.

---

## The Important Idea

The automation buttons determine what happens when control passes between **Bitwig and you**.

The key questions are:

```text
Before I touch:
Who has control?

While I move:
What is being written?

When I release:
What happens next?
```

That makes the main modes easier to distinguish:

```text
WRITE
   → write automation directly

TOUCH
   → take control while touched,
     then return to automation

LATCH
   → take control,
     then retain the new value

READ/OFF
   → control automation playback state

OPTION + READ/OFF
   → reset automation overrides
```

And the motor fader makes that relationship physical.

You move it.

Bitwig remembers.

Then Bitwig moves it back.

---

## Coming Next

So far, most of our navigation has treated the eight visible channels as a relatively flat bank.

But Bitwig projects can contain structures within structures:

- groups;
- instruments;
- layers;
- drum pads.

DrivenByMoss allows the X-Touch to navigate those structures too.

Next we will look at:

**Groups, Layers and Drum Pads.**
