'''
Store any views/url endpoints for the functioning front end of the website that pertain to authorization (login, signup, etc.)
'''

from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)
#use blueprint decorators for our auth pages, define routes here.
@auth.route('/logout')
def logout():
    return "<p>Logout</p>"

#Define the methods that we are willing to accept from this route (GET, POST are allowed).
@auth.route('/login', methods=['GET','POST'])
def login():
    return render_template("login.html", text="Testing")

@auth.route('/sign-up', methods=['GET','POST'])
def sign_up():
    if request.method == "POST":
        email = request.form.get('email')
        username = request.form.get('username')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            #flash is a flask function, allows us to flash a set message. Define a category name and reference it in base.html for formatting
            flash('Email must be greater than 3 characters.', category='error') 
        elif len(username) <2:
            flash('name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            flash('Account Successfully Created.', category='success')


    
    return render_template("sign_up.html")


