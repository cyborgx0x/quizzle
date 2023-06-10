from tkinter import *
from tkinter import messagebox
gui = Tk()
gui.title("QUIZ making fun")
gui.iconbitmap("logo.ico")
gui.geometry("800x450")
gui.mainloop()

class Ui:
    def __init__(self, title, icon, size):
        self.main = Tk()
        self.main.title(title)
        self.main.iconbitmap(icon)
        self.main.geometry(size)
        self.node = {}
        pass
    def createElement(self, element):
        element = Frame(self.main)
        element.pack()
        pass