from tkinter import *
THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self):
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250)
        self.canvas.create_text(150,125,text="title",font=("Arial",20,"italic"))

        score_label=Label(text="Score :",bg=THEME_COLOR,highlightthickness=0,fg="white")
        score_label.grid(row=0,column=1)

        correct_img=PhotoImage("images/true.png")
        correct_button = Button(image=correct_img)
        correct_button.grid(row=2,column=1)
        wrong_img=PhotoImage("images/false.png")
        wrong_button = Button(image=wrong_img)
        wrong_button.grid(row=2,column=0)

        self.window.mainloop()