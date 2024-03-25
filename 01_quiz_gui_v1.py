from tkinter import *
import random

class Quiz:
  def __init__(self):

    # Setting up the GUI
    self.quiz_frame = Frame()
    self.quiz_frame.grid()

    self.quiz_title = Label(self.quiz_frame,
                            text="Simple Math Quiz",
                            font=("Helvetica", 20, "bold"),
                            fg="#FFFFFF")
    self.quiz_title.grid(row=0, padx=100, pady=15)

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
                            fg="#FFFFFF")
    self.quiz_instructions.grid(row=1, padx=100, pady=15)

    self.quiz_question = Label(self.quiz_frame,
                            text="",
                            font=("Helvetica", 16),
                            fg="#FFEE00")
    self.quiz_question.grid(row=2, padx=100, pady=15)

    self.submit_button = Button(self.quiz_frame,
                                text="Submit",
                                font=("Helvetica", 16),
                                fg="#FFFFFF", bg="#E11584",
                                command=self.generate_nums)
    self.submit_button.grid(row=3)

  def generate_nums(self):
    nums_list = [0, 0]
    nums_list[0]=random.randint(1,10)
    nums_list[1]=random.randint(1,10)
    question_text="{} + {} =".format(nums_list[0], nums_list[1])
    self.quiz_question.config(text=question_text)


 # Main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Simple Math Quiz")
  Quiz()
  root.mainloop()