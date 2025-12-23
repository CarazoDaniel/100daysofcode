from turtle import Turtle
from paddle import HEIGHT

HEIGHT = HEIGHT - 45     
FONT = ('Courier', 24 ,'normal')
FINISH_FONT = ('Courier', 34 ,'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self, visible = False):
        super().__init__(visible=visible)
        self.color("white")
        self.penup()
        self.score1 = 0
        self.score2 = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.teleport(x=-30,y=HEIGHT)
        self.write(f"{self.score2}",move = False,align=ALIGNMENT,font= FONT)
        self.teleport(x= 30,y=HEIGHT)
        self.write(f"{self.score1}",move = False,align=ALIGNMENT,font= FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(f"GAME OVER",move = False,align=ALIGNMENT,font= FINISH_FONT)