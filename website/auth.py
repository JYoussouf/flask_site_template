'''
Store any views/url endpoints for the functioning front end of the website that pertain to authorization (login, signup, etc.)
'''
from . import db #this takes "db" from __init__.py
from .models import User
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user #security features of flask_login
from werkzeug.security import generate_password_hash, check_password_hash #flask login add-on that hashes passwords (don't store passwords as plaintext)

'''
hashing functions = non-inversible function
x -> y
f(x) = x+1
f(y) = y-1  (inversible, no good!)
y -> x 
'''

auth = Blueprint('auth', __name__)
#use blueprint decorators for our auth pages, define routes here.
@auth.route('/logout')
@login_required #this decorator forces the user to be logged in before they can access this function
def logout():
    logout_user() #logs out current user
    return redirect(url_for('auth.login'))

#Define the methods that we are willing to accept from this route (GET, POST are allowed).
@auth.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST': #if login is sent
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                #logs in current user until user clears browser session or logs out or upon server restarts
                login_user(user, remember=True) 
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, please try again', category='error')
        else:
            flash('No user found with this email address.', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            #email has already been used, ensures no duplicate emails.
            flash('Account already exists with this email.', category='error')
        elif len(email) < 4:
            #flash is a flask function, allows us to flash a set message. Define a category name and reference it in base.html for formatting
            flash('Email must be greater than 3 characters.', category='error') 
        elif len(username) <2:
            flash('name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            new_user = User(email=email, username=username, password=generate_password_hash(password1, method='scrypt'))
            db.session.add(new_user) #add new user to the database
            db.session.commit() #commit the new_user to the database
            flash('Account Successfully Created.', category='success')
            return redirect(url_for('auth.login')) #takes us to views.home url. Dynamic way of putting "url_for('/')"
    
    return render_template("sign_up.html", user=current_user)