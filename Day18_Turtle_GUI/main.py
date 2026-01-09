#
#import colorgram
#
#colors = colorgram.extract('image.jpg', 7*12)
#print(colors)
#
#rgbs = [] 
#
#for color in colors:
#    rgbs.append((color.rgb.r,color.rgb.g,color.rgb.b))
#print(rgbs)


import turtle as t
import random

extracted_rgbs = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), 
                  (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
                  (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171),
                    (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), 
                    (107, 127, 153), (176, 192, 208), (168, 99, 102), (66, 64, 60), (219, 178, 183), (178, 198, 202)
                    , (112, 139, 141), (254, 194, 0)]
NUM_DOTS = 30
DOT_SIZE = 10

screen = t.Screen()
screen.clearscreen()
tom = t.Turtle()
tom.hideturtle()
tom.speed(0)
t.colormode(255)
tom.pensize(DOT_SIZE)
tom.teleport(-250,-250) 

def new_color():
    tom.pencolor(random.choice(extracted_rgbs))


for _ in range(NUM_DOTS):
    for i in range(NUM_DOTS):
        new_color()
        tom.pendown()
        tom.forward(1)
        tom.penup()
        tom.forward(500/NUM_DOTS)
    tom.penup()
    tom.left(90)
    tom.forward(500/NUM_DOTS)
    tom.left(90)
    tom.forward(500+NUM_DOTS)
    tom.left(180)


screen.exitonclick()