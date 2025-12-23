from turtle import Turtle
STARTING_X= 0
STARTING_Y=-280
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
UP = 90


class Player(Turtle):
    def __init__(self, shape = "turtle"):
        super().__init__(shape = shape)
        self.penup()
        self.speed(0)
        self.color('green')
        self.setheading(UP)
        self.recenter()
        
    def recenter(self):
        self.teleport(STARTING_X,STARTING_Y)

    def move_f(self):
        self.forward(MOVE_DISTANCE)

    def next_level(self):
        self.recenter()
    