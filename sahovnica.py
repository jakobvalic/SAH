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
    print("RAZRED ŠAHOVNICA")

    def __init__(self, master):
        # nastavitve velikosti
        self.velikost_polj = 110
        self.odmik = 80
        self.platno = tk.Canvas(master, width=self.velikost_polj * 10, height=self.velikost_polj * 10)
        self.platno.pack()

        self.sah = logika.Šah()
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
        x, y = self.odmik + 8 * self.velikost_polj / 2, self.odmik / 2
        self.platno.create_window(x, y, window=okvir_oznake, width = 140)

        self.začni_igro()


    def klik(self, event):
        '''Zazna klik in to sporoči logiki igre.'''



        # najprej pridobi koordinate
        i = int((event.y - self.odmik) // self.velikost_polj) # vrstica
        j = int((event.x - self.odmik) // self.velikost_polj) # stolpec

        stolpci = 'ABCDEFGH'
        if 0 <= i <= 7 and 0 <= j <= 7:
            self.izpis_potez.set('Kliknil si na {}{}.'.format(stolpci[j], 7 - i + 1))
            # poda sporočilo logiki igre !!!
            # self.sah.odgovor_na_klik(i, j)


        if self.oznacena_figura is None:
            # jo označimo
            if self.IGRA[i][j] is not None: # nismo kliknili 'v prazno':
                self.oznacena_figura = self.IGRA[i][j]
                # sedaj tudi pobarvamo polje z označeno figuro
                self.oznaceno_polje = self.platno.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)[0]
                self.platno.itemconfig(self.oznaceno_polje, fill="blue")
                self.oznacena_figura = self.IGRA[i][j]
                # povemo logiki, katero figuro smo označili; logika vrne možne poteze in pokliče metodo za barvanje kvadratkov

        else:
            # ponastavimo barvo polja :)
            barva_polja = "white" if (i + j) % 2 == 1 else "gray"
            self.platno.itemconfig(self.oznaceno_polje, fill=barva_polja)
            if (i, j) in self.sah.dovoljene_poteze:
                # sporočimo logiki, da se je nekaj spremenilo
                self.sah.premakni_figuro(self.oznacena_figura, i, j)
                # pobrišemo prejšnjo sliko figure


                # premaknemo sliko figure na novi koordinati
                x = self.odmik + (j * self.velikost_polj) + self.velikost_polj / 2 # centriramo klik
                y = self.odmik + (i * self.velikost_polj) + self.velikost_polj / 2
                # če je na polju kakšna druga figura, jo 'pojemo'
                if self.IGRA[i][j] is not None:
                    nasprotna_figura = self.IGRA[i][j]
                    id_slike = nasprotna_figura.id_slike
                    self.platno.delete(id_slike)
                # narišemo novo sliko in shranimo nov id_slike
                foto = self.oznacena_figura.foto
                id_slike = self.platno.create_image(x, y, image=foto)
                self.oznacena_figura.id_slike = id_slike

            # odznačimo figuro
            self.oznacena_figura = None





        # kar smo delali na vajah


        # self.oznaceno_polje = self.platno.find_overlapping(event.x, event.y, event.x + 1, event.y + 1)[0]
        # self.oznacena_figura = self.IGRA[i][j]
        # print(self.oznacena_figura)
        # if self.oznacena_figura is not None: # označimo figuo
        #     # pobarvamo polje z označeno figuro
        #     self.platno.itemconfig(self.oznaceno_polje, fill="blue")
        #     # sedaj se pozanimamo, kakšne poteze lahko opravi


        # ob naslednjem kliku (bodisi premik ali napačna izbira) nazaj nastavimo barvo polja





    def začni_igro(self):
        '''Prične igro.'''
        self.prikaz_figur()
  
        
    







    def prikaz_figur(self):
        '''Na šahovnici prikaže figure.'''
        for i in range(8):
            for j in range(8):
                figura = self.IGRA[i][j]
                if figura is not None:
                    i, j = figura.polozaj # rišemo lahko direktno iz položaja figur, lahko bi tudi iz položaja v matriki
                    foto = figura.foto
                    x = self.odmik + (j * self.velikost_polj) + self.velikost_polj / 2
                    y = self.odmik + (i * self.velikost_polj) + self.velikost_polj / 2
                    id_slike = self.platno.create_image(x, y, image=foto)
                    figura.id_slike = id_slike


root = tk.Tk()

pratija_saha = Sahovnica(root)

root.mainloop()


