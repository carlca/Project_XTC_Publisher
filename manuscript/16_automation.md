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

The X-Touch provides five buttons in its AUTOMATION section:

```text
READ/OFF   WRITE   TRIM   TOUCH   LATCH
```

These labels come from the Mackie Control world.

DrivenByMoss maps them onto the automation modes that Bitwig actually provides.

The verified mapping is:

```text
READ/OFF
   → Disable Arranger automation recording

WRITE
   → Enable Arranger automation recording
     in Write mode

TRIM
   → Enable Read mode
     because Bitwig has no Trim mode

TOUCH
   → Enable Arranger automation recording
     in Touch mode

LATCH
   → Enable Arranger automation recording
     in Latch mode
```

There is also:

```text
OPTION + READ/OFF
   → Reset automation overrides
```

The important lesson is already familiar:

> **The words printed on the X-Touch tell us where the controls came from. DrivenByMoss determines what they do in Bitwig.**

---

## Three Useful Questions

The automation modes become easier to understand if we ask three questions:

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

Pressing **READ/OFF** disables Arranger automation recording.

This puts us back into the normal situation where existing automation can be read without our movements being written as a new automation pass.

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

Pressing **WRITE** enables Arranger automation recording in Write mode.

Write is the most direct of the automation-writing modes.

When Write is active, the current parameter values are written into the automation while the automation pass is running.

Conceptually:

```text
WRITE active
     │
     ▼
Automation recording
     │
     ▼
Current values written
     │
     ▼
Move control
     │
     ▼
New values written
```

Write is powerful precisely because it is direct.

It also deserves care.

If you leave Write active while playing through a section, you can replace automation that you intended to keep.

Think of WRITE as:

> **Write the current control state into the automation.**

That makes it useful when deliberately creating or replacing an automation passage.

---

## TOUCH

Pressing **TOUCH** enables Arranger automation recording in Touch mode.

TOUCH makes particular sense with the X-Touch because the faders are touch-sensitive.

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

That distinction is fundamental to Touch automation.

---

## LATCH

Pressing **LATCH** enables Arranger automation recording in Latch mode.

LATCH begins similarly to Touch.

Existing automation can play until you take control of the parameter.

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

Instead of immediately returning to the previously recorded automation, the new value continues to be written.

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
normal automation
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

## What About TRIM?

The X-Touch has a button labelled:

```text
TRIM
```

On some automation systems, Trim is a distinct mode for making relative changes to existing automation.

**Bitwig does not provide a Trim automation mode.**

DrivenByMoss therefore maps the X-Touch's TRIM button to:

```text
TRIM
   ↓
Read mode
```

This is important because we should not infer functionality from the word printed on the hardware.

Pressing TRIM does **not** give Bitwig a console-style Trim automation mode that Bitwig itself does not possess.

The button exists because it is part of the Mackie Control layout.

DrivenByMoss gives it the closest useful Bitwig behaviour.

---

## The Labels Belong to the MCU

TRIM gives us a particularly clear example of a principle that applies throughout the X-Touch.

The hardware carries labels such as:

```text
READ/OFF
WRITE
TRIM
TOUCH
LATCH
```

because those controls belong to the Mackie Control design.

But our actual system is:

```text
X-Touch
   │
   ▼
Mackie Control messages
   │
   ▼
DrivenByMoss
   │
   ▼
Bitwig
```

So:

> **Trust the current DrivenByMoss mapping, not assumptions based solely on the button legend.**

We have encountered the same principle elsewhere with controls such as USER, DROP and the function buttons.

---

## Resetting Automation Overrides

DrivenByMoss provides a particularly useful modified command:

```text
OPTION + READ/OFF
```

This resets automation overrides.

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

This gives you a quick way to clear overridden automation states and return parameters to normal automation control.

---

## Arranger Automation

There is one more important word in the mappings above:

**Arranger.**

The automation buttons normally control **Arranger automation recording**.

That distinction becomes important because Bitwig also has its Launcher environment.

As we saw in Chapter 19, Arranger and Launcher recording states are related but separate concepts.

DrivenByMoss also provides configuration that can change the priority between Arranger and Clip automation behaviour.

We will return to that in Chapter 21.

For now, the normal automation-button model is:

```text
Automation buttons
       │
       ▼
Arranger automation
```

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

With automation recording disabled, you may simply be observing playback.

In TOUCH, touching the fader can deliberately hand control to you.

In WRITE, parameter states may be written continuously.

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
- Mixer Edit Modes;
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

FLIP can place the relevant control onto a fader in supported contexts.

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
3. disable automation recording;
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

In TOUCH, Bitwig returns to the existing automation behaviour.

### 7. Play the section again

Disable automation recording if necessary and listen to the result while the motor fader reproduces the automation.

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

A Send ride becomes something you play.

A filter movement becomes something you play.

And because the X-Touch can reproduce the resulting movement, the surface remains connected to that performance afterwards.

---

## The Important Idea

The automation buttons determine what happens when control passes between **Bitwig and you**.

The verified normal mappings are:

```text
READ/OFF
   → Disable Arranger automation recording

WRITE
   → Write mode

TRIM
   → Read mode
     (Bitwig has no Trim mode)

TOUCH
   → Touch mode

LATCH
   → Latch mode

OPTION + READ/OFF
   → Reset automation overrides
```

For Touch and Latch, the particularly useful question is:

```text
Before I touch:
Who has control?

While I move:
What is being written?

When I release:
What happens next?
```

And the motor fader makes that relationship physical.

You move it.

Bitwig remembers.

Then Bitwig moves it back.

---

## Coming Next

So far, most of our navigation has treated the eight visible channels as a relatively flat bank.

But Bitwig projects can contain structures within structures:

- Groups;
- instruments;
- layers;
- drum pads.

DrivenByMoss allows the X-Touch to navigate those structures too.

Next we will look at:

**Groups, Layers and Drum Pads.**
