from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>This is index page</h1><p>Hello, World!</p>"