import random
from tkinter import BooleanVar
  

class Quiz:
    """
    Generate the question
    """
    def __init__(self, question, solution, *arg, hint, full_solution):
        self.question = question
        self.solution = solution
        self.other_answer = arg
        self.hint = hint
        self.full_solution = full_solution
        self.ans_bank = self.generate()

    def answer(self, choice):
        print(choice)
        key_to_compare = choice.upper()
        if key_to_compare in self.ans_bank and self.ans_bank[key_to_compare] == self.solution:
            print(self.full_solution)
            return "You Should Try Again"
        else: 
            print(self.hint)
            return "Correct"

    def generate(self):
        answer_bank = [self.solution, *self.other_answer]
        answer_bank = random.sample(answer_bank,4)
        key_answer = ["A","B","C","D"]
        show = dict(zip(key_answer,answer_bank))
        return show

