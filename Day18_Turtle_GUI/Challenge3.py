from turtle import Turtle, Screen
import random

screen = Screen()
screen.clearscreen()
tom = Turtle()
tom.shape('circle')
tom.teleport(-100,200)

gcolor = random.random()
rcolor = random.random()
bcolor = random.random()
    
    

for i in range(3,11):
    tom.pencolor(rcolor,gcolor,bcolor)
    for _ in range(i):
        tom.forward(100)
        tom.right(360/i)
    gcolor = random.random()
    rcolor = random.random()
    bcolor = random.random()


screen.exitonclick()