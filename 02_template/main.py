
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', random_number = random.random())

if __name__ == "__main__":
    app.run(debug=True)