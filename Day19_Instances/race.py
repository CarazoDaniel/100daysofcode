import turtle as t
import random

WIDTH = 700
HEIGHT = 500
screen = t.Screen()
screen.setup(width= WIDTH, height= HEIGHT)
start = False
user_pick = screen.textinput(title='Make your bet',prompt="choose your color ('red','orange','yellow','green','blue','purple'])")
options = ['red','orange','yellow','green','blue','purple']
start_pos = - (HEIGHT - 50) / 2
distance = (HEIGHT - 50) / (len(options)-1)
positions = []
all_of_them = []
for i in range(len(options)):
    positions.append(start_pos + (distance * i))

for turtle_index in range(len(options)):
    tut = t.Turtle(shape='turtle')
    tut.penup()
    tut.color(options[turtle_index])
    tut.goto(x=-WIDTH/2+20, y=positions[turtle_index])
    all_of_them.append(tut)

if user_pick:
    start = True

while start:
    for turt in all_of_them:
        if turt.xcor() > WIDTH / 2 - 20:
            start = False
            win_color = turt.pencolor()
            if win_color == user_pick:
                print(f"You have won, the color: {turt.pencolor()} has won the race!")
            else:
                print(f"You have lost, the color: {turt.pencolor()} has won the race!")
        turt.forward(random.randint(0,10))


screen.exitonclick()

    
