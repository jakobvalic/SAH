# šahovnica
# GUI: tukaj se zgolj riše in zaznava klike !!!


import tkinter as tk

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
    def __init__(self, master, IGRA):
        # nastavitve velikosti
        self.velikost = 800
        self.odmik = self.velikost / 10
        self.velikost_polj = self.velikost / 10
        self.platno = tk.Canvas(master, width=self.velikost, height=self.velikost)
        self.platno.pack()


        self.sah = fig.Sah()
        self.IGRA = self.sah.IGRA
        
        self.oznacena_figura = None


        # PRIPOROČILA PROFESORJA:
        # matrika je zaradi rekonstrukcije, zato da programer vidi, kaj se dogaja
        # IGRA v logiki
        # najprej spremeniš v logiki, nato sporočiš GUI, da nariše drugam
        # class Figura: x, y, barva -> kar je skupno vsem figuram
        # class Kmet(Figura): mozne poteze, slika


        # narišemo šahovnico
        narisi_sahovnico(self.platno, self.velikost_polj, self.odmik)

        # registriramo se za klike z miško
        self.platno.bind('<Button-1>', self.klik)

        # naredimo oznako za izpisovanje
        okvir_oznake = tk.LabelFrame(self.platno)
        okvir_oznake.pack() 
        self.izpis_potez = tk.StringVar(value='klikni nekam')
        oznaka_izpis_potez = tk.Label(okvir_oznake, textvariable=self.izpis_potez)
        oznaka_izpis_potez.pack()
        self.platno.create_window(self.velikost / 2, 20, window=okvir_oznake, width = 140)

    def začni_igro(self):
        '''Prične igro.'''
  
        
    

    def klik(self, event):
        '''Zazna klik in to sporoči logiki igre.'''       
        # najprej pridobi koordinate
        i = int((event.y - self.odmik) // self.velikost_polj) # vrstica
        j = int((event.x - self.odmik) // self.velikost_polj) # stolpec
        stolpci = 'ABCDEFGH'
        if 0 <= stolpec <= 7 and 0 <= vrstica <= 7:  
            self.izpis_potez.set('Kliknil si na {}{}.'.format(stolpci[stolpec], 7 - vrstica + 1))
            print(stolpec, 7 - vrstica)
            # poda sporočilo logiki igre !!!
            self.sah.odgovor_na_klik(i, j)

        
        

            
            
            
            
        




    def prikaz_figur(self):
        '''Na šahovnici prikaže figure.'''
        for i in range(8):
            for j in range(8):
                figura = self.IGRA[i][j]
                if figura is not None:
                    # jo narišemo
                    slika = figura.photo #  kmet = tk.Image.open("kmet.png")
                                         #  figura.photo = ImageTk.PhotoImage(kmet)
                    self.platno.place(x=10, y=20) # tu izračunamo x in y koordinate glede na polje, v katerem se nahajamo
    
            
root = tk.Tk()

sah = Sahovnica(root)

root.mainloop()


