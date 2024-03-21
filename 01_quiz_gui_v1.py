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

    self.var_num1=IntVar()
    self.var_num1.set(0)
    self.var_num2=IntVar()
    self.var_num2=set(0)

    self.quiz_question = Label(self.quiz_frame,
                            text="{} + {} =".format(num1, num2),
                            font=("Helvetica", 16),
                            fg="#FFEE00")
    self.quiz_question.grid(row=2, padx=100, pady=15)

  def numbers(self):
    num_1=random.randint(1,10)
    num_2=random.randint(1,10)


# Main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Simple Math Quiz")
  root.mainloop()

  print(answer)