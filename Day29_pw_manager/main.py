from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip 

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def new_one():
    passentry.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(numbers) for _ in range(randint(2,4))]
    password_numbers = [choice(symbols) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    passentry.insert(END,password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = nameentry.get()
    email = emailentry.get()
    pwd = passentry.get()
    
    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Failed", message="Please fill all the requiered info")
    elif messagebox.askokcancel(title=website, message=f"These are the details to save: \n {website} \n {email} \n {pwd}\n is it ok to save?"):
        with open("./data.txt", mode='a') as data:
            data.write(f'{website} | {email} | {pwd}\n')
            nameentry.delete(0,END)
            passentry.delete(0,END)
        
# ---------------------------- UI SETUP ------------------------------- #

RED = "#e7305b"
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=20,pady=20)

canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file = "./logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1,row=0)


#Label name
namelabel = Label(text="Website:")
namelabel.grid(column=0,row=1)

#Entries
nameentry = Entry(width=35)
nameentry.focus() # get the cursor started here
nameentry.grid(column=1,row=1,columnspan=2)


emaillabel = Label(text="Email/Website:")
emaillabel.grid(column=0,row=2)


#Entries
emailentry = Entry(width=35)
#Add some text to begin with
emailentry.insert(END, string="@gmail.com")
#Gets text in entry
emailentry.grid(column=1,row=2,columnspan=2)


passlabel = Label(text="Password:")
passlabel.grid(column=0,row=3)

#Entries
passentry = Entry(width=21)
#Gets text in entry
passentry.grid(column=1,row=3)

#calls action() when pressed
passbutton = Button(text="Generate password", command=new_one)
passbutton.grid(column=3,row=3)


#calls action() when pressed
add_button = Button(text="Add new password", command=save,width = 36)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()