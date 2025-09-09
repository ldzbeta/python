BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
from random import choice
flip_fn=None
item={}
try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data= pandas.read_csv("data/french_words.csv")
finally :
    data_dict=data.to_dict(orient="records") #to change the way of making dict. {'French': 'enfant', 'English': 'child'}

def flip():
    canvas.itemconfig(card,image=card_back)
    canvas.itemconfig(title,text="English",fill="white")
    canvas.itemconfig(word, text=item["English"], fill="white")
    window.after_cancel(flip_fn)

def generate_data():
    global item
    item =choice(data_dict)
    canvas.itemconfig(card,image=card_front)
    canvas.itemconfig(title,text="French",fill="black")
    canvas.itemconfig(word,text=item["French"],fill="black")

    global flip_fn
    flip_fn=window.after(3000,func=flip)

def know():
    data_dict.remove(item)
    data_obj=pandas.DataFrame(data_dict)
    data_obj.to_csv("data/words_to_learn.csv",index=False)  # don't add index to output or it will each time we run the program
    generate_data()

window = Tk()
window.title("flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

card_front=PhotoImage(file="images/card_front.png")
card_back=PhotoImage(file="images/card_back.png")

canvas = Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
card=canvas.create_image(400,263,image=card_front)
title = canvas.create_text(400,150,text="title",font=("Arial",40,"italic"))
word = canvas.create_text(400,263,text="word",font=("Arial",60,"bold"))
canvas.grid(row=0,column=0,columnspan=2)

flip_fn=window.after(3000,flip)

right=PhotoImage(file="images/right.png")
right_button=Button(image=right,highlightthickness=0,border=0,command=know)
right_button.grid(row=1,column=1)
wrong=PhotoImage(file="images/wrong.png")
wrong_button=Button(image=wrong,highlightthickness=0,border=0,command=generate_data)
wrong_button.grid(row=1,column=0)

generate_data()

window.mainloop()
