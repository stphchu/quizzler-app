from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
Q_FONT = ("Arial", 18, "italic")


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_text = Label(text=f"Score: {self.score} / {len(self.quiz.question_list)}", bg=THEME_COLOR,
                                fg="white", font=("Arial", 13, "normal"))
        self.score_text.grid(column=1, row=0)
        self.canvas = Canvas(height=250, width=300)
        self.current_q = self.canvas.create_text(150, 125, text=f"Question", font=Q_FONT, width=300)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_img = PhotoImage(file="images/true.png")
        false_img = PhotoImage(file="images/false.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.press_true)
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.press_false)
        self.true_button.grid(column=0, row=2)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.current_q, fill="black")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.score} / {len(self.quiz.question_list)}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.current_q, text=q_text)
        else:
            self.canvas.itemconfig(self.current_q, text=f"You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def press_true(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def press_false(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.canvas.itemconfig(self.current_q, fill="white")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
