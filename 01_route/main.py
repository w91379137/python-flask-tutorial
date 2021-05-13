
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Hello, World!'

@app.route('/hi')
def hi():
    return 'Hi!'

if __name__ == "__main__":
    app.run(debug=True)