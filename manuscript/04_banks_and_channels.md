---
chapter: 4
title: Banks and Channels
revision: "1.0"
status: draft
---

One of the first things to understand about the X-Touch is that it always provides **eight physical channel strips**, regardless of how many tracks exist in your Bitwig project.

If your project contains more than eight tracks, the X-Touch simply changes *which* eight tracks are currently under your control. This is where the ideas of **channels** and **banks** become important.

## Channels

Each motor fader represents a **channel**.

In the simplest case:

| X-Touch | Bitwig |
|---------|---------|
| Channel 1 | Track 1 |
| Channel 2 | Track 2 |
| Channel 3 | Track 3 |
| ... | ... |
| Channel 8 | Track 8 |

If your project contains eight tracks or fewer, this relationship never changes.

The X-Touch behaves very much like a traditional hardware mixer.

## Banks

Once your project grows beyond eight tracks, the controller cannot display every track at once.

Instead, it displays a **bank** of eight consecutive tracks.

The first bank contains:

- Tracks 1–8

The second bank contains:

- Tracks 9–16

The third bank contains:

- Tracks 17–24

and so on.

Changing bank simply changes which group of eight tracks is currently mapped onto the eight physical channel strips.

::: field-note

The hardware never changes.

Only the relationship between the hardware and the Bitwig project changes.

:::

## BANK Buttons

The **BANK ◀** and **BANK ▶** buttons move one complete bank at a time.

For example, if you are currently controlling Tracks 1–8:

- Press **BANK ▶** once.
- The scribble strips now display Tracks 9–16.
- The motor faders immediately move to the stored levels for those tracks.

Press **BANK ◀** to return to the previous bank.

Watching the motor faders reposition themselves is one of the most satisfying demonstrations of what a motorised control surface can do.

## CHANNEL Buttons

The **CHANNEL ◀** and **CHANNEL ▶** buttons work differently.

Instead of moving by eight tracks, they move by **one track**.

Imagine you are currently controlling:

| Fader | Track |
|-------|-------|
| 1 | Track 1 |
| 2 | Track 2 |
| 3 | Track 3 |
| 4 | Track 4 |
| 5 | Track 5 |
| 6 | Track 6 |
| 7 | Track 7 |
| 8 | Track 8 |

Press **CHANNEL ▶** once.

Now the mapping becomes:

| Fader | Track |
|-------|-------|
| 1 | Track 2 |
| 2 | Track 3 |
| 3 | Track 4 |
| 4 | Track 5 |
| 5 | Track 6 |
| 6 | Track 7 |
| 7 | Track 8 |
| 8 | Track 9 |

Every channel shifts along by one track.

This makes it easy to bring a particular track into view without jumping an entire bank.

::: reality-check

If a track seems to have "disappeared", it has probably moved outside the currently visible bank.

Use the BANK or CHANNEL buttons to bring it back into view.

:::

## Reading the Scribble Strips

Whenever you change bank or channel offset, the scribble strips update immediately.

Experienced users naturally glance at the displays before touching a fader.

This simple habit avoids accidental edits to the wrong track.

## Why This Matters

Understanding banks and channels makes the rest of the X-Touch much easier to understand.

Whether you are controlling volume, sends, plug-ins or automation, the same principle always applies:

> The X-Touch controls the tracks that are currently visible.

Everything else in the controller builds upon this idea.

::: exercise

Create a Bitwig project containing at least twelve tracks.

Use the **BANK ▶** and **BANK ◀** buttons to move between the first and second banks.

Then experiment with the **CHANNEL ▶** button and watch how the scribble strips and motor faders update.

Pay particular attention to which track appears on Channel 1 after each movement.

:::
