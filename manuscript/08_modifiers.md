---
chapter: 8
title: "Modifiers: SHIFT, OPTION, CONTROL and ALT"
---

# Modifiers: SHIFT, OPTION, CONTROL and ALT

So far, most of the controls in this guide have been considered one at a time.

Press a button.

Turn a V-Pot.

Move a fader.

But the X-Touch has far more functions than it has physical controls.

One of the ways DrivenByMoss solves this is through **modifier buttons**.

The four important modifiers are:

- SHIFT
- OPTION
- CONTROL
- ALT

Hold one of these while operating another control, and the second control may perform a different function.

If you are familiar with keyboard shortcuts, the principle is already familiar:

```text
control
   +
modifier
   =
another function
```

The important thing is not to memorise every possible combination immediately.

It is to understand the pattern.

---

## One Surface, More Functions

Consider a control we already know: the Jog Wheel.

Turn it normally and it changes the transport position.

But DrivenByMoss can reinterpret that same physical movement when a modifier is held:

```text
Jog Wheel
    │
    ├── normally       → transport position
    │
    ├── OPTION         → tempo
    │
    ├── CONTROL        → loop start
    │
    └── ALT            → loop length
```

The Jog Wheel has not physically changed.

Its **context** has.

This is the same principle introduced earlier in this guide when we looked at modes.

A modifier creates a temporary context.

---

## Modifiers Are Temporary Modes

There is a useful way to think about the four modifier buttons:

> **Holding a modifier temporarily changes the meaning of another control.**

A normal mode may remain active until you leave it.

A modifier usually lasts only while you hold its button.

Conceptually:

```text
Normal context
      │
      │ hold OPTION
      ▼
OPTION context
      │
      │ release OPTION
      ▼
Normal context
```

This makes modifiers particularly useful for secondary operations.

The main function remains immediately available, while the less frequently needed function sits behind a modifier.

---

## SHIFT

SHIFT is probably the modifier you will encounter most often.

It frequently provides:

- a secondary version of an operation;
- finer control;
- reverse movement through a sequence.

For example, when adjusting some continuous parameters, SHIFT gives finer resolution.

With the Jog Wheel:

```text
Jog Wheel
    → move transport position

SHIFT + Jog Wheel
    → move transport position more finely
```

In other contexts SHIFT selects a related secondary operation.

You will see examples throughout the following chapters.

Do not assume that SHIFT *always* means "fine adjustment", however.

Its exact meaning depends on the control and the current mode.

---

## OPTION

OPTION often changes **what the operation acts upon** or exposes a related operation.

For example, BANK and CHANNEL normally move the controller's view through the project.

With OPTION held, DrivenByMoss can instead use those controls to move objects within the project.

Conceptually:

```text
BANK / CHANNEL
      │
      ├── normally
      │      move the VIEW
      │
      └── OPTION
             move an OBJECT
```

OPTION is also important in several workflows we will meet later.

For example:

```text
OPTION + MARKER
```

creates a marker.

And:

```text
OPTION + REWIND
OPTION + FORWARD
```

navigate between markers.

OPTION therefore does not have one universal definition.

Think of it as:

> **Give this control its alternative operation.**

---

## CONTROL

CONTROL frequently exposes a structural operation or another dimension of control.

One particularly useful example appears in Device Mode.

Holding CONTROL allows the V-Pots to expose devices so that a particular device can be selected directly.

CONTROL also changes the Jog Wheel:

```text
CONTROL + Jog Wheel
```

adjusts the loop start.

With SHIFT added:

```text
CONTROL + SHIFT + Jog Wheel
```

provides finer adjustment.

Again, CONTROL does not have one fixed meaning.

The current mode still matters.

---

## ALT

ALT is another modifier used to expose alternative parameter operations.

With the Jog Wheel:

```text
ALT + Jog Wheel
```

adjusts loop length.

Adding SHIFT gives finer control:

```text
ALT + SHIFT + Jog Wheel
```

adjusts loop length more precisely.

ALT also appears in other specialised workflows, including operations concerned with clip length.

These will make more sense when we reach the relevant chapters.

---

## Modifiers Can Be Combined

Modifiers are not necessarily used alone.

SHIFT can be combined with another modifier.

The Jog Wheel gives us an excellent example:

| Control | Function |
|---|---|
| Jog Wheel | Transport position |
| SHIFT + Jog Wheel | Fine transport position |
| OPTION + Jog Wheel | Tempo |
| OPTION + SHIFT + Jog Wheel | Fine tempo |
| CONTROL + Jog Wheel | Loop start |
| CONTROL + SHIFT + Jog Wheel | Fine loop start |
| ALT + Jog Wheel | Loop length |
| ALT + SHIFT + Jog Wheel | Fine loop length |

There is a pattern here.

SHIFT does not change *what* OPTION, CONTROL or ALT selects.

Instead, it changes the **precision** with which that parameter is adjusted.

So:

```text
OPTION
   ↓
Tempo

OPTION + SHIFT
   ↓
Tempo, but finer
```

This is exactly the sort of relationship worth learning.

It reduces the number of apparently unrelated commands you need to remember.

---

## Modifier Patterns, Not Modifier Rules

You may already have noticed some tendencies:

```text
SHIFT
   → secondary / finer / reverse

OPTION
   → alternative operation

CONTROL
   → structural or additional control

ALT
   → another specialised parameter
```

These are useful mental shortcuts.

But they are **not rules**.

DrivenByMoss assigns modifier combinations according to what is useful in a particular context.

For example:

```text
OPTION + MARKER
```

creates a marker.

There is no useful way to derive "create marker" from a universal definition of OPTION.

You simply learn that command as part of the Marker workflow.

The purpose of recognising modifier patterns is therefore not to predict every command.

It is to make the controller easier to understand when you encounter one.

---

## Order Matters Less Than the Combination

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

The `+` notation means **use these controls together**.

It does not mean that you should press them as a rapid sequence.

---

## Modifier Buttons and Modes Work Together

Modifiers do not replace modes.

They work **inside** them.

This distinction is important.

Suppose the controller is in Device Mode.

The V-Pots already have meanings determined by Device Mode.

Now hold OPTION.

The V-Pots can acquire another set of meanings appropriate to that mode.

So the complete context may be thought of as:

```text
Physical control
      +
Current mode
      +
Held modifier
      =
Current function
```

This extends the mental model from Chapter 3.

The function of a physical control is not necessarily inherent in the control itself.

It emerges from context.

---

## The Display Is Your Ally

Modifier combinations can make the surface seem complicated if you try to remember everything from button labels alone.

Don't.

As discussed in Chapter 7, the displays are part of the control system.

When a modifier or mode changes what controls mean, look at the feedback the X-Touch and Bitwig provide.

The controller should be treated as a conversation:

```text
You change context
      ↓
DrivenByMoss changes assignments
      ↓
The displays provide feedback
      ↓
You make the next decision
```

This becomes especially important in Device Mode, Browser Mode and the advanced edit modes.

---

## Don't Learn the Modifier Table

It is tempting at this point to make a huge table containing every possible combination of:

```text
SHIFT
OPTION
CONTROL
ALT
```

with every button on the X-Touch.

That would turn this guide into exactly the kind of manual we are trying to avoid.

Instead, learn modifier combinations **with the task they perform**.

When we study markers, we will learn:

```text
OPTION + MARKER
```

because it is part of the marker workflow.

When we study Device Mode, we will learn CONTROL and OPTION combinations because they help navigate devices and parameter pages.

When we study recording, we will learn the RECORD modifiers because they make sense in the context of recording.

The modifier is not the subject.

**The job you are trying to do is the subject.**

---

## A Useful Mental Model

At this point we can expand our model of the X-Touch considerably.

Earlier we had:

```text
physical control
      ↓
current mode
      ↓
current function
```

Now we can add modifiers:

```text
                ┌──────────────┐
                │ Current Mode │
                └──────┬───────┘
                       │
                       ▼
┌────────────────┐   context   ┌─────────────────┐
│ Physical       │─────────────│ Current         │
│ Control        │             │ Function        │
└────────────────┘             └─────────────────┘
                       ▲
                       │
                ┌──────┴───────┐
                │ Modifier     │
                │ if held      │
                └──────────────┘
```

You do not need to consciously think through this diagram every time you touch the controller.

Its purpose is to explain why the same V-Pot, button or wheel can perform so many different jobs without the surface becoming physically enormous.

---

## What Comes Next

Now that we understand modifiers, the next chapters can use them without stopping repeatedly to explain what SHIFT, OPTION, CONTROL and ALT are.

We will see them applied to:

- V-Pots;
- motor faders;
- transport;
- the Jog Wheel;
- devices;
- Browser navigation;
- mixer modes;
- markers;
- automation;
- groups;
- recording.

The individual combinations will be introduced when they become useful.

---

## The Important Idea

If there is one thing to take away from this chapter, it is this:

> **A modifier temporarily changes the context of another control.**

You do not need to memorise every modifier combination.

Learn the basic controls first.

Then learn the modified versions as part of real workflows.

Once that pattern becomes familiar, SHIFT, OPTION, CONTROL and ALT stop looking like four more sets of commands to memorise.

They become something much more useful:

**four ways of asking the X-Touch to do a little more.**
