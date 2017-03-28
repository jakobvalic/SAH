# logika igre
# tukaj se ZARES DOGAJA :)

from figure import *

class Šah:
    '''Kraljevska igra kraljev.'''


    def __init__(self):

        # bele figure
        K = Kralj('beli')
        D = Dama('beli')
        T1 = Trdnjava('beli')
        T2 = Trdnjava('beli')
        L1 = Lovec('beli')
        L2 = Lovec('beli')
        S1 = Konj('beli')
        S2 = Konj('beli')
        k1, k2, k3, k4, k5, k6, k7, k8 = [Kmet('beli') for _ in range(8)]

        # črne figure
        K_ = Kralj('crni')
        D_ = Dama('crni')
        T1_ = Trdnjava('crni')
        T2_ = Trdnjava('crni')
        L1_ = Lovec('crni')
        L2_ = Lovec('crni')
        S1_ = Konj('crni')
        S2_ = Konj('crni')
        k1_, k2_, k3_, k4_, k5_, k6_, k7_, k8_ = [Kmet('crni') for _ in range(8)]

        # možnosti za rošado:
        self.rosada_b1 = True # leva
        self.rosada_b2 = True
        self.rosada_c1 = True
        self.rosada_c2 = True


        self.postavi_figure()
        self.poteza = 0 # šteje poteze
        self.dovoljene_poteze_nasprotnika = [] # tja se naš kralj ne sme premakniti
        self.dovoljene_poteze = []
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

        self.postavi_figure()

    def odgovor_na_klik(self, i, j):
        '''Se odloči, kako bo odgovoril na klik.'''

        # označi figuro
        if self.oznacena_figura is None: # ni bila še nobena označena
            if mesto is not None: # označili smo figuro
                self.oznacena_figura = self.IGRA[i][j]
        else: # je že označena, sedaj jo lahko premakne
            if (i, j) in self.dovoljene_poteze:
                # izvede premik
                povleci_potezo(self.oznacena_figura, i, j)
            # če poteza ni veljavna, odznači figuro
            self.oznacena_figura = None
            


    def postavi_figure(self):
        '''Na začetku postavi figure na šahovnico.'''
        

    def na_potezi(self):
        '''Vrne, kdo je trenutno na potezi.'''
        if self.poteza is None:
            return 'konec igre'
        if self.poteza % 2 == 0:
            return 'beli'
        return 'črni'

    def veljavne_poteze(self):
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
        

     
