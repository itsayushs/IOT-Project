#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:24:12 2018
All the WTForms classes
@author: Ayush Sharma
"""
from wtforms import StringField, PasswordField, BooleanField  
from wtforms.validators import InputRequired, Email, Length, EqualTo
#from flask_wtf import FlaskForm
from wtforms import Form, TextField, PasswordField, validators


class UserLoginForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20),validators.InputRequired()])
    password = PasswordField('Password', [validators.Length(min=6, max=20),validators.InputRequired()])
    piip = TextField('Your RaspberryPi IP Address', [validators.InputRequired()])
    
class UserRegistrationForm(Form):
    username = TextField('Username', [validators.Length(min=4, max=20)])
    email = TextField('Email Address', [validators.Length(min=6, max=50)])
    password = PasswordField('New Password', [
        validators.Required(),
        validators.EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Repeat Password')

