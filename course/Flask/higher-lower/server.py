from flask import Flask
from random import randint

app=Flask(__name__)

@app.route('/')
def heading():
    return '<h1>Guess a number between 0 and 9</h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif" />'

randnum = randint(0,9)
@app.route('/<int:num>')
def check(num):
    if randnum==num:
        return '<h1 style="color :green">You Found me</h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif" />'
    if randnum>num:
        return '<h1 style="color :red">Too low,Try again!</h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif" />'
    if randnum<num:
        return '<h1 style="color :violet">Too high,Try again!</h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif" />'


if __name__=="__main__":
    app.run(debug=True)
