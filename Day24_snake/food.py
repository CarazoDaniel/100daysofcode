from turtle import Turtle
import random

WIDTH = 280
HEIGHT = 280 ##using abs value, for range purpose

class Food(Turtle):
    def __init__(self, shape = "turtle"):
        super().__init__(shape)
        self.penup()
        self.shapesize(stretch_wid=0.25, stretch_len=0.25)
        self.color("red")
        self.respawn()

    def respawn(self):
        rand_x = random.randint(-WIDTH,WIDTH)
        rand_y = random.randint(-HEIGHT,HEIGHT)
        self.teleport(rand_x,rand_y)


