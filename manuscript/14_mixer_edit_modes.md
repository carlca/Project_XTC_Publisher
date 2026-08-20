---
chapter: 14
title: "Mixer Edit Modes"
status: draft
---

# Mixer Edit Modes

By now, we have become used to an important characteristic of the X-Touch:

> **The physical controls stay in the same place, but what they control can change.**

The eight channel strips normally give us a familiar view of the mixer.

We have faders for track levels, V-Pots for parameters, and buttons for operations such as SELECT, MUTE, SOLO and ARM.

DrivenByMoss can take this idea further.

Instead of thinking only in terms of eight complete channel strips, we can temporarily ask the X-Touch to concentrate on **one particular aspect of the mixer**.

That is the idea behind the mixer edit modes.

---

## Looking Across the Mixer

Imagine eight tracks:

```text
Track 1   Track 2   Track 3   Track 4   Track 5   Track 6   Track 7   Track 8
```

There are several different ways we might want to look across them.

We could ask:

```text
What are their volumes?
```

or:

```text
What are their panorama positions?
```

or:

```text
How much of each track is being sent to Send 1?
```

The tracks have not changed.

What changes is the **dimension of the mixer that we are looking at**.

Conceptually:

```text
                    Tracks 1–8
                        │
          ┌─────────────┼─────────────┐
          │             │             │
          ▼             ▼             ▼
       Volume       Panorama        Sends
```

This is a useful way to understand the mixer edit modes.

---

## Track Edit Mode

Press **TRACK** to enter Track Edit Mode.

Rather than treating each V-Pot simply as the normal control for its channel strip, Track Edit Mode exposes parameters associated with the selected track.

This gives the V-Pots another role:

```text
Selected Track
      │
      ▼
Track Edit Mode
      │
      ▼
V-Pots → Track Parameters
```

The precise parameters available can depend on the current DrivenByMoss configuration.

The important point is the change in perspective.

We are no longer primarily looking **across eight tracks**.

We are looking more deeply at **one selected track**.

---

## Volume Edit Mode

Press **TRACK** again and DrivenByMoss switches to Volume Edit Mode.

Now the V-Pots provide another way of controlling the volumes of the eight tracks in the current bank.

Conceptually:

```text
V-Pot 1  → Track 1 Volume
V-Pot 2  → Track 2 Volume
V-Pot 3  → Track 3 Volume
...
V-Pot 8  → Track 8 Volume
```

Of course, the X-Touch already has eight motor faders.

So why would we want volume on the V-Pots as well?

One answer is **FLIP**, which we met earlier.

The ability to exchange the roles of faders and rotary controls becomes much more useful when the controller can present parameters in different ways.

The important lesson is not that one control is the "correct" way to adjust volume.

It is that DrivenByMoss allows the surface to be reorganised around the task.

---

## Panorama Edit Mode

Press **PAN** to enter Panorama Edit Mode.

The eight V-Pots now control the panorama positions of the eight tracks in the current bank:

```text
V-Pot 1  → Track 1 Pan
V-Pot 2  → Track 2 Pan
V-Pot 3  → Track 3 Pan
...
V-Pot 8  → Track 8 Pan
```

This is perhaps the clearest example of an edit mode.

Instead of thinking:

```text
Channel 1
   ├── Volume
   ├── Pan
   ├── Mute
   └── Solo
```

we temporarily rotate our view through ninety degrees and think:

```text
Pan
   ├── Track 1
   ├── Track 2
   ├── Track 3
   ├── ...
   └── Track 8
```

The information is the same.

The **view onto it** has changed.

---

## Fine Adjustment with SHIFT

As we saw in Chapter 8, SHIFT frequently provides finer adjustment of continuous parameters.

That pattern applies here too.

Hold **SHIFT** while turning a V-Pot when you need more precise control.

Conceptually:

```text
Turn V-Pot
     ↓
Normal adjustment

SHIFT + Turn V-Pot
     ↓
Finer adjustment
```

This is a good example of why we introduced modifiers before exploring the advanced modes.

The modifier itself is no longer something new to learn.

We simply apply an existing idea to a new task.

---

## Send Edit Modes

The SEND control opens another particularly useful family of mixer views.

Press **SEND** and the V-Pots control a Send across the eight tracks.

For example, in the first Send mode:

```text
             SEND 1

Track 1  ─────────────► Send 1
Track 2  ─────────────► Send 1
Track 3  ─────────────► Send 1
Track 4  ─────────────► Send 1
Track 5  ─────────────► Send 1
Track 6  ─────────────► Send 1
Track 7  ─────────────► Send 1
Track 8  ─────────────► Send 1
```

The eight V-Pots now answer one question:

> **How much of each track is being sent to this destination?**

This is an especially natural way to work with effects sends.

If Send 1 feeds a reverb, for example, you can adjust the amount of reverb for eight tracks without changing the basic mixer bank.

---

## Moving Through the Sends

A project may contain more than one Send.

Repeated presses of **SEND** move through the available Send modes.

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
  ↓
...
```

DrivenByMoss supports Send modes 1–8.

Hold **SHIFT** while pressing SEND to move through the Sends in the opposite direction.

So:

```text
SEND
   → next Send

SHIFT + SEND
   → previous Send
```

This is another modifier pattern we have already encountered:

SHIFT can provide the related or reverse operation.

---

## Jumping Directly to a Send

Cycling is useful when moving between neighbouring Sends.

But if you already know which Send you want, DrivenByMoss provides a quicker route.

Hold **SEND** and use the channel SELECT buttons to choose the Send directly.

Conceptually:

```text
SEND + SELECT 1  → Send 1
SEND + SELECT 2  → Send 2
SEND + SELECT 3  → Send 3
...
SEND + SELECT 8  → Send 8
```

This is an important example of a control acquiring a new meaning from context.

Normally:

```text
SELECT 3
```

means:

> Select Track 3.

But while SEND is being used as the context:

```text
SEND + SELECT 3
```

means:

> Select Send 3.

The physical SELECT button has not changed.

The context has.

---

## Switching a Send On or Off

Send level and Send state are two different things.

Turning a V-Pot adjusts the amount being sent.

DrivenByMoss also allows the Send itself to be switched on or off.

In Send Mode:

```text
OPTION + V-Pot press
```

toggles the corresponding Send.

So one rotary control can provide both:

```text
Turn
   ↓
Send level

OPTION + Press
   ↓
Send on/off
```

This is exactly the kind of compact interaction for which modifiers are useful.

The common operation remains immediately available.

The related secondary operation is one modifier away.

---

## Send Mode as a Mixing Tool

Send Mode is worth thinking about as more than a shortcut.

Suppose Send 1 contains a reverb and Send 2 contains a delay.

You can move between two complete views of your mix:

```text
Send 1 — Reverb
────────────────────
Track 1 amount
Track 2 amount
Track 3 amount
...
Track 8 amount
```

then:

```text
Send 2 — Delay
────────────────────
Track 1 amount
Track 2 amount
Track 3 amount
...
Track 8 amount
```

Rather than visiting each track and adjusting one Send at a time, you can work across the mix according to the effect you are shaping.

For dub-style mixing in particular, this way of thinking can be extremely useful.

---

## ARM, MUTE and SOLO

The channel-strip buttons continue to provide immediate control over the tracks.

### ARM

Press **ARM** on a channel strip to arm that track for recording.

The bank of ARM buttons allows record state to be managed directly from the surface.

### MUTE

Press **MUTE** to mute the corresponding track.

### SOLO

Press **SOLO** to solo the corresponding track.

These are familiar mixer operations, but DrivenByMoss also provides modified versions for useful bank-wide or related operations.

---

## Clearing Mutes

When several tracks have been muted, clearing them individually can be tedious.

DrivenByMoss provides a global operation for clearing active mutes.

This is particularly useful after using mute creatively during playback.

Rather than searching the surface for every illuminated MUTE button, the controller can return the mixer to an unmuted state in one operation.

The exact global-control combination will be included in the Quick Reference once the final command set has been verified against the current DrivenByMoss version.

---

## Clearing Solos

The same problem occurs with Solo.

During mixing it is easy to accumulate a state in which one or more tracks are soloed.

DrivenByMoss provides a global operation for clearing active solos.

Again, the important workflow idea is:

```text
Experiment
    ↓
Mute / Solo tracks
    ↓
Return the mixer to a known state
```

The controller is not merely a way to activate states.

It also provides efficient ways to **recover from them**.

---

## Monitoring

SHIFT-modified channel buttons provide access to monitoring-related functions.

These are useful when recording and will become more meaningful when we look at advanced recording workflows later in the guide.

For now, the important distinction is that ARM, MUTE and SOLO buttons are not necessarily limited to the words printed on their caps.

Like the rest of the X-Touch, they participate in the modifier system.

---

## FLIP

FLIP changes the relationship between rotary and fader control.

This becomes especially useful in the mixer edit modes.

A parameter that would normally be controlled from a V-Pot can be placed onto the motor faders.

Why might we want that?

Because a fader gives us:

- a long physical travel;
- touch sensitivity;
- motorised feedback;
- a very different physical feel from a rotary encoder.

For some adjustments, the V-Pot is ideal.

For others, the fader is more expressive.

FLIP lets the controller adapt.

Conceptually:

```text
Before FLIP

V-Pots   → parameter
Faders   → volume


After FLIP

V-Pots   → volume
Faders   → parameter
```

The exact result depends on the current mode, but the principle remains the same:

> **FLIP exchanges control roles.**

---

## Mixing by Dimension

The most useful way to think about this chapter is not as a collection of modes.

Think of it as several different ways to **slice through the same mixer**.

### By channel

```text
Track 1
   ├── Volume
   ├── Pan
   ├── Sends
   ├── Mute
   └── Solo
```

### By parameter

```text
Pan
   ├── Track 1
   ├── Track 2
   ├── Track 3
   └── ...
```

### By Send

```text
Reverb Send
   ├── Track 1
   ├── Track 2
   ├── Track 3
   └── ...
```

None of these is more correct than another.

They are different views of the same project.

---

## Choosing the Useful View

A good control surface should reduce the distance between an intention and an action.

If your intention is:

> Turn Track 4 down.

the motor fader is probably already exactly what you want.

If your intention is:

> Spread these eight tracks across the stereo field.

Panorama Mode gives you eight related controls together.

If your intention is:

> Decide which tracks should feed the delay.

Send Mode gives you a complete view of that Send across the bank.

The important skill is therefore not memorising modes.

It is recognising **which view best matches the job you are doing**.

---

## The Important Idea

Mixer Edit Modes let you reorganise the X-Touch around a particular mixing task.

Instead of always seeing:

```text
eight tracks
×
many different controls
```

you can temporarily see:

```text
one kind of control
×
eight tracks
```

That change of perspective is what makes these modes useful.

The X-Touch is still an eight-channel control surface.

But DrivenByMoss lets those eight channels become eight simultaneous views of:

- volume;
- panorama;
- Sends;
- track parameters;

depending on what you need at that moment.

Once this way of thinking becomes natural, the controller begins to feel less like a fixed bank of knobs and faders and more like a surface that **reorganises itself around the mix**.

---

## Coming Next

Mixer Edit Modes help us change **what** we are controlling.

The next chapter deals with another question:

> **Where are we in the project?**

Markers give us named positions in the timeline, and DrivenByMoss gives the X-Touch several ways to create, display and navigate them.

In the next chapter we will look at **Markers and Advanced Navigation**.
