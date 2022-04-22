from website import create_app

app = create_app()

if __name__ == '__main__':
    FLASK_APP = '__main__'
    app.run(debug=True)

