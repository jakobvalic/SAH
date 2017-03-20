# figure

def je_v_polju(poteza):
    '''Preveri, ali je poteza v polju.'''
    x, y = poteza
    return 0 <= min(x, y) <= max(x, y) <= 7

class Konj():
    def __init__(self, polozaj):
        '''Zameril si se mi, konj!'''
        self.polozaj = polozaj
        self.poteze = []
        self.mozne_poteze(polozaj) # napolnimo self.poteze z možnimi potezami

    def mozne_poteze(self, polozaj):
        '''Vrne seznam možnih potez konja.'''
        st = list('ABCDEFGH'.split())
        vr = [1, 2, 3, 4, 5, 6, 7, 8]
        x, y = polozaj # x: A, B, C, D, E, F, G, H;    y: 1, 2, 3, 4, 5, 6, 7, 8
        mozne_p = list()
        veljavne_mozne  = list()
        # gor in dol
        gor = y + 2
        dol = y - 2
        mozne_p += [(x-1, gor), (x+1, gor)]
        mozne_p += [(x-1, dol), (x+1, dol)]
        # levo in desno
        levo = x - 2
        desno = x + 2
        mozne_p += [(levo, y-1), (levo, y+1)]
        mozne_p += [(desno, y-1), (desno, y+1)]
        for poteza in mozne_p:
            if je_v_polju(poteza):
                veljavne_mozne.append(poteza)
        self.poteze.extend(veljavne_mozne)
        return veljavne_mozne

polozaj = (1, 4)
polozaj2 = (0, 0)
polozaj3 = (4, 4)

konj = Konj((1, 4))
print('konji\n', konj.poteze, sep = '')

konj = Konj(polozaj2)
print(konj.poteze)

konj = Konj(polozaj3)
print(konj.poteze)

class Lovec():
    def __init__(self, polozaj):
        self.polozaj = polozaj
        self.poteze = []
        self.mozne_poteze(polozaj)

    def mozne_poteze(self, polozaj):
        '''Vrne seznam vseh možnih potez lovca.'''
        mozne_veljavne = []
        x, y = polozaj
        odmik = 1
        # desno 
        while x + odmik <= 7:
            if 0 <= y - odmik:
                mozne_veljavne.append((x + odmik, y - odmik)) # dol
            if y + odmik <= 7:
                mozne_veljavne.append((x + odmik, y + odmik)) # gor
            odmik += 1
        # levo
        odmik = 1
        while 0 <= x - odmik:
            if 0 <= y - odmik:
                mozne_veljavne.append((x - odmik, y - odmik)) # dol
            if y + odmik <= 7:
                mozne_veljavne.append((x - odmik, y + odmik)) # gor
            odmik += 1
        self.poteze.extend(mozne_veljavne)
        return mozne_veljavne

lovec = Lovec(polozaj)
print('\nlovci\n', polozaj, lovec.poteze, sep = '')

lovec = Lovec(polozaj2)
print(polozaj2, lovec.poteze)

lovec = Lovec(polozaj3)
print(polozaj3, lovec.poteze)
                
            
            
        













    
