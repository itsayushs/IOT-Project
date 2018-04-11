#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 00:50:32 2018

@author: stark
"""

import RPi.GPIO as GPIO
import time
import cap
import mailme
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO_TRIGGER = 23
GPIO_ECHO = 24
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
def distance():
    GPIO.output(GPIO_TRIGGER, True)
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    TimeElapsed = StopTime - StartTime
    distance = (TimeElapsed * 34300) / 2 
    return distance

        
def start_us():
    tcap=True
    while tcap==True:
        dist = distance()
        if int(dist) > 25:
            if tcap==True:
                cap.clkpic()
                mailme.mail()
                tcap=False
                GPIO.cleanup()
            time.sleep(1)
start_us()            
GPIO.cleanup()