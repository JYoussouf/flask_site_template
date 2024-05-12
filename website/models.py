'''
Store our database models here, define schema. A db model is a layout/blueprint for an object that's going to be stored in your database.
All objects need to conform to these classes so that info is consistent.
'''

from . import db #this takes "db" from __init__.py
from flask_login import UserMixin #this is a custom class our User object inherits from.
from sqlalchemy.sql import func

class Note(db.Model):
    '''
    Define the columns we want to have stored associated with the notes each user publishes.
    '''
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True) #primary_key will be added automatically, unique identifier.
    data = db.Column(db.String(10000), nullable=False)
    date = db.Column(db.DateTime(timezone=True), default=func.now()) #gets current data and time for us, no need to define it.
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) #associate note with user, foreign key references id from another object
    #this is a one to many relationship (one user to many keys), need to look at user.id (sql will automatically take our classes and lowercase them) to verify.

class User(db.Model, UserMixin):
    '''
    Define all columns we want to have stored in this table. Defining a schema for this User object.
    '''
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True) #define primary key, unique identifier, typically int, that represents our object. db will set this id for you.
    email = db.Column(db.String(150), unique=True, nullable=False) #150 is max length, needed when defining string. 'unique' states that it is invalid to use an email that already exists in the db
    password = db.Column(db.String(150), nullable=False)
    username = db.Column(db.String(150), nullable=False)
    notes = db.relationship('Note') #list that stores all notes that a particular user owns
