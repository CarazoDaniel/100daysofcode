import turtle

screen = turtle.Screen()
screen.clearscreen()

tom = turtle.Turtle()

def move_forward():
    tom.forward(5)

def move_backwards():
    tom.backward(5)

def move_right():
    tom.setheading(tom.heading() - 5)

def move_left():
    tom.setheading(tom.heading() + 5)

def clear_it():
    tom.clear()
    tom.teleport(0,0)

screen.listen()
screen.onkey(move_forward,"w")
screen.onkey(move_backwards,"s")
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
screen.onkey(clear_it,"c")

screen.exitonclick()