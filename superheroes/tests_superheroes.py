import unittest
from superheroes import *
import datetime

class TestsHeroes(unittest.TestCase):

    def test_is_date(self):
        self.assertTrue(esFecha('8-4-1970'))
        self.assertFalse(esFecha('31-4-1970'))
        self.assertFalse(esFecha(''))

    def test_is_yesterday(self):
        self.assertTrue(esFecha('8-4-1970'))
        self.assertFalse(esFecha('8-4-2970'))

    def test_asigna_nombre(self):
        self.assertEqual(asignaNombre('Ana'), nombreSuperHeroes['A'])
        self.assertEqual(asignaNombre('ana'), nombreSuperHeroes['A'])
        self.assertEqual(asignaNombre(' ana'), nombreSuperHeroes['A'])

    def test_asigna_apellido(self):
        self.assertEqual(asignaApellido('Maldonado'), apellidoSuperHeroe['M'])
        self.assertEqual(asignaApellido('maldonado'), apellidoSuperHeroe['M'])
        self.assertEqual(asignaApellido(' maldonado'), apellidoSuperHeroe['M'])
        self.assertEqual(asignaApellido('Ñañez'), 'no asignado')

    def test_asigna_super_poder(self):
        nac = datetime.datetime.strptime('8-4-1970', "%d-%m-%Y")
        self.assertEqual(asigna_super_poder(nac), superPoderes[3])
        self.assertEqual(asigna_super_poder('8-4-1970'), 'no asignado')

    def test_asigna_color(self):
        nac = datetime.datetime.strptime('8-4-1970', "%d-%m-%Y")
        self.assertEqual(asigna_color(nac), colorTraje[0])
        self.assertEqual(asigna_color('8-4-1970'), 'no asignado')

    def test_asigna_arma(self):
        nac = datetime.datetime.strptime('1-4-1970', "%d-%m-%Y")
        self.assertEqual(asigna_arma(nac), armas[0])
        self.assertEqual(asigna_arma('8-4-1970'), 'no asignado')

