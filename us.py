#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:39:20 2018

@author: stark
"""

import RPi.GPIO as GPIO
import time
import cap
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 #set GPIO Pins
GPIO_TRIGGER = 18
GPIO_ECHO = 24
 
#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
 
def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
 
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
  
    return distance

def ledfunc(s):
    GPIO.setup(17,GPIO.OUT)
#    GPIO.setup(6,GPIO.OUT)
    if s==True:
        GPIO.output(17,GPIO.HIGH)
        time.sleep(0.25) 
        GPIO.output(17,GPIO.LOW)
    else:
        GPIO.output(17,GPIO.HIGH)
#def redoff():    
#    GPIO.setup(12,GPIO.OUT)
#    GPIO.setup(6,GPIO.OUT)
#    GPIO.output(6,GPIO.HIGH)
#    GPIO.output(12,GPIO.LOW)
if __name__ == '__main__':
    try:
#       temp var to capture only 1 image when the object is removed
        tcap=True
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            if int(dist) > 25:
                print "Obj Removed"
                if tcap==True:
                    cap.clkpic()
                    tcap=False
                ledfunc(True)
            else:
                ledfunc(False)
                print "Object Present"
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
