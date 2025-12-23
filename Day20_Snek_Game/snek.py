from turtle import Turtle

class Snake:
    """Creates a base Snake"""
    def __init__(self):
        self.new_snek=[]
        self.initiate_the_snek()
        self.head = self.new_snek[0]
        
    def initiate_the_snek(self):
        for i in range(3):
            tail = Turtle(shape='square')
            tail.color('white')
            tail.shapesize(stretch_wid=0.5, stretch_len=0.5)
            tail.penup()
            tail.teleport(x=-10*i,y=0)
            self.new_snek.append(tail)    

    def move_snek(self):
        """Move forward"""
        for i in range(len(self.new_snek) - 1):
            last = len(self.new_snek) - 1 - i
            next_x = self.new_snek[last -1].xcor()
            next_y = self.new_snek[last -1].ycor()
            self.new_snek[last].goto(next_x,next_y)
        self.head.forward(20)

    def up(self):
        """Change the Heading to 90"""
        if self.head.heading() != 270:
            self.head.setheading(90)
    def down(self):
        """Change the Heading to 270"""
        if self.head.heading() != 90:
            self.head.setheading(270)  
    def left(self):
        """Change the Heading to 180"""
        if self.head.heading() != 0:
            self.head.setheading(180)  
    def right(self):
        """Change the Heading to 0"""
        if self.head.heading() != 180:
            self.head.setheading(0)  