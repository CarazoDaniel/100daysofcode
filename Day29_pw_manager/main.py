# ---------------------------- PASSWORD GENERATOR ------------------------------- #
from tkinter import *

RED = "#e7305b"
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file = "./logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1,row=1)


# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #


window.mainloop()