from tkinter import *
import random

class Quiz:
  def __init__(self):

    # Setting up the GUI
    self.quiz_frame = Frame()
    self.quiz_frame.grid()
    self.quiz_frame.configure(bg="#1BA1E2")

    self.quiz_title = Label(self.quiz_frame,
                            text="Simple Math Quiz",
                            font=("Helvetica", 20, "bold"),
                            fg="#FFFFFF", bg="#1BA1E2")
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
                            fg="#FFFFFF", bg="#1BA1E2")
    self.quiz_instructions.grid(row=1, padx=70, pady=15)

    self.quiz_question = Label(self.quiz_frame,
                            text="{} + {} =".format(random.randint(1,10), random.randint(1,10)),
                            font=("Helvetica", 30, "bold"),
                            fg="#FFEE00", bg="#1BA1E2")
    self.quiz_question.grid(row=2, padx=70, pady=15)

    self.answer_entry = Entry(self.quiz_frame,
                            font=("Helvetica", 24)
                            )
    self.answer_entry.grid(row=3, padx=10, pady=10)

    self.feedback_message = Label(self.quiz_frame,
                                 text="This is a placeholder",
                                 font=("Helvetica", 14, "bold"),
                                 fg="#FFEE00", bg="#1BA1E2")
    self.feedback_message.grid(row=4)

    self.button_frame = Frame(self.quiz_frame)
    self.button_frame.grid(row=5)
    self.button_frame.configure(bg="#1BA1E2")
    
    self.submit_button = Button(self.button_frame,
                                text="Submit",
                                font=("Helvetica", 24, "bold"),
                                fg="#FFFFFF", bg="#E11584",
                                command=self.check_input)
    self.submit_button.grid(row=5, column=0, padx=10, pady=10)

    self.results_button = Button(self.button_frame,
                                text="Results",
                                font=("Helvetica", 24, "bold"),
                                fg="#FFFFFF", bg="#008A00")
    self.results_button.grid(row=5, column=1, padx=10, pady=10)

  def check_input(self):
    response = self.answer_entry.get()

    try:
      guess = int(response)
    except ValueError:
      self.feedback_message.config(text="Please enter an integer as your answer.")
      self.feedback_message.config(fg="#FF0000")

    if self.feedback_message.cget("text") != "Please enter an integer as your answer.":
      self.generate_nums()
    

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