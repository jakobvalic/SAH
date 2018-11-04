import tkinter
from tkinter import ttk


class Promocija(tkinter.Toplevel, object):
    def __init__(self, parent):
        self.figura = None
        tkinter.Toplevel.__init__(self, parent)
        frame = tkinter.Frame(self)
        frame.pack()
        c1 = ttk.Button(self, text = 'Dama', command = self.kraljica)
        c1.pack()

        c2 = ttk.Button(self, text = 'Konj', command = self.konj)
        c2.pack()

        c3 = ttk.Button(self, text = 'Trdnjava', command = self.trdnjava)
        c3.pack()

        c4 = ttk.Button(self, text = 'Lovec', command = self.lovec)
        c4.pack()
        
        self.transient(parent)
        self.title("Dialog")
        self.focus_force
        self.grab_set()

        self.protocol("WM_DELETE_WINDOW", self.destroy)

    def kraljica(self):
        self.figura = 'kraljica'
        self.grab_release()
        self.destroy()

    def konj(self):
        self.figura = 'konj'
        self.grab_release()
        self.destroy()

    def trdnjava(self):
        self.figura = 'trdnjava'
        self.grab_release()
        self.destroy()

    def lovec(self):
        self.figura = 'lovec'
        self.grab_release()
        self.destroy()

