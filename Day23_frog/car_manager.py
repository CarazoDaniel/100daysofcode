import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
LENGTHS = [3,4,5]
HEIGHT = 240


class Car(Turtle):
    def __init__(self, shape = "square"):
        super().__init__(shape = shape)
        self.color(random.choice(COLORS))
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=random.choice(LENGTHS))
        self.setheading(180)
    
class CarManager:
    def __init__(self):
        self.level = 0
        self.cars = []
        self.start_cars()

    def start_cars(self):
        for i in range(random.randint(5,20) + self.level * 5):
            self.starty = random.randint(-HEIGHT,HEIGHT)
            self.startx = random.randint(-HEIGHT,HEIGHT)
            self.cars.append(Car())
            self.cars[i].teleport(self.startx,self.starty)

    def cars_forward(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT*self.level)
    
    def up_level(self):
        self.level += 1
    
    def add_cars(self):
        self.range = random.randint(0,2) + self.level * 5
        self.len = len(self.cars)
        if self.range > 0:
            for i in range(self.range):
                self.start = random.randint(-HEIGHT,HEIGHT)
                self.cars.append(Car())
                self.cars[self.len+i].teleport(350,self.start)




