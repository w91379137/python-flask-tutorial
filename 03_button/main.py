
# https://flask.palletsprojects.com/en/1.1.x/quickstart/

from flask import Flask, render_template
import random

app = Flask(__name__)
length = 31

@app.route('/')
@app.route('/index')
def index():
    
    w = random.randrange(4) + 3
    h = random.randrange(4) + 3

    button_info_list = []
    for i in range(w):
        for j in range(h):
            id = i + j * w
            dict = {
                'left': f'{ i * length + length}px',
                'top': f'{ j * length + length}px',
                'title': str(id).zfill(2),
            }
            button_info_list.append(dict)
            

    return render_template('index.html', button_info_list = button_info_list)

if __name__ == "__main__":
    app.run(debug=True)