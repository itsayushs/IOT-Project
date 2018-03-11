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


app=Flask(__name__)
app.secret_key = '66049c07d9e8546699fe0872fd32d8f6'


@app.route('/')
def intro():
    return render_template('index.html')

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
        ip = form.piip.data
        dets=dbHandler.retrieveUsers(username)
        hashed=dets[0][0]
        email=dets[0][1]
        if sha256_crypt.verify(request.form['password'],hashed):
            session['logged_in'] = True
            session['username'] = request.form['username']
            session['email'] = email
            session['ip'] = ip
            flash("You are now logged in")
            return redirect(url_for('home'))
        else:
            flash("incorrect password!")
            return render_template("login.html", form=form)
    return render_template("login.html", form=form)

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
    return render_template("home.html",uname=user,email=email)

@app.route("/logout/")
@login_required
def logout():
    session.clear()
    flash("You have been logged out!")
    return redirect(url_for('intro'))

if __name__ == "__main__":
    app.run(debug=True)