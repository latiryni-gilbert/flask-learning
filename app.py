from flask import Flask
from flask import request
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def hello():
    name = request.args.get("name", "Flask")
    return f"Hello, {escape(name)}!"

@app.route('/expenses')
def expenses():
    return {'total': 0, 'count': 0}

if __name__ == '__main__':
    app.run(debug=True)