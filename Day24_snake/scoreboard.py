from turtle import Turtle

HEIGHT = 260 ##using abs value, for range purpose
FONT = ('Courier', 24 ,'normal')
FINISH_FONT = ('Courier', 34 ,'normal')
ALIGNMENT = 'center'

class Score(Turtle):
    def __init__(self, visible = False):
        super().__init__(visible=visible)
        self.color("white")
        self.penup()
        self.teleport(x=-50,y=HEIGHT)
        self.score = 0
        with open("./data.txt") as data:
            self.highest = int(data.read())
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} Highest Score: {self.highest}",move = False,align=ALIGNMENT,font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    

    def reset(self):
        if self.score > self.highest:
            self.highest = self.score
            with open("./data.txt", mode='w') as data:
                data.write(f'{self.highest}')
        self.score = 0
        self.update_score()

#    def game_over(self):
#        self.teleport(0,0)
#        self.write(f"GAME OVER",move = False,align=ALIGNMENT,font= FINISH_FONT)