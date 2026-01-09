from turtle import Turtle

FONT = ('Courier', 8 ,'bold')
FINISH_FONT = ('Courier', 34 ,'normal')
ALIGNMENT = 'center'

class Write(Turtle):
    def __init__(self, visible = False):
        super().__init__(visible=visible)
        self.color("black")
        self.penup()

    def update_name(self,name,x,y):
        self.teleport(x,y)
        self.write(f"{name}",move = False,align=ALIGNMENT,font= FONT)

    def game_over(self):
        self.teleport(0,0)
        self.write(f"You got it!",move = False,align=ALIGNMENT,font= FINISH_FONT)

    