from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

class Naipe(Label):
    def __init__(self, parent):
        self.load('2b.png')
        Label.__init__(self, image=self.photo)


    def load(self, img):
        self.sourceImg = Image.open("images/{}".format(img))
        self.photo = ImageTk.PhotoImage(self.sourceImg)


class Baraja(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'])
        self.naipe = Naipe(self)
        self.naipe.pack(side=TOP, fill=X)

class MainApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title('Baraja')
        self.geometry("{}x{}".format(410, 285))

        self.baraja = Baraja(self, width=150, height=200)
        self.baraja.place(x=0, y=0)

    def start(self):
        self.mainloop()

if __name__ == '__main__':
    app = MainApp()
    app.start()