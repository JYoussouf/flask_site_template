'''
Makes 'website' an importable package. Everything in __init__.py will automatically run.
'''

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    '''
    initialize app
    '''
    app = Flask(__name__) 
    app.config['SECRET_KEY'] = 'joseppy_secret_key'  #secures cookie and session data related to the website
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}' #Define where our SQLAlchemy database is located at, sqlite:///
    db.init_app(app) #initialize the database, links the app we're building with the database 

    from .views import views #import views blueprints
    from .auth import auth #import auth blueprints
    # "register blueprints" so they work, define the prefix users would need to use to access these blueprint pages
    # ex. if url_prefix for auth was '/auth/', you would need to go to domainname/auth/login to get to the login page.
    app.register_blueprint(views,url_prefix='/') 
    app.register_blueprint(auth,url_prefix='/')

    return app