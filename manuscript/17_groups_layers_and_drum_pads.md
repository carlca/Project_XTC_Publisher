---
chapter: 17
title: "Groups, Layers and Drum Pads"
status: draft
---

# Groups, Layers and Drum Pads

So far, we have often treated the Bitwig project as though it were a relatively simple row of tracks:

```text
Track 1   Track 2   Track 3   Track 4   Track 5   Track 6   Track 7   Track 8
```

The X-Touch gives us eight channel strips, and banking lets that eight-channel window move across a larger project.

But Bitwig projects are not necessarily flat.

A track can belong to a Group.

An instrument can contain layers.

A Drum Machine can contain pads.

So the project may look more like this:

```text
Project
   │
   ├── Group
   │     │
   │     ├── Track
   │     ├── Track
   │     └── Track
   │
   ├── Instrument Track
   │     │
   │     └── Instrument
   │           │
   │           ├── Layer
   │           ├── Layer
   │           └── Layer
   │
   └── Drum Track
         │
         └── Drum Machine
               │
               ├── Pad
               ├── Pad
               ├── Pad
               └── ...
```

DrivenByMoss allows the X-Touch to navigate these structures.

That introduces another important idea:

> **The eight channel strips can show a level of a hierarchy.**

---

## A Window into the Project

Think back to banking.

If a project contains sixteen tracks, the X-Touch cannot show all sixteen simultaneously.

Instead, it shows a window:

```text
Project

1   2   3   4   5   6   7   8   9   10  11  12  13  14  15  16
└───────────────┘
     X-Touch
```

Bank to the right and the window moves.

Hierarchical navigation adds another possibility.

The window can move not only:

```text
← sideways →
```

but also:

```text
↓ deeper
↑ outward
```

into and out of project structures.

---

## Flat and Hierarchical Navigation

DrivenByMoss provides two approaches to track navigation:

- **flat navigation**;
- **hierarchical navigation**.

The distinction affects what happens when the project contains Groups.

---

## Flat Navigation

In a flat view, tracks can be presented as part of a single navigable sequence.

Conceptually:

```text
Group A
   ├── Bass
   ├── Guitar
   └── Keys

Drums

Vocals
```

may be approached more like:

```text
Bass   Guitar   Keys   Drums   Vocals
```

The hierarchy is not the main navigational concern.

This can be convenient when you primarily want to move rapidly across tracks.

---

## Hierarchical Navigation

Hierarchical navigation preserves the idea that some tracks exist **inside** other structures.

The same project is understood as:

```text
Project
   │
   ├── Group A
   │      ├── Bass
   │      ├── Guitar
   │      └── Keys
   │
   ├── Drums
   │
   └── Vocals
```

The controller can then enter Group A and expose its contents.

Conceptually:

```text
Project level

┌─────────┐  ┌─────────┐  ┌─────────┐
│ Group A │  │ Drums   │  │ Vocals  │
└────┬────┘  └─────────┘  └─────────┘
     │
     │ enter
     ▼

Inside Group A

┌─────────┐  ┌─────────┐  ┌─────────┐
│ Bass    │  │ Guitar  │  │ Keys    │
└─────────┘  └─────────┘  └─────────┘
```

The eight physical channel strips have not changed.

What they represent has.

---

## Going Down a Level

When hierarchical navigation is enabled, selecting and entering a Group lets the X-Touch descend into that Group.

The channel strips can then represent its child tracks.

Think of this as opening a folder:

```text
Group
  │
  │ enter
  ▼
Contents of Group
```

The important conceptual distinction is between:

```text
SELECT
   → establish focus
```

and:

```text
ENTER
   → descend into the focused structure
```

This builds naturally on the SELECT-button principle introduced earlier in the guide.

First establish **which object** you mean.

Then decide **what to do with it**.

---

## Coming Back Out

If we can descend into a hierarchy, we also need a way back.

DrivenByMoss provides navigation back towards the parent level.

Conceptually:

```text
Project
   │
   ▼
Group
   │
   ▼
Track
```

and then:

```text
Track
   │
   ▲
Group
   │
   ▲
Project
```

The important mental model is:

> **You are moving the X-Touch's point of view through the project hierarchy.**

You are not moving the tracks themselves.

---

## Hierarchy Is Another Kind of Banking

There is a useful connection with Chapter 4.

Ordinary banking moves the X-Touch's view **across** a collection:

```text
← BANK                                  BANK →
```

Hierarchical navigation moves the view **between levels**:

```text
      Parent
        ▲
        │
        │
        ▼
       Child
```

So we can think of navigation as having two dimensions:

```text
                Parent
                  ▲
                  │
Previous  ◄──── Current ────► Next
                  │
                  ▼
                 Child
```

That is a much more powerful model than thinking of the X-Touch as permanently attached to eight particular tracks.

---

## Why Hierarchical Navigation Helps

Consider a large project containing:

```text
Drums
Bass
Guitars
Keyboards
Vocals
FX
```

where several of those are Groups.

At the top level, you may want the X-Touch to behave almost like a stem mixer:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

That is an excellent high-level view for balancing the song.

But now suppose the snare is too loud.

Instead of abandoning the control surface, you can descend into the Drums Group:

```text
Drums
  │
  ▼
Kick   Snare   Hats   Toms   Percussion   ...
```

Make the adjustment.

Then return to the project level:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

The surface has changed scale.

---

## From Mixing Desk to Magnifying Glass

This gives the X-Touch two complementary roles.

At one moment it can behave like a broad mixing desk:

```text
Drums   Bass   Guitars   Keys   Vocals
```

A moment later it can act almost like a magnifying glass:

```text
Kick   Snare   Hat   Tom 1   Tom 2   Shaker
```

The hardware is identical.

Only the level of detail has changed.

That is one of the advantages of a context-sensitive control surface.

---

## Instrument Layers

Hierarchy does not stop at track Groups.

Bitwig instruments can themselves contain multiple layers.

Conceptually:

```text
Instrument Track
       │
       ▼
   Instrument
       │
       ├── Layer 1
       ├── Layer 2
       ├── Layer 3
       └── Layer 4
```

DrivenByMoss can expose these layers on the X-Touch.

When the appropriate layer view is active, the channel strips cease to represent ordinary project tracks and instead represent the layers within the selected instrument.

Again:

> **The channel strip represents whatever object the current context assigns to it.**

---

## Layer Mode

For a layered instrument, the controller can enter a Layer-oriented view.

The eight channel strips can then represent up to eight visible layers:

```text
Layer 1   Layer 2   Layer 3   Layer 4   Layer 5   Layer 6   Layer 7   Layer 8
```

If more layers exist, banking provides access to the others.

This should already feel familiar.

We are applying the same eight-channel-window model to a different collection of objects.

---

## Mixing Layers

Once layers are exposed on the channel strips, they can be treated in mixer-like ways.

Depending on the current layer mode, the surface provides access to properties including:

- Volume;
- Panorama;
- Sends;
- Mute;
- Solo.

So a layered sound can be mixed from the X-Touch much as a set of tracks can.

Conceptually:

```text
                Layered Instrument

             ┌────────┬────────┬────────┐
             │Layer 1 │Layer 2 │Layer 3 │
             └───┬────┴───┬────┴───┬────┘
                 │        │        │
              Volume   Volume   Volume
                Pan      Pan      Pan
               Sends    Sends    Sends
```

This can be much more immediate than repeatedly opening device panels and adjusting the layers with a mouse.

---

## Volume and Panorama

The same perspective we used in Chapter 14 applies here.

We can look at layers by object:

```text
Layer 1
   ├── Volume
   ├── Pan
   └── Sends
```

or by dimension:

```text
Volume
   ├── Layer 1
   ├── Layer 2
   ├── Layer 3
   └── ...
```

The X-Touch can reorganise its controls according to the job.

The principles do not change merely because the objects are now layers rather than tracks.

---

## Sends from Layers

Layer Sends can be particularly useful for building complex instruments.

Different layers may need different amounts of:

- reverb;
- delay;
- modulation;
- other send effects.

Instead of treating the layered instrument as one indivisible sound, the X-Touch can help expose its internal mix.

Conceptually:

```text
Layer 1 ────────► Reverb
Layer 2 ──►      Reverb
Layer 3 ─────────────► Reverb
Layer 4 ─────►    Reverb
```

Once again, we are mixing **inside** something that previously appeared to be a single track.

---

## Mute and Solo for Layers

Mute and Solo become particularly useful when investigating a layered sound.

Suppose an instrument contains four layers and something in the combined sound is muddy.

Solo the layers individually.

Or mute one layer and listen to what disappears.

The workflow becomes:

```text
Listen
  ↓
Solo / Mute Layer
  ↓
Identify contribution
  ↓
Adjust
  ↓
Restore full sound
```

This is another example of the X-Touch helping you work by ear rather than requiring constant visual navigation through Bitwig's device interface.

---

## Drum Pads

A Drum Machine introduces another hierarchy.

Conceptually:

```text
Drum Track
    │
    ▼
Drum Machine
    │
    ├── Kick Pad
    ├── Snare Pad
    ├── Closed Hat Pad
    ├── Open Hat Pad
    ├── Clap Pad
    ├── Tom Pad
    └── ...
```

From the project's top level, this may appear to be one track.

Inside the Drum Machine, however, it contains an entire collection of sounds.

DrivenByMoss can expose those pads through the X-Touch.

---

## Drum Pad Mode

In the appropriate Drum Pad view, the channel strips represent individual pads.

For example:

```text
Ch 1      Ch 2      Ch 3      Ch 4      Ch 5      Ch 6      Ch 7      Ch 8

Kick      Snare     C.Hat     O.Hat     Clap      Tom       Rim       Perc
```

Now the X-Touch behaves almost like a mixer for the internal elements of the drum kit.

The same physical faders that previously controlled entire tracks may now control individual drum sounds.

---

## Mixing a Drum Machine

This can be extremely useful.

Suppose the overall drum track is at the correct level, but the hi-hat is too loud.

At project level:

```text
Drums
  │
  └── one fader
```

does not solve the problem.

Descend to the Drum Machine's pads and the view becomes:

```text
Kick   Snare   C.Hat   O.Hat   Clap   Tom   ...
```

Now the problem is directly accessible.

Turn the hi-hat down.

Then return to the higher-level mix.

---

## Drum Pad Volume

In a volume-oriented pad view:

```text
Fader 1 → Kick
Fader 2 → Snare
Fader 3 → Closed Hat
Fader 4 → Open Hat
...
```

The X-Touch becomes a conventional-looking mixer for something that Bitwig represents internally as a device.

This is another reminder that the distinction between:

```text
Track
Device
Layer
Pad
```

matters less to the hardware than you might initially expect.

What matters is the **current collection of controllable objects**.

---

## Drum Pad Panorama

Pads can also be treated as individual mixer elements for panorama.

That makes operations such as spreading percussion across the stereo field much more tactile.

Instead of repeatedly selecting pads on screen:

```text
select pad
   ↓
adjust pan
   ↓
select next pad
   ↓
adjust pan
```

the X-Touch can present several pad panorama controls together.

---

## Drum Pad Sends

The same applies to Sends.

Perhaps:

- the snare needs plenty of reverb;
- the kick needs almost none;
- the clap needs delay;
- the percussion needs a little of both.

The pad-oriented Send view allows these internal relationships to be mixed from the surface.

This is exactly the same **mixing by dimension** principle introduced in Chapter 14, now operating one level deeper.

---

## Mute and Solo for Drum Pads

Mute and Solo are especially useful with drums.

Want to hear the groove without the kick?

Mute it.

Want to find which percussion pad is producing an unwanted sound?

Solo pads until you identify it.

Want to audition the rhythm without the hats?

Mute them.

The channel-strip buttons make these operations immediate.

Again, the X-Touch is acting not merely as a track mixer, but as a mixer for the **contents of a device**.

---

## The Same Eight Strips, Again and Again

At this point, the eight channel strips may have represented:

```text
Project tracks

Group contents

Instrument layers

Drum pads
```

This may sound complicated until we notice that the interaction pattern remains remarkably consistent.

The surface repeatedly asks:

> **What eight things are we looking at now?**

Then the familiar controls operate on those things.

Conceptually:

```text
                 X-Touch
                    │
                    ▼
             Eight channel strips
                    │
       ┌────────────┼────────────┐
       │            │            │
       ▼            ▼            ▼
     Tracks       Layers        Pads
```

Once you understand the window, you do not need to relearn the surface every time the contents change.

---

## SELECT Still Means Focus

The SELECT-button principle remains valuable throughout hierarchical navigation.

At whatever level you are working:

> **SELECT establishes focus.**

At project level, SELECT may focus a track or Group.

Inside a Group, it may focus one of its child tracks.

In a layer-oriented context, it may focus a layer.

In a pad-oriented context, it may focus a drum pad.

The object changes.

The principle does not.

That consistency is what makes a complex hierarchy manageable.

---

## ENTER Means Go Deeper

A useful companion principle is:

> **ENTER descends into something that has contents.**

Not every selected object has another meaningful level beneath it.

But when it does, ENTER provides a natural conceptual operation:

```text
SELECT
   ↓
"This one"

ENTER
   ↓
"Show me inside it"
```

That pairing is worth remembering.

---

## CANCEL Means Back Out

Likewise, navigation needs a way to retreat from the current level.

Think of CANCEL as the complementary idea:

```text
ENTER
   → go in

CANCEL
   → come back out
```

The precise behaviour still depends on the current context, but this provides a useful mental model for hierarchical navigation.

---

## Don't Confuse Navigation with Rearrangement

There is an important distinction here.

When you enter a Group or expose layers, you are changing the controller's **view**.

You are not moving objects in the Bitwig project.

This is similar to the distinction introduced in Chapter 4.

Compare:

```text
Navigate hierarchy
      ↓
Move the X-Touch's view
```

with:

```text
Move track
      ↓
Change the project structure
```

Those are fundamentally different operations.

If something unexpected happens, ask yourself:

> **Am I moving the view, or moving the object?**

That question resolves many apparently confusing control-surface operations.

---

## A Practical Group Workflow

Suppose the top-level mix contains:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

and the snare needs adjustment.

### 1. Select Drums

Use the appropriate channel SELECT button.

### 2. Enter the Group

Descend into its contents.

The surface now shows something like:

```text
Kick   Snare   Hats   Toms   Percussion
```

### 3. Adjust Snare

Use the familiar channel controls.

### 4. Return to the parent

Back out of the Group.

The X-Touch returns to:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

No mouse was required simply to change the scale at which you were mixing.

---

## A Practical Drum Workflow

Suppose a Drum Machine contains:

```text
Kick   Snare   Hat   Clap   Rim   Shaker   Conga   Tamb
```

and you want to shape the internal mix.

You can:

1. enter the appropriate pad view;
2. balance the pad volumes;
3. adjust panorama;
4. work with Sends;
5. mute or solo individual sounds;
6. return to the higher-level track view.

The important point is that you have not left the X-Touch's basic interaction model.

You have simply moved deeper into the project.

---

## Hierarchy and Mouse-Lite Working

Hierarchical navigation addresses one of the common reasons for reaching for a mouse:

> **I need to get at something inside that thing.**

Without a control-surface hierarchy, the usual response is:

```text
look at screen
    ↓
find Group or device
    ↓
expand it
    ↓
find child object
    ↓
select it
```

With a navigable hierarchy:

```text
SELECT
   ↓
ENTER
   ↓
work
   ↓
CANCEL
```

The exact number of steps depends on the project, but the principle is powerful.

The controller can change its point of view without requiring you to manipulate the visual interface first.

---

## A Project Is Not Flat

This is the larger lesson of the chapter.

At the beginning of the guide, it was convenient to imagine:

```text
Track 1   Track 2   Track 3   Track 4   ...
```

That model remains useful.

But a real Bitwig project may be closer to:

```text
Project
   │
   ├── Group
   │     ├── Track
   │     └── Track
   │
   ├── Instrument Track
   │     └── Instrument
   │           ├── Layer
   │           └── Layer
   │
   └── Drum Track
         └── Drum Machine
               ├── Pad
               ├── Pad
               └── Pad
```

DrivenByMoss allows the X-Touch to follow that structure.

---

## The Important Idea

The eight channel strips are not permanently eight tracks.

They are an **eight-object window**.

Depending on context, those objects may be:

```text
Tracks
Groups
Child tracks
Layers
Drum pads
```

Banking moves the window across objects.

Hierarchical navigation moves the window between levels.

So our mental model can now expand again:

```text
                    PROJECT

                      │
             ┌────────┴────────┐
             │                 │
           Group            Instrument
             │                 │
       ┌─────┴─────┐      ┌────┴────┐
       │           │      │         │
     Track       Track   Layer     Layer

                      Drum Machine
                           │
                    ┌──────┼──────┐
                    │      │      │
                   Pad    Pad    Pad
```

The X-Touch does not need a separate physical surface for every level.

It changes what its existing surface represents.

Once that becomes intuitive, even a deeply structured Bitwig project can remain accessible from the same eight channel strips.

---

## Coming Next

We have now moved:

- sideways through banks;
- between mixer dimensions;
- through markers;
- into Groups;
- into layers;
- into Drum Machine pads.

The next chapter moves somewhere different again:

**upwards, to the project as a whole.**

We will look at the Master channel and the project-level operations that DrivenByMoss places on the X-Touch.

Next:

**Master Mode and Project Control.**
