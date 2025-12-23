import time
from turtle import Screen
from player import Player,FINISH_LINE_Y
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

game_is_on = True
cars_running = CarManager()
player = Player()
scoreboard = Score()
counter = 0

screen.listen()
screen.onkey(player.move_f,"Up")

while game_is_on:
    time.sleep(0.1)
    cars_running.cars_forward()
    if counter % 10 == 0:
        cars_running.add_cars()
    if player.ycor() >= FINISH_LINE_Y:
        cars_running.up_level()
        player.next_level()
        scoreboard.next_level()
    for i in cars_running.cars:
        if player.distance(i) < 25:
            scoreboard.game_over()
            game_is_on = False
    screen.update()
    counter +=1

screen.exitonclick()
