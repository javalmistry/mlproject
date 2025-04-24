from flask import Flask
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def index():
    return 'Index Page 1'


@app.route("/hello")
def hello():
    return "<h1>This is index page</h1><p>Hello, World!</p>"

@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {escape(username)}'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return f' Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return f'Subpath {esacpe(subpath)}'

@app.route('/projects/')
def projects():
    return 'The Project Page'

@app.route('/about')
def abount():
    return 'The About Page'