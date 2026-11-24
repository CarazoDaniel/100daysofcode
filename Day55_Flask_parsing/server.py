from flask import Flask
import random

app = Flask(__name__)
answer = random.randint(0,25)


@app.route('/')
def hello_world():
    #Rendering HTML Elements
    return '<h1 style="text-align: center">Guess a number between 0 and 25</h1>' \
           '<p>This is a paragraph.</p>' \
           '<img src="https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdnd6ZGpmZ3A5bnM0azFtdWJ4Z3Y0MXYwZDVlN3hvNnY0ODJkcHBtdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hvLwZ5wmarjnNKEJqq/giphy.gif" width=500>'


#Different routes using the app.route decorator
@app.route("/<int:guess>")
def guess_number(guess):
    if guess > answer:
        return "<h1 style='color: purple'>Too high, try again!</h1>" \
               "<img src='https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaGFyMDN6dnc0eTM3aHFld2g2czc0bmc0OGl0aDkzdHNldjkweWdldCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/K4kSJ51JJeC7cHAQ1a/giphy.gif'/>"

    elif guess < answer:
        return "<h1 style='color: red'>Too low, try again!</h1>"\
               "<img src='https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExc2hsdmNmMWo4Mmx0MXgxc2FwemV4dGthMmd0MDB0bTdybnZyNXppMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/MAeewHC2J8gQS0IGAO/giphy.gif'/>"
    else:
        return "<h1 style='color: green'>You found me!</h1>" \
               "<img src='https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWIweXh5dHJ0eDEybTJrcXk1NjMzdG9rcXFwZHVycGYxNTdyODVvZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ic1F7e9rw8VL6Xlm3O/giphy.gif'/>"

if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)
