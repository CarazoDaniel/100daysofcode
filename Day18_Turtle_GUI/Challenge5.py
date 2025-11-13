from turtle import Turtle, Screen
import random

screen = Screen()
screen.clearscreen()
tom = Turtle()
tom.shape('circle')
tom.hideturtle()
tom.speed(0)


def random_color():
    gcolor = random.random()
    rcolor = random.random()
    bcolor = random.random()
    tom.pencolor(rcolor,gcolor,bcolor)

for _ in range(90):
    random_color()
    tom.circle(50)
    tom.left(4)



screen.exitonclick()