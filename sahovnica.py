# šahovnica
import tkinter as tk

def narisi_sahovnico(platno, d):
    '''Nariše šahovnico 8d X 8d. Desno spodaj je belo polje.'''
    odmik = d
    x1, y1 = odmik, odmik
    for i in range(8): # vrstice
        for j in range(8): # stolpci
            barva = "white" if (i + j) % 2 == 0 else "black"
            print(i, j)
            platno.create_rectangle(x1, y1, x1 + d, y1 + d, fill = barva)
            x1 += d # naslednji kvadratek v vrsti
        x1, y1 = odmik, odmik * (i + 2) # premaknemo se eno vrstico navzdol



class Sahovnica:
    def __init__(self, master, polozaj_belih, polozaj_crnih):
        self.velikost = 800
        self.platno = tk.Canvas(master, width=self.velikost, height=self.velikost)
        self.platno.pack()

        # narišemo šahovnico
        narisi_sahovnico(self.platno, self.velikost / 10)

        # registriramo se za klike z miško
        self.platno.bind('<Button-1>', command=katero_polje)
        

    def katero_polje(self, event):
        '''Vrne koordinate polja, v katerega je uporabnik kliknil.'''
        
            
        








root = tk.Tk()

sah = Sahovnica(root, [], [])

root.mainloop()


