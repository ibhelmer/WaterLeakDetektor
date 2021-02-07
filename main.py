#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Author: Ib Helmer Nielsen
Version: 0.5.1
Email: ihn@ucn.dk
Status: Prove of concept
License: MPL 2.0
Description: Test of simple algorithms for detecting water leak by measuring the difference
             between the water pipe temperature and the surrounding air temperature. The sensors
             are two DS1820 attached to the one-wire bus.
"""
import time
from w1thermsensor import W1ThermSensor

start = time.time()                                         # For debug purpose
utlim = 8.0                                                 # Upper temperature limit
ltlim = 5.0                                                 # Lower temperature limit
tcount = 0                                                  # Hold minutes since last lower limit reached
ttcl =  600                                                 # Time to check for leak 10 hours after last use (600 minutes)
ltl  = 2.0                                                  # Leak temperature limit
while True:
    mess = []
    for sensor in W1ThermSensor.get_available_sensors():
        mess.append(sensor.get_temperature())                # Two measurement approx. 1.5 Sec

    diff = mess[0]-mess[1]                                   # Temp diff

    if diff < ltlim :                                        # Increment time since last use
        tcount += 1
        if tcount >= 600:                                    # Measure static diff
            if dif > ltl:                                    # There is a leak !!!!
                print("There is detected a leak ")           # Turn on led, sound or send push message
    if diff > utlim :                                        # Reset timer
        tcount = 0

    time.sleep(59)		                                    # Wait approx. 1 minutes