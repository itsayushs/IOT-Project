#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 11:29:09 2018
Vault Gate Lock_Unlock
@author: stark
use during ssh python -c 'import [filename]; filname.funcname()'
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
r=16
g=26
GPIO.setwarnings(False)
GPIO.setup(r,GPIO.OUT) #green
GPIO.setup(g,GPIO.OUT) #red
GPIO.output(r,GPIO.HIGH)
def entry():
#    green on | red off 
    GPIO.output(g,GPIO.HIGH)
    GPIO.output(r,GPIO.LOW)
def noentry():
#    green off | red on 
    GPIO.output(r,GPIO.HIGH)
    GPIO.output(g,GPIO.LOW)
def alloff():
    GPIO.output(r,GPIO.LOW)
    GPIO.output(6,GPIO.LOW)

pin=6969
cnt=0
while cnt!=3:
    k=input("Input Your Vault PIN")
    if k==pin:
        print("Unlocked")
        cnt=3
        entry()
    else:
        cnt=cnt+1
        print("wrong password")
        noentry()
        
        