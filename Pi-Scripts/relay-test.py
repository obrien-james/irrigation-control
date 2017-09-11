#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

#Set up GPIO mode to board numbering
GPIO.setmode(GPIO.BOARD)

#Set zone variables to pin numbers
Zone1 = 36
Zone2 = 38 
Zone3 = 40
Zone4 = 37

#Set up pins to output mode:
GPIO.setup(Zone1, GPIO.OUT)
GPIO.setup(Zone2, GPIO.OUT)
GPIO.setup(Zone3, GPIO.OUT)
GPIO.setup(Zone4, GPIO.OUT)

#Set all pins to high as relay board active low
GPIO.output(Zone1, GPIO.HIGH)
GPIO.output(Zone2, GPIO.HIGH)
GPIO.output(Zone3, GPIO.HIGH)
GPIO.output(Zone4, GPIO.HIGH)

print "Running test now"
#Turning relays on in sequence:
GPIO.output(Zone1, GPIO.LOW)
time.sleep(5)
GPIO.output(Zone2, GPIO.LOW)
time.sleep(5)
GPIO.output(Zone3, GPIO.LOW)
time.sleep(5)
GPIO.output(Zone4, GPIO.LOW)
time.sleep(5)

#Turn relays off in sequence:
GPIO.output(Zone1, GPIO.HIGH)
time.sleep(5)
GPIO.output(Zone2, GPIO.HIGH)
time.sleep(5)
GPIO.output(Zone3, GPIO.HIGH)
time.sleep(5)
GPIO.output(Zone4, GPIO.HIGH)
time.sleep(5)

#All on
GPIO.output(Zone1, 0)
GPIO.output(Zone2, 0)
GPIO.output(Zone3, 0)
GPIO.output(Zone4, 0)

time.sleep(3)

#All off:
GPIO.output(Zone1, 1)
GPIO.output(Zone2, 1)
GPIO.output(Zone3, 1)
GPIO.output(Zone4, 1)

print "Test end!"
#Reset GPIO pins
GPIO.cleanup()

