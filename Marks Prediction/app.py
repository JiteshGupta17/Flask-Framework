from flask import Flask,render_template,redirect,request
import joblib
import pickle


# __name__ == __main__
app = Flask(__name__)

model = joblib.load("model.pkl")

## for GET request
@app.route('/')
def hello():
	return render_template("index.html")


## for POST request
@app.route('/',methods = ['POST'])
def marks():

	if request.method == 'POST':
		hours = float(request.form['hours'])

		marks = str(model.predict([[hours]])) ## in 2-D array
	return render_template("index.html", your_marks = marks)

if __name__ == '__main__':
	app.run(debug = True)