#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 13:21:02 2018
Flask init [App]
@author: Ayush Sharma
"""
from flask import Flask, render_template, flash, request, url_for, redirect, session
from forms import UserRegistrationForm,UserLoginForm
from passlib.hash import sha256_crypt
from functools import wraps
import models as dbHandler
import connect

app=Flask(__name__)
app.secret_key = '66049c07d9e8546699fe0872fd32d8f6'


@app.route('/',methods=['GET','POST'])
def intro():
    connect.redon()
#    connect.uson()
    if request.method == "POST":		
            ip = request.form['ip']
            session['ip'] = ip
            return redirect(url_for('login'))
#    elif session['logged_in'] == True:
#            return redirect(url_for('home'))
#    else:    
    return render_template('index.html')

@app.route('/act',methods=['GET','POST'])
def active():
    connect.uson()
    flash("Sensor activeated")
    return redirect(url_for('intro'))

@app.route('/register/', methods=["GET","POST"])
def register_page():
        form = UserRegistrationForm(request.form)
        if request.method == "POST" and form.validate():
            username  = form.username.data
            email = form.email.data
            password = sha256_crypt.encrypt((str(form.password.data)))
            dbHandler.insertUser(username, password,email)            
#            session['logged_in'] = True
#            session['username'] = username
            return redirect(url_for('login'))
        return render_template("register.html", form=form)

@app.route('/login/', methods=["GET","POST"])
def login():
    form = UserLoginForm(request.form)
    if request.method == "POST" and form.validate():
        username  = form.username.data
        dets=dbHandler.retrieveUsers(username)
        hashed=dets[0][0]
        email=dets[0][1]
        if sha256_crypt.verify(request.form['password'],hashed):
            session['logged_in'] = True
            session['username'] = request.form['username']
            session['email'] = email
            connect.greenon()
#            connect.usoff()
            flash("You are now logged in")
            return redirect(url_for('home'))
        else:
            flash("incorrect password!")
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)
@app.route('/about/')
def about():
    return render_template("about.html")

def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("You need to login first")
            return redirect(url_for('login'))
    return wrap


@app.route('/home')
@login_required
def home():
    user=session['username']
    email=session['email']
    ip_pi=connect.ip
    ip_pi_l="{}:8081".format(ip_pi)
    return render_template("home.html",uname=user,email=email,link=ip_pi_l)

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    return redirect(url_for('intro'))

if __name__ == "__main__":
    app.run(debug=True)