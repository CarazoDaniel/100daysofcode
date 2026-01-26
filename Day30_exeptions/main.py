from tkinter import *
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip 
import json

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
    new_data = {
        website: {
            "email":email,
             "password":pwd,
             }
        }
    
    if len(website) == 0 or len(pwd) == 0:
        messagebox.showinfo(title="Failed", message="Please fill all the requiered info")
    elif messagebox.askokcancel(title=website, message=f"These are the details to save: \n {website} \n {email} \n {pwd}\n is it ok to save?"):
        try:
            with open("./data.json", mode='r') as data_file:
                #read current data
                data = json.load(data_file)
                
        except FileNotFoundError:
            with open("./data.json", mode='w') as data_file:
                json.dump(new_data, data_file, indent=4)       
        
        else: 
            #updating the data with the new one (adding/append)
                data.update(new_data)
            #save the updated data
                with open("./data.json", mode='w') as data_file:
                    json.dump(data, data_file, indent=4)    
        finally:
            nameentry.delete(0,END)
            passentry.delete(0,END)
        
# ---------------------------- SEARCH FUNCTION ------------------------------- #

def search_password():
    website = nameentry.get()
    if len(website) == 0:
        messagebox.showinfo(title="Failed", message="Please fill all the requiered info")
    else:
        try:
            with open("./data.json", mode='r') as data_file:
                #read current data
                website_data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Failed", message="No Data File found")           
        else:
            if website in website_data:
                data = f"Email: {website_data[website]['email']}\nPassword: {website_data[website]['password']}"
            else:
                data = "No details for the website exist"
                nameentry.delete(0,END)
        finally:
            messagebox.showinfo(title=website, message=data)
                  
    

# ---------------------------- UI SETUP ------------------------------- #

RED = "#e7305b"
FONT_NAME = "Courier"

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

#logo
canvas = Canvas(width=200,height=200,highlightthickness=0)
logo_img = PhotoImage(file = "./logo.png")
canvas.create_image(100,100, image = logo_img)
canvas.grid(column=1,row=0)


#Label name
namelabel = Label(text="Website:")
namelabel.grid(column=0,row=1)

#Entries
nameentry = Entry(width=21)
nameentry.focus() # get the cursor started here
nameentry.grid(column=1,row=1)


emaillabel = Label(text="Email/Website:")
emaillabel.grid(column=0,row=2)


#Entries
emailentry = Entry(width=40)
#Add some text to begin with
emailentry.insert(END, string="@gmail.com")
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

search_button = Button(text="Search", width= 13, command=search_password)
search_button.grid(column=3,row=1)

window.mainloop()