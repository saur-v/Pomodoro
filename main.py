from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
my_timer=None
reps=0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk("My Pomodoro")
screen.config(bg = PINK)
screen.config(padx=100, pady=50)

def start_timer():
    global reps 
    reps+=1
    work_second = WORK_MIN*60
    long_break = LONG_BREAK_MIN*60
    short_break = SHORT_BREAK_MIN*60
    if(reps%8==0):
        count = long_break
        my_text.config(text="BREAK", fg=GREEN)
    elif(reps%2==0):
        count=short_break
        my_text.config(text="BREAK", fg=GREEN)
    else:
        count=work_second  
        my_text.config(text="WORK", fg=RED) 
    count_down(count)       
    

    
def count_down(count):
    count_minute=math.floor(count/60)
    count_second=count%60
    if(count_second<10):
        count_second=f"0{count_second}"
    if(count_minute<10):
        count_minute=f"0{count_minute}"  
    my_canva.itemconfigure(my_count, text=f"{count_minute}:{count_second}")
    if count>0:
        global my_timer
        my_timer=screen.after(1000, count_down, count-1)
    else:
        start_timer()
        mark=""
        work_sessions=math.floor(reps/2)  
        for i in range(work_sessions):
            mark+="✓"  
        my_check.config(text=mark, fg=GREEN)   


def reset_timer():
    screen.after_cancel(my_timer)
    my_canva.itemconfig(my_count, text="00:00")
    my_text.config(text="TIMER", fg=GREEN)
    my_check.config(text="")
    global reps
    reps=0



my_canva = Canvas(width=200, height=224, bg = PINK, highlightthickness=0)
My_pic = PhotoImage(file = "tomato.png")
my_canva.create_image(100, 112, image = My_pic)
my_count=my_canva.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
my_canva.grid(column = 2, row = 1)

my_text = Label(text = "TIMER", fg = GREEN, font = ("arial", 50, "bold"), bg = PINK)
my_text.grid(column = 2, row = 0, ipady=20)


start_button = Button(text="Start", fg=RED, bg="white", font=("courier", 10), highlightthickness=0, command=start_timer)
start_button.grid(column = 1, row = 2)

reset_button = Button(text="Reset", fg=RED, bg="white", font=("courier", 10), highlightthickness=0, command=reset_timer)
reset_button.grid(column = 3, row = 2)

my_check = Label(text = "", fg = RED, font = ("arial", 15), bg = PINK)
my_check.grid(column = 2, row = 3)
count=10


screen.mainloop()
