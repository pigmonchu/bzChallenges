import unittest
from traslation import *

class TestTraslation(unittest.TestCase):

    def test_translate_char_simple(self):
        self.assertEqual(cifra('A', 5), 'F')
        self.assertEqual(cifra('a', 5), 'f')
        self.assertEqual(cifra1('A', 5), 'F')
        self.assertEqual(cifra1('a', 5), 'f')
        self.assertEqual(cifra2('A', 5), 'F')
        self.assertEqual(cifra2('a', 5), 'f')
    
    def test_translate_char_overflow(self):
        self.assertEqual(cifra('X', 5), 'C')
        self.assertEqual(cifra('x', 5), 'c')
        self.assertEqual(cifra1('X', 5), 'C')
        self.assertEqual(cifra1('x', 5), 'c')
        self.assertEqual(cifra2('X', 5), 'C')
        self.assertEqual(cifra2('x', 5), 'c')

    def test_translate_vocales(self):
        self.assertEqual(cifra('cigüeñón', 0), 'cigueñon')
        self.assertEqual(cifra1('cigüeñón', 0), 'cigueñon')
        self.assertEqual(cifra2('cigüeñón', 0), 'cigueñon')

    def test_translate_frase(self):
        self.assertEqual(cifra('Hola, corazón de cigüeña', 4), 'Lsoe, gsvedsq hi gmkyire')
        self.assertEqual(cifra1('Hola, corazón de cigüeña', 4), 'Lsoe, gsvedsq hi gmkyire')
        self.assertEqual(cifra2('Hola, corazón de cigüeña', 4), 'Lsoe, gsvedsq hi gmkyire')

    def test_translate_with_numbers(self):
        self.assertEqual(cifra('Nací el 8 de abril de 1970', 3), 'Pdfl hñ 1 gh deulñ gh 4203')
        self.assertEqual(cifra1('Nací el 8 de abril de 1970', 3), 'Pdfl hñ 1 gh deulñ gh 4203')
        self.assertEqual(cifra2('Nací el 8 de abril de 1970', 3), 'Pdfl hñ 1 gh deulñ gh 4203')
