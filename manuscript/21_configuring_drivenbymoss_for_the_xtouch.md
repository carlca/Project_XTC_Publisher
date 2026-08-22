---
chapter: 21
title: "Configuring DrivenByMoss for the X-Touch"
status: draft
---

# Configuring DrivenByMoss for the X-Touch

For most of this guide, we have concentrated on using the X-Touch.

Press a button.

Turn a V-Pot.

Move a fader.

Select a mode.

But all of those operations take place inside an environment created by **DrivenByMoss configuration**.

The complete system is:

```text
X-Touch
   │
   ▼
Mackie Control Protocol
   │
   ▼
DrivenByMoss
   │
   ▼
Bitwig Studio
```

DrivenByMoss does more than translate button presses.

Its preferences determine:

- how the hardware is represented;
- what appears in the track banks;
- how Groups are navigated;
- what happens when a fader is touched;
- which mode appears at startup;
- how quickly the encoders respond;
- whether Arranger or Launcher functions have priority;
- how Browser information is presented;
- what programmable buttons and footswitches do.

So configuration is not separate from workflow.

It helps **define the workflow**.

---

# Configuration Should Reduce Decisions

A good configuration removes unnecessary decisions from the musical moment.

For example, if you normally create four-bar clips, setting an appropriate New Clip Length means the recording workflow can become:

```text
Create
   ↓
Record
```

rather than:

```text
Create
   ↓
Choose Length
   ↓
Confirm
   ↓
Record
```

Likewise, if you prefer hierarchical project navigation, configuring that once means you do not need to rethink the controller's navigation model every session.

A useful principle is:

> **Configure beforehand so that you have less to configure while making music.**

---

# The Preferences Are Global

DrivenByMoss stores these preferences globally rather than separately for each project.

That is important.

Changing a controller preference affects the way the X-Touch behaves generally.

It is not merely modifying the current Bitwig project.

So think of the settings as defining:

```text
My X-Touch Environment
```

rather than:

```text
This Song's X-Touch Settings
```

That makes configuration worth doing deliberately.

---

# Start with the X-Touch Profile

DrivenByMoss provides hardware profiles for supported controllers.

For the Behringer X-Touch, choose the appropriate X-Touch profile.

The profile configures the relevant MCU hardware options for the controller.

One slightly unusual detail is worth knowing:

> **The Profile menu does not remain showing the selected profile afterwards.**

That is intentional.

The profile is a convenient way of setting the hardware options.

It is not itself a persistent mode indicator.

So do not assume that the setup has failed merely because the menu no longer visibly says X-Touch.

---

# X-Touch Hardware Requirements

The DrivenByMoss documentation specifies three important requirements for full X-Touch support.

## Firmware

Use the current X-Touch firmware documented by DrivenByMoss:

```text
1.22
```

This is particularly important for display-colour support.

## Operating Mode

The X-Touch must be set to:

```text
MC
```

for Mackie Control operation.

Conceptually:

```text
X-Touch
   │
   ▼
MC Mode
   │
   ▼
DrivenByMoss MCU Extension
```

If the hardware is in another protocol mode, the behaviour described throughout Project XTC should not be expected to match.

## Display Colours

The X-Touch display-colour option should be enabled.

Selecting the X-Touch hardware profile is the easiest way to configure the appropriate display settings.

---

# Get the Foundation Right First

Before adjusting advanced preferences, make sure the basic control surface works.

A useful order is:

```text
X-Touch in MC Mode
       ↓
DrivenByMoss Controller Active
       ↓
MIDI Communication Working
       ↓
Transport Working
       ↓
Faders Working
       ↓
Feedback Working
       ↓
Advanced Preferences
```

Do not troubleshoot specialised Layer Mode or Browser behaviour while the fundamental controller connection is uncertain.

---

# Two-Way Communication Matters

The X-Touch is not merely sending commands to Bitwig.

Bitwig and DrivenByMoss also send information back.

For example:

```text
Move Fader
    ↓
Bitwig Changes
```

but also:

```text
Bitwig Changes
      ↓
Motor Fader Moves
```

Likewise, the return path supplies:

- scribble-strip information;
- assignment displays;
- LEDs;
- V-Pot rings;
- VU information;
- motor positions.

So a working X-Touch needs a conversation:

```text
X-Touch
   ⇄
DrivenByMoss
   ⇄
Bitwig
```

not a one-way stream of commands.

---

# A Simple Connection Test

Before changing preferences, try a few basic operations.

## Fader to Bitwig

Move a channel fader.

Does the corresponding Bitwig track volume change?

## Bitwig to Fader

Move the same track volume in Bitwig.

Does the physical fader follow?

## Track Selection

Press SELECT.

Does the expected track become selected?

## Transport

Press PLAY and STOP.

Does Bitwig respond?

## Display Feedback

Do the scribble strips contain meaningful track or parameter information?

If these basics work, the foundation is sound.

---

# Hardware Setup

DrivenByMoss exposes several Hardware Setup options.

The X-Touch profile should normally configure these appropriately, but understanding what they mean is useful.

---

## Main Display

This tells DrivenByMoss that the controller has a main MCU-style display.

For hardware consisting of eight separate display sections rather than one uninterrupted display, DrivenByMoss also provides a seven-character display option.

The purpose is simple:

```text
Bitwig State
     ↓
DrivenByMoss
     ↓
Correct Display Format
     ↓
Readable X-Touch Feedback
```

---

## Segment Display

The X-Touch has a segment display capable of showing transport-related information.

DrivenByMoss can use it for:

```text
Play Position
```

and supplementary information such as:

```text
Tempo
```

or:

```text
Ticks
```

The Segment Display preferences control what information is presented there.

---

## Assignment Display

The assignment display shows the current mode.

For a highly contextual surface, this is particularly valuable.

The controller may currently be in:

```text
Panorama Mode

Send Mode

Device Mode

Browser Mode

Marker Mode
```

and the assignment display helps make that context visible.

---

## Motor Faders

DrivenByMoss includes a hardware option indicating that the controller has motor faders.

For the X-Touch, of course, this should be enabled.

Without correct motor-fader handling, one of the controller's most important feedback mechanisms would be lost.

---

## Display Colours

The X-Touch supports coloured scribble-strip backlighting.

DrivenByMoss has an explicit:

```text
Display Colors
```

option for the Behringer X-Touch and X-Touch Extender.

Again, choosing the X-Touch hardware profile is the simplest way to establish the appropriate setup.

---

# VU Meters

DrivenByMoss can send VU information to compatible MCU hardware.

The settings include:

```text
VU Meters
```

and:

```text
Always Send VU Meters
```

The latter exists for controllers that stop showing a VU value if they do not receive repeated updates when the level is unchanged.

This is mainly a hardware-compatibility setting.

For normal use, the aim is straightforward:

```text
Audio Level
    ↓
DrivenByMoss
    ↓
Physical Meter Feedback
```

---

# Use Faders Like Editing Knobs

DrivenByMoss has a preference named:

```text
Use faders like editing knobs
```

This causes the faders to execute the functions normally assigned to the V-Pots.

The documentation specifically notes that this can be useful for recording automation.

This is closely related to the X-Touch's FLIP behaviour.

Conceptually:

```text
Knob Assignment
      ↓
Fader
```

The attraction is obvious for parameters that benefit from:

- long physical travel;
- touch sensitivity;
- motorised feedback.

---

# Track Navigation

One of the most important workflow preferences is:

```text
Track Navigation
```

DrivenByMoss provides two approaches:

```text
Flat
```

and:

```text
Hierarchical
```

These produce meaningfully different SELECT-button behaviour.

---

# Flat Track Navigation

In Flat mode, tracks are shown together in a flat track bank.

Conceptually:

```text
Track 1
Track 2
Track 3
Track 4
Track 5
...
```

Groups do not become separate controller-navigation levels in the same way.

If an already selected Group is selected again:

```text
SELECT Group again
        │
        ▼
Toggle Expanded State
```

This can be convenient if you prefer thinking of the project as one long mixer.

---

# Hierarchical Track Navigation

In Hierarchical mode, the controller follows the project structure.

For example:

```text
Project
   │
   ├── Drums
   │
   ├── Bass
   │
   ├── Guitars
   │
   ├── Keys
   │
   └── Vocals
```

Select a Group:

```text
SELECT Drums
```

then select it again:

```text
SELECT Drums again
       │
       ▼
Enter Group
```

The X-Touch can now show:

```text
Kick   Snare   Hats   Toms   Percussion
```

To leave:

```text
Long-press any SELECT
```

This is the navigation model described in Chapters 6 and 17.

---

# Choosing Flat or Hierarchical

Neither choice is universally better.

Ask how you think about a project.

If the natural model is:

> **Give me one long mixer.**

Flat may suit you.

If the natural model is:

> **Show me the broad project structure and let me drill into detail.**

Hierarchical may be preferable.

For large, well-organised projects, hierarchical navigation can make eight channel strips feel considerably less restrictive.

---

# Include FX and Master Tracks in the Track Bank

DrivenByMoss provides:

```text
Include FX and master tracks in track bank
```

When enabled, these tracks are included in the normal track bank.

This can be useful on controllers that do not have dedicated access to those tracks.

On an X-Touch, the decision is more about workflow.

You may prefer:

```text
ordinary audio / instrument tracks
```

as the main bank,

or you may want:

```text
FX and Master
```

included in the same navigation sequence.

The setting changes what the eight-channel window contains.

---

# Pin FX Tracks to the Last Device

For multi-controller systems, DrivenByMoss can:

```text
Pin FX tracks to last device
```

This creates a bank of up to eight FX tracks on the right-most controller.

The instrument/audio track bank is reduced accordingly.

For a single X-Touch this option is less central.

With an Extender setup it can be extremely useful.

Conceptually:

```text
Main Track Surface
        +
Dedicated FX Surface
```

We discuss expansion in Chapter 22.

---

# Exclude Deactivated Items

The Workflow preferences contain:

```text
Exclude deactivated items
```

When enabled, deactivated tracks and similar items are not shown on the controller.

This can make the banks cleaner.

For example:

```text
Active
Active
Deactivated
Active
Deactivated
Active
```

can effectively become:

```text
Active
Active
Active
Active
```

on the controller.

But there is a trade-off.

If the item is excluded, you also lose the ability to activate it from the surface.

So the choice is:

```text
Cleaner Navigation
```

versus:

```text
Access to Deactivated Items
```

Choose according to the way you work.

---

# Startup Mode

DrivenByMoss lets you choose:

```text
Startup Mode
```

This determines which parameter mode becomes active when the controller starts.

That sounds like a minor convenience.

In daily use it can be significant.

Suppose most sessions begin with ordinary mixing.

A useful startup context might be one that immediately gives you the controls you normally expect.

If most sessions begin with another task, choose accordingly.

The principle is:

> **Start where you usually work.**

---

# New Clip Length

DrivenByMoss provides a configurable:

```text
New Clip Length
```

This determines the length of clips created by the relevant New/clip-creation workflows.

For example, if you regularly build four-bar loops:

```text
New Clip Length
      │
      ▼
4 Bars
```

then commands such as the clip-based recording workflows begin with a useful default.

This connects directly with Chapter 19.

---

# Configure for the Common Case

Suppose your new clips are roughly:

```text
70%   4 bars

20%   8 bars

10%   something else
```

A four-bar default makes sense.

It does not have to cover every possibility.

A good default is the one that removes a decision **most often**.

---

# Fader-Touch Behaviour

The current DrivenByMoss preferences expose two particularly useful fader-touch options:

```text
Select Channel on Fader Touch
```

and:

```text
Activate Volume mode on Fader Touch
```

These deserve careful explanation because they affect the physical feel of the controller.

---

# Select Channel on Fader Touch

When enabled:

```text
Touch Fader
     │
     ▼
Select Corresponding Channel
```

This can make mixing very fluid.

You hear something on the Vocal.

Reach for the Vocal fader.

The act of touching it establishes the Vocal as the selected track.

The workflow becomes:

```text
Touch
  ↓
Focus
  ↓
Adjust
```

rather than:

```text
SELECT
   ↓
Touch
   ↓
Adjust
```

---

# Why You Might Disable Fader Selection

Touch-to-select is not universally desirable.

You may want to:

```text
keep Synth selected
```

while simultaneously:

```text
adjust Vocal volume
```

If touching the Vocal fader automatically changes the selection, that may interrupt another controller context.

So DrivenByMoss makes the behaviour configurable.

This corrects an important assumption:

> **Fader touch selecting the track should be treated as configurable behaviour, not an unavoidable property of the X-Touch mapping.**

---

# Activate Volume Mode on Fader Touch

DrivenByMoss can also temporarily activate Volume Mode when a fader is touched.

Conceptually:

```text
Current Mode
     │
     ▼
Touch Fader
     │
     ▼
Volume Mode
     │
     ▼
Release Fader
     │
     ▼
Previous Context
```

This can be useful if you want fader interaction to return temporarily to an obvious volume-oriented view.

Again, it is a workflow preference.

Some users will find it reassuring.

Others may prefer the controller context to remain unchanged.

---

# Knob Sensitivity

DrivenByMoss provides separate settings for:

```text
Knob Sensitivity Default
```

and:

```text
Knob Sensitivity Slow
```

Negative values slow the encoder response.

Positive values speed it up.

This lets you tune the relationship between:

```text
Physical Turn
```

and:

```text
Parameter Change
```

---

# Why Sensitivity Matters

Suppose a small V-Pot movement causes a very large parameter change.

The encoder may feel too fast.

Reduce the sensitivity.

Conversely, if reaching the desired value requires excessive turning, increase it.

The useful question is:

> **Does the physical movement feel proportional to the musical adjustment?**

The correct value is the one that feels predictable.

---

# Default and Slow Sensitivity

The two sensitivity settings correspond to the normal and slower/fine-adjustment behaviour.

This means you can separately tune:

```text
Normal Adjustment
```

and:

```text
Fine Adjustment
```

Rather than assuming that the factory relationship is ideal for everyone, DrivenByMoss lets the physical response be adapted.

---

# Encoder Knob Slow Down

The preferences also contain:

```text
Encoder Knob Slow Down
```

This applies to the main encoder.

Use a higher value if the encoder changes values too quickly.

Again, the purpose is predictability.

A control surface should not feel twitchy.

It should feel like the software is following the physical gesture.

---

# Transport Behaviour

DrivenByMoss exposes configurable behaviour for:

```text
Behaviour on Stop
```

and:

```text
Behaviour on Pause
```

The first controls what happens when playback is stopped with STOP.

The second controls what happens when playback is stopped using PLAY.

This matters because the Transport chapter showed that STOP and PLAY are not necessarily identical ways of ending playback.

The preferences let that distinction be customised.

---

# Flip Arranger and Clip Record / Automation

This is one of the most important workflow preferences in the entire MCU configuration.

DrivenByMoss calls it:

```text
Flip arranger and clip record / automation
```

Normally, the mapping gives the unmodified controls an Arranger-oriented role and SHIFT provides the related Launcher/Clip operation.

Conceptually:

```text
Normal
   → Arranger-oriented function

SHIFT
   → Clip / Launcher-oriented function
```

With the preference enabled:

```text
Normal
   → Clip / Launcher-oriented function

SHIFT
   → Arranger-oriented function
```

The relationship is reversed.

---

# Why Flip the Recording Functions?

Imagine two users.

One mainly works in the Arranger.

The other builds music primarily in the Clip Launcher.

For the first user:

```text
Arranger function
   → easiest gesture
```

makes sense.

For the second:

```text
Launcher function
   → easiest gesture
```

makes more sense.

DrivenByMoss therefore lets the normal-versus-SHIFT priority follow the workflow.

---

# Why This Preference Matters to Documentation

This setting can make two correctly configured X-Touch systems appear to behave differently.

One user reports:

> **The normal button does the Arranger operation.**

Another reports:

> **Mine does the Launcher operation.**

Both can be correct.

The difference may simply be:

```text
Flip arranger and clip record / automation
```

So throughout Project XTC we describe the **normal mapping** unless a configuration-dependent behaviour is explicitly stated.

---

# Quantize Amount

The Play and Sequence preferences include:

```text
Quantize Amount
```

This determines how strongly the Quantize operation moves notes towards the timing grid.

At:

```text
100%
```

the affected notes are aligned fully to the grid.

Lower values retain more of the original timing while still moving the notes towards the grid.

This setting does not quantize anything by itself. It defines the amount used when the Quantize operation is executed.

---

# Browser Preferences

DrivenByMoss also lets you hide Browser filter columns that you do not use.

This may sound cosmetic.

On the X-Touch it can be quite useful.

Browser Mode has limited physical display space.

If irrelevant filter columns are hidden:

```text
Fewer Columns
     ↓
Less Noise
     ↓
Relevant Choices Easier to Find
```

This is another example of configuration reducing decisions during the actual workflow.

---

# Configure Browser Mode Around Your Search Habits

If you consistently ignore a Browser filter category, there is little benefit in forcing it to occupy controller attention.

A good Browser setup can therefore make the hardware workflow feel substantially more direct.

The principle remains:

> **Remove recurring friction, not theoretical possibilities.**

---

# Display Track Names

DrivenByMoss can configure the first display row to show track names rather than mode labels.

This is another trade-off.

Track names answer:

> **What channels am I looking at?**

Mode labels answer:

> **What controller context am I in?**

Both forms of information are useful.

Choose the display arrangement that makes the surface easiest for you to read.

---

# Use Vertical Zoom to Change Modes

DrivenByMoss also provides:

```text
Use vertical zoom to change modes
```

When enabled, the up/down arrows in Zoom Mode can select parameter modes.

This gives the arrow keys another possible controller-level role.

It is a good example of a preference that may be useful to one workflow and unnecessary complication to another.

Do not enable features simply because they exist.

Enable them because they solve a real problem.

---

# The Segment Display

If the hardware has a segment display, DrivenByMoss lets you choose whether the play position is represented as:

```text
Time
```

or:

```text
Beats / Measures
```

It can also choose whether the final digits display:

```text
Tempo
```

or:

```text
Ticks
```

For music production, measures and tempo may feel natural.

For another workflow, absolute time may be more useful.

Again, configuration determines what information reaches you most efficiently.

---

# Configure for Mixing

If your X-Touch is used primarily as a mixer, priorities may include:

- clear track names;
- predictable banking;
- sensible V-Pot response;
- immediate volume control;
- fader-touch selection if useful;
- Sends;
- reliable VU feedback.

A good mixing configuration should feel like:

```text
Find Channel
     ↓
Touch / Select
     ↓
Adjust
```

with very little controller-management overhead.

---

# Configure for Large Projects

For large projects, priorities may change.

Hierarchical navigation can become especially useful.

A top-level view such as:

```text
Drums   Bass   Guitars   Keys   Vocals   FX
```

gives the project a manageable structure.

Then:

```text
SELECT Drums
      ↓
SELECT again
      ↓
Kick   Snare   Hats   Toms   Percussion
```

reveals the detail only when it is required.

For this kind of workflow, the Track Navigation preference has a much greater effect than a subtle knob-sensitivity adjustment.

---

# Configure for Launcher Work

A Launcher-oriented setup may prioritise:

```text
New Clip Length
```

and:

```text
Flip arranger and clip record / automation
```

The desired workflow may be:

```text
Select Destination
      ↓
Create
      ↓
Record
      ↓
Overdub
      ↓
Listen
```

with Launcher functions available on the simplest physical gestures.

Configuration should support the musical model you actually use.

---

# Configure for Device Work

A device-heavy workflow may care particularly about:

- display readability;
- knob sensitivity;
- fine adjustment;
- fader-as-knob behaviour;
- startup mode;
- Browser filter visibility.

The goal is:

```text
Track
  ↓
Device
  ↓
Page
  ↓
Parameter
```

with as little unnecessary physical navigation as possible.

---

# Configure for Performance Mixing

Our Chapter 20 dub example suggests another set of priorities.

A performance-oriented mixer benefits from:

- predictable fader response;
- useful fader-touch behaviour;
- clear channel feedback;
- fast Send access;
- sensible V-Pot sensitivity;
- stable track banking;
- immediate effect control.

When mixing performatively, predictability matters enormously.

You do not want to wonder:

> **What will happen if I touch this?**

The configuration should make the answer obvious.

---

# Change One Thing at a Time

When experimenting with preferences, avoid changing many settings simultaneously.

Use:

```text
Change One Setting
       ↓
Test
       ↓
Understand Result
       ↓
Keep or Revert
```

rather than:

```text
Change Six Settings
       ↓
Controller Feels Different
       ↓
Which Setting Did It?
```

This is particularly important with a contextual controller.

One preference may affect several different workflows.

---

# Test Configuration Musically

A preference can look sensible in a settings panel but still feel awkward in practice.

If you change:

```text
Track Navigation
```

navigate a real project.

If you change:

```text
Knob Sensitivity
```

adjust real parameters.

If you change:

```text
Fader Touch
```

mix something.

If you change:

```text
New Clip Length
```

create some clips.

The real question is not:

> **Does this setting technically work?**

It is:

> **Does this make the workflow better?**

---

# Keep a Known-Good Setup

Once the controller behaves reliably, it is useful to know what that setup consists of.

Record important information such as:

```text
Bitwig Version

DrivenByMoss Version

X-Touch Firmware

X-Touch Mode

Track Navigation

Fader-Touch Preferences

New Clip Length

Important Sensitivity Values

Custom Assignments
```

If something changes after an update, you now have a known reference.

---

# Version Matters

DrivenByMoss continues to develop.

Bitwig continues to develop.

The mapping may therefore change over time.

Project XTC should state the versions against which its behaviour has been verified.

That does not mean the guide instantly becomes obsolete after an update.

It means the reader knows:

> **This is the configuration against which these instructions were tested.**

A newer version can then be compared against something concrete.

---

# Perform a Sanity Check After Updates

After updating Bitwig or DrivenByMoss, test a few fundamentals.

For example:

```text
Transport       ✓

Faders          ✓

SELECT          ✓

BANK / CHANNEL  ✓

Displays        ✓

V-Pots          ✓

Device Mode     ✓

Sends           ✓
```

Then test any specialised workflows you depend on.

This takes little time and can prevent a great deal of confusion.

---

# Troubleshooting by Layer

Remember the system:

```text
X-Touch Hardware
       │
       ▼
MC Mode
       │
       ▼
MIDI Communication
       │
       ▼
DrivenByMoss
       │
       ▼
Bitwig
```

If something fails, work from the bottom upwards.

---

## Is the X-Touch in MC Mode?

If not, fix that first.

---

## Does Basic Transport Work?

If PLAY and STOP do not work, the problem is probably more fundamental than Browser Mode or Layers.

---

## Do Faders Send and Receive?

If moving a fader changes Bitwig but the motor never moves in response, investigate the return communication.

---

## Do Displays Update?

If control works but assignments are unclear or stale, investigate the feedback path and hardware/display setup.

---

## Does Only One Advanced Feature Fail?

Now inspect:

- the relevant mode;
- the relevant preference;
- the selected track/device;
- the current project structure.

Troubleshooting becomes much easier when approached in layers.

---

# Don't Forget the Obvious Things

Sophisticated control-surface problems can have wonderfully uninteresting causes.

Check:

```text
Power

MC Mode

Controller Extension Active

Correct Communication

Expected Track Selected

Expected Mode Selected

Expected Device Exists

Expected Project Object Exists
```

Do not begin by assuming an obscure MCU protocol failure.

---

# A Sensible Starting Configuration

Project XTC should not prescribe one universal configuration.

But for someone following the workflows in this guide, a sensible starting point is:

```text
X-Touch
   → MC Mode

Hardware
   → X-Touch Profile

Firmware
   → Current supported X-Touch firmware

Track Navigation
   → Choose Flat or Hierarchical deliberately

New Clip Length
   → Set to common working length

Fader Touch
   → Configure deliberately rather than accidentally

Knob Sensitivity
   → Adjust only if physical response feels wrong

Startup Mode
   → Choose normal starting workflow

Advanced Preferences
   → Leave alone until they solve a real problem
```

Then use the controller.

Let actual workflow friction tell you which setting deserves attention.

---

# Configuration Should Eventually Disappear

This may sound odd in a chapter about configuration.

But the goal of good configuration is to stop thinking about configuration.

Eventually:

```text
Turn On X-Touch
      ↓
Open Bitwig
      ↓
Work
```

The controller should not require a ritual of preference checking at the start of every session.

The setup has succeeded when it becomes invisible.

---

# The Important Idea

DrivenByMoss configuration determines the environment in which all the controls described in Project XTC operate.

Important preferences include:

```text
Hardware Profile

Display Setup

Track Navigation

FX / Master Track Banking

Startup Mode

New Clip Length

Fader-Touch Behaviour

Knob Sensitivity

Transport Behaviour

Arranger / Launcher Priority

Quantize Amount

Browser Filtering
```

The aim is not to create the most sophisticated possible setup.

It is to create the most **predictable** one.

A good configuration reduces repeated decisions.

It makes the physical behaviour match the way you think about the project.

And then it gets out of the way.

The ideal result is:

```text
Intention
    ↓
Physical Action
    ↓
Musical Result
```

with the configuration quietly supporting that connection in the background.

---

## Coming Next

DrivenByMoss configuration determines how the standard X-Touch workflow behaves.

But the system can go further.

Function buttons and footswitches can be assigned.

Bitwig Actions can be attached to physical controls.

Clip Based Looper provides a specialised performance workflow.

And additional MCU-compatible surfaces can expand the number of physical channel strips.

Next:

**Customisation and Expansion.**
