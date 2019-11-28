from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68


class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Roman Calculator")
        self.geometry("{}x{}".format(_widthBtn*4, _heightBtn*6))

    def start(self):
        self.mainloop()    

if __name__ == '__main__':
    app = MainApp()
    app.start()