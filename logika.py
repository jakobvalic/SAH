# logika igre
# tukaj se ZARES DOGAJA :)

from figure import *

class Šah:
    '''Kraljevska igra kraljev.'''


    def __init__(self):

        # self.sahovnica = sahovnica.Sahovnica

        # bele figure
        K = Kralj('beli', (7, 4))
        D = Dama('beli', (7, 3))
        T1 = Trdnjava('beli', (7, 0))
        T2 = Trdnjava('beli', (7, 7))
        L1 = Lovec('beli', (7, 2))
        L2 = Lovec('beli', (7, 5))
        S1 = Konj('beli', (7, 1))
        S2 = Konj('beli', (7, 6))
        k1, k2, k3, k4, k5, k6, k7, k8 = [Kmet('beli', (6, i)) for i in range(8)]

        # črne figure
        K_ = Kralj('crni', (0, 4))
        D_ = Dama('crni', (0, 3))
        T1_ = Trdnjava('crni', (0,0))
        T2_ = Trdnjava('crni', (0, 7))
        L1_ = Lovec('crni', (0, 2))
        L2_ = Lovec('crni', (0, 5))
        S1_ = Konj('crni', (0, 1))
        S2_ = Konj('crni', (0, 6))
        k1_, k2_, k3_, k4_, k5_, k6_, k7_, k8_ = [Kmet('crni', (1, i)) for i in range(8)]

        # možnosti za rošado:
        self.rosada_b1 = True # leva
        self.rosada_b2 = True
        self.rosada_c1 = True
        self.rosada_c2 = True


        self.poteza = 0 # šteje poteze
        self.dovoljene_poteze_nasprotnika = [] # tja se naš kralj ne sme premakniti
        self.dovoljene_poteze = [(i, j) for i in range(8) for j in range(8)] # na začetku, za lažje premikanje :)
        self.oznacena_figura = None



        
        # matrika s trenutno pozicijo
        self.IGRA = [
            [T1_ , S1_ , L1_ , D_  , K_  , L2_ , S2_ , T2_ ],
            [k1_ , k2_ , k3_ , k4_ , k5_ , k6_ , k7_ , k8_ ],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [None, None, None, None, None, None, None, None],
            [k1  , k2  , k3  , k4  , k5  , k6  , k7  , k8  ],
            [T1  , S1  , L1  , D   , K   , L2  , S2  , T2  ]]
        [print(i) for i in self.IGRA]


    def odgovor_na_klik(self, i, j):
        '''Vhodni argumenti: i - vrstica, od zgoraj; j - stolpec, od zgoraj.
        Določi odgovor na klik.'''

        mesto = self.IGRA[i][j]

        if self.oznacena_figura is None: # klik1
            if mesto is not None: # ni kliknil na prazno polje
                # označimo figuro
                self.oznacena_figura = mesto

                # sporočiš veljavna polja, GUI pobarva polja


        else: # klik2
            if (i, j) in self.dovoljene_poteze:
                # izvede premik
                povleci_potezo(self.oznacena_figura, i, j)

                # logika spremeni self.IGRO
                self.oznacena_figura.x = j
                self.oznacena_figura.y = i
                # pokliči GUI, da se poteza nariše

                # daj potezo nasprotniku


            # če poteza ni veljavna, odznači figuro
            else:
                self.oznacena_figura = None



        

    def na_potezi(self):
        '''Vrne, kdo je trenutno na potezi.'''
        if self.poteza is None:
            return 'konec igre'
        if self.poteza % 2 == 0:
            return 'beli'
        return 'črni'

    def veljavne_poteze(self):
        pass

        '''Osveži seznam vseh veljavnih potez igralca, ki je na vrsti.'''
        veljavne_poteze = []
        for i in range(7):
            for j in range(7): # gremo čez vsako polje v šahovnici
                na_potezi = na_potezi(self)
                figura = self.IGRA[i][j]
                if figura is not None:
                    if figura.barva == na_potezi:
                        veljavne_poteze.append(figura.veljavne_poteze)
        self.veljavne_poteze.extend(veljavne_poteze)

    def premakni_figuro(self, oznacena_figura, i, j):
        '''Premakne figuro v matriki igre.'''
        # polje, ki ga je figura zapustila, je prazno
        stari_i, stari_j = oznacena_figura.polozaj
        self.IGRA[stari_i][stari_j] = None
        # premaknemo na novi koordinati
        self.IGRA[i][j] = oznacena_figura






            

    def povleci_potezo(self, figura, i, j, poteza): # preveč: položaj lahko izvemo iz figure
        '''Spremeni matriko IGRA.'''
        novi_i, novi_j = poteza
        # spremenimo stanje v matriki
        self.IGRA[i][j] = None
        self.IGRA[novi_i][novi_j] = figura

        # sporočimo GUI-ju, naj potezo nariše
        

        # povečamo števec potez in ponastavimo seznam dovoljenih potez
        self.dovoljene_poteze_nasprotnika = self.dovoljene_poteze.copy()
        self.dovoljene_poteze = []
        self.poteza += 1
        

     
