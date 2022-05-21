'''
Call this file to start up the flask server
'''

############# Referencing https://www.youtube.com/watch?v=dam0GPOAvVI for flask website and security
############# Referencing https://www.youtube.com/watch?v=hQl2wyJvK5k for substituting MySQL instead of SQLAlchemy


from website import create_app #this works because we have an __init__ file in the website folder

app = create_app()

if __name__ == '__main__': #"only if we run app.py, not import app.py, we will run this code"
    FLASK_APP = '__main__'
    app.run(debug=True) #For testing only, debug mode: whenever a change is made to the code, automatically re-run the server

