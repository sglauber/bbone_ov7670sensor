# Digital reads
# Reading 0 or 1 (low or high), (true or false), (on or off)
# Doing digital reads from the pins that we setup as inputs
# Using push buttons
# Blue pins on the pin diagrams
# Reads a percentage from the potentionmeter from 0V to 1.8V
# If we want to change to the voltage we just multiply the value * 1.8V
# THE MAX VALUE MUST BE 1.8V OR U CAN MESS UP THE BEAGLE BONE.

# Analag to Digital Converter Library
import Adafruit_BBIO.ADC as ADC
ADC.setup()
while true:
    reading = ADC.read("P9_33") * 1.8
    print("Value is: ", reading)
