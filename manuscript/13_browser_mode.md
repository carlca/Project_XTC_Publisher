---
chapter: 13
title: "Browser Mode"
status: draft
---

# Browser Mode

Sooner or later, controlling a project means adding something that is not already there.

You may want to add:

- an instrument;
- an audio effect;
- a note effect;
- a preset;
- a device before another device;
- a device after another device;
- a replacement for an existing device.

Normally, these operations involve Bitwig's Browser and therefore encourage a return to the mouse.

DrivenByMoss gives the X-Touch direct access to the Browser.

This is one of the most important steps toward a Mouse-Lite workflow.

---

# The USER Button

On the X-Touch, the physical button used for Browser access is:

```text
USER
```

DrivenByMoss maps it to Browser operations.

The basic action is:

```text
USER
   → Open Browser
```

So when this guide refers to the Browser button, it means the physical:

```text
USER
```

button on the X-Touch.

---

# Opening the Browser

Press:

```text
USER
```

to open Bitwig's Browser.

Conceptually:

```text
Current Project
      │
      │ USER
      ▼
Bitwig Browser
```

The X-Touch now changes context.

The controls that previously represented mixer or device functions become Browser controls.

This is an important transition:

```text
Normal Control Context
        ↓
      USER
        ↓
Browser Control Context
```

---

# Browser Mode Is Contextual

The USER button illustrates one of the most important ideas in Project XTC:

> **A button's meaning can depend on the context in which you press it.**

Before the Browser is open:

```text
USER
   → Open Browser
```

But once Browser Mode is active:

```text
USER
   → Confirm Selection
     and Close Browser
```

The physical button has not changed.

The context has.

This is exactly the kind of behaviour for which the X-Touch's displays and feedback are important.

---

# Three Ways to Enter the Browser

DrivenByMoss gives USER three useful entry operations.

Press:

```text
USER
```

for the normal Browser operation.

Use:

```text
SHIFT + USER
```

to open the Browser for insertion:

```text
before
```

the current device.

Use:

```text
OPTION + USER
```

to open it for insertion:

```text
after
```

the current device.

So:

```text
USER
   → Browser

SHIFT + USER
   → Browser Insert Before

OPTION + USER
   → Browser Insert After
```

These operations determine the purpose of the Browser before you begin choosing what to insert.

---

# Insertion Position Matters

Suppose a track contains:

```text
Instrument
    ↓
EQ
    ↓
Compressor
    ↓
Delay
```

and the Compressor is the current device.

If you use:

```text
SHIFT + USER
```

the Browser is opened to insert something before the current device:

```text
EQ
    ↓
New Device
    ↓
Compressor
```

If you use:

```text
OPTION + USER
```

the Browser is opened to insert after it:

```text
Compressor
    ↓
New Device
    ↓
Delay
```

This lets the hardware express not merely:

> **Add a device.**

but:

> **Add a device here.**

---

# Before Entering and After Entering Are Different Contexts

There is an important detail here.

Before Browser Mode is active:

```text
SHIFT + USER
   → Browser Insert Before
```

But after Browser Mode is active:

```text
SHIFT + USER
   → Discard Browser Selection
     and Close
```

So the same combination has two meanings:

```text
Before Browser Opens
        │
        │ SHIFT + USER
        ▼
Insert Before
```

versus:

```text
Browser Already Open
        │
        │ SHIFT + USER
        ▼
Discard / Cancel
```

This is deliberate contextual reuse.

It is not a contradiction.

---

# USER Also Changes Meaning Once the Browser Is Open

The unmodified USER button behaves similarly.

Before Browser Mode:

```text
USER
   → Open Browser
```

Once Browser Mode is active:

```text
USER
   → Confirm
     and Close Browser
```

So:

```text
Before Browser
     USER
      ↓
     Open
```

and:

```text
Inside Browser
     USER
      ↓
Confirm / Close
```

This makes USER act rather like a context-sensitive Browser key:

```text
Enter Browser
     ↓
Work
     ↓
Confirm Browser
```

using the same physical button.

---

# Confirming a Browser Selection

DrivenByMoss provides two ways to confirm the current Browser selection.

You can press:

```text
ENTER
```

or, while Browser Mode is active:

```text
USER
```

Both mean:

```text
Confirm Selection
      ↓
Close Browser
```

So:

```text
ENTER
   → Confirm and Close
```

and:

```text
USER
   → Confirm and Close
     when Browser Mode is active
```

This gives you a choice between a dedicated confirmation control and the same button that originally opened the Browser.

---

# Cancelling a Browser Operation

Likewise, DrivenByMoss provides two ways to abandon the current Browser operation.

Press:

```text
CANCEL
```

or, while Browser Mode is active:

```text
SHIFT + USER
```

Both discard the Browser operation.

So:

```text
CANCEL
   → Discard and Close
```

and:

```text
SHIFT + USER
   → Discard and Close
     when Browser Mode is active
```

This creates a useful symmetry:

```text
ENTER
or USER
   → Accept
```

```text
CANCEL
or SHIFT + USER
   → Reject
```

---

# The Important Context Rule

The contextual USER behaviour is worth memorising as a small table:

```text
BEFORE BROWSER MODE

USER
   → Open Browser

SHIFT + USER
   → Insert Before

OPTION + USER
   → Insert After
```

Once Browser Mode is active:

```text
INSIDE BROWSER MODE

USER
   → Confirm and Close

SHIFT + USER
   → Discard and Close

ENTER
   → Confirm and Close

CANCEL
   → Discard and Close
```

The crucial distinction is:

```text
Before Browser
```

versus:

```text
Inside Browser
```

Do not interpret a modifier combination without considering the current context.

---

# Why Contextual Reuse Makes Sense

At first, this may appear confusing.

Why should:

```text
SHIFT + USER
```

mean both:

```text
Insert Before
```

and:

```text
Cancel
```

?

Because those operations occur at different stages.

Before Browser Mode:

```text
SHIFT + USER
```

answers:

> **How should I enter the Browser?**

Inside Browser Mode:

```text
SHIFT + USER
```

answers:

> **What should I do with this Browser operation?**

The meanings do not compete because the controller can only be in one of those contexts at a time.

---

# Browser Feedback

Once Browser Mode is active, the X-Touch's displays become particularly important.

The scribble strips can show Browser-related choices rather than track or device parameters.

Conceptually:

```text
Normal Mode

Track / Parameter Information
          ↓
        USER
          ↓
Browser Mode

Browser Choices
```

This is another example of the principle from Chapter 7:

> **Read before you touch.**

The same physical V-Pot may represent something entirely different once the Browser is active.

---

# The V-Pots Become Browser Controls

In Browser Mode, the eight V-Pots provide access to Browser choices.

Rather than controlling parameters such as:

```text
Pan

Send Level

Cutoff

Feedback
```

they can now represent categories or choices within the Browser.

The physical row becomes a Browser-navigation interface.

Conceptually:

```text
V-Pot 1
V-Pot 2
V-Pot 3
...
V-Pot 8
```

becomes:

```text
Browser Choice 1
Browser Choice 2
Browser Choice 3
...
Browser Choice 8
```

The displays tell you what those choices currently mean.

---

# Turn to Navigate, Press to Choose

The general interaction follows the familiar V-Pot pattern.

Turn a V-Pot:

```text
Turn
   ↓
Move Through Choices
```

Press a V-Pot:

```text
Press
   ↓
Choose / Enter
```

The exact Browser level represented by each control depends on the current Browser state.

The important point is that the X-Touch can navigate the Browser without requiring every selection to be made with the mouse.

---

# Browser Navigation Is Hierarchical

Bitwig's Browser contains different levels of choice.

Conceptually:

```text
What Kind of Thing?
        ↓
Which Category?
        ↓
Which Device?
        ↓
Which Preset?
```

DrivenByMoss exposes this hierarchy through the X-Touch.

The V-Pots and displays provide a moving window onto the current Browser level.

This should feel familiar by now.

We have already seen the same basic idea with:

```text
Tracks
   ↓
Devices
   ↓
Parameter Pages
   ↓
Parameters
```

Browser Mode applies contextual hardware navigation to another hierarchy.

---

# Do Not Navigate Blindly

Browser Mode is not a good place to rely entirely on memorised knob positions.

The available choices change according to:

- what you are browsing for;
- the current category;
- the current device context;
- the available content;
- the current Browser state.

So:

```text
Look at Display
      ↓
Identify Choice
      ↓
Turn / Press
```

is safer than:

```text
I think Pot 4 was Reverb last time
```

Browser choices are contextual.

Read them.

---

# A Basic Browser Workflow

A typical operation might be:

```text
Select Track
     ↓
USER
     ↓
Navigate Browser
     ↓
Choose Device
     ↓
ENTER
```

or:

```text
Select Track
     ↓
USER
     ↓
Navigate Browser
     ↓
Choose Device
     ↓
USER
```

Both final routes confirm and close the Browser.

The difference is simply which physical confirmation control you prefer.

---

# Adding a Device Before the Current Device

Suppose you want to insert an EQ before a Compressor.

Select the Compressor as the current device.

Then:

```text
SHIFT + USER
```

This opens the Browser in Insert-Before context.

Navigate to:

```text
EQ+
```

Then confirm with either:

```text
ENTER
```

or:

```text
USER
```

The resulting chain becomes:

```text
EQ+
 ↓
Compressor
```

The whole operation can be initiated and confirmed from the X-Touch.

---

# Adding a Device After the Current Device

Suppose you want to add a Delay after the Compressor.

Use:

```text
OPTION + USER
```

Navigate to the Delay.

Confirm:

```text
ENTER
```

or:

```text
USER
```

The chain becomes:

```text
Compressor
    ↓
Delay
```

Again, the insertion location was specified before entering the Browser.

---

# Cancelling an Insert-Before Operation

This provides a useful example of the contextual SHIFT + USER behaviour.

Start with:

```text
SHIFT + USER
```

At this point it means:

```text
Open Browser
for Insert Before
```

Suppose you then decide not to insert anything.

While Browser Mode is active, press:

```text
SHIFT + USER
```

again.

Now it means:

```text
Discard
and Close Browser
```

So the complete sequence can be:

```text
SHIFT + USER
      ↓
Enter Insert-Before Browser
      ↓
Browse
      ↓
Change Your Mind
      ↓
SHIFT + USER
      ↓
Discard / Close
```

The same combination begins and abandons the operation because its meaning changes with Browser context.

---

# USER Can Form a Complete Browser Round Trip

The unmodified USER button can likewise form a neat round trip:

```text
USER
   ↓
Open Browser
   ↓
Navigate
   ↓
USER
   ↓
Confirm and Close
```

This is worth practising.

Once familiar, USER becomes not merely:

```text
the button that opens the Browser
```

but:

```text
the contextual Browser button
```

It can take you into the Browser and, once there, accept the result.

---

# ENTER and CANCEL Remain the Clearest Choices

Although USER and SHIFT + USER provide contextual confirmation and cancellation, the dedicated buttons remain very clear:

```text
ENTER
   → Yes
```

```text
CANCEL
   → No
```

For a new user, these may initially be easier to remember.

Then, as the contextual USER behaviour becomes familiar:

```text
USER
   → Confirm
```

and:

```text
SHIFT + USER
   → Cancel
```

can make Browser operation more compact.

There is no need to force yourself to use the shortest route immediately.

---

# Context Before Combination

Browser Mode gives us a particularly good example of a wider X-Touch rule.

Do not ask only:

> **What does SHIFT + USER do?**

Ask:

> **What does SHIFT + USER do in my current context?**

The answer is:

```text
Outside Browser Mode
   → Open Browser for Insert Before

Inside Browser Mode
   → Discard and Close
```

So the more general rule is:

```text
Physical Control
      +
Modifier
      +
Current Context
      =
Actual Operation
```

This is the same contextual model we have been building throughout the guide.

---

# Browser Mode and Device Mode Work Together

Browser Mode becomes especially useful when combined with Device Mode.

For example:

```text
SELECT Track
     ↓
DEVICE
     ↓
Select Device
     ↓
SHIFT + USER
     ↓
Insert Before
```

or:

```text
SELECT Track
     ↓
DEVICE
     ↓
Select Device
     ↓
OPTION + USER
     ↓
Insert After
```

Device Mode establishes:

```text
Where am I?
```

Browser Mode then answers:

```text
What do I want to add here?
```

The two modes complement one another.

---

# Browser Mode Can Change the Project

Unlike simple navigation, Browser operations can modify the project.

When you confirm an insertion:

```text
Project Structure
      ↓
Changes
```

A device may be added or replaced.

This means Browser Mode deserves a little more care than simply changing track bank.

Before confirming, check:

```text
Correct Track?

Correct Device Position?

Correct Browser Item?

Correct Insert Mode?
```

Then confirm.

---

# Confirm Versus Cancel

A useful safety habit is:

```text
Unsure?
   ↓
CANCEL
```

or:

```text
Unsure?
   ↓
SHIFT + USER
```

while Browser Mode is active.

You can always reopen the Browser once the intended operation is clear.

There is no benefit in confirming an uncertain insertion merely because you have already navigated part of the way through the Browser.

---

# Browser Mode and the Mouse-Lite Workflow

Browser Mode is important because browsing is traditionally a very mouse-heavy task.

Without hardware control:

```text
Open Browser
     ↓
Click Category
     ↓
Scroll
     ↓
Click Device
     ↓
Choose Preset
     ↓
Insert
```

With the X-Touch:

```text
USER
     ↓
Read Displays
     ↓
Turn / Press V-Pots
     ↓
USER or ENTER
```

The aim is not necessarily to make every Browser operation faster.

The aim is to make routine browsing possible without constantly changing physical interface.

---

# When the Screen Is Still Better

The Bitwig Browser can display a great deal of information.

For exploratory browsing, the screen may still be preferable.

For example:

- searching a large preset library;
- comparing many similarly named presets;
- browsing unfamiliar content;
- examining tags;
- navigating complex categories.

The X-Touch is particularly useful when:

```text
you broadly know what you want
```

and want to reach it without interrupting the hardware workflow.

Again, Mouse-Lite does not mean Mouse-Banned.

---

# A Practical Browser Exercise

Open a simple project.

Select a track.

### 1. Open the Browser

Press:

```text
USER
```

Observe the scribble strips.

Notice that their meaning has changed.

### 2. Navigate

Use the V-Pots to move through the available Browser choices.

Read the displays before pressing anything.

### 3. Cancel

Press:

```text
CANCEL
```

Confirm that the Browser closes without completing the operation.

### 4. Open Again

Press:

```text
USER
```

Navigate to a harmless choice.

### 5. Confirm with ENTER

Press:

```text
ENTER
```

Observe the result.

The purpose is to establish:

```text
USER
   → Enter Browser

ENTER
   → Confirm

CANCEL
   → Discard
```

before introducing the contextual shortcuts.

---

# A Practical Contextual USER Exercise

Now repeat the exercise using USER itself for confirmation.

Press:

```text
USER
```

to open the Browser.

Navigate to a choice.

Then press:

```text
USER
```

again.

The second press now means:

```text
Confirm and Close
```

So practise:

```text
USER
  ↓
Browse
  ↓
USER
```

until the context change feels natural.

---

# A Practical Contextual SHIFT + USER Exercise

Select a device.

Press:

```text
SHIFT + USER
```

This means:

```text
Insert Before
```

because Browser Mode is not yet active.

Once the Browser is open, do not confirm anything.

Press:

```text
SHIFT + USER
```

again.

This time it means:

```text
Discard and Close
```

The complete exercise is:

```text
SHIFT + USER
      ↓
Browser Opens
      ↓
SHIFT + USER
      ↓
Browser Cancels
```

The purpose is not the operation itself.

It is to experience directly how **context changes the meaning of the same physical combination**.

---

# A Practical Insert-Position Exercise

Create a simple device chain:

```text
Instrument
    ↓
Compressor
    ↓
Delay
```

Select the Compressor.

Try:

```text
SHIFT + USER
```

and insert an EQ.

Observe where it appears.

Undo if necessary.

Then select the Compressor again and try:

```text
OPTION + USER
```

Insert another device.

Observe the difference.

The goal is to establish:

```text
SHIFT
   → Before
```

```text
OPTION
   → After
```

when entering Browser Mode.

---

# If Browser Mode Becomes Confusing

Ask these questions in order:

```text
Is the Browser already open?

Which track is selected?

Which device is current?

How did I enter Browser Mode?

What do the scribble strips show?

Am I choosing or confirming?

Do I want to accept or discard?
```

The first question is especially important because it determines the contextual meaning of USER and SHIFT + USER.

---

# A Useful Mental Model

Think of Browser Mode as having two phases.

## Phase 1 — Enter

```text
USER
   → Browse Normally

SHIFT + USER
   → Insert Before

OPTION + USER
   → Insert After
```

Then the context changes.

## Phase 2 — Resolve

```text
USER
or ENTER
   → Confirm
```

```text
SHIFT + USER
or CANCEL
   → Discard
```

So:

```text
          OUTSIDE BROWSER
                │
      ┌─────────┼──────────┐
      │         │          │
    USER    SHIFT+USER  OPTION+USER
      │         │          │
      ▼         ▼          ▼
   Browse     Before      After
      │         │          │
      └─────────┼──────────┘
                ▼
          INSIDE BROWSER
                │
        ┌───────┴───────┐
        │               │
 USER / ENTER   SHIFT+USER / CANCEL
        │               │
        ▼               ▼
     Confirm          Discard
        │               │
        └───────┬───────┘
                ▼
           Browser Closed
```

That diagram captures the contextual behaviour more accurately than memorising the buttons as a flat list.

---

# The Important Idea

Browser Mode brings one of Bitwig's most mouse-oriented workflows onto the X-Touch.

Before Browser Mode is active:

```text
USER
   → Open Browser
```

```text
SHIFT + USER
   → Browser Insert Before
```

```text
OPTION + USER
   → Browser Insert After
```

Once Browser Mode is active, USER and SHIFT + USER acquire contextual meanings:

```text
USER
   → Confirm and Close
```

```text
SHIFT + USER
   → Discard and Close
```

The dedicated controls remain available:

```text
ENTER
   → Confirm and Close
```

```text
CANCEL
   → Discard and Close
```

So the key lesson is not merely a list of shortcuts.

It is:

> **The meaning of USER depends on whether you are entering the Browser or already inside it.**

That gives us a compact Browser workflow:

```text
Enter
  ↓
Navigate
  ↓
Confirm or Discard
```

entirely from the control surface.

And it reinforces one of the central ideas of Project XTC:

```text
Physical Control
      +
Modifier
      +
Context
      =
Function
```

Once that principle becomes familiar, contextual mappings stop feeling arbitrary and start becoming one of the X-Touch's greatest strengths.

---

## Coming Next

Browser Mode lets us add and place devices without immediately returning to the mouse.

Next we return to the mixer and look at another way the same eight V-Pots can be transformed into a much broader editing surface.

Next:

**Mixer Edit Modes.**
