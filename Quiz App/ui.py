import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Label
        self.score_label = Label(text=f"Score: {self.quiz.score}",
                                 bg=THEME_COLOR, fg="white")
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="Some question text",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        # Butoon
        true_image = PhotoImage(file='images/true.png')
        false_image = PhotoImage(file='images/false.png')
        self.true_button = Button(image=true_image,
                                  highlightthickness=0, command=self.hit_true)
        self.false_button = Button(image=false_image,
                                   highlightthickness=0, command=self.hit_false)
        self.true_button.grid(row=2, column=0)
        self.false_button.grid(row=2, column=1)

        # Init question
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def hit_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def hit_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)
