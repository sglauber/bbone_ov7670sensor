# Using GPIO outputs to blink LEDS with python on our beagle bone
# We're going to use PIN_11 and PIN_12
# And two 330Ohms resistors
# GND

import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("PIN_11",OUT)
GPIO.setup("PIN_12",OUT)

from time import sleep

for i in range(0,5):
    GPIO.output("PIN_11",HIGH)
    sleep(1)
    GPIO.output("PIN_12",HIGH)
    sleep(1)
    GPIO.output("PIN_11",LOW)
    GPIO.output("PIN_12",LOW)
    sleep(1)
    GPIO.output("PIN_11",HIGH)
    GPIO.output("PIN_12",HIGH)
GPIO.cleanup()
