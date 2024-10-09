from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz
        self.window = Tk()
        self.title = self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR, padx=20, pady=20)

        self.score_label = Label(text="Score: 0", background=THEME_COLOR,  fg="white")
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=25)
        self.question_canvas = self.canvas.create_text(150, 125, width=280,font=("Arial", "20", "italic"),
                                                       text="Amazon acquired Twitch in August 2014 for"
                                                            " $970 million dollars")

        self.true_img = PhotoImage(file="images/true.png")
        self.false_img = PhotoImage(file="images/false.png")

        self.true_btn = Button(image=self.true_img, highlightthickness=0, border=0, cursor="hand2", command=self.true_check)
        self.false_btn = Button(image=self.false_img, highlightthickness=0, border=0, cursor="hand2", command=self.false_check)

        self.true_btn.grid(row=2, column=0)
        self.false_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_canvas, text=q_text)
        else:
            self.canvas.itemconfig(self.question_canvas, text="End of Quiz")
            self.true_btn.configure(state="disabled", cursor="circle")
            self.false_btn.configure(state="disabled", cursor="circle")



    def true_check(self):
        is_right = self.quiz_brain.check_answer("True")
        self.give_feedback(is_right)



    def false_check(self):
        is_right = self.quiz_brain.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)