# -*- coding: utf-8 -*-
"""
Spyder Editor
Click Pic!
This is a temporary script file.
"""
import commands as cm 
def clkpic():
    cmd="fswebcam img.jpg"
    sts,cmdx=cm.getstatusoutput(cmd)
    if sts==0:
        print "Captured"
    else:
        print "Error"
        