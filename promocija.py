from tkinter import *
from tkinter import ttk

class Promocija():
    def __init__(self):
        self.gui= Toplevel()
        self.gui.title("Promocija")
        self.gui.attributes("-topmost", True)
        frame = Frame(self.gui)
        frame.pack()
        self.figura = None
        self.prvic = False

        c1 = ttk.Button(self.gui, text = 'Dama', command = self.kraljica)
        c1.pack()

        c2 = ttk.Button(self.gui, text = 'Konj', command = self.konj)
        c2.pack()

        c3 = ttk.Button(self.gui, text = 'Trdnjava', command = self.trdnjava)
        c3.pack()

        c4 = ttk.Button(self.gui, text = 'Lovec', command = self.lovec)
        c4.pack()

    def kraljica(self):
        self.figura = 'kraljica'
        self.prvic = True
        self.gui.destroy()

    def konj(self):
        self.figura = 'konj'
        self.prvic = True
        self.gui.destroy()

    def trdnjava(self):
        self.figura = 'trdnjava'
        self.prvic = True
        self.gui.destroy()

    def lovec(self):
        self.figura = 'lovec'
        self.prvic = True
        self.gui.destroy()

