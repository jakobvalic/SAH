from tkinter import *
from tkinter import ttk

class Promocija():
    def __init__(self,sah):
        self.sah=sah
        self.gui= Toplevel()
        self.gui.title("Promocija")
        self.gui.attributes("-topmost", True)
        self.log = None
        frame = Frame(self.gui)
        frame.pack()

        c1 = ttk.Button(self.gui, text = 'Dama', command = self.kraljica)
        c1.pack()

        c2 = ttk.Button(self.gui, text = 'Konj', command = self.konj)
        c2.pack()

        c3 = ttk.Button(self.gui, text = 'Trdnjava', command = self.trdnjava)
        c3.pack()

        c4 = ttk.Button(self.gui, text = 'Lovec', command = self.lovec)
        c4.pack()

    def kraljica(self):
        self.sah.log = 'dama'
        self.gui.destroy()

    def konj(self):
        self.sah.log = 'konj'
        self.gui.destroy()

    def trdnjava(self):
        self.sah.log = 'trdnjava'
        self.gui.destroy()

    def lovec(self):
        self.sah.log = 'lovec'
        self.gui.destroy()

