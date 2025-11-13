from turtle import Turtle, Screen

tom = Turtle()

for i in range(4):
    tom.forward(100)
    tom.left(90)

screen = Screen()
screen.exitonclick()