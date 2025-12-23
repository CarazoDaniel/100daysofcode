import turtle as t
from snek import Snake
import random
import time

WIDTH = 600
HEIGHT = 600

screen = t.Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor('black')
screen.title('Just a Snek Game')
screen.tracer(0) ##screen updates torned off

snek = Snake()
game = True

screen.listen()
screen.onkey(snek.up,"Up")
screen.onkey(snek.down,"Down")
screen.onkey(snek.left,"Left")
screen.onkey(snek.right,"Right")

while game:
    time.sleep(.1)
    screen.update()
    snek.move_snek()










screen.exitonclick()