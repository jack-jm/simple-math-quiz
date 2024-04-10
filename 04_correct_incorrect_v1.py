from tkinter import *
import random


class Quiz:

  def __init__(self):

    # Setting up the GUI
    self.quiz_frame = Frame()
    self.quiz_frame.grid()
    self.quiz_frame.configure(bg="#1BA1E2")

    self.num1 = random.randint(1, 10)
    self.num2 = random.randint(1, 10)

    self.quiz_title = Label(self.quiz_frame,
                            text="Simple Math Quiz",
                            font=("Helvetica", 20, "bold"),
                            fg="#FFFFFF",
                            bg="#1BA1E2")
    self.quiz_title.grid(row=0, padx=70, pady=15)

    instructions = ("Welcome to Simple Math Quiz!\n\n" \
                    "To start solving some math problems, simply " \
                    "type your answer into the text box and press " \
                    "'Submit' when you're sure.\n\n"
                    "After you've answered all the questions you want " \
                    "to, press 'Results' to see how many you got correct.")

    self.quiz_instructions = Label(self.quiz_frame,
                                   text=instructions,
                                   wraplength=400,
                                   font=("Helvetica", 12),
                                   fg="#FFFFFF",
                                   bg="#1BA1E2")
    self.quiz_instructions.grid(row=1, padx=70, pady=15)

    self.quiz_question = Label(self.quiz_frame,
                               text="{} + {} =".format(self.num1, self.num2),
                               font=("Helvetica", 30, "bold"),
                               fg="#FFEE00",
                               bg="#1BA1E2")
    self.quiz_question.grid(row=2, padx=70, pady=15)

    self.answer_entry = Entry(self.quiz_frame, font=("Helvetica", 24))
    self.answer_entry.grid(row=3, padx=10, pady=10)

    self.feedback_message = Label(self.quiz_frame,
                                  text="This is a placeholder",
                                  font=("Helvetica", 14, "bold"),
                                  fg="#FFEE00",
                                  bg="#1BA1E2")
    self.feedback_message.grid(row=4)

    self.button_frame = Frame(self.quiz_frame)
    self.button_frame.grid(row=5)
    self.button_frame.configure(bg="#1BA1E2")

    self.submit_button = Button(self.button_frame,
                                text="Submit",
                                font=("Helvetica", 24, "bold"),
                                fg="#FFFFFF",
                                bg="#E11584",
                                command=self.check_input)
    self.submit_button.grid(row=5, column=0, padx=10, pady=10)

    self.results_button = Button(self.button_frame,
                                 text="Results",
                                 font=("Helvetica", 24, "bold"),
                                 fg="#FFFFFF",
                                 bg="#008A00")
    self.results_button.grid(row=5, column=1, padx=10, pady=10)

  def check_input(self):
    try:
      self.guess = int(self.answer_entry.get())
      self.correct_incorrect()
    except ValueError:
      self.feedback_message.config(text="Please enter an integer as your answer.")
      self.feedback_message.config(fg="b22222")

  def correct_incorrect(self):
    correct_answer = self.num1 + self.num2
    if self.guess == correct_answer:
      self.feedback_message.config(text="Correct!")
      self.feedback_message.config(fg="#00FF00")
    else:
      self.feedback_message.config(text="Incorrect: the answer was {}.".format(correct_answer))
      self.feedback_message.config(fg="#b22222")
    self.generate_nums()

  def generate_nums(self):
    self.num1 = random.randint(1, 10)
    self.num2 = random.randint(1, 10)
    self.quiz_question.config(text="{} + {} =".format(self.num1, self.num2))

# Main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Simple Math Quiz")
  Quiz()
  root.mainloop()
