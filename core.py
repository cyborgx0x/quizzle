from tkinter import *
from quiz import Quiz
from functools import partial

gui = Tk()
gui.title("QUIZ making fun")
gui.iconbitmap("logo.ico")
gui.geometry("800x450")

main = Frame(gui)
main.pack()

q = Quiz("What does the fox say?", "dig dig dig", *["nah", "no", "oh"], hint= "not true", full_solution="yes!!!")
title = Label(main, text=q.question)
title.pack()

for item in q.ans_bank:
    print(item, q.ans_bank[item])

select = StringVar()
select.set(0)

for item in q.ans_bank:
    a = Radiobutton(main, variable=item, text=q.ans_bank[item], value=item)
    a.pack(anchor=W)
    print(a, a.info())

answer = partial(q.answer, select.get())
button = Button(main, text="Answer", padx=20, pady=5, command=answer)
button.pack()

gui.mainloop()




