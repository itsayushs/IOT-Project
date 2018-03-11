#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 00:09:30 2018

@author: Ayush Sharma
"""

import sqlite3 as sql

def insertUser(username,password,email):
    con = sql.connect("database.db")
    cur = con.cursor()
    cur.execute("INSERT INTO users (username,password,email) VALUES (?,?,?)", (username,password,email))
    con.commit()
    con.close()

def retrieveUsers(username):
	con = sql.connect("database.db")
	cur = con.cursor()
	cur.execute("SELECT password,email FROM users where username='{}'".format(username))
	users = cur.fetchall()
	con.close()
	return users

#a=retrieveUsers("ayush")
#print a[0][1] email
#print a[0][0] passw