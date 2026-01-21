from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello, World!'

@app.route('/expenses')
def expenses():
    return {'total': 0, 'count': 0}

if __name__ == '__main__':
    app.run(debug=True)