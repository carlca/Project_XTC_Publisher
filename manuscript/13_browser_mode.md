---
chapter: 13
title: "Browser Mode"
status: draft
---

# Browser Mode

Device Mode lets us control devices that are already present.

Browser Mode answers a different question:

> **What if the device, preset or item I want is not there yet?**

Bitwig's Browser is where new material enters the project.

Normally, that means reaching for the mouse.

DrivenByMoss gives the X-Touch a hardware route into the Browser.

The surface can be used to:

- open the Browser;
- navigate Browser tabs and columns;
- scroll results;
- insert a device before the current device;
- insert a device after the current device;
- replace the current device;
- confirm the selection;
- cancel the operation.

So Browser Mode is not merely another edit mode.

It is the point where the X-Touch can help **bring something new into the project**.

---

# Entering Browser Mode

DrivenByMoss maps the X-Touch's USER button to the Browser.

Press:

```text
USER
   │
   ▼
Open Browser
```

This starts a normal Browser operation.

The X-Touch controls then acquire Browser-specific meanings.

---

# USER Is Not Just "User"

The button is physically labelled:

```text
USER
```

because that is part of the Mackie Control layout.

DrivenByMoss gives it a useful Bitwig-specific role:

```text
USER
   → Browser
```

This is another example of a principle we have already encountered:

> **The printed MCU label does not necessarily describe the literal Bitwig function.**

The DrivenByMoss mapping is what matters.

---

# Three Ways to Start Browsing

DrivenByMoss documents three Browser-entry commands:

```text
USER
   → Start Browser
```

```text
SHIFT + USER
   → Insert new device before
     the current device
```

```text
OPTION + USER
   → Insert new device after
     the current device
```

So the modifier determines the intended insertion point.

---

# Normal Browser Entry

Pressing:

```text
USER
```

opens the Browser in its normal context.

Think:

> **I want to browse.**

Once inside, the Browser-specific controls determine what happens next.

---

# SHIFT + USER — Insert Before

Hold SHIFT and press USER:

```text
SHIFT + USER
      │
      ▼
Insert New Device
Before Current Device
```

Suppose a device chain is:

```text
EQ
   ↓
Compressor
   ↓
Delay
```

and Compressor is the current device.

Using:

```text
SHIFT + USER
```

starts the Browser with the intention of inserting something before Compressor.

Conceptually:

```text
Before

EQ
   ↓
[Compressor]
   ↓
Delay
```

then:

```text
SHIFT + USER
```

and after choosing a new device:

```text
EQ
   ↓
New Device
   ↓
[Compressor]
   ↓
Delay
```

---

# OPTION + USER — Insert After

OPTION gives the complementary operation:

```text
OPTION + USER
       │
       ▼
Insert New Device
After Current Device
```

Using the same chain:

```text
EQ
   ↓
[Compressor]
   ↓
Delay
```

OPTION + USER begins a Browser operation that inserts after the current device.

After choosing something:

```text
EQ
   ↓
[Compressor]
   ↓
New Device
   ↓
Delay
```

So the pair is easy to understand:

```text
SHIFT + USER
   → before

OPTION + USER
   → after
```

---

# Why Insertion Position Matters

A device chain is ordered.

Changing the order can change the sound.

For example:

```text
Distortion
   ↓
Delay
```

does not necessarily sound the same as:

```text
Delay
   ↓
Distortion
```

So Browser insertion is not simply:

> **Add something.**

It is:

> **Add something at the correct place in the chain.**

DrivenByMoss lets the insertion intention be established before browsing begins.

---

# The Browser Changes the Surface

Once Browser Mode is active, controls that previously manipulated tracks or parameters now navigate the Browser.

Conceptually:

```text
Normal Context
      │
      ▼
Mixer / Device Controls
```

then:

```text
USER
  ↓
Browser Context
      │
      ▼
Browser Navigation Controls
```

The hardware has not changed.

The job has.

---

# Browser Tabs

Bitwig's Browser can contain several tabs or categories of browsing context.

DrivenByMoss maps the vertical arrow buttons to them:

```text
↑
   → Previous Browser Tab
```

```text
↓
   → Next Browser Tab
```

So the up/down arrows move between Browser tabs rather than behaving as ordinary keyboard arrows while this context is active.

---

# Browser Tabs as a Higher Level

A useful way to think about Browser navigation is:

```text
Browser
   │
   ├── Tab
   │     │
   │     └── Columns / Filters
   │             │
   │             └── Results
```

The vertical arrows operate at the Tab level.

The V-Pots and Jog Wheel work further down inside the Browser.

---

# V-Pots Navigate Browser Columns

The eight V-Pots become Browser controls.

DrivenByMoss uses them to navigate the Browser columns.

Conceptually:

```text
Browser Column 1
      │
      ▼
V-Pot 1

Browser Column 2
      │
      ▼
V-Pot 2

Browser Column 3
      │
      ▼
V-Pot 3

...
```

Turning a V-Pot moves through the choices available in that column.

---

# Turning Means Choosing from a List

Outside Browser Mode, a V-Pot often changes a continuous value:

```text
0% ─────────────── 100%
```

In Browser Mode, it moves through discrete choices:

```text
Bass
Keys
Lead
Pad
Percussion
FX
```

So:

```text
Turn V-Pot
      │
      ▼
Move through Browser choices
```

The encoder works equally well for both because it has no fixed physical endpoint.

---

# Pressing a V-Pot

Pressing a V-Pot enters or confirms the current filter or result at that Browser level.

Conceptually:

```text
Turn
   → choose
```

then:

```text
Press
   → enter / confirm
```

This makes the V-Pot a two-part Browser control:

```text
Turn
   → navigate

Press
   → select
```

That is a very natural extension of the rotary-and-push design.

---

# The Jog Wheel Scrolls Results

DrivenByMoss also maps the Jog Wheel to Browser result navigation.

In Browser Mode:

```text
Jog Wheel
   → Scroll Browser Results
```

This is particularly useful once the broad filters have narrowed the Browser to a list of candidate items.

Think:

```text
V-Pots
   → narrow the search

Jog Wheel
   → move through results
```

The controls divide the Browser into different navigation jobs.

---

# Browser Filtering and Result Selection

Conceptually, the workflow can be:

```text
Choose Browser Tab
       ↓
Use V-Pots to choose filters
       ↓
Use Jog Wheel to scroll results
       ↓
Choose Result
       ↓
ENTER
```

This allows a large part of the Browser interaction to remain on the X-Touch.

---

# LEFT — Insert Before

Once Browser Mode is active, the left arrow has a device-insertion meaning.

DrivenByMoss documents:

```text
←
   → Insert Before Current Device
```

This allows the insertion intention to be changed from within the Browser.

Conceptually:

```text
Current Device
      │
      ▼
←
      │
      ▼
Insert Before
```

---

# RIGHT — Insert After

The right arrow provides the complementary operation:

```text
→
   → Insert After Current Device
```

So inside Browser Mode:

```text
←
   → before
```

```text
→
   → after
```

The spatial relationship makes this particularly easy to remember.

---

# ZOOM — Replace the Current Device

DrivenByMoss assigns another Browser function to the ZOOM button:

```text
ZOOM
   → Replace Current Device
```

This gives us a third insertion strategy.

We can:

```text
Insert Before

Insert After

Replace
```

without leaving the Browser workflow.

---

# Three Placement Choices

The Browser therefore offers three device-placement intentions:

```text
←
   → Before
```

```text
ZOOM
   → Replace
```

```text
→
   → After
```

Conceptually:

```text
        Current Device

Before      Replace      After
   │           │           │
   ▼           ▼           ▼
   ←         ZOOM          →
```

That is a remarkably compact physical model.

---

# Why Replace Is Different

Insertion preserves the current device and adds another one.

Replacement removes the current device from that position and substitutes the chosen Browser result.

So:

```text
Insert
   → add
```

while:

```text
Replace
   → substitute
```

That is a consequential difference.

Use ZOOM deliberately when browsing.

---

# ENTER — Confirm and Close

Once you have chosen the desired Browser result:

```text
ENTER
   → Confirm Selection
     and Close Browser
```

This is one of the clearest uses of ENTER on the X-Touch.

The operation means exactly what its label suggests:

> **Yes — use this.**

---

# CANCEL — Discard

If you decide not to use the Browser selection:

```text
CANCEL
   → Discard Browser Operation
```

Think:

> **No — leave things as they were.**

So Browser Mode gives ENTER and CANCEL a very natural pair:

```text
ENTER
   → accept

CANCEL
   → reject
```

---

# ENTER and CANCEL Finally Have Their Obvious Jobs

Earlier chapters deliberately clarified that ENTER and CANCEL are **not** used for hierarchical Group navigation.

That workflow uses SELECT.

Browser Mode is where ENTER and CANCEL become particularly intuitive:

```text
Browser Result
      │
      ├── ENTER
      │      ↓
      │    Keep It
      │
      └── CANCEL
             ↓
           Discard
```

This separation of roles is worth learning.

---

# A Basic Browser Workflow

Suppose you want to add a delay after the currently selected device.

A hardware-oriented workflow might be:

```text
OPTION + USER
       ↓
Browser Opens
       ↓
Choose Browser Tab
       ↓
Use V-Pots
       ↓
Narrow to Delay
       ↓
Use Jog Wheel
       ↓
Choose Result
       ↓
ENTER
       ↓
Delay Inserted After
Current Device
```

The mouse need not be involved.

---

# A Replace Workflow

Suppose a track already contains one delay but you want to audition another.

Start Browser Mode.

Then choose:

```text
ZOOM
   → Replace
```

Navigate the Browser.

Select another delay.

Press:

```text
ENTER
```

The current device is replaced by the selected result.

If you change your mind before confirming:

```text
CANCEL
```

abandons the operation.

---

# Auditioning Possibilities

Browser Mode can be especially useful when you know broadly what you want but not the exact item.

For example:

> **I want a delay, but I am not sure which one.**

The process becomes:

```text
Open Browser
     ↓
Filter to Delay
     ↓
Scroll Results
     ↓
Try Candidate
     ↓
Choose
```

The controller handles the navigation while your attention stays on the musical result.

---

# Browser Mode Is About Decisions

Device Mode is mostly about:

```text
adjusting something that already exists
```

Browser Mode is about:

```text
choosing something new
```

That difference is important.

In Device Mode:

```text
Turn
   → change value
```

In Browser Mode:

```text
Turn
   → move through possibilities
```

The X-Touch changes from an editor into a selector.

---

# The V-Pots Become a Menu

A useful way to think about the Browser is that the V-Pot row becomes a physical menu system.

Normally:

```text
V-Pot
   → parameter
```

In Browser Mode:

```text
V-Pot
   → Browser choice
```

Turn:

```text
Next / Previous Choice
```

Press:

```text
Choose
```

This is another example of the V-Pots acting as general-purpose contextual controls.

---

# Browse by Category, Not by Screen Position

A mouse-driven Browser workflow often feels spatial:

```text
Where is the category?

Where is the result?

Where is the scroll bar?
```

The X-Touch workflow is more conceptual:

```text
Which category?

Which filter?

Which result?
```

That can become faster once the Browser structure is familiar.

---

# Browser Mode and the Scribble Strips

The scribble strips become especially important in Browser Mode because the V-Pots are no longer controlling familiar mixer parameters.

They need to tell you:

```text
which Browser field
```

and:

```text
which current choice
```

each V-Pot represents.

So:

> **Read before you turn.**

This principle is at least as important in Browser Mode as in Device Mode.

---

# Do Not Browse Blindly

If you forget which Browser column a V-Pot currently represents, do not simply turn controls until something useful happens.

Instead:

```text
Look
  ↓
Read Labels
  ↓
Understand Current Filter
  ↓
Turn
```

Browser navigation is inherently about making choices.

Good feedback makes those choices deliberate.

---

# Browser Mode Can Change the Project

Browser operations are consequential.

Depending on the chosen operation, you may:

```text
Insert Device Before
```

```text
Insert Device After
```

or:

```text
Replace Current Device
```

These are project edits, not merely navigation.

So before confirming with ENTER, ask:

> **Is this the item I want, and is it going to the right place?**

That is a useful Browser habit.

---

# CANCEL Is Your Safety Net

Because Browser Mode can change the device chain, CANCEL is valuable.

If you become unsure:

```text
CANCEL
```

Discard the operation.

Then begin again.

There is no prize for forcing an uncertain Browser choice through to completion.

The controller gives you an explicit way out.

---

# Browser Mode and Device Chains

Suppose the current track contains:

```text
EQ
   ↓
Compressor
   ↓
Delay
```

with Compressor selected.

The Browser can now support three different intentions.

## Before

```text
SHIFT + USER
```

or choose the left-arrow insertion behaviour.

Result:

```text
EQ
   ↓
New Device
   ↓
Compressor
   ↓
Delay
```

## After

```text
OPTION + USER
```

or choose the right-arrow insertion behaviour.

Result:

```text
EQ
   ↓
Compressor
   ↓
New Device
   ↓
Delay
```

## Replace

```text
ZOOM
```

Result:

```text
EQ
   ↓
New Device
   ↓
Delay
```

This gives the Browser a clear structural relationship with the device chain.

---

# Starting Before or After Can Save a Step

If you already know the desired insertion position, it is efficient to begin with:

```text
SHIFT + USER
```

or:

```text
OPTION + USER
```

rather than opening the Browser first and changing the insertion mode afterwards.

This follows a useful workflow principle:

> **Establish intention as early as possible.**

The Browser then opens already aimed at the correct kind of operation.

---

# The Arrow Keys Let You Change Your Mind

But perhaps you opened the Browser normally and then realise:

> **Actually, this should go before the compressor.**

Use:

```text
←
```

Or:

> **It should go after it.**

Use:

```text
→
```

The Browser workflow is flexible.

You do not necessarily need to cancel and start again merely because the insertion point changes.

---

# Replace Is Particularly Useful for Comparison

Suppose you are choosing between several compressors.

The current track contains:

```text
EQ
   ↓
Compressor A
   ↓
Saturator
```

Using Browser Replace, you can substitute:

```text
Compressor B
```

at the same position.

This makes comparison more straightforward because the surrounding chain remains structurally similar.

The important idea is:

```text
same place
   +
different device
```

rather than continually adding new devices to the chain.

---

# Browser Mode and the Mouse-Lite Workflow

The Browser is one of the more ambitious parts of a Mouse-Lite workflow.

For a completely unfamiliar Browser search, the graphical interface may still be faster.

For a familiar task such as:

> **Add a delay after the current device**

the X-Touch route can be very direct:

```text
OPTION + USER
       ↓
Filter
       ↓
Choose
       ↓
ENTER
```

The point is not to prove that every Browser operation can be performed without the mouse.

The point is that routine Browser tasks no longer have to begin with it.

---

# When the Mouse Is Better

Bitwig's graphical Browser may still be preferable when:

- exploring unfamiliar categories;
- reading long names;
- comparing lots of metadata;
- dragging items to precise locations;
- searching visually through a large set of results.

That is fine.

Project XTC's Mouse-Lite principle remains:

> **Use the interface best suited to the task.**

Hardware browsing becomes valuable when it reduces friction, not when it merely proves that hardware browsing is possible.

---

# Browser Mode as a Performance Tool

Browser Mode can also support experimentation.

Suppose playback is running and you decide the selected track needs another effect.

You can:

```text
Open Browser
     ↓
Choose Effect
     ↓
Insert
     ↓
Return to Listening
```

The creative cycle remains:

```text
Hear
  ↓
Choose
  ↓
Listen
```

rather than:

```text
Hear
  ↓
Leave musical focus
  ↓
Navigate interface
  ↓
Return
```

This is where hardware Browser access can feel particularly useful.

---

# A Practical Browser Exercise

Create a track containing at least one device.

Select that device.

### 1. Press USER

Observe the Browser open.

### 2. Use ↑ and ↓

Move between Browser tabs.

### 3. Turn the V-Pots

Observe the available filters or columns change.

### 4. Press a V-Pot

Enter or select the corresponding Browser choice.

### 5. Turn the Jog Wheel

Move through the result list.

### 6. Press CANCEL

Discard the operation.

Repeat the exercise until the Browser navigation itself feels comfortable.

---

# A Practical Insertion Exercise

Now try three placement operations.

Start with a simple chain:

```text
Device A
   ↓
Device B
```

Select Device B.

### Insert Before

Use:

```text
SHIFT + USER
```

choose a new device, then:

```text
ENTER
```

Observe where it appears.

Undo if required.

### Insert After

Use:

```text
OPTION + USER
```

choose another device and confirm.

### Replace

Open Browser Mode and use:

```text
ZOOM
```

choose a replacement and confirm.

The aim is to make these three intentions distinct:

```text
before

after

replace
```

---

# A Useful Mental Model

Browser Mode can be summarised as:

```text
                    Browser
                       │
            ┌──────────┼──────────┐
            │          │          │
         Before     Replace      After
            │          │          │
            ▼          ▼          ▼
       SHIFT+USER     ZOOM     OPTION+USER
```

Then inside the Browser:

```text
↑ / ↓
   → Browser Tabs

V-Pots
   → Browser Columns / Choices

Jog Wheel
   → Results

←
   → Insert Before

→
   → Insert After

ZOOM
   → Replace

ENTER
   → Confirm

CANCEL
   → Discard
```

The Browser therefore becomes another temporary control environment.

---

# The Important Idea

Browser Mode gives the X-Touch a hardware route for **choosing and inserting new material**.

The verified entry commands are:

```text
USER
   → Start Browser

SHIFT + USER
   → Insert New Device Before
     Current Device

OPTION + USER
   → Insert New Device After
     Current Device
```

Inside the Browser:

```text
↑ / ↓
   → Previous / Next Browser Tab

V-Pots
   → Navigate Browser Columns

Jog Wheel
   → Scroll Results

←
   → Insert Before

→
   → Insert After

ZOOM
   → Replace Current Device

ENTER
   → Confirm and Close

CANCEL
   → Discard
```

The central workflow is:

```text
Choose Placement
      ↓
Browse
      ↓
Choose Item
      ↓
Confirm
```

Device Mode answers:

> **How do I control what is already here?**

Browser Mode answers:

> **How do I bring in something new?**

Together, the two modes make the X-Touch far more than a mixer.

They give it a route into the structure and contents of the Bitwig project itself.

---

## Coming Next

We have now completed the main Part II chapters:

- V-Pots;
- Motor Faders;
- Transport;
- Device Mode;
- Browser Mode.

The next part goes deeper into the less obvious DrivenByMoss functionality.

We begin by reorganising the mixer around particular tasks rather than individual channel strips.

Next:

**Mixer Edit Modes.**
