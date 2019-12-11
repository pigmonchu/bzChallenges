from tkinter import *
from tkinter import ttk

_heightBtn = 50
_widthBtn = 68




class CalcButton(ttk.Frame):

    def __init__(self, parent, **kwargs):
        name = kwargs.get('id')
        ttk.Frame.__init__(self, parent, height=kwargs['height'], width=kwargs['width'], name=name)
        self.pack_propagate(0)

        self.__btn = ttk.Button(self, text=kwargs['text'], command=kwargs['command'])
        self.__btn.pack(fill=BOTH, expand=True)


class Display(ttk.Frame):
    
    def __init__(self, parent, **kwargs):
        name = kwargs.get('id')
        ttk.Frame.__init__(self, parent, height=50, width=272, name=name)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use('alt')
        s.configure('my.TLabel', font=('Helvetica 42'))
        self.__lbl = ttk.Label(self, text="Pantalla", style='my.TLabel', anchor=E, foreground="white",background="black")
        self.__lbl.pack(fill=BOTH, expand=True)

class Selector(ttk.Frame):
    def __init__(self, parent, **kwargs):
        name = kwargs.get('id')
        ttk.Frame.__init__(self, parent, height=50, width=58, name=name)
        self.value = StringVar()
        self.value.trace("w", self.selected)
        self.pack_propagate(0)

        self.command = kwargs.get('command')

        self.rbR = ttk.Radiobutton(self, command=lambda: self.command('R'), text='R', variable=self.value, value='R', name='optR')
        self.rbA = ttk.Radiobutton(self, command=lambda: self.command('A'), text='A', variable=self.value, value='A', name='optA')

        self.value.set('R')

        self.rbR.pack(fill=BOTH, side=TOP)
        self.rbA.pack(fill=BOTH, side=TOP)
    
    def selected(self, *args):
        self.command(self.value.get())
    

class Calculator(ttk.Frame):
    my_var = None
    layouts = {}
    selectedLayout = None

    def createRomanLayout(self):
        layoutRoman = ttk.Frame(self, name='layoutRoman')
        CalcButton(layoutRoman, text= 'C', command=None, height=_heightBtn, width=_widthBtn*3, id='btnRomanCan').grid(column=0, row=0, columnspan=3)
        CalcButton(layoutRoman, text='÷', command=None, height=_heightBtn, width=_widthBtn, id='btnRomanDiv').grid(column=3, row=0)

        CalcButton(layoutRoman, text='C', command=None, height=_heightBtn, width=_widthBtn, id='btnRomanC').grid(column=0, row=1)
        CalcButton(layoutRoman, text='D', command=None, height=_heightBtn, width=_widthBtn, id='btnRomanD').grid(column=1, row=1)
        CalcButton(layoutRoman, text='M', command=None, height=_heightBtn*3, width=_widthBtn, id='btnM').grid(column=2, row=1, rowspan=3)
        CalcButton(layoutRoman, text='x', command=None, height=_heightBtn, width=_widthBtn, id='btnMul').grid(column=3, row=1)

        CalcButton(layoutRoman, text='X', command=None, height=_heightBtn, width=_widthBtn, id='btnX').grid(column=0, row=2)
        CalcButton(layoutRoman, text='L', command=None, height=_heightBtn, width=_widthBtn, id='btnL').grid(column=1, row=2)
        CalcButton(layoutRoman, text='-', command=None, height=_heightBtn, width=_widthBtn, id='btnSub').grid(column=3, row=2)

        CalcButton(layoutRoman, text='I', command=None, height=_heightBtn, width=_widthBtn, id='btnI').grid(column=0, row=3)
        CalcButton(layoutRoman, text='V', command=None, height=_heightBtn, width=_widthBtn, id='btnV').grid(column=1, row=3)
        CalcButton(layoutRoman, text='+', command=None, height=_heightBtn, width=_widthBtn, id='btnAdd').grid(column=3, row=3)

        CalcButton(layoutRoman, text='=', command=None, height=_heightBtn, width=_widthBtn*2, id='btnEqu').grid(column=2, row=4, columnspan=2)
        return layoutRoman

    def createArabicLayout(self):
        layoutArabic = ttk.Frame(self, name='layoutArabic')
        CalcButton(layoutArabic, text= 'C', command=None, height=_heightBtn, width=_widthBtn, id='btnCan').grid(column=0, row=0)
        CalcButton(layoutArabic, text= '+/-', command=None, height=_heightBtn, width=_widthBtn, id='btnCSg').grid(column=1, row=0)
        CalcButton(layoutArabic, text= '%', command=None, height=_heightBtn, width=_widthBtn, id='btnPer').grid(column=2, row=0)
        CalcButton(layoutArabic, text='÷', command=None, height=_heightBtn, width=_widthBtn, id='btnDiv').grid(column=3, row=0)

        CalcButton(layoutArabic, text='7', command=None, height=_heightBtn, width=_widthBtn, id='btn7').grid(column=0, row=2)
        CalcButton(layoutArabic, text='8', command=None, height=_heightBtn, width=_widthBtn, id='btn8').grid(column=1, row=2)
        CalcButton(layoutArabic, text='9', command=None, height=_heightBtn, width=_widthBtn, id='btn9').grid(column=2, row=2)
        CalcButton(layoutArabic, text='x', command=None, height=_heightBtn, width=_widthBtn, id='btnMul').grid(column=3, row=2)

        CalcButton(layoutArabic, text='4', command=None, height=_heightBtn, width=_widthBtn, id='btn4').grid(column=0, row=3)
        CalcButton(layoutArabic, text='5', command=None, height=_heightBtn, width=_widthBtn, id='btn5').grid(column=1, row=3)
        CalcButton(layoutArabic, text='6', command=None, height=_heightBtn, width=_widthBtn, id='btn6').grid(column=2, row=3)
        CalcButton(layoutArabic, text='-', command=None, height=_heightBtn, width=_widthBtn, id='btnSub').grid(column=3, row=3)

        CalcButton(layoutArabic, text='1', command=None, height=_heightBtn, width=_widthBtn, id='btn1').grid(column=0, row=4)
        CalcButton(layoutArabic, text='2', command=None, height=_heightBtn, width=_widthBtn, id='btn2').grid(column=1, row=4)
        CalcButton(layoutArabic, text='3', command=None, height=_heightBtn, width=_widthBtn, id='btn3').grid(column=2, row=4)
        CalcButton(layoutArabic, text='+', command=None, height=_heightBtn, width=_widthBtn, id='btnAdd').grid(column=3, row=4)

        CalcButton(layoutArabic, text='0', command=None, height=_heightBtn, width=_widthBtn, id='btn0').grid(column=1, row=5)
        CalcButton(layoutArabic, text=',', command=None, height=_heightBtn, width=_widthBtn, id='btnPoi').grid(column=2, row=5)
        CalcButton(layoutArabic, text='=', command=None, height=_heightBtn, width=_widthBtn, id='btnEqu').grid(column=3, row=5)
        return layoutArabic

    def selectLayout(self, key):
        if self.selectedLayout:
            self.selectedLayout.grid_forget()

        self.selectedLayout = self.layouts.get(key)
        if self.selectedLayout:
            self.selectedLayout.grid(column=0, row=1, columnspan=4, rowspan=5)

    def __init__(self, parent, id=None):
        ttk.Frame.__init__(self, parent, name=id)

        self.__display = Display(self, id='disp')
        self.__display.grid(row=0, column=0, columnspan=4)

        self.layouts['R'] = self.createRomanLayout()
        self.layouts['A'] = self.createArabicLayout()
        self.selectLayout('R')

        Selector(self, command=self.selectLayout, id='sel').grid(column=0, row=5, sticky=W+S, padx=5)

