from flask import Flask, render_template, request
from predict import *



app = Flask(__name__)
@app.route('/')
def home():
	return render_template("index.html")
	

@app.route('/about')
def about():
	return render_template('about.html')

@app.route('/test')
def test():
	return render_template('test.html')

@app.route('/prediction', methods=["GET", "POST"])
def prediction():
	if request.method == "POST" and "username" in request.form:
		username = request.form['username']
		prediction, first_10_tweets, link, fact = get_prediction(username)
		return render_template('prediction.html', username=username, predicted_type=prediction, tweets=first_10_tweets, link= link, fact= fact)

app.run(debug=True)

