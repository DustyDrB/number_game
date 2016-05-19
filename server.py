from flask import Flask, render_template, request, session, redirect
import random

app = Flask(__name__)
app.secret_key = "adorable_beagles"

@app.route('/restart')
def restart():
    session.clear()
    return redirect('/')

@app.route('/')
def num_game():
    if not 'num' in session:
        session['num'] = random.randrange(1, 101)
    if not 'result' in session:
        session['result'] = { 'classname': '', 'text' : ''}
    return render_template('index.html')

@app.route('/answer', methods=["POST"])
def check_answer():
    guess = int(request.form['guess'])

    # compare guess against a secret number
    if guess == session['num']:
        session['result']['classname'] = True
        session['result']['text'] = "YOU GOT IT!"
    elif guess < session['num']:
        session['result']['classname'] = 'below'
        session['result']['text'] = "TOO LOW!"
    else:
        session['result']['classname'] = 'above'
        session['result']['text'] = "TOO HIGH!"

    return redirect('/')

    ## Here I am trying to gather the form input from index.html
    ## and compare it to a random number.
    # if not 'num' in session:
    #     session['num'] = random.randrange(0, 101)
    # answer = request.form['guess']
    # if session['num'] > int(answer):
    #     if session['num'] > answer:
    #         statement = "Too low! Try again!"
    #     elif session['num'] < answer:
    #         statement = "Too high! Try again!"
    #     elif session['num'] == answer:
    #         statement = "Correct!"
    #
    # return redirect('/', data = session['statement'])
if __name__ =="__main__":
    app.run(debug=True)
