# šahovnica
# GUI: tukaj se zgolj riše in zaznava klike !!!


import tkinter as tk
import logika


def narisi_sahovnico(platno, velikost_polj, odmik):
    '''Nariše šahovnico 8d X 8d. Desno spodaj je belo polje.'''
    x1, y1 = odmik, odmik # določimo odmik
    for i in range(8): # vrstice
        for j in range(8): # stolpci
            barva = "white" if (i + j) % 2 == 0 else "gray"
            platno.create_rectangle(x1, y1, x1 + velikost_polj, y1 + velikost_polj, fill=barva, activefill="blue")
            x1 += velikost_polj # naslednji kvadratek v vrsti
        x1, y1 = odmik, odmik + velikost_polj * (i + 1) # premaknemo se eno vrstico navzdol



class Sahovnica:
    def __init__(self, master):
        # nastavitve velikosti
        self.velikost_polj = 110
        self.odmik = 80
        self.platno = tk.Canvas(master, width=self.velikost_polj * 10, height=self.velikost_polj * 10)
        self.platno.pack()

        šah = logika.Šah()
        self.IGRA = šah.IGRA
        
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
        x, y = self.odmik + 8 * self.velikost_polj / 2, self.odmik / 2
        self.platno.create_window(x, y, window=okvir_oznake, width = 140)

        self.začni_igro()


    def začni_igro(self):
        '''Prične igro.'''
        self.prikaz_figur()
  
        
    
    def klik(self, event):
        '''Zazna klik in to sporoči logiki igre.'''       
        # najprej pridobi koordinate
        vrstica = int((event.y - self.odmik) // self.velikost_polj)
        stolpec = int((event.x - self.odmik) // self.velikost_polj)
        stolpci = 'ABCDEFGH'
        if 0 <= stolpec <= 7 and 0 <= vrstica <= 7:  
            self.izpis_potez.set('Kliknil si na {}{}.'.format(stolpci[stolpec], 7 - vrstica + 1))
            print(stolpec, 7 - vrstica)

            # pobarvamo tisti stolpec


            # poda sporočilo logiki igre !!!
            # self.sah.odgovor_na_klik(i, j)

        # kar smo delali na vajah
        i, j = vrstica, stolpec
        self.oznaceno_polje = self.platno.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)[0]
        self.oznacena_figura = self.IGRA[i][j]
        print(self.oznacena_figura)
        if self.oznacena_figura is not None: # označimo figuo
            # pobarvamo polje z označeno figuro
            self.platno.itemconfig(self.oznaceno_polje, fill="blue")
            # sedaj se pozanimamo, kakšne poteze lahko opravi
        # ob naslednjem kliku (bodisi premik ali napačna izbira) nazaj nastavimo barvo polja





    def prikaz_figur(self):
        '''Na šahovnici prikaže figure.'''
        for i in range(8):
            for j in range(8):
                figura = self.IGRA[i][j]
                if figura is not None:
                    foto = figura.foto
                    x = self.odmik + (j * self.velikost_polj) + self.velikost_polj / 2
                    y = self.odmik + (i * self.velikost_polj) + self.velikost_polj / 2
                    self.platno.create_image(x, y, image=foto)


root = tk.Tk()

sah = Sahovnica(root)

root.mainloop()


