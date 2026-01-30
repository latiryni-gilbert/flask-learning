# I am following the flask.palletsprojects.com quickstart guide

from flask import Flask
from flask import request
from markupsafe import escape
from flask import url_for

app = Flask(__name__)

#Routing
@app.route("/")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route('/index')
def index():
    return 'Index Page'

@app.route('/login')
def login():
    return 'login'

# POST AND GET (HTTP Methods)
#@app.route('/login', methods=['GET', 'POST'])
#def_login():
    # if request.method == 'POST':
        # return do_the_login()
    # else:
        # return show_the_login_form()

#@app.route('/login')
#def login_get():
    #return show_the_login_form()

#@app.post('/login')
#def login_post():
    #return do_the_login()

#Variable Rules
@app.route('/user/<username>')
def profile(username):
    # show the user profile for that user
    return f'{username}\'s profile'

# URL Building
with app.test_request_context():
    print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post {post_id}'

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return f'Subpath {escape(subpath)}'

#Unique URLS/Redirection Behavior
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

# Debug mode
if __name__ == '__main__':
    app.run(debug=True)