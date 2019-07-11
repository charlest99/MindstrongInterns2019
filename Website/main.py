from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def MainPageTest():
	return render_template("MainPageTest.html")

@app.route('/cars', methods=['GET', 'POST'])
def Cars():
	return render_template('Cars.html')

@app.route('/news', methods=['GET','POST'])
def News():
	return render_template('News.html')

if __name__ == "__main__":
	app.run(host="0.0.0.0", port="80")
