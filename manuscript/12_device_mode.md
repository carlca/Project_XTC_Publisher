---
chapter: 12
title: "Device Mode"
status: draft
---

# Device Mode

A Bitwig track can contain far more than a volume control and a Pan knob.

It may contain:

- instruments;
- audio effects;
- note effects;
- modulators;
- utility devices;
- whole chains of devices.

The X-Touch gives us eight V-Pots.

So how can eight physical knobs control a device that may expose dozens of parameters?

DrivenByMoss solves this with:

```text
Device Selection
      +
Parameter Pages
      +
Direct Selection
```

This is the heart of Device Mode.

---

# Entering Device Mode

Press:

```text
DEVICE
```

The X-Touch enters Device Mode for the currently selected track.

The eight V-Pots now control the current page of parameters on the selected device.

Conceptually:

```text
Selected Track
      │
      ▼
Selected Device
      │
      ▼
Current Parameter Page
      │
      ▼
V-Pots 1–8
```

The channel strip has not changed.

The controller's focus has moved deeper into the track.

---

# Device Mode Needs a Selected Track

Device Mode acts on the currently selected track.

So a common workflow is:

```text
SELECT Track
     ↓
DEVICE
     ↓
Edit Device
```

This is why SELECT is so important.

It establishes the track context.

DEVICE then moves the X-Touch into the device context for that track.

---

# The First Eight Parameters

Suppose the selected device exposes:

```text
Parameter 1
Parameter 2
Parameter 3
Parameter 4
Parameter 5
Parameter 6
Parameter 7
Parameter 8
```

The V-Pots map directly:

```text
V-Pot 1  → Parameter 1
V-Pot 2  → Parameter 2
V-Pot 3  → Parameter 3
V-Pot 4  → Parameter 4
V-Pot 5  → Parameter 5
V-Pot 6  → Parameter 6
V-Pot 7  → Parameter 7
V-Pot 8  → Parameter 8
```

Turn a V-Pot:

```text
Turn
   ↓
Change Parameter
```

Press it:

```text
Press
   ↓
Reset Parameter
```

The modifier behaviours from Chapter 9 also apply where appropriate.

---

# More Than Eight Parameters

Many devices expose far more than eight parameters.

DrivenByMoss therefore groups them into pages.

For example:

```text
Page 1
   Parameters 1–8

Page 2
   Parameters 9–16

Page 3
   Parameters 17–24

Page 4
   Parameters 25–32
```

The X-Touch only needs eight V-Pots because those eight controls can be repopulated with another page whenever necessary.

---

# CHANNEL Navigates Parameter Pages

In Device Mode, the CHANNEL buttons change meaning.

Normally:

```text
CHANNEL <
CHANNEL >
   → move through tracks
```

In Device Mode:

```text
CHANNEL <
   → Previous Parameter Page

CHANNEL >
   → Next Parameter Page
```

This is one of the most important context changes in the X-Touch.

The same physical buttons now navigate **inside the selected device**.

---

# BANK Navigates Devices

The BANK buttons also change meaning in Device Mode.

Normally:

```text
BANK <
BANK >
   → move track bank by 8
```

In Device Mode:

```text
BANK <
   → Previous Device

BANK >
   → Next Device
```

So Device Mode gives us two navigation axes:

```text
BANK
   → Devices

CHANNEL
   → Parameter Pages
```

That distinction is worth learning.

---

# A Useful Device-Mode Map

Think:

```text
Track
  │
  ▼
Device Chain
  │
  ├── Device 1
  ├── Device 2
  ├── Device 3
  └── Device 4
```

Use BANK to move between devices.

Then, inside the selected device:

```text
Device
  │
  ├── Page 1
  ├── Page 2
  ├── Page 3
  └── Page 4
```

Use CHANNEL to move between parameter pages.

So:

```text
BANK
   → movement through device chain

CHANNEL
   → movement through parameter pages
```

The physical layout stays the same.

The navigation target changes.

---

# BANK Is the Larger Structural Step

There is a useful pattern here.

BANK handles the larger structural object:

```text
whole device
```

CHANNEL handles the finer-grained object:

```text
parameter page
```

This echoes the broader relationship introduced in Chapter 4:

> **BANK moves at the larger level; CHANNEL moves at the finer level.**

The literal targets change, but the hierarchy of movement remains understandable.

---

# Direct Device Selection with CONTROL

Stepping through devices with BANK is useful.

But if a track contains many devices, repeated BANK presses can become tedious.

DrivenByMoss provides a faster route.

Hold:

```text
CONTROL
```

The V-Pots temporarily display the devices on the selected track.

Conceptually:

```text
Hold CONTROL
      │
      ▼
Device 1   Device 2   Device 3   Device 4   ...
   │          │          │          │
   ▼          ▼          ▼          ▼
Pot 1      Pot 2      Pot 3      Pot 4
```

Press the V-Pot corresponding to the device you want.

---

# Choosing a Device Directly

Suppose the selected track contains:

```text
EQ
Compressor
Saturator
Chorus
Delay
Reverb
```

Hold CONTROL.

The V-Pots now represent:

```text
1  EQ
2  Compressor
3  Saturator
4  Chorus
5  Delay
6  Reverb
```

Press V-Pot 5:

```text
Hold CONTROL
      ↓
Press V-Pot 5
      ↓
Delay Selected
```

This is much faster than stepping through five devices one at a time.

---

# Direct Parameter-Page Selection with OPTION

OPTION provides the corresponding shortcut for parameter pages.

Hold:

```text
OPTION
```

DrivenByMoss temporarily displays the available parameter pages across the V-Pots.

Conceptually:

```text
Hold OPTION
      │
      ▼
Page 1   Page 2   Page 3   Page 4   ...
  │        │        │        │
  ▼        ▼        ▼        ▼
Pot 1    Pot 2    Pot 3    Pot 4
```

Press the V-Pot corresponding to the page you want.

---

# Two Ways to Navigate Devices

So we now have two device-navigation methods.

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

The first is ideal when moving one step.

The second is ideal when jumping directly to a known device.

---

# Two Ways to Navigate Parameter Pages

Likewise, parameter pages can be navigated sequentially:

```text
CHANNEL <
CHANNEL >
   → Previous / Next Page
```

or directly:

```text
Hold OPTION
      ↓
Press Page V-Pot
```

So Device Mode supports both:

```text
step through
```

and:

```text
jump directly
```

That is a very useful design.

---

# Direct Selection Reduces Button Repetition

Suppose a device has eight parameter pages and you want Page 7.

Sequentially:

```text
CHANNEL >
CHANNEL >
CHANNEL >
CHANNEL >
CHANNEL >
CHANNEL >
```

Directly:

```text
Hold OPTION
      ↓
Press V-Pot 7
```

Similarly, if the desired device is far along a device chain:

```text
Hold CONTROL
      ↓
Press its V-Pot
```

The direct-selection modifiers turn the V-Pot row into a temporary menu.

---

# The V-Pot Row Becomes Eight Choices

This is one of the recurring patterns we identified in Chapter 9.

Normally, the eight V-Pots are:

```text
8 parameters
```

With CONTROL held:

```text
8 device choices
```

With OPTION held:

```text
8 page choices
```

So the same physical row alternates between:

```text
editing
```

and:

```text
selection
```

depending on context.

---

# OPTION + DEVICE — Pin the Cursor Device

DrivenByMoss also provides:

```text
OPTION + DEVICE
   → Pin Cursor Device
```

Pinning is useful when you want the controller to stay attached to the current device rather than following another device-selection change elsewhere in Bitwig.

Conceptually:

```text
Current Device
      │
      │ OPTION + DEVICE
      ▼
Pinned Device
```

This can make Device Mode more predictable in workflows where Bitwig's cursor device would otherwise change automatically.

---

# Why Pinning Matters

Suppose you are repeatedly adjusting the same delay device while selecting or manipulating other things in the project.

Without pinning:

```text
Bitwig Focus Changes
      ↓
Cursor Device May Change
      ↓
X-Touch Follows
```

With the device pinned:

```text
OPTION + DEVICE
      ↓
Device Remains Target
```

The controller can remain focused on the thing you actually care about.

---

# Pinning Is a Focus Tool

It is useful to think of pinning as:

> **Hold this context steady.**

Earlier we learned:

```text
SELECT
   → establish focus
```

Pinning adds:

```text
OPTION + DEVICE
   → keep this device focus
```

This is another way in which DrivenByMoss helps reduce repeated navigation.

---

# Project / Track Parameter Mode

DEVICE has another documented function.

If Device Mode is already active, press:

```text
DEVICE
```

again.

DrivenByMoss switches to:

```text
Project / Track Parameter Mode
```

Conceptually:

```text
DEVICE
   ↓
Device Mode
   ↓
DEVICE again
   ↓
Project / Track Parameters
```

This gives the same eight V-Pots access to the currently selected set of eight Project or Track parameters.

---

# Eight Project / Track Parameters

In this mode:

```text
V-Pot 1  → Parameter 1
V-Pot 2  → Parameter 2
V-Pot 3  → Parameter 3
V-Pot 4  → Parameter 4
V-Pot 5  → Parameter 5
V-Pot 6  → Parameter 6
V-Pot 7  → Parameter 7
V-Pot 8  → Parameter 8
```

The important distinction is what those parameters belong to.

Ordinary Device Mode asks:

> **Which parameters belong to this device?**

Project / Track Parameter Mode asks:

> **Which Project or Track parameters are currently selected for control?**

The physical editing method remains familiar:

```text
Eight V-Pots
     ↓
Eight Parameters
```

Only the parameter context has changed.

---

# DEVICE Is Therefore Contextual Even Within Device Editing

It is tempting to think:

```text
DEVICE
   → Device Mode
```

and stop there.

But the fuller model is:

```text
Press DEVICE
      ↓
Device Edit Mode

Press DEVICE again
      ↓
Project / Track Parameter Mode
```

So the DEVICE button can move between two related parameter-editing contexts.

As always, watch the displays.

The scribble strips tell you what the V-Pots currently represent.

---

# Instrument Device Edit Mode

DrivenByMoss also maps:

```text
INSTRUMENT
```

to:

```text
Instrument Device Edit Mode
```

This provides a specialised route to the instrument device on the selected track.

Conceptually:

```text
Selected Track
      │
      ▼
INSTRUMENT
      │
      ▼
Instrument Device
      │
      ▼
V-Pot Parameter Editing
```

This is useful when the thing you want to edit is specifically the track's instrument rather than another device elsewhere in its chain.

---

# Why Instrument Mode Is Useful

Consider a track containing:

```text
Note Effect
    ↓
Instrument
    ↓
EQ
    ↓
Compressor
    ↓
Delay
```

General Device Mode lets you navigate through the device chain.

But if your intention is simply:

> **I want to edit the instrument.**

then:

```text
INSTRUMENT
```

provides a more direct conceptual route.

Instead of thinking:

```text
Enter Device Mode
      ↓
Find Instrument
```

you can think:

```text
INSTRUMENT
      ↓
Edit Instrument
```

This is the same reason specialised modes such as EQ Mode are useful.

They reduce navigation when your destination is already known.

---

# General and Specialised Device Access

We can now distinguish several related routes.

```text
DEVICE
   → General Device Editing
```

```text
DEVICE again
   → Project / Track Parameters
```

```text
INSTRUMENT
   → Instrument Device Editing
```

```text
EQ
   → EQ+ Editing
```

These are not four unrelated features.

They are different routes into parameter control.

Conceptually:

```text
                  Parameter Editing
                         │
          ┌──────────────┼──────────────┐
          │              │              │
       DEVICE       INSTRUMENT          EQ
          │              │              │
          ▼              ▼              ▼
    Device Chain     Instrument        EQ+
          │
          │ DEVICE again
          ▼
 Project / Track
    Parameters
```

The X-Touch uses the same physical controls while DrivenByMoss changes the target.

---

# Device Feedback

Because Device Mode is highly contextual, feedback is essential.

The X-Touch needs to tell you:

- which device is selected;
- which parameter page is active;
- what each V-Pot currently controls;
- what the current parameter values are.

So the complete interaction is:

```text
Choose Device
     ↓
Choose Page
     ↓
Read Scribble Strips
     ↓
Turn V-Pot
     ↓
Read LED Ring / Bitwig
```

The controller is not merely receiving commands.

It is continually reporting the current assignment back to you.

---

# Read Before You Turn

This principle is especially important in Device Mode.

A V-Pot may control:

```text
Cutoff
```

then after a page change:

```text
Resonance
```

then after a device change:

```text
Delay Feedback
```

then after changing parameter context:

```text
Track Parameter
```

The physical knob did not move.

Its assignment did.

So:

> **Read before you turn.**

That habit prevents a great deal of accidental parameter editing.

---

# Parameter Names Can Be Abbreviated

The X-Touch scribble strips have limited space.

A Bitwig parameter name may therefore appear abbreviated.

For example:

```text
Feedback
```

might appear as:

```text
Feedbk
```

or another shortened form.

The display does not need to reproduce Bitwig's full graphical label.

It needs to give you enough information to identify the parameter confidently.

Familiarity makes these abbreviations much easier to read.

---

# FLIP in Device Mode

Chapter 10 introduced FLIP as a way of moving the current V-Pot assignments onto the motor faders.

That becomes particularly useful in Device Mode.

Normally:

```text
V-Pots
   → Device Parameters

Faders
   → Track Volumes
```

Press:

```text
FLIP
```

and the current device-parameter assignments can be controlled from the faders.

For example:

```text
Filter Cutoff

Effect Mix

Feedback

Macro Amount
```

may benefit from the longer physical travel of a fader.

This does not introduce a different kind of FLIP.

It is the same FLIP behaviour described in Chapter 10, applied to the current Device Mode assignments.

For the full explanation of FLIP, motorised recall and `SHIFT + FLIP`, see Chapter 10.

---

# Device Automation

Once a device parameter is exposed on the X-Touch, it can participate in automation.

Conceptually:

```text
Device Parameter
      │
      ▼
V-Pot or Fader
      │
      ▼
Automation
```

This means a filter sweep or effect movement can be performed physically rather than drawn first.

Chapter 16 covers the automation workflow itself.

The important point here is that Device Mode provides the parameter access required for that performance.

---

# DEVICE Is a Mode, Not a One-Shot Command

When you press DEVICE, you are not merely performing one device operation.

You are changing the controller's working context.

While Device Mode is active:

```text
BANK
   → Devices

CHANNEL
   → Parameter Pages

V-Pots
   → Parameters

CONTROL
   → Direct Device Selection

OPTION
   → Direct Page Selection
```

And another press of DEVICE gives access to:

```text
Project / Track Parameters
```

So DEVICE creates a family of related parameter-editing contexts.

---

# Leaving Device Mode

To leave Device Mode, select another edit mode.

For example:

```text
PAN

SEND

TRACK

USER
```

or another appropriate mode button.

The V-Pots and navigation controls then acquire the assignments belonging to that new context.

This is another reason to think of modes as:

> **views onto the controller**

rather than commands that merely happen once.

---

# Device Mode and the Mouse-Lite Idea

Device Mode can substantially reduce mouse dependence for routine parameter work.

A graphical route might be:

```text
Find Track
    ↓
Click Track
    ↓
Find Device
    ↓
Click Device
    ↓
Find Parameter
    ↓
Drag
```

A hardware route can become:

```text
SELECT Track
    ↓
DEVICE
    ↓
Choose Device
    ↓
Choose Page
    ↓
Turn V-Pot
```

Or, for an instrument:

```text
SELECT Track
    ↓
INSTRUMENT
    ↓
Adjust Parameter
```

Once the controller workflow is familiar, these routes can become much faster.

---

# When the Mouse Is Still Better

Device Mode does not replace the graphical device interface.

Some devices expose:

- complex visual editors;
- modulation graphs;
- sequencers;
- spectral displays;
- drag-and-drop structures;
- parameter relationships that are easier to understand visually.

For those tasks, use the screen.

The point of Device Mode is not:

> **Never look at the device GUI.**

It is:

> **Routine parameter access should not always require the GUI.**

That is the Mouse-Lite principle.

---

# Device Chains as Physical Destinations

A useful way to think about a track's device chain is:

```text
Track
  │
  ├── Device 1
  ├── Device 2
  ├── Device 3
  ├── Device 4
  └── Device 5
```

BANK navigates those destinations.

CONTROL lets you choose one directly.

Once there, CHANNEL navigates parameter pages.

OPTION lets you choose a page directly.

So the X-Touch gives the device chain both:

```text
sequential navigation
```

and:

```text
direct navigation
```

This is more efficient than thinking of Device Mode as a single linear sequence of pages.

---

# A Practical Device Exercise

Create or open a track containing several devices.

For example:

```text
EQ+
Compressor
Saturator
Delay
Reverb
```

Select the track and press:

```text
DEVICE
```

### 1. Use BANK

Press:

```text
BANK >
```

several times.

Watch the selected device change.

Then use:

```text
BANK <
```

to move back.

### 2. Use CHANNEL

Select a device with several pages.

Press:

```text
CHANNEL >
```

to move through parameter pages.

Then use:

```text
CHANNEL <
```

to move back.

### 3. Use CONTROL

Hold CONTROL.

Observe the device names across the V-Pots.

Press the V-Pot for a device several positions away.

### 4. Use OPTION

Hold OPTION.

Observe the parameter-page choices.

Press one directly.

The purpose of the exercise is to make this relationship instinctive:

```text
BANK
   → Devices

CHANNEL
   → Pages

CONTROL
   → Direct Device

OPTION
   → Direct Page
```

---

# A Practical Project / Track Parameter Exercise

Enter Device Mode:

```text
DEVICE
```

Then press:

```text
DEVICE
```

again.

Observe the scribble strips and V-Pot assignments.

The surface should now represent the currently selected Project / Track parameters rather than the ordinary device-page context.

Turn a V-Pot carefully and observe the corresponding parameter in Bitwig.

The aim is to recognise:

```text
DEVICE
   → Device Parameters

DEVICE again
   → Project / Track Parameters
```

as two related but distinct contexts.

---

# A Practical Instrument Exercise

Select an instrument track containing an instrument and several additional devices.

Press:

```text
INSTRUMENT
```

Observe which device becomes the editing target.

Compare this with entering general Device Mode and navigating the chain manually.

The point of the exercise is to understand INSTRUMENT as a **direct destination**:

```text
Known Destination
      ↓
INSTRUMENT
      ↓
Instrument Editing
```

---

# A Practical Pinning Exercise

Select a device you want to keep under X-Touch control.

Press:

```text
OPTION + DEVICE
```

Now change focus elsewhere in Bitwig.

Observe whether the cursor device remains pinned according to the DrivenByMoss behaviour.

Then unpin when appropriate.

The purpose is to understand pinning as a way of keeping controller focus stable.

---

# EQ Mode

The X-Touch also has an EQ button.

DrivenByMoss provides a specialised EQ edit mode built around Bitwig's EQ+ device.

This is conceptually related to Device Mode because it exposes device parameters on the V-Pots.

But EQ Mode gives a faster route to a very common mixing task.

---

# Entering EQ Mode

Press:

```text
EQ
```

DrivenByMoss targets the EQ+ device for the selected track.

If the selected track does not already contain an EQ+ in the required context, DrivenByMoss can insert one automatically.

Conceptually:

```text
SELECT Track
     ↓
EQ
     ↓
EQ+ Available
     ↓
V-Pots Control EQ Parameters
```

This is a powerful workflow shortcut.

---

# EQ Mode Can Modify the Project

The automatic insertion behaviour deserves attention.

Entering EQ Mode is not always a purely navigational operation.

If DrivenByMoss adds an EQ+ device, the project has changed.

So:

```text
EQ
```

can mean either:

```text
Control Existing EQ+
```

or:

```text
Insert EQ+
and then Control It
```

depending on the selected track.

That makes EQ Mode slightly more consequential than a simple view change.

---

# Why Automatic EQ+ Insertion Is Useful

EQ is one of the most common mixing tasks.

Without the specialised mode:

```text
SELECT Track
     ↓
Open Browser
     ↓
Find EQ+
     ↓
Insert
     ↓
DEVICE
     ↓
Select EQ+
```

With EQ Mode:

```text
SELECT Track
     ↓
EQ
     ↓
Work
```

That is a significant reduction in interaction.

It is exactly the kind of workflow compression a control surface is good at.

---

# EQ Mode Uses Familiar Principles

Once EQ Mode is active, the interaction remains familiar:

```text
V-Pots
   → Parameters

CHANNEL
   → Parameter Pages

Feedback
   → Scribble Strips / LED Rings
```

So EQ Mode does not require learning an entirely new physical language.

It is a specialised application of the same device-control model.

---

# Device, Instrument and EQ Modes Compared

We now have three useful routes into device-oriented editing.

Device Mode asks:

> **Which device on this track do I want to control?**

Instrument Mode says:

> **Take me directly to the track's instrument.**

EQ Mode says:

> **Take me directly to the track's equalizer.**

So:

```text
DEVICE
   → General Device Navigation

INSTRUMENT
   → Direct Instrument Editing

EQ
   → Specialised EQ Workflow
```

And within the DEVICE family:

```text
DEVICE again
   → Project / Track Parameters
```

All use the same underlying idea:

```text
Choose Context
      ↓
Expose Parameters
      ↓
Use Physical Controls
```

---

# Don't Confuse Device Selection with Track Selection

When using Device Mode, there are now two levels of focus:

```text
Selected Track
      │
      ▼
Selected Device
```

SELECT changes the track.

BANK or CONTROL changes the device.

This distinction matters.

If the wrong device appears, ask:

```text
Is the correct track selected?

Is the correct device selected?
```

Those are separate questions.

---

# A Complete Device Workflow

Suppose you want to adjust the feedback of a delay on the Vocal track.

A hardware-oriented workflow might be:

```text
SELECT Vocal
      ↓
DEVICE
      ↓
Hold CONTROL
      ↓
Press Delay V-Pot
      ↓
Hold OPTION
      ↓
Choose Parameter Page
      ↓
Turn Feedback V-Pot
```

If the parameter is on the current page already, some of those steps disappear.

The workflow scales according to how directly you can reach the required control.

---

# A Faster Workflow with Familiarity

At first, you may think:

```text
Which device?

Which page?

Which knob?
```

Later:

```text
Vocal
  ↓
DEVICE
  ↓
Delay
  ↓
Feedback
```

And eventually your hands may perform the sequence almost automatically.

This is the recurring Project XTC progression:

```text
Remember
   ↓
Recognise
   ↓
Repeat
   ↓
Muscle Memory
```

---

# Device Mode as a Moving Window

The eight V-Pots are another moving window.

Across devices:

```text
BANK
   → choose which device
```

Within the device:

```text
CHANNEL
   → choose which parameter page
```

Across the page:

```text
V-Pots 1–8
   → choose which parameter
```

And DEVICE itself can change the parameter context:

```text
Device Parameters
      ↕
Project / Track Parameters
```

So the complete model is:

```text
Track
  │
  ▼
Parameter Context
  │
  ▼
Device
  │
  ▼
Parameter Page
  │
  ▼
Parameter
```

Not every context uses every level, but the X-Touch can navigate remarkably deeply into the project using the same small collection of physical controls.

---

# The Important Idea

Device Mode turns the X-Touch into a contextual parameter editor.

The normal mapping begins:

```text
DEVICE
   → Enter Device Mode
```

Inside Device Mode:

```text
BANK <
BANK >
   → Previous / Next Device
```

```text
CHANNEL <
CHANNEL >
   → Previous / Next Parameter Page
```

```text
V-Pots
   → Current Device Parameters
```

For direct selection:

```text
Hold CONTROL
   → Show Devices
   → Press V-Pot to Select Device
```

```text
Hold OPTION
   → Show Parameter Pages
   → Press V-Pot to Select Page
```

And:

```text
OPTION + DEVICE
   → Pin Cursor Device
```

DEVICE itself has another parameter context:

```text
DEVICE again
   → Project / Track Parameter Mode
```

while specialised device routes include:

```text
INSTRUMENT
   → Instrument Device Edit Mode
```

and:

```text
EQ
   → Control EQ+
   → Insert EQ+ Automatically
     if Required
```

FLIP can still be applied to the current device parameters:

```text
FLIP
   → Device Parameters on Faders
```

but this is simply the general FLIP behaviour already explained in Chapter 10.

So the most useful mental model is:

```text
SELECT Track
     ↓
Choose Editing Context
     ↓
Choose Device if Required
     ↓
Choose Page if Required
     ↓
Adjust Parameter
```

Once that sequence becomes familiar, the X-Touch can reach deeply into a Bitwig track without requiring every parameter change to begin with the mouse.

---

## Coming Next

Device Mode gives us direct access to devices and parameters that already exist.

But sometimes the thing we want is not in the project yet.

DrivenByMoss also gives the X-Touch a hardware route into Bitwig's Browser:

- opening it;
- navigating categories and results;
- inserting devices before or after the current device;
- replacing a device;
- confirming or cancelling the selection.

Next:

**Browser Mode.**
