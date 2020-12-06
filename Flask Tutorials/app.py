from flask import Flask,render_template,redirect,request

# __name__ == __main__
app = Flask(__name__)

# @app.route('/')
# def hello():
# 	return "Hello World"

friends = ["Zeeshan", "Rohit","Vishesh"]
num = 5

@app.route('/')
def hello():
	return render_template("index.html",my_friends = friends,num = num)

@app.route('/about')
def about():
	return "<h1> About Page </h1>"

@app.route('/home')
def home():
	return redirect('/')

@app.route('/submit', methods = ['POST']) ## In all previous routes method 'GET'by default
## POST route can not be open directly by entering URL, i.e can only be called

def submit_data():
	if request.method == 'POST':
		name = request.form['username']
		no1 = int(request.form['no1'])
		no2 = int(request.form['no2'])

		## files come in separate dict files not in form dict
		f = request.files['userfile']
		f.save(f.filename) ## saves the file with same name which it had while uploaded by user

	return '<h1> Hello {}'.format(name + " " + str(no1 + no2))


if __name__ == '__main__':
	app.run(debug = True)