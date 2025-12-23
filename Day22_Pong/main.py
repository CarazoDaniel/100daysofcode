from turtle import Screen
from paddle import Paddle,WIDTH,HEIGHT,PLAY_DISTANCE
from ball import Ball
from scoreboard import Score
import time


WIDTH = WIDTH * 2
HEIGHT = HEIGHT * 2


screen = Screen()
screen.setup(width=WIDTH,height=HEIGHT)
screen.bgcolor('black')
screen.title('Just a Simple Pong')
screen.tracer(0) ##screen updates torned off

player1 = Paddle()
player2 = Paddle()
player1.player1()
player2.player2()
ball = Ball()
scoreboard = Score()

game = True


screen.listen()
screen.onkey(player1.up,"Up")
screen.onkey(player1.down,"Down")
screen.onkey(player2.up,"w")
screen.onkey(player2.down,"s")




while game:
    time.sleep(ball.ballspeed)
    screen.update()
    ball.move()
    #upper colission
    if ball.ycor() > HEIGHT/2 -20 or ball.ycor() < -HEIGHT/2 +20:
       ball.bounce_y()
    #paddle colission
    if ball.xcor() > WIDTH/2 - 1.5 * PLAY_DISTANCE and ball.distance(player1) < PLAY_DISTANCE+10 or ball.xcor() < -WIDTH/2 + 1.5* PLAY_DISTANCE and ball.distance(player2) < PLAY_DISTANCE+10:
        ball.bounce_x()
    #right side colission
    if ball.xcor() > WIDTH/2 - 10:
        ball.restart(1)
        scoreboard.score2 +=1
        scoreboard.update_score()
        #left side colission
    if ball.xcor() < -WIDTH/2 + 10:
        ball.restart(0)
        scoreboard.score1 +=1
        scoreboard.update_score()
    if scoreboard.score1 >= 7 or scoreboard.score2 >=7:
        scoreboard.game_over()
        game = False


screen.exitonclick()


