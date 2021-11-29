from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.os = {}
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        s = 0
        for (_,v) in self.os.items():
            s = s + v._lukumaara
        return s
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        s = 0 
        for (_,v) in self.os.items():
            s = s + v.hinta()
        return s
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        if lisattava.nimi() in self.os:
            self.os[lisattava.nimi()].muuta_lukumaaraa(1)
        else:
            self.os[lisattava.nimi()] = Ostos(lisattava)

    def poista_tuote(self, poistettava: Tuote):
        del self.os[poistettava.nimi()]

    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.os = {}

    def ostokset(self):
        return self.os
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
