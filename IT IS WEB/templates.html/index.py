from flask import Flask

app= Flask(__name__)
@app.route('/')
def home():
    return 'helo world'


    if __name__ == '_main_':
        app.run()