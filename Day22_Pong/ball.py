from turtle import Turtle
from paddle import WIDTH, HEIGHT
import random


class Ball(Turtle):
    def __init__(self, shape = "circle"):
        super().__init__(shape)
        self.color('white')
        self.penup()
        self.start()
        self.ballspeed = 0.01

    def start(self):
        angle_range = [random.randint(-45,45),random.randint(135,225)] # -45 and 45 is rightside
        #135 and 225 is left side
        self.setheading(random.choice(angle_range)) # rand choice of side.
    
    def move(self):
        self.forward(5)
    
    def bounce_y(self):
        current = self.heading()
        if 0 < current < 180:
            self.setheading(0 - current)
        else:
            self.setheading(360 - current)
    def bounce_x(self):
        current = self.heading()
        if  0 < current < 180:
            self.setheading(180 - current)
        else:
            self.setheading(540 - current)
        self.ballspeed *= 0.9
    
    def restart(self,side):
        self.teleport(0,0)
        angle_range = [random.randint(-45,45),random.randint(135,225)]
        self.setheading(angle_range[side])
        self.ballspeed = 0.01
