import Adafruit_BBIO.GPIO as GPIO

# Using GPIO we going to turn our GPIOs PINS ON/OFF using python
# Here we're simulating digital outputs to our beagle bone
# That mean HIGH (1) and LOW (0) binaries values.
# Our voltage on the digital write go from 0V (low/off/0) to 3.3V (high/on/1)

# We can do digital writes using the green GPIO pins (check the pinout diagram)
# We'll be using the header to reference our PINS on this project
# The headers are printed closer to the pins on the beagle bone


# To work on a digital write we going to use pins on the left
# Using the P9 header we going to use the P9_2 as our GND
# And P9_12 as our GPIO pin
# We may also set variable names to our PINS
# As outPin = "P9_12"

# Here we're setting our PIN 12 at header P9 as an output PIN.
GPIO.setup("P9_12",OUT)
# We may turn it on and off Using the output method
# Saying that we going to write to the PIN and set it (on - > HIGH)
GPIO.output("P9_12",HIGH)
# In the same way we can turn it off using output method
GPIO.output("P9_12",LOW)

# Here we clean the settings that we just did to our PINS
GPIO.cleanup()
