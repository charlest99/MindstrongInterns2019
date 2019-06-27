from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/hicontrast', methods=['GET', 'POST'])
def hicontrast():
    return render_template('hicontrast.html')


@app.route('/tapping', methods=['GET', 'POST'])
def tapping():
    return render_template('tapping.html')

if __name__ == '__main__':
	app.run(host='0.0.0.0')