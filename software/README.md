# Software

## Current controller

[`eye_assistant.py`](eye_assistant.py) is the latest integrated Raspberry Pi controller. It combines:

- PCA9685 servo control
- cosine-eased eye motion
- randomized idle movement and blinking
- wake-word and conversation handling
- Google speech recognition and text-to-speech
- OpenAI chat responses
- interruption detection while audio is playing

The script initializes the PCA9685 and searches for a microphone at startup, so it is intended to run on the completed Raspberry Pi hardware rather than a development laptop.

## Calibration

[`calibration/servo_range_test.py`](calibration/servo_range_test.py) exercises the configured eye ranges. Read the repository's [calibration notes](../docs/build-notes.md#servo-calibration) before running it.

## Prototypes

The `prototypes/` directory preserves earlier development stages. They remain useful as a record of how the eye-only and voice-only systems were combined, but they are not the recommended entry points.

