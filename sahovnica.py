# šahovnica
import tkinter as tk
# from figure import *

def narisi_sahovnico(platno, d, odmik):
    '''Nariše šahovnico 8d X 8d. Desno spodaj je belo polje.'''
    x1, y1 = odmik, odmik
    for i in range(8): # vrstice
        for j in range(8): # stolpci
            barva = "white" if (i + j) % 2 == 0 else "black"
            platno.create_rectangle(x1, y1, x1 + d, y1 + d, fill = barva)
            x1 += d # naslednji kvadratek v vrsti
        x1, y1 = odmik, odmik * (i + 2) # premaknemo se eno vrstico navzdol



class Sahovnica:
    def __init__(self, master, polozaj_belih, polozaj_crnih):
        self.velikost = 800
        self.odmik = self.velikost / 10
        self.velikost_polj = self.velikost / 10
        self.platno = tk.Canvas(master, width=self.velikost, height=self.velikost)
        self.platno.pack()

        # bele figure
        K = Kralj('b')
        D = Dama('b')
        T1 = Trdnjava('b')
        T2 = Trdnjava('b')
        L1 = Lovec('b')
        L2 = Lovec('b')
        S1 = Konj('b')
        S2 = Konj('b')
        k1, k2, k3, k4, k5, k6, k7, k8 = Kmet('b'), Kmet('b'), Kmet('b'), Kmet('b'), Kmet('b'), Kmet('b'), Kmet('b'), Kmet('b') # kako bi to naredili z zanko ?

        # črne figure
        K_ = Kralj('č', self.IGRA)
        D_ = Dama('č')
        T1_ = Trdnjava('č')
        T2_ = Trdnjava('č')
        L1_ = Lovec('č')
        L2_ = Lovec('č')
        S1_ = Konj('č')
        S2_ = Konj('č')
        k1_, k2_, k3_, k4_, k5_, k6_, k7_, k8_ = Kmet('č'), Kmet('č'), Kmet('č'), Kmet('č'), Kmet('č'), Kmet('č'), Kmet('č'), Kmet('č')

        # imamo trenutno pozicijo
        self.IGRA = [
            [T1_ , S1_ , L1_ , D_  , K_  , L2_ , S_2 , T2_ ],
            [k1_ , k2_ , k3_ , k4_ , k5_ , k6_ , k7_ , k8_ ],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [k1  , k2  , k3  , k4  , k5  , k6  , k7  , k8  ],
            [T1  , S1  , L1  , D   , K   , L2  , S2  , T2  ]]

        # matrika je zaradi rekonstrukcije, zato da programer vidi, kaj se dogaja
        # IGRA v logiki
        # najprej spremeniš v logiki, nato sporočiš GUI, da nariše drugam
        # class Figura: x, y, barva -> kar je skupno vsem figuram
        # class Kmet(Figura): mozne poteze, slika


        # narišemo šahovnico
        narisi_sahovnico(self.platno, self.velikost_polj, self.odmik)

        # registriramo se za klike z miško
        self.platno.bind('<Button-1>', self.katero_polje)

        # naredimo oznako za izpisovanje
        okvir_oznake = tk.LabelFrame(self.platno)
        okvir_oznake.pack() 
        self.izpis_potez = tk.StringVar(value='klikni nekam')
        oznaka_izpis_potez = tk.Label(okvir_oznake, textvariable=self.izpis_potez)
        oznaka_izpis_potez.pack()
        self.platno.create_window(self.velikost / 2, 20, window=okvir_oznake, width = 140)

    
        

    def katero_polje(self, event):
        '''Vrne koordinate polja, v katerega je uporabnik kliknil.'''
        stolpec = int((event.x - self.odmik) // self.velikost_polj)
        vrstica = 7 - int((event.y - self.odmik) // self.velikost_polj)
        stolpci = 'ABCDEFGH'
        if 0 <= stolpec <= 7 and 0 <= vrstica <= 7:  
            self.izpis_potez.set('Kliknil si na {}{}.'.format(stolpci[stolpec], vrstica + 1))
            print(stolpec, vrstica)
            return (stolpec, vrstica) # npr (0, 0)
    
            
        








root = tk.Tk()

sah = Sahovnica(root, [], [])

root.mainloop()


