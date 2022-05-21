'''
Store main views/url endpoints for the functioning front end of the website - Store where most pages go.
'''

from . import db #this takes "db" from __init__.py
from .models import Note
from unicodedata import category
from flask import Blueprint, flash, render_template, request, jsonify
from flask_login import login_required, current_user #security features of flask_login
import json

views = Blueprint('views', __name__)
#use blueprint decorators for our views pages, define routes here.
@views.route('/', methods=['GET','POST']) 
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
        
    return render_template("home.html", user=current_user) #reference current_user in our templates and check if it's authenticated

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data) #takes data from post request, loads as dict
    noteID = note['noteID'] #load the noteID attribute
    note = Note.query.get(noteID) #look for the actual note that has that ID 
    if note:
        if note.user_id == current_user.id: #if the signed in user owns the note, then delete the note.
            db.session.delete(note)
            db.session.commit()

    return jsonify({}) #return empty response
