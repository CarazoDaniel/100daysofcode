import turtle
import pandas
from write import Write

screen = turtle.Screen()
screen.title('U.S. States Game')
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
write = Write()
states = pandas.read_csv("50_states.csv")

names = states.state.to_list()
states.index =  names
x = states.x.to_list()
y = states.y.to_list()

correct = 0


while correct < 50:
    answer = screen.textinput(title=f"({correct}/50) Guess the state",prompt= "What's another state name?").title()
    if answer == "Exit":
        names = pandas.DataFrame(names)
        names.to_csv("states_to_learn.csv")
        break
    
    if answer in names:
        accepted = names.index(answer)
        stated = states.loc[answer]
        correct +=1
        write.update_name(answer,stated.x,stated.y)
        names.pop(accepted)
    #for each in names:
        #if each == answer:
            #accepted = names.index(each)
            #stated = states.loc[each]
            #correct += 1
            #write.update_name(each,stated.x,stated.y)
            #write.update_name(each,x[accepted],y[accepted])
            #x.pop(accepted)
            #y.pop(accepted)
            #names.pop(accepted)

    if correct == 50:
        write.game_over()


screen.exitonclick()