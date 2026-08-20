---
chapter: 15
title: "Markers and Advanced Navigation"
status: draft
---

# Markers and Advanced Navigation

Transport controls let us move through a project.

We can play, stop, rewind, fast-forward and use the Jog Wheel to position the cursor precisely.

But as a project grows, there is another way to think about navigation.

Instead of asking:

> **How far should I move?**

we can ask:

> **Where do I want to go?**

That is where markers become useful.

A marker gives a position in the project a meaningful identity.

Instead of remembering that the chorus begins somewhere around bar 33, we can create a marker called:

```text
Chorus
```

and navigate directly in terms of the structure of the music.

DrivenByMoss extends this idea onto the X-Touch.

---

## From Position to Structure

Without markers, navigation is principally about position:

```text
1       9       17      25      33      41
│-------│-------│-------│-------│-------│
```

With markers, the same timeline can acquire musical meaning:

```text
Intro       Verse       Chorus       Breakdown
  │           │            │             │
  ▼           ▼            ▼             ▼
──●───────────●────────────●─────────────●──────
```

Now the project is not merely a sequence of bars.

It has landmarks.

And once those landmarks exist, the X-Touch can use them for navigation.

---

## The MARKER Button

The **MARKER** button is the centre of marker operations.

Pressing MARKER enters Marker Mode.

This changes the context of the controller so that markers can be accessed from the surface.

As with the other modes we have encountered:

> **The hardware has not changed. Its current meaning has.**

Marker Mode turns the X-Touch from a device that moves through time into one that can navigate the **structure** of the project.

---

## Creating a Marker

Hold **OPTION** and press **MARKER**:

```text
OPTION + MARKER
```

to create a marker at the current position.

Conceptually:

```text
Current Position
       │
       │ OPTION + MARKER
       ▼
    New Marker
```

This is particularly useful because creating the marker does not require breaking away from the control surface and reaching for the mouse.

Imagine playback reaching the beginning of an important section.

You stop at the required position and press:

```text
OPTION + MARKER
```

That position is now represented by a marker in the project.

The operation that originally looked like an obscure modifier combination now makes sense as part of a workflow:

```text
Navigate
   ↓
Find an important position
   ↓
OPTION + MARKER
   ↓
Create a landmark
```

---

## Showing and Hiding Markers

Hold **SHIFT** and press **MARKER**:

```text
SHIFT + MARKER
```

to show or hide the markers.

This provides another example of the modifier vocabulary introduced in Chapter 8.

MARKER performs the primary marker operation.

SHIFT + MARKER accesses a related secondary operation.

You do not need to remember this as an isolated shortcut.

Think:

```text
MARKER
   → work with markers

SHIFT + MARKER
   → change their visibility
```

---

## Previous and Next Marker

Once markers exist, REWIND and FORWARD gain useful alternative functions.

Normally these controls move through the timeline.

Hold **OPTION**, however, and they navigate between markers:

```text
OPTION + REWIND
   → previous marker

OPTION + FORWARD
   → next marker
```

This gives us two distinct forms of navigation:

```text
REWIND / FORWARD
        │
        ├── normally
        │      move through time
        │
        └── OPTION
               move through structure
```

That distinction is worth remembering.

Without OPTION, you are navigating **distance**.

With OPTION, you are navigating **landmarks**.

---

## A Different Way to Move Through a Song

Suppose a project contains:

```text
Intro
Verse 1
Chorus 1
Verse 2
Chorus 2
Breakdown
Final Chorus
Outro
```

With markers placed at those positions, moving through the project no longer requires repeatedly turning the Jog Wheel or holding FORWARD.

Instead:

```text
OPTION + FORWARD
```

can step through the musical sections.

Likewise:

```text
OPTION + REWIND
```

moves back through them.

So navigation begins to resemble:

```text
Verse 1
   │
   ▼
Chorus 1
   │
   ▼
Verse 2
   │
   ▼
Chorus 2
```

rather than:

```text
bar 17
   │
   ▼
bar 33
   │
   ▼
bar 49
```

Both views are useful.

Markers simply add another level of meaning.

---

## Playing from a Marker

In Marker Mode, the V-Pots give us another way to interact with markers.

Press the V-Pot associated with a marker to start playback from that marker.

Conceptually:

```text
Marker
   │
   │ press associated V-Pot
   ▼
Playback starts here
```

This turns the X-Touch into something closer to a set of structural navigation controls.

Instead of moving to a location and then pressing PLAY, the marker itself becomes the starting point.

---

## Why Marker Mode Matters

Marker Mode may initially seem like a fairly specialised feature.

It becomes much more useful when we consider how often navigation interrupts a workflow.

Imagine repeatedly working on a transition between a verse and chorus.

With ordinary transport navigation, the cycle might be:

```text
Stop
  ↓
Find the position
  ↓
Reposition
  ↓
Play
```

With a marker already placed at the start of the section:

```text
Select marker
      ↓
Play from marker
```

The mechanical part of the operation becomes smaller.

That matters because every navigation operation is something happening **between musical decisions**.

---

## Markers as a Project Map

There is a broader principle here.

A well-marked project effectively contains a map of itself.

For example:

```text
SONG
 │
 ├── Intro
 │
 ├── Verse 1
 │
 ├── Chorus 1
 │
 ├── Verse 2
 │
 ├── Chorus 2
 │
 ├── Breakdown
 │
 ├── Final Chorus
 │
 └── Outro
```

The X-Touch can then navigate that map.

This is fundamentally different from using the controller merely as a remote transport.

The transport controls know about **time**.

Markers know about **places**.

Together they provide both.

---

## Markers During Arrangement

Markers are particularly useful while arranging.

Suppose you are deciding whether the breakdown is too long.

You might repeatedly compare:

```text
Chorus 2
    ↓
Breakdown
    ↓
Final Chorus
```

Marker navigation lets you move between those structural points quickly.

You can concentrate on questions such as:

- Does the transition work?
- Does the next section arrive soon enough?
- Does the energy drop too far?
- Does the final chorus have enough impact?

The X-Touch handles the navigation while your attention remains on the arrangement.

---

## Markers During Mixing

Markers are equally useful during mixing.

A mix rarely needs attention everywhere at once.

You may want to revisit:

```text
Vocal entrance
Bass drop
Busy chorus
Quiet breakdown
Final hit
```

Markers can turn these into repeatable destinations.

For example:

```text
OPTION + FORWARD
      ↓
Busy Chorus
      ↓
listen
      ↓
OPTION + FORWARD
      ↓
Quiet Breakdown
      ↓
listen
```

This is much faster than repeatedly finding those positions visually.

It also encourages listening rather than screen-watching.

---

## Markers During Performance

Markers can also provide a useful structural framework when Bitwig is being used more performatively.

The important point is not that markers replace clips, scenes or Launcher workflows.

They do not.

Markers describe positions in the Arranger timeline.

But where the Arranger itself forms part of a performance, marker navigation gives the X-Touch another way to interact with that structure.

As always, the appropriate tool depends on the job.

---

## Marker Navigation and the Transport Controls

We first encountered REWIND and FORWARD as transport controls.

Now we can see that they have two related roles.

### Ordinary transport

```text
REWIND
FORWARD
```

move through the timeline.

### Structural navigation

```text
OPTION + REWIND
OPTION + FORWARD
```

move through markers.

This is why modifier commands are best learned in context.

If Chapter 8 had simply presented:

```text
OPTION + FORWARD = next marker
```

as one line in a large table, it would have been another fact to memorise.

Here, its purpose is obvious.

---

## Marker Mode and the Mental Model

Markers also fit neatly into the mental model developed throughout this guide.

The same physical controls can acquire meaning from context.

For example:

```text
V-Pot
  +
Marker Mode
  =
Marker interaction
```

And:

```text
FORWARD
   +
OPTION
   =
Next Marker
```

So our increasingly complete model is:

```text
Physical Control
       +
Current Mode
       +
Modifier
       =
Current Function
```

The surface is not a collection of controls with permanently fixed meanings.

It is a system of **contextual controls**.

---

## A Practical Marker Workflow

A simple workflow might look like this.

### 1. Find the beginning of a section

Use the normal transport controls or Jog Wheel.

```text
Navigate
   ↓
Beginning of Chorus
```

### 2. Create the marker

```text
OPTION + MARKER
```

### 3. Repeat for other important sections

For example:

```text
Intro
Verse
Chorus
Breakdown
Outro
```

### 4. Navigate structurally

Use:

```text
OPTION + REWIND
OPTION + FORWARD
```

to move between those landmarks.

### 5. Enter Marker Mode when appropriate

Use MARKER to expose marker-oriented control from the X-Touch.

### 6. Start playback from the required marker

Press the corresponding V-Pot.

The result is a project that can increasingly be navigated by **musical structure rather than screen position**.

---

## You Don't Need a Marker Everywhere

Markers are useful because they simplify navigation.

Too many markers can have the opposite effect.

A project containing:

```text
Intro
Verse
Chorus
Breakdown
Outro
```

provides obvious destinations.

A project containing a marker every few bars may simply replace one navigation problem with another.

Use markers for positions you expect to revisit.

Good candidates include:

- major song sections;
- important transitions;
- difficult edits;
- mix-check locations;
- unusual events;
- positions needed repeatedly during a session.

The aim is not to document every metre of the timeline.

It is to create useful landmarks.

---

## Less Looking, More Listening

There is another benefit to marker navigation that fits the larger aim of Project XTC.

If you know that the next press of:

```text
OPTION + FORWARD
```

will take you to the next important section, you do not need to locate that section visually.

Your eyes do not need to find the mouse pointer.

The pointer does not need to find the timeline.

The timeline does not need to be zoomed to the right scale.

You simply move to the next landmark.

This is a small example of the mouse-lite principle we will return to later:

> **The best control-surface operation is often the one that lets your attention remain on the music.**

---

## The Important Idea

Transport navigation answers:

> **How do I move through time?**

Marker navigation answers:

> **How do I move through the structure of my project?**

DrivenByMoss gives the X-Touch both.

The essential marker commands are:

```text
MARKER
   → Marker Mode

OPTION + MARKER
   → Create marker

SHIFT + MARKER
   → Show/hide markers

OPTION + REWIND
   → Previous marker

OPTION + FORWARD
   → Next marker
```

And within Marker Mode, the V-Pots allow markers to become direct playback destinations.

Once markers are part of your normal project workflow, navigation stops being purely a matter of bars, beats and cursor positions.

The project acquires **places you can go**.

---

## Coming Next

So far we have used the motor faders to control parameters and respond to changes from Bitwig.

But their touch sensitivity becomes particularly powerful when Bitwig is **recording those movements**.

That brings us to one of the areas where a motorised control surface can feel dramatically different from using a mouse.

Next:

**Automation.**
