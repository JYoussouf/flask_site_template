'''
Store main views/url endpoints for the functioning front end of the website - Store where most pages go.
'''

from flask import Blueprint, render_template

views = Blueprint('views', __name__)
#use blueprint decorators for our views pages, define routes here.
@views.route('/') 
def home():
    return render_template("home.html")