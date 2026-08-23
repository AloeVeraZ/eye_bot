<div align="center">

# Animatronic AI Eye Software

### Python controller, servo kinematics, conversational AI, and calibration scripts

[![Language](https://img.shields.io/badge/Language-Python_3-3776ab?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![Hardware](https://img.shields.io/badge/Hardware-Raspberry_Pi-c51a4a?style=flat-square&logo=raspberrypi&logoColor=white)](https://www.raspberrypi.com/)
[![PWM Driver](https://img.shields.io/badge/Driver-PCA9685-7c3aed?style=flat-square)](#current-controller)
[![Parent](https://img.shields.io/badge/Project-Animatronic_AI_Eye-0078d4?style=flat-square)](../)

This folder has the main Raspberry Pi controller, servo calibration tools, and the older prototypes that led to the current assistant.

<strong>Quick navigation:</strong><br>
[Current Controller](#current-controller) | [Package Layout](#package-layout) | [Calibration](#calibration) | [Back to AI Eye](../)

</div>

---

## Current Controller

[`eye_assistant.py`](eye_assistant.py) is the primary integrated Raspberry Pi controller. It coordinates mechanical actuation and multimodal voice interactions:

- **PCA9685 PWM Control:** Direct 16-channel I²C communication for 4 servos.
- **Organic Motion:** Cosine-eased trajectory generation for lifelike eye and eyelid movement.
- **Autonomous States:** Randomized idle movement, natural double blinks, and listening poses.
- **Voice Pipeline:** Hotword detection, speech-to-text, OpenAI conversation, and text-to-speech.
- **Barge-in / Interruption:** Detects user speech to interrupt spoken output in real time.

| Module / Script | Function | Target Environment |
| --- | --- | --- |
| [`eye_assistant.py`](eye_assistant.py) | Full integrated voice and motion assistant | Raspberry Pi with PCA9685 & USB Mic |
| [`calibration/servo_range_test.py`](calibration/servo_range_test.py) | Mechanical limit and angle verification | Hardware testbench |
| `prototypes/` | Preserved early voice & motion experiments | Development reference |

## Package Layout

```text
software/
├── eye_assistant.py             # Primary integrated assistant
├── calibration/
│   └── servo_range_test.py      # Individual servo angle tester
└── prototypes/                  # Preserved development iterations
```

## Calibration

> [!CAUTION]
> Disconnect the eyelid linkages before running calibration scripts for the first time. Always verify PWM pulse limits to avoid stalling or damaging micro-servos against mechanical stops.

Read the complete [calibration notes](../docs/build-notes.md#servo-calibration) before adjusting pulse ranges.

---

<div align="center">

Designed and documented for **[Animatronic AI Eye](../)**.

</div>

