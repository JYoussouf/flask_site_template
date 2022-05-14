'''
Call this file to start up the flask server
'''

############# Referencing https://www.youtube.com/watch?v=dam0GPOAvVI, Currently at 1:29:00

from website import create_app #this works because we have an __init__ file in the website folder

app = create_app()

if __name__ == '__main__': #"only if we run app.py, not import app.py, we will run this code"
    FLASK_APP = '__main__'
    app.run(debug=True) #For testing only, debug mode: whenever a change is made to the code, automatically re-run the server

