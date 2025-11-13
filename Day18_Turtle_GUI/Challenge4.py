from turtle import Turtle, Screen
import random

screen = Screen()
screen.clearscreen()
tom = Turtle()
tom.shape('circle')
tom.hideturtle()
tom.speed(0)
tom.pensize(10)


def random_color():
    gcolor = random.random()
    rcolor = random.random()
    bcolor = random.random()
    tom.pencolor(rcolor,gcolor,bcolor)

def random_direction():
    direction = [0,90,180,270]
    tom.left(random.choice(direction))

for _ in range(200):

    random_color()
    tom.forward(20)
    random_direction()




screen.exitonclick()