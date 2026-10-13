![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Autodesk Maya](https://img.shields.io/badge/Autodesk-Maya-0696D7?style=for-the-badge)

# Channel Control Editor for Autodesk Maya

---

## Overview

**Channel Control Editor** is a lightweight rigging utility designed to help riggers quickly **show or hide standard transform attributes in Maya's Channel Box** across multiple selected controllers.

Preparing a rig often involves repeating the same Channel Box cleanup steps on dozens of controllers. Instead of editing each controller's channel settings individually, this tool provides a simple checkbox interface for applying consistent channel settings to the entire selection in one operation.

The tool can be installed by dragging its Python installer directly into the Maya viewport. It creates a shelf button for quick access.

> **Note:** This tool changes attribute locking and keyability/channel visibility settings. It does **not** delete attributes, hide controllers in the viewport, or reset attribute values.

---

## Features

- **Drag-and-drop installation** directly into the Maya viewport
- **Automatic shelf button creation** on the currently active Maya shelf
- **Batch editing** of multiple selected transform controllers
- **Checkbox-based channel selection** for Translate, Rotate, Scale, and Visibility
- **Show / Hide controls** to quickly change Channel Box availability
- **All checkbox** for selecting or clearing every supported channel group
- **Self-contained shelf command** — no external script path required after installation
- **Readable Python source** — no Base64 or compressed code payload
- **Reinstall support** — updates an existing matching shelf button instead of creating a duplicate on that shelf

---

## Supported Attributes

| Checkbox | Maya Attributes | Description |
|---|---|---|
| **Translate** | `tx`, `ty`, `tz` | Position channels |
| **Rotate** | `rx`, `ry`, `rz` | Rotation channels |
| **Scale** | `sx`, `sy`, `sz` | Scale channels |
| **Visible** | `v` | Object visibility attribute |
| **All** | All channels above | Selects or clears all four groups |

The checkboxes choose **which attributes will be affected**; they do not directly change channel settings until **ShowAttribute** or **HideAttribute** is clicked.

---

## Workflow Concept

### Batch Channel Box Editing

Select one or more controllers, enable the checkboxes for the attribute groups you want to change, then click **ShowAttribute** or **HideAttribute**.

The same operation is applied to every selected transform, making repeated rig setup and Channel Box cleanup much faster.

### Show Attributes

**ShowAttribute** applies the following settings to the checked channels:

- `lock=False` — unlocks the attribute
- `keyable=True` — makes the attribute keyable and visible in the Channel Box

### Hide Attributes

**HideAttribute** applies the following settings to the checked channels:

- `lock=True` — locks the attribute
- `keyable=False` — makes the attribute non-keyable and normally removes it from the Channel Box

> **Important:** Hiding is not merely a cosmetic Channel Box toggle: it also locks the affected attributes. Showing them unlocks them again.

---

## Installation

1. Open **Autodesk Maya**.
2. Choose the **shelf tab** where you want the tool installed.
3. Drag and drop `ChannelControlEditor_Install_Readable.py` into the **Maya viewport**.
4. A shelf button labelled **Channel** will be created automatically.
5. Click **Channel** to open the Channel Control Editor window.

The installer embeds the editor code in the shelf button, so you do not need to maintain a separate script file path after installation.

If a shelf button with the same tool annotation already exists on the current shelf, running the installer again updates that button's command.

---

## Usage

### Example 1 — Hide Scale Channels on Multiple Controllers

1. Select several rig controllers in Maya.
2. Click the **Channel** shelf button.
3. Clear **All**, then check **Scale** only.
4. Click **HideAttribute**.
5. `sx`, `sy`, and `sz` will be locked and set to non-keyable on all selected transforms.

### Example 2 — Show Translation and Rotation Channels

1. Select one or more controllers.
2. Check **Translate** and **Rotate**; uncheck **Scale** and **Visible**.
3. Click **ShowAttribute**.
4. Translation and rotation channels will be unlocked and made keyable for the selected controllers.

### Example 3 — Apply All Supported Channels

1. Select the intended controllers.
2. Enable **All**.
3. Click **ShowAttribute** or **HideAttribute** to apply the chosen setting to every supported channel group.

---

## Production Use Cases

- Preparing animator-friendly controller Channel Boxes
- Locking unnecessary scale channels across an entire controller selection
- Restoring hidden standard transform channels during rigging revisions
- Applying consistent attribute settings to multiple controls without repetitive manual clicks
- Speeding up controller cleanup before animation handoff

---

## Notes & Limitations

- The tool targets selected **transform nodes** and their standard Translate, Rotate, Scale, and Visibility attributes.
- It does **not** read individual attribute highlights in Maya's Channel Box. Use the tool's checkboxes to choose the attributes to edit.
- Custom attributes are **not** included in the current checkbox options.
- It does not change current attribute values or animation keys.
- Changing lock/keyable settings may affect an existing rig workflow; use carefully on referenced rigs or connected attributes.
- The source uses standard `maya.cmds` and `maya.mel` APIs, but compatibility should be tested in the Maya versions used by your team.

---

## Feedback & Contributions

This is an evolving personal rigging workflow tool.

Feedback, production suggestions, and improvement ideas are welcome. If you encounter issues or would like to suggest enhancements, feel free to open an issue or reach out.

---

## License

Provided **as-is** for personal and educational use.
