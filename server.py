from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "adorable_beagles"
                                                                                                                                                    

@app.route('/')
def num_game():
	## Just displaying the index here
	return render_template('index.html')

@app.route('/answer', methods=["POST"])
def check_answer():
	## Here I am trying to gather the form input from index.html
	## and compare it to a random number.
	if not 'num' in session:
		session['num'] = random.randrange(0, 101)
	answer = request.form['guess']
	if session['num'] > int(answer):
		if session['num'] > answer:
			statement = "Too low! Try again!"
		elif session['num'] < answer:
			statement = "Too high! Try again!"
		elif session['num'] == answer:
			statement = "Correct!"
		
	return redirect('/', data = session['statement'])
if __name__ =="__main__":
	app.run(debug=True)