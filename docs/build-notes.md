# Build and calibration notes

## Mechanical progression

### Eye movement

The two movement servos are hidden inside the eye. One servo directly tilts the eye up and down; the other rotates that servo's mount to pan the entire assembly left and right. A central bolt connects the mechanism to a spare monitor arm.

### Upper eyelid

The upper-lid servo mount uses four available holes in the monitor arm. A short linkage connects the servo horn to the top of the lid. The projecting features on the arm mount were thickened after early iterations proved too fragile.

### Lower eyelid

The lower lid follows the same general linkage layout. Its pivot was made approximately 5 mm thicker after the upper pivot broke during testing. A relief slot lets the upper lid nest into the lower-lid area because both rotate around the same region. The more distant lower servo uses a longer linkage.

## Servo calibration

1. Remove the eyelid linkages or disconnect servo power.
2. Confirm the PCA9685 address is `0x40` and I²C bus `1` is available.
3. Place every servo near its mechanical midpoint before attaching horns.
4. Run [`software/calibration/servo_range_test.py`](../software/calibration/servo_range_test.py) with conservative limits.
5. Move one channel at a time and record the first angle before a hard stop.
6. Back each limit away from the collision point before reconnecting the mechanism.
7. Update the channel limits and open/closed positions in [`software/eye_assistant.py`](../software/eye_assistant.py).

The current build uses 50 Hz PWM and maps `0°–180°` to approximately `500–2500 µs`. Not every hobby servo supports that entire pulse range, so treat the checked-in values as build-specific rather than universal defaults.

## Wiring checklist

- Raspberry Pi SDA and SCL connected to the PCA9685 I²C pins
- Raspberry Pi ground connected to PCA9685 logic ground
- Servo supply connected to the PCA9685 servo power rail
- Servo supply ground tied to the Raspberry Pi/PCA9685 ground
- Servo signal leads connected to channels `0`, `1`, `2`, and `15`
- Servo voltage and supply current matched to the selected servos

## Noise and microphone placement

Servo movement can interfere with speech input mechanically and electrically. Keep the microphone away from linkages, use a dedicated servo supply, route audio wiring separately from servo power, and retain the eased motion profile to reduce abrupt mechanical noise.

