"""Early fixed-position motion sequence preserved from project development."""

import math
import time

import smbus


class PCA9685:
    __MODE1 = 0x00
    __PRESCALE = 0xFE
    __LED0_ON_L = 0x06
    __LED0_ON_H = 0x07
    __LED0_OFF_L = 0x08
    __LED0_OFF_H = 0x09

    def __init__(self, address=0x40):
        self.bus = smbus.SMBus(1)
        self.address = address
        self.write(self.__MODE1, 0x00)

    def write(self, reg, value):
        self.bus.write_byte_data(self.address, reg, value)

    def setPWMFreq(self, freq):
        prescaleval = 25000000.0 / 4096.0 / float(freq) - 1
        prescale = math.floor(prescaleval + 0.5)
        oldmode = self.bus.read_byte_data(self.address, self.__MODE1)
        self.write(self.__MODE1, oldmode & 0x7F | 0x10)
        self.write(self.__PRESCALE, int(prescale))
        self.write(self.__MODE1, oldmode)
        time.sleep(0.005)
        self.write(self.__MODE1, oldmode | 0x80)

    def setServoAngle(self, channel, angle):
        angle = max(0, min(180, angle))
        pulse = 500 + (angle / 180.0) * 2000
        pulse_length = int(pulse * 4096 / 20000)
        self.setPWM(channel, 0, pulse_length)

    def setPWM(self, channel, on, off):
        self.write(self.__LED0_ON_L + 4 * channel, on & 0xFF)
        self.write(self.__LED0_ON_H + 4 * channel, on >> 8)
        self.write(self.__LED0_OFF_L + 4 * channel, off & 0xFF)
        self.write(self.__LED0_OFF_H + 4 * channel, off >> 8)


pwm = PCA9685()
pwm.setPWMFreq(50)

while True:
    # Close the lids and center the eye.
    pwm.setServoAngle(2, 100)
    pwm.setServoAngle(15, 80)
    pwm.setServoAngle(0, 90)
    pwm.setServoAngle(1, 90)
    time.sleep(1)

    # Open the lids and visit the four corners of the tested range.
    pwm.setServoAngle(2, 170)
    pwm.setServoAngle(15, 0)
    for horizontal, vertical in ((30, 90), (140, 90), (120, 80), (60, 80)):
        pwm.setServoAngle(0, horizontal)
        pwm.setServoAngle(1, vertical)
        time.sleep(1)
