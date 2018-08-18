# Analog values are variables
# Digital values are used to represent if something is on or off 1 or 0

# Here we're going to do analog writes or at least simulate analog writes using pulse with modulations
# We can simulate analog outputs turning our voltage on and off really quiclky generating a analog signal.
# Fow PWM we can use the purple PINS on our beagle bone black. (See the diagram).
# Here I'm using PINs P8_13 and GND P8_1

import Adafruit_BBIO.PWM as PWM

# Setting up the PIN to use and its start values
# Setting up the Duty cycle, in percentage as 0%
# Setting up the frequency as 1000Hz or 1Mhz
# Having a duty cycle of 0, it means that its ON for 0% of the time, if we try to read values here it should output 0V
PWM.start("P8_13",0, 1000)

# We can use the method PWM.set_duty_cycle() to re-write our previous value.
# Having a duty cycle of 100%, means that the signal is ON for 100% of the time, and now it must output 3.3V on our reading
PWM.set_duty_cycle("P8_13",100)

# Getting an input from the user is also possible
# vcc = input("What your desired voltage?:")
# duty = V/(3.365*100)
# if (duty > 100):
#   dc = 100
duty = input("Whats the duty cycle that you want?: ")

# And then assigning it to our PWM

PWM.set_duty_cycle("P8_13",duty)

# We can change the frequency using
# Changing the frequency doesn't really affect the PWM since its changing based on the duty cycle
# PWM.set_frequency("P8_13", 100)


# Stopping the settings
PWM.stop("P8_13")
# Cleaning up the settings
PWM.cleanup()



# We can create dimable LEDS applying PWM to a circuit
# Using PINS GND > P9_1 and PWM pins P9_14 and P9_22
# Python code to control the bright of our LEDS.

PWM.start("P8_14",0, 1000)
PWM.start("P8_22",0, 1000)
