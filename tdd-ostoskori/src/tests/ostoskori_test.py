import unittest
from ostos import Ostos
from ostoskori import Ostoskori
from tuote import Tuote

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)

    def test_kori_lisaa_tuote(self):
        tuote = Tuote("maito", 1.0)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.os["maito"].hinta(),1.0)
        self.assertIsInstance(self.kori.os["maito"], Ostos)
    
    def test_kori_tyhjenna(self):
        tuote = Tuote("maito", 1.0)
        self.kori.lisaa_tuote(tuote)
        self.kori.tyhjenna()
        self.assertEqual(self.kori.os,{})

    def test_kori_hinta(self):
        self.kori.tyhjenna()
        tuote = Tuote("kalja", 3000.0)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(),6000.0)

    def test_tavaroita_korissa(self):
        self.kori.tyhjenna()
        tuote = Tuote("kalja", 3000.0)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)
        tuote = Tuote("kulju", 4000.0)
        self.kori.lisaa_tuote(tuote)
        self.assertEqual(self.kori.hinta(),10000.0)
        self.assertEqual(self.kori.tavaroita_korissa(),3)
    
    def test_poista(self):
        self.kori.tyhjenna()
        tuote = Tuote("kalja", 3000.0)
        self.kori.lisaa_tuote(tuote)
        self.kori.lisaa_tuote(tuote)
        self.kori.poista_tuote(tuote)
        self.assertEqual(self.kori.tavaroita_korissa(),0)
        self.assertEqual(self.kori.hinta(),0)
        self.assertEqual(self.kori.os,{})