from turtle import Screen
from snek import Snake
from scoreboard import Score
import time
from food import Food

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor('black')
screen.title('Just a Snek Game')
screen.tracer(0) ##screen updates torned off

snek = Snake()
game = True
food = Food()
score = Score()

screen.listen()
screen.onkey(snek.up,"Up")
screen.onkey(snek.down,"Down")
screen.onkey(snek.left,"Left")
screen.onkey(snek.right,"Right")

while game:
    time.sleep(.1)
    screen.update()
    snek.move_snek()
    # getting fed, colision with food
    if snek.head.distance(food) < 8:
        food.respawn()
        score.increase_score()
        snek.tail_extension()

    # colision with walls:
    if snek.head.xcor() > WIDTH/2 - 10 or  snek.head.xcor() < -WIDTH/2 + 10 or snek.head.ycor() > HEIGHT/2 - 10 or  snek.head.ycor() < -HEIGHT/2 + 10:
        screen.resetscreen()
        score.reset()
        snek.reset_snek()
        food.respawn()
        

    ##Slicing [start:finish:pase] neg pase reverses the slicing
    for tail in snek.new_snek[1:]: 
        if snek.head.distance(tail) < 5:
            screen.resetscreen()
            score.reset()
            snek.reset_snek()
            food.respawn()
            








screen.exitonclick()