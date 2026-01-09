from tkinter import *


def conver_km():
    value = float(input.get())
    value *= 1.6
    value_lable.config(text=round(value,2))

def switch():
    pass

def convert_mi():
    value = float(input.get())
    value *= 0.62
    value_lable.config(text=f"{round(value,2)}")



window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=100, pady=200)


#Label
label_from = Label(text="Miles", font=("Arial", 24, "bold"))
label_from.grid(column=2, row=0)
label_from.config(padx=50, pady=50)

#Label
lable_to = Label(text="Km", font=("Arial", 24, "bold"))
lable_to.grid(column=2, row=1)
lable_to.config(padx=50, pady=50)

#Label
my_label = Label(text="is equal to: ", font=("Arial", 24, "bold"))
my_label.grid(column=0, row=1)
my_label.config(padx=50, pady=50)

#Label
value_lable = Label(text="0", font=("Arial", 24, "bold"))
value_lable.grid(column=1, row=1)
value_lable.config(padx=50, pady=50)

#Buttonv, font=("Arial
button = Button(text="Convert", command=conver_km)
button.grid(column=1, row=2)

def listbox_used(event):
    # Gets current selection from listbox
    if listbox.get(listbox.curselection()) == "Mi to Km":
        label_from.config(text="Miles")
        lable_to.config(text="km")
        button.config(command=conver_km)
    else:
        label_from.config(text="km")
        lable_to.config(text="Miles")
        button.config(command=convert_mi)

listbox = Listbox(height=2)
units = ["Mi to Km", "Km to Mi"]
for item in units:
    listbox.insert(units.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=2, row=2)

#Entry
input = Entry(width=10)
input.grid(column=1, row=0)









window.mainloop()