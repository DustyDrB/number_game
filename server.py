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
    
if __name__ =="__main__":
    app.run(debug=True)
