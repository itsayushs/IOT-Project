#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 01:52:48 2018
Connecting Pi wih cloud
@author: Ayush Sharma
"""

import commands as cm
import config
ip=config.pi_ip

def redon():
    cmd="sshpass -p a ssh pi@{} \"python -c 'import ve; ve.noentry()'\"".format(ip)
    sts,cmdx=cm.getstatusoutput(cmd)
    return True

def greenon():
    cmd="sshpass -p a ssh pi@{} \"python -c 'import ve; ve.entry()'\"".format(ip)
    sts,cmdx=cm.getstatusoutput(cmd)
    return True

def uson():
    cmd="sshpass -p a ssh pi@{} \"python uss.py &\"".format(ip)
    sts,cmdx=cm.getstatusoutput(cmd)
    return True

def usoff():
    cmd="sshpass -p a ssh pi@{} \"python -c 'import uss; uss.us_off()'\"".format(ip)
    sts,cmdx=cm.getstatusoutput(cmd)
    return True