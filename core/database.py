import os, sys
from quiz.quiz import Quiz
from core.models import Quizbank, session

class Question(Quiz):
    def insert_post(question,solution,other_answer_1, other_answer_2, other_answer_3,hint,full_solution):
        newpost = Quizbank(question=question, solution=solution, other_answer_1=other_answer_1,other_answer_2=other_answer_2,other_answer_3=other_answer_3, hint=hint, full_solution=full_solution )
        session.add(newpost)
        session.commit()  

    def delete_all_post():
        selected = session.query(Quizbank).all()
        for i in selected:
            session.delete(i)
        session.commit()
    def view_all_post():
        selected = session.query(Quizbank).all()
        for i in selected:
            yield i
