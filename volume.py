#!/usr/bin/python

# Modified from: https://github.com/gigafide/raspberrypi_spotify_radio/blob/master/volume.py

from RPi import GPIO
from time import sleep
import os

clk = 17
dt = 27

GPIO.setmode(GPIO.BCM)
GPIO.setup(clk, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(dt, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

counter = 0
clkLastState = GPIO.input(clk)
currVolume = 50

try:
    while True:
        clkState = GPIO.input(clk)
        dtState = GPIO.input(dt)
        if clkState != clkLastState:
            if dtState != clkState:
                currVolume += 5
            else:
                currVolume -= 5
            print currVolume
            os.system("mpc volume " + str(currVolume))
            clkLastState = clkState
            sleep(0.01)
finally:
    GPIO.cleanup
