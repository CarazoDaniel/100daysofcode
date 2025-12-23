from turtle import Turtle

HEIGHT = 300 - 55     
FONT = ('Courier', 24 ,'normal')
FINISH_FONT = ('Courier', 34 ,'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self, visible = False):
        super().__init__(visible=visible)
        self.color("black")
        self.penup()
        self.score = 1
        self.teleport(-200,HEIGHT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Level: {self.score}",move = False,align=ALIGNMENT,font= FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(f"GAME OVER",move = False,align=ALIGNMENT,font= FINISH_FONT)

    def next_level(self):
        self.score +=1
        self.update_score()
    