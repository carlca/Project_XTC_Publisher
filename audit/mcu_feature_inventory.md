# DrivenByMoss MCU Feature Inventory

> **Purpose:** Editorial feature inventory for Project XTC.
>
> **Primary source:** `DrivenByMoss-Documentation/Mackie/Mackie-MCU.md`
>
> This document records the functionality described by the DrivenByMoss Mackie MCU documentation. It is an **audit checklist**, not a chapter of the book.
>
> No attempt is made here to decide whether a feature is already covered by Project XTC, where it should be taught, or how much explanation it deserves. Those decisions belong to the next stage of the audit.

---

# 1. X-Touch Configuration

## Hardware requirements

* Use the latest supported X-Touch firmware; the source documentation specifies **1.22**.
* Set the X-Touch operating mode to **MC**.
* Enable the X-Touch display-colour option in DrivenByMoss, or select the **X-Touch** hardware profile.

---

# 2. Transport

## PLAY

* **PLAY** — Start or stop playback.
* **Double-click PLAY** — Move the play cursor to the start of the song.
* **SHIFT + PLAY** — Toggle repeat.
* **OPTION + PLAY** — Toggle Punch In.
* **OPTION + SHIFT + PLAY** — Toggle Punch Out.

## RECORD

* **RECORD** — Start or stop recording.
* **SHIFT + RECORD** — Toggle Launcher overdub.
* **OPTION + RECORD** — Create a new clip on the selected track and slot, start playback and enable overdub.

## REWIND / FORWARD

* **REWIND (`<<`)** — Move the play cursor left.
* **FORWARD (`>>`)** — Move the play cursor right.
* **OPTION + REWIND** — Move to the closest marker before the current play position.
* **OPTION + FORWARD** — Move to the closest marker after the current play position.

## REPEAT

* **REPEAT** — Toggle repeat.

## STOP

* **STOP** — Stop playback.
* **STOP again** — Move the play cursor to the start of the song.
* **Double-click STOP** — Move the play cursor to the end of the song.

---

# 3. Jog Wheel and Navigation

## Jog Wheel

* **Jog Wheel** — Move the play cursor.
* **SHIFT + Jog Wheel** — Fine adjustment of the play cursor.
* **OPTION + Jog Wheel** — Change tempo.
* **OPTION + SHIFT + Jog Wheel** — Change tempo with fine adjustment.
* **CONTROL + Jog Wheel** — Change loop start.
* **CONTROL + SHIFT + Jog Wheel** — Change loop start with fine adjustment.
* **ALT + Jog Wheel** — Change loop length.
* **ALT + SHIFT + Jog Wheel** — Change loop length with fine adjustment.

## Arrow buttons

* **LEFT / RIGHT / UP / DOWN** — Behave like the corresponding computer keyboard arrow keys.

## ZOOM

When Zoom is active:

* **LEFT / RIGHT** — Zoom the Arranger horizontally.
* **UP / DOWN** — Toggle track height.

A preference can also allow vertical Zoom controls to select parameter modes.

## SCRUB

* **SCRUB** — Toggle through the available editing modes.

## NUDGE

* **NUDGE** — Execute Tap Tempo.

---

# 4. Display and Layout Controls

## Display Mode

* **Display Mode** — Toggle display of track names in the first display.

## Tempo / Ticks

* **Tempo/Ticks** — Toggle the final three digits of the segment display between ticks and song tempo.

## Global View / Edit

* **GLOBAL VIEW / EDIT** — Toggle VU meters.

## Layout buttons

* **AUX** — Switch to Arrange layout.
* **BUSSES** — Switch to Mix layout.
* **OUTPUTS** — Switch to Edit layout.

## New clip length

* **SHIFT + Track SELECT buttons** — Select a new-clip length:

  * 16 bars
  * 8 bars
  * 4 bars
  * 2 bars
  * 1 bar
  * 2 beats
  * 1 beat
  * 32 bars

---

# 5. Modifier and Function Buttons

## SHIFT

* Used with other controls to access additional functions.

## OPTION

* Used with other controls to access additional functions.

## F1–F8

* Functions can be assigned to the function buttons in the DrivenByMoss settings.

## UNDO

* **UNDO** — Undo the last action.
* **SHIFT + UNDO** — Redo the last undone action.

---

# 6. Assignment Controls

## TRACK

* **TRACK** — Select Track Edit Mode.
* **TRACK again** — Select Volume Edit Mode.
* **OPTION + TRACK** — Pin the cursor track.

## PAN

* **PAN** — Select Panorama Edit Mode.

## SEND

* **SEND** — Select Send Edit Mode.
* Press repeatedly to cycle through Send 1–8.
* **SHIFT + SEND** — Move backwards through the sends.
* **SEND + Track SELECT 1–8** — Select the corresponding send directly.

## DEVICE

* **DEVICE** — Select Device Edit Mode.
* **DEVICE again** — Select Project/Track Parameter Mode.
* **OPTION + DEVICE** — Pin the cursor device.

## EQ

* **EQ** — Select Equalizer Edit Mode.

## INSTRUMENT

* **INSTRUMENT** — Select Instrument Device Edit Mode.

---

# 7. Automation

## READ / OFF

* **READ/OFF** — Disable Arranger automation recording.
* **OPTION + READ/OFF** — Reset automation overrides.

## WRITE

* **WRITE** — Enable Arranger automation recording in Write mode.

## TRIM

* **TRIM** — Select Trim automation behaviour.
* Bitwig does not provide a Trim mode, so DrivenByMoss enables Read mode instead.

## TOUCH

* **TOUCH** — Enable Arranger automation recording in Touch mode.

## LATCH

* **LATCH** — Enable Arranger automation recording in Latch mode.

---

# 8. Utility Controls

## Note Editor

* **MIDI TRACKS / Note Editor** — Toggle the Note Editor pane.

## Automation Editor

* **INPUTS / Automation Editor** — Toggle the Automation Editor pane.

## Device Window

* **AUDIO TRACKS / Toggle Device** — Toggle a plug-in window.
* **SHIFT + Toggle Device** — Toggle between layouts.
* **OPTION + Toggle Device** — Toggle the selected device's expanded state.

## Mixer

* **AUDIO INSTRUMENT / Mixer** — Toggle the Mixer pane.

---

# 9. Browser Shortcuts

## BROWSER

* **BROWSER / USER** — Start the Browser for browsing presets.
* **SHIFT + BROWSER** — Start the Browser to insert a new device before the current device.
* **OPTION + BROWSER** — Start the Browser to insert a new device after the current device.

Further Browser Mode controls are listed under Browser Mode below.

---

# 10. Metronome

* **CLICK / Metronome** — Toggle the metronome.
* **SHIFT + Metronome** — Toggle metronome ticks.
* **SHIFT + Master Fader** — Change metronome volume.

---

# 11. Global Solo, Mute and Overdub Operations

## SOLO

* **SOLO** — Deactivate all solos.
* **SHIFT + SOLO** — Deactivate all mutes.

## OVR / REPLACE

* **OVR** — Toggle Arranger overdub.
* **SHIFT + OVR** — Toggle Launcher overdub.

---

# 12. Project and Marker Operations

## SAVE

* **SAVE** — Save the current project.

## MARKER

* **MARKER** — Activate Marker Mode.
* **SHIFT + MARKER** — Toggle display of markers in the Arranger.
* **OPTION + MARKER** — Insert a marker at the current play position.

## DROP

* **DROP** — Duplicate the selected track.

---

# 13. Fader Controls

## LOCK

* **LOCK** — Lock the faders.
* This control is noted by the source as not being present on the standard MCU.

## FLIP

* **FLIP** — Toggle the **Use faders like knobs** option.
* **SHIFT + FLIP** — Toggle between Instrument/Audio/Hybrid tracks and Effect tracks.

## CANCEL

* While browsing: cancel the Browser operation.
* Otherwise: behave like the computer keyboard's Escape key.

## ENTER

* While browsing: confirm the Browser operation.
* Otherwise: behave like the computer keyboard's Enter key.

---

# 14. Common Edit-Mode Functions

These functions apply across the edit modes.

## Record Arm

* **ARM 1–8** — Arm the corresponding track for recording.
* **SHIFT + ARM** — Toggle record-arm state for all tracks in the active Bitwig bank page.

## Mute

* **MUTE 1–8** — Mute/unmute the corresponding track or layer.
* **OPTION + MUTE** — Deactivate all mutes.
* **SHIFT + MUTE** — Toggle monitor.

## Solo

* **SOLO 1–8** — Solo/unsolo the corresponding track or layer.
* **OPTION + SOLO** — Deactivate all solos.
* **SHIFT + SOLO** — Toggle auto-monitor.

## Track SELECT buttons

* **SELECT 1–8** — Select the corresponding track.
* With hierarchical track navigation:

  * Press SELECT again on the selected group/folder to enter it.
  * Long-press a SELECT button to leave the group/folder.
* With flat track navigation:

  * Selecting an already selected group track toggles its expanded state.
* Press SELECT again on a selected track containing an instrument with layers or drum pads to enter Layers Mode.
* **SHIFT + SELECT** — Multi-select tracks where supported by the DAW.
* **OPTION + SELECT** — Stop the playing clip on that track.
* **CONTROL + SELECT** — Open or close the group folder when the track is a group.
* **ALT + SELECT** — Set the length of a new clip.
* **SEND + SELECT 1–8** — Select Send 1–8.

## Track faders

* **Faders 1–8** — Change the volume of the eight selected/banked tracks.
* Touching a fader can automatically select its track.

## Master fader

* **Master Fader** — Change master volume.
* Touching it selects the master track and enters Master Edit Mode.

## V-Pot / knob press

Normally:

* **Press knob** — Reset the current parameter to its default value.

With modifiers:

* **SHIFT + knob press** — Set parameter to its centre value.
* **CONTROL + knob press** — Set parameter to minimum.
* **ALT + knob press** — Set parameter to maximum.
* **OPTION + knob press** — When controlling a send level, toggle that send on/off.

---

# 15. Track Banking and Movement

## BANK

Outside Device Mode:

* **BANK LEFT** — Move track-bank focus by eight tracks in one direction.
* **BANK RIGHT** — Move track-bank focus by eight tracks in the other direction.
* **OPTION + BANK LEFT/RIGHT** — Move the selected device left/right.

Device Mode changes the BANK behaviour; see Device Edit Mode.

## CHANNEL

Outside Device Mode:

* **CHANNEL LEFT** — Move track-bank focus by one track.
* **CHANNEL RIGHT** — Move track-bank focus by one track.
* **OPTION + CHANNEL LEFT/RIGHT** — Move the selected track left/right.

Device Mode changes the CHANNEL behaviour; see Device Edit Mode.

---

# 16. Track Edit Mode (`tr`)

Enter by:

* Pressing **TRACK**, or
* Pressing **PAN twice**.

The eight knobs control parameters of the selected track:

* Volume
* Panorama
* Crossfader
* Send 1
* Send 2
* Send 3
* Send 4
* Send 5

Hold **SHIFT** for fine adjustment.

A DrivenByMoss preference can hide the Crossfader parameter and provide six sends instead.

---

# 17. Volume Edit Mode (`Vl`)

Enter by pressing **TRACK twice**.

* Knobs 1–8 — Change the volume of the corresponding channel.
* Hold **SHIFT** for fine adjustment.

---

# 18. Panorama Edit Mode (`Pn`)

Enter by pressing **PAN**.

* Knobs 1–8 — Change panorama for the corresponding channel.
* Hold **SHIFT** for fine adjustment.

---

# 19. Send Edit Modes (`S1`–`S8`)

Enter by pressing **SEND**.

* Repeated presses select Send 1 through Send 8.
* **SEND + Track SELECT 1–8** directly selects the corresponding send.
* Knobs 1–8 change the selected send level for the corresponding channels.
* Hold **SHIFT** for fine adjustment.

---

# 20. Layer / Drum Pad Edit Modes

For tracks containing instruments with layers or drum pads:

* Select the track.
* Press its SELECT button again to enter Layers/Drum Pad Mode.
* Mode buttons select the different layer modes.
* Layers and drum pads can be edited for:

  * Volume
  * Panorama
  * Sends
  * Mute
  * Solo
* Long-press any SELECT button to leave Layers Mode.

---

# 21. Master Edit Mode (`Nt`)

Enter by touching the Master Fader.

* **Knob 1** — Change master volume.

  * Press to reset.
* **Knob 2** — Change master panorama.

  * Press to reset.
* **Knobs 3–5** — Press to toggle the audio engine on/off for the project.
* **Knob 7** — Press to switch to the previous project.
* **Knob 8** — Press to switch to the next project.

---

# 22. Device Edit Mode (`dC`)

* **Device Knobs 1–8** — Change the currently selected eight device parameters.
* **BANK LEFT** — Select previous device.
* **BANK RIGHT** — Select next device.
* **CHANNEL LEFT** — Select previous parameter page.
* **CHANNEL RIGHT** — Select next parameter page.

## Direct device selection

* Hold **CONTROL** to display the devices on the selected track.
* Press the corresponding knob to select a device for editing.

## Direct parameter-page selection

* Hold **OPTION** to display the parameter pages of the selected device.
* Press the corresponding knob to select a parameter page.

---

# 23. Equalizer Edit Mode (`E9`)

* Operates similarly to Device Edit Mode, but targets the track's equalizer device.
* For Bitwig, the documented equalizer is **EQ+**.
* If EQ Mode is activated on a track without an equalizer, an equalizer device is automatically added.

---

# 24. Project / Track Parameter Edit Mode (`PP` / `tP`)

* **Device Knobs 1–8** — Change the currently selected eight project/track parameters.

---

# 25. Browser Mode (`Br`)

Enter with **BROWSER / USER**.

## Navigation

* Track Control knobs — Navigate Browser columns.
* Press a knob — Enter a filter or results list.
* Press again — Confirm.
* Jog Wheel — Scroll results.

## Confirm / Cancel

* **BROWSER** or **ENTER** — Confirm a patch/device selection and close the Browser.
* **CANCEL** or **SHIFT + BROWSER** — Discard the selection.

## Arrow controls

* **UP** — Previous Browser tab, where available.
* **DOWN** — Next Browser tab, where available.
* **LEFT** — Switch to inserting a device before the selected device.
* **RIGHT** — Switch to inserting a device after the selected device.
* **ZOOM** — Switch to replacing the selected device.

---

# 26. Marker Mode (`Mr`)

Enter by pressing **MARKER**.

If the controller has no Marker button, the command can be assigned to a function button.

* Press a knob corresponding to a marker — Start playback from that marker position.

Related Marker commands outside Marker Mode:

* **SHIFT + MARKER** — Toggle marker display in the Arranger.
* **OPTION + MARKER** — Insert a marker at the current play position.
* **OPTION + REWIND** — Jump to the closest previous marker.
* **OPTION + FORWARD** — Jump to the closest following marker.

---

# 27. Footswitches

## Footswitch 1

* MCU USER A.
* Function can be assigned in DrivenByMoss settings.

## Footswitch 2

* MCU USER B.
* Function can be assigned in DrivenByMoss settings.

---

# 28. DrivenByMoss Hardware Preferences

## Profile

* Hardware profiles configure appropriate settings for supported controllers, including the X-Touch.

## Displays

Configurable options include:

* Main display.
* Seven-character display mode.
* Second display.
* Segment display.
* Assignment display.
* Display track names in the first display.
* X-Touch display colours.

## Faders

Configurable options include:

* Controller has motor faders.
* Controller has only one fader.
* Use faders like editing knobs.

## VU meters

Options include:

* Enable VU meters.
* Select the appropriate VU implementation.
* Always send VU-meter updates.

## Vertical Zoom

* Optionally use UP/DOWN in Zoom Mode to select parameter modes.

---

# 29. Extender Setup

Controllers can be configured as:

* **Main**
* **Extender**
* **MCU Extender**

Main controllers provide the master fader and additional commands such as transport controls.

Multiple Main devices are supported.

Changing extender settings requires restarting the extension.

---

# 30. Segment Display Preferences

* Choose between displaying **time** or **beats/measures** for the play position.
* Choose whether the final three digits display **tempo** or **ticks**.

---

# 31. Track Preferences

## Include FX and Master tracks

* Optionally include FX and Master tracks in the track bank.

## Pin FX tracks

* FX tracks can be pinned to the right-most controller.
* The instrument/audio track-bank page size is reduced accordingly.

## Track navigation

Two approaches are available:

### Flat

* All tracks are shown.
* Selecting an already selected group track toggles its expanded state.

### Hierarchical

* Groups/folders are presented hierarchically.
* Press SELECT again to enter a group/folder.
* Long-press SELECT to leave it.

---

# 32. Assignable Buttons

Configurable controls include:

* Footswitch 1
* Footswitch 2
* F1–F5

The assigned operation can be selected in DrivenByMoss settings.

## Clip Based Looper

When assigned:

* Uses the currently selected MIDI clip slot.
* Creates a clip if the slot is empty.
* Uses the configured New Clip Length.
* Starts playback.
* Holding the footswitch enables overdub.
* Releasing the footswitch disables overdub.

## Action

* An arbitrary available action can be selected for execution.

---

# 33. Transport Preferences

## Behaviour on Stop

* Configure the action performed when playback is stopped using STOP.

## Behaviour on Pause

* Configure the action performed when playback is stopped using PLAY.

## Flip Arranger and Clip Record / Automation

* Swaps the normal and SHIFT-modified Record/Automation behaviours.
* Intended particularly for users who work primarily in the Clip Launcher rather than the Arranger.

---

# 34. Play and Sequence Preferences

## Quantize Amount

* Sets the amount of quantisation used when Quantize is executed.
* 100% aligns notes fully to the grid.

---

# 35. Workflow Preferences

## Exclude deactivated items

* Hide deactivated items such as tracks from the controller's banks.
* This simplifies the displayed banks but prevents activation of those items from the controller.

## Startup Mode

* Select the edit mode activated when the extension starts.

## New Clip Length

* Configure the length of clips created by the New function.

## Zoom

* Configure arrow keys for Arranger zooming.

## Select Channel on Fader Touch

* Select the channel associated with a touched fader.

## Activate Volume Mode on Fader Touch

* Temporarily activate Volume Mode while a fader is being touched.

## Knob Sensitivity Default

* Negative values slow knob changes.
* Positive values speed them up.

## Knob Sensitivity Slow

* Adjust sensitivity when using the slower/fine knob behaviour.

## Encoder Knob Slow Down

* Increase the value when the main encoder changes values too quickly.

---

# 36. Browser Preferences

* Individual Browser filter columns can be hidden.
* This can simplify Browser navigation by exposing only relevant filter columns.

---

# Audit Status

This inventory intentionally contains **no Project XTC coverage judgements yet**.

The next audit stage should classify every relevant item as:

* **✓ Covered adequately**
* **△ Covered but needs expansion**
* **✗ Missing**
* **N/A Not applicable to the X-Touch / scope of Project XTC**

Where a feature is missing or incomplete, the audit should also identify:

* the most appropriate existing chapter, or
* whether the material warrants a new chapter or section.

---

# Source

DrivenByMoss Documentation — Mackie MCU:

`Mackie/Mackie-MCU.md`

The source documentation explicitly lists the **Behringer X-Touch / X-Touch Extender** among the devices used to test the Mackie MCU implementation.
