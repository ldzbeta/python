from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class QuizInterface:
    # to access the methods/ functions of quiz brain we have to specify the quiz_brain is passed in QuizBrain type    
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz=quiz_brain
        self.window= Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        self.canvas = Canvas(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,text="title",fill=THEME_COLOR,font=("Arial",20,"italic"),width=280) #specify width to wrap the text
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.score_label=Label(text="Score : 0",bg=THEME_COLOR,highlightthickness=0,fg="white")
        self.score_label.grid(row=0,column=1)

        correct_img=PhotoImage(file="images/true.png")
        self.correct_button = Button(image=correct_img,highlightthickness=0,command=self.check_true)
        self.correct_button.grid(row=2,column=1)
        wrong_img=PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=wrong_img,highlightthickness=0,command=self.check_false)
        self.wrong_button.grid(row=2,column=0)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.itemconfig(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.itemconfig(self.question_text,text=self.quiz.next_question())
            self.score_label.config(text=f"Score : {self.quiz.score}")
        else:
            self.canvas.itemconfig(self.question_text,text="You have reached end of the quiz.")
            self.correct_button.config(state="disabled") #command will not work
            self.wrong_button.config(state="disabled") 


    def check_true(self):
        self.give_feedback(self.quiz.check_answer(True))

    def check_false(self):
        self.give_feedback(self.quiz.check_answer(False))
  
    def give_feedback(self,is_right):
        if is_right:
            self.canvas.itemconfig(bg="green")
        else:
            self.canvas.itemconfig(bg="red")
        
        self.window.after(1000,self.get_next_question)

        
            