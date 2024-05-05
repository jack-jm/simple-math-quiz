from tkinter import *
import random


class Quiz:

  def __init__(self):

    # Setting up the GUI frame, grid and background colour
    self.quiz_frame = Frame()
    self.quiz_frame.grid()
    self.quiz_frame.configure(bg="#1BA1E2")

    # Creating numbers 1 and 2, which will both be random between 1 and 10
    # and be either added or subtracted
    self.num1 = random.randint(1, 10)
    self.num2 = random.randint(1, 10)
    # List of possible operations
    self.operation_list = ["+", "-"]
    # Randomly picking one operation to be used
    self.operation = self.operation_list[random.randint(0, 1)]

    # Creating the main title and giving its position
    self.quiz_title = Label(self.quiz_frame,
                            text="Simple Math Quiz",
                            font=("Helvetica", 20, "bold"),
                            fg="#FFFFFF",
                            bg="#1BA1E2")
    self.quiz_title.grid(row=0, padx=70, pady=15)

    # Instructions for the user to read
    instructions = ("Welcome to Simple Math Quiz!\n\n" \
                    "To start solving some math problems, simply " \
                    "type your answer into the text box and press " \
                    "'Submit' when you're sure.\n\n"
                    "After you've answered all the questions you want " \
                    "to, press 'Results' to see how many you got correct.")

    # Creating instructions label and giving its position
    self.quiz_instructions = Label(self.quiz_frame,
                                   text=instructions,
                                   wraplength=400,
                                   font=("Helvetica", 12),
                                   fg="#FFFFFF",
                                   bg="#1BA1E2")
    self.quiz_instructions.grid(row=1, padx=70, pady=15)

    # Creating question text, which will include num1, num2, and operation
    self.quiz_question = Label(self.quiz_frame,
                               text="{} {} {} =".format(self.num1, self.operation, self.num2),
                               font=("Helvetica", 30, "bold"),
                               fg="#FFEE00",
                               bg="#1BA1E2")
    self.quiz_question.grid(row=2, padx=70, pady=15)

    # Creating entry box for the user to input their guess
    self.answer_entry = Entry(self.quiz_frame, font=("Helvetica", 24))
    self.answer_entry.grid(row=3, padx=10, pady=10)

    # Creating feedback message label to tell the user 
    # if they are correct, incorrect, or have an error.
    self.feedback_message = Label(self.quiz_frame,
                                  text="",
                                  font=("Helvetica", 14, "bold"),
                                  fg="#FFEE00",
                                  bg="#1BA1E2")
    self.feedback_message.grid(row=4)

    # Creating a new frame for the two buttons called button frame
    self.button_frame = Frame(self.quiz_frame)
    self.button_frame.grid(row=5)
    self.button_frame.configure(bg="#1BA1E2")

    # Creating submit button that will go to check_input
    self.submit_button = Button(self.button_frame,
                                text="Submit",
                                font=("Helvetica", 24, "bold"),
                                fg="#FFFFFF",
                                bg="#E11584",
                                command=self.check_input)
    self.submit_button.grid(row=0, column=0, padx=10, pady=10)

    # Creating results button which is currently not being used
    self.results_button = Button(self.button_frame,
                                 text="Results",
                                 font=("Helvetica", 24, "bold"),
                                 fg="#FFFFFF",
                                 bg="#008A00",
                                 state=DISABLED,
                                 command=self.to_results)
    self.results_button.grid(row=0, column=1, padx=10, pady=10)

  # This function will check that the user has entered an integer
  def check_input(self):
    # Try and see if the guess was an integer then try to go to correct_incorrect function
    try:
      self.guess = int(self.answer_entry.get())
      self.results_button.config(state=NORMAL)
      self.correct_incorrect()
    # If there is a value error, change the feedback message to an error message
    except ValueError:
      self.feedback_message.config(text="Please enter an integer as your answer.")
      self.feedback_message.config(fg="#b22222")
    # This clears the entry box for the next question
    self.answer_entry.delete(0, "end")

  # This function will see if the guess was the correct answer or not.
  def correct_incorrect(self):
    # If operation is plus, correct answer is num1 + num2
    if self.operation == "+":
      correct_answer = self.num1 + self.num2
    # If operation is minus, correct answer is num1 - num2
    else:
      correct_answer = self.num1 - self.num2
    # If the guess is the correct answer, tell the user they are correct
    if self.guess == correct_answer:
      self.feedback_message.config(text="Correct!")
      self.feedback_message.config(fg="#00FF00")
    # Otherwise, tell them they are incorrect
    else:
      self.feedback_message.config(text="Incorrect: the answer was {}.".format(correct_answer))
      self.feedback_message.config(fg="#b22222")
    # Whether or not they are correct, send them to generate_nums function
    self.generate_nums()

  # This function will generate two new random numbers into num1
  # and num2 for the next question
  def generate_nums(self):
    # num1 and num2 equal a new random number between 1 and 10
    self.num1 = random.randint(1, 10)
    self.num2 = random.randint(1, 10)
    # operation equals a new random operation
    self.operation = self.operation_list[random.randint(0, 1)]
    # Configure the question text with the new numbers and new operation
    self.quiz_question.config(text="{} {} {} =".format(self.num1, self.operation, self.num2))

  def to_results(self):
    # Go to the results class
    Results(self)

class Results:

  def __init__(self, partner):
    # Creating the results box
    self.results_box = Toplevel()

    # Disable the results button on the main quiz so no more windows can be created
    partner.results_button.config(state=DISABLED)

    # Creating results frame
    self.results_frame = Frame(self.results_box, bg="#60A917")
    self.results_frame.grid()

    # Creating the heading for the results page
    self.results_heading = Label(self.results_frame,
                                 bg="#60A917",
                                 fg= "#FFFFFF",
                                 text="Results",
                                 font=("Helvetica", 20, "bold"))
    self.results_heading.grid(row=0)

    # Main results text to be shown
    results_text = "\nWell done!\n\n" \
                   "You answered _ out of _ questions correctly.\n\n" \
                   "That's _%!\n\n" \
                   "Play again soon to try for an even better score!\n\n" \
                   "If you want to view your results and all the answers you\n" \
                   "gave, you can export a text file " \
                   "by pressing 'Export'.\n\n" \
                   "Otherwise, you can close this menu with 'Close'.\n"

    # Creating results text label
    self.results_text_label = Label(self.results_frame,
                                    bg="#60A917",
                                    fg= "#FFFFFF",
                                    text=results_text,
                                    font=("Helvetica", 11))
    self.results_text_label.grid(row=1, padx=10)

    # Creating the entrybox for the filename
    self.results_filename_entry = Entry(self.results_frame, font=("Helvetica", 24))
    self.results_filename_entry.grid(row=2, padx=40, pady=10)

    # Creating the feedback message
    self.results_feedback_message = Label(self.results_frame,
                                          bg="#60A917",
                                          fg="#FFFFFF",
                                          text="This is a placeholder",
                                          font=("Helvetica", 14, "bold"))
    self.results_feedback_message.grid(row=3)

    # Creating the frame for the buttons
    self.results_button_frame = Frame(self.results_frame)
    self.results_button_frame.grid(row=4)
    self.results_button_frame.configure(bg="#60A917")

    # Creating export button
    self.export_button = Button(self.results_button_frame,
                                text="Export",
                                font=("Helvetica", 24, "bold"),
                                fg="#FFFFFF",
                                bg="#E11584")
    self.export_button.grid(row=0, column=0, padx=10, pady=10)

    # Creating close button
    self.close_button = Button(self.results_button_frame,
                               text="Close",
                               font=("Helvetica", 24, "bold"),
                               fg="#FFFFFF",
                               bg="#1BA1E2")
    self.close_button.grid(row=0, column=1, padx=10, pady=10)


# Main routine
if __name__ == "__main__":
  root = Tk()
  root.title("Simple Math Quiz")
  Quiz()
  root.mainloop()