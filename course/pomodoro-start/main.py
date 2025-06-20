from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
repes=0
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    heading.config(text="Timer")
    check_marks.config(text="")
    global repes
    repes=0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global repes
    repes+=1
    work_sec = WORK_MIN *60
    short_break_sec= SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN * 60
    if repes==8:
        heading.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif repes%2:
        heading.config(text="Work",fg=GREEN)
        count_down(work_sec)
    else :
        heading.config(text="Break",fg=PINK)
        count_down(short_break_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    count_min = count//60
    count_sec = count % 60
    if count_sec<10:
        count_sec=f"0{count_sec}" #dynamic type casting where int var changed to str type
    canvas.itemconfig(timer_text,text=f"{count_min} : {count_sec}") # config method for a canvas object to make changes
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1) # it will update call the fn with args folled after teh fn name , we can't directly use while loop to update the text as it Tk uses here event driven architecture. so it is running all time we are using the window

    else :
        start_timer()
        marks=""
        work_sessions = repes//2
        for _ in range(work_sessions):
            marks+="✔️"
        check_marks.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50 , bg=YELLOW)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0) #allow us to put object one above another
# highlightthickness is for to remove border formed around the canvas image
tomato_img = PhotoImage(file="tomato.png") #method from tk inter to hold image , can't directly pass to create image
canvas.create_image(103,112,image=tomato_img) # x,y position. and image
timer_text = canvas.create_text(100,130,text="00 : 00", fill="white", font={FONT_NAME,35,"bold"})
canvas.grid(row=1, column=1)

heading = Label(text="Timer",font={FONT_NAME,50}, fg=GREEN,bg=YELLOW)
heading.grid(row=0, column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset",highlightthickness=0)
reset_button.grid(row=2, column=2)

check_marks = Label(text="✔️",fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)

window.mainloop()