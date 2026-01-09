from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 1
rep = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global rep 
    global timer
    rep -= 1
    title.config(text=f"Timer, rep: {rep}")
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text= "00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global rep
    if rep % 2 == 0:
        title.config(text="Work",fg=GREEN)
        count_down(WORK_MIN * 60)
        rep +=1
    elif rep % 7 == 0:
        title.config(text="Long break",fg=RED)
        count_down(LONG_BREAK_MIN *60)
        rep +=1
        check.config(text="✓"*math.floor(rep/2))

    else:
        title.config(text="Short break",fg=PINK)
        count_down(SHORT_BREAK_MIN *60)
        rep +=1
        check.config(text="✓"*math.floor(rep/2))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = math.floor(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    
    canvas.itemconfig(timer_text, text= f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000,count_down,count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=100,bg=YELLOW)

title = Label(text="Timer", font=(FONT_NAME, 30, "bold"), fg= GREEN,bg=YELLOW)
title.grid(column=1, row=0)
title.config(padx=50, pady=50)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file = "./tomato.png")
canvas.create_image(100,112, image = tomato_img)
timer_text = canvas.create_text(100,111,text="00:00",fill="white",font=(FONT_NAME,30,"bold"))
canvas.grid(column=1,row=1)

starting = Button(text="Start", font=(FONT_NAME, 12, "bold"),bg=YELLOW, highlightthickness=0, command=start_timer)
starting.grid(row=2,column=0)


stoping = Button(text="Reset",font=(FONT_NAME, 12, "bold"),bg=YELLOW,highlightthickness=0, command=reset_timer)
stoping.grid(row=2,column=2)

check = Label(font=(FONT_NAME, 12, "bold"), fg= GREEN,bg=YELLOW)
check.grid(column=1, row=3)
check.config(padx=50, pady=50)

window.mainloop()