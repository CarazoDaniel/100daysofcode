from tkinter import *
from tkinter import messagebox
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = 'Arial'

# Words
try:
    words = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    words = pandas.read_csv("./data/italian_words_5k.csv")
finally:    
    words = words.to_dict(orient="records")


# Functions:
def to_ask(word):
    front_canvas.itemconfig(image, image = front_card_image)
    front_canvas.itemconfig(card_title, text = "Italiani",fill= "Black")
    front_canvas.itemconfig(card_word, text = word,fill= "Black")
    
def to_answer(word):
    front_canvas.itemconfig(image, image = back_card_image)
    front_canvas.itemconfig(card_title, text= "English", fill = "White")
    front_canvas.itemconfig(card_word, text = word, fill = "White")
    
def new_word():
    global flip_timer, next_word
    next_word = choice(words)
    window.after_cancel(flip_timer)
    to_ask(next_word["Italian"])
    flip_timer = window.after(5000,to_answer,next_word["English"])
    
def known_word():
    global flip_timer, next_word
    words.remove(next_word)
    data = pandas.DataFrame(words)
    data.to_csv("./data/words_to_learn_it.csv",index=False)
    new_word()


    
# UI 
window = Tk()
window.title("Flash Card Game")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR,)


wrong_image = PhotoImage(file="./images/wrong.png")
right_image = PhotoImage(file="./images/right.png")
front_card_image = PhotoImage(file="./images/card_front.png")
back_card_image = PhotoImage(file="./images/card_back.png")



wrong_button = Button(image=wrong_image, highlightthickness=0, command= new_word)
wrong_button.grid(row=1,column=0)

right_button = Button(image=right_image, highlightthickness=0, command= known_word)
right_button.grid(row=1,column=1)




#front card
front_canvas = Canvas(width=800,height=526,highlightthickness=0)
image = front_canvas.create_image(400,263,image = front_card_image)
card_title = front_canvas.create_text(400, 150, text='', font=(FONT_NAME, 40, "italic"), )
card_word = front_canvas.create_text(400, 263, text="", font=(FONT_NAME, 60, "bold"), )
front_canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
front_canvas.grid(column=0,row=0,columnspan=2)
flip_timer = window.after(1,new_word)



window.mainloop()