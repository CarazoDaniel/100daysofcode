from turtle import Turtle, Screen
screen = Screen()
screen.clearscreen()
tom = Turtle()
tom.teleport(-300)
tom.shape('circle')

for i in range(60):
    if i % 2 == 0:
        tom.up()
    else:
        tom.down()
    tom.forward(10)

screen.exitonclick()