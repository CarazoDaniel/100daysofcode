from turtle import Turtle

UP = 90 ## 90degrees
WIDTH = 400
HEIGHT = 300 #Abs values
PLAY_DISTANCE = 50

class Paddle(Turtle):
    def __init__(self, shape = "square"):
        super().__init__(shape)
        self.color("white")
        self.setheading(UP) 
        self.penup()
        self.speed(0)#fastest
        self.shapesize(stretch_wid=1, stretch_len=5)
    
    def player1(self):
        self.teleport(WIDTH - PLAY_DISTANCE,0)
        
    def player2(self):
        self.teleport(-WIDTH + PLAY_DISTANCE,0)

    def up(self):
        self.forward(50)
        
    def down(self):
        self.backward(50)