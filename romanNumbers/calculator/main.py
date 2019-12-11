from tkinter import *
from tkinter import ttk

from calculator import _widthBtn, _heightBtn, Calculator

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Roman Calculator")
        self.geometry("{}x{}".format(_widthBtn*4, _heightBtn*6))

        self.calculator = Calculator(self, height=_heightBtn*6, width=_widthBtn*4)
        self.calculator.place(x=0, y=0)

    def start(self):
        self.mainloop()    

if __name__ == '__main__':
    app = MainApp()
    app.start()