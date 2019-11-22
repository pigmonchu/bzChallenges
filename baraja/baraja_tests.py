import unittest
from unittest.mock import patch
from baraja import *

class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.baraja = create_deck()

    def test_create_deck(self):
        self.assertEqual(len(self.baraja), 40)
        self.assertEqual(self.baraja[0], 'Ao')
        self.assertEqual(self.baraja[10], 'Ac')
        self.assertEqual(self.baraja[20], 'Ae')
        self.assertEqual(self.baraja[30], 'Ab')

    @patch('baraja.eligeCarta', lambda max, excepted: (excepted + 1) % max )
    def test_shuffle_deck(self):
        shuffle_deck(self.baraja)
        print(self.baraja)
        self.assertEqual(len(self.baraja), 40)
        self.assertEqual(self.baraja[0], 'Ao')
        self.assertEqual(self.baraja[1], '3o')
        self.assertEqual(self.baraja[39], '2o')

class TestDeckOfCards(unittest.TestCase):
    def setUp(self):
        self.baraja = Baraja()

    def test_Baraja_constructor(self):
        self.assertEqual(len(self.baraja.naipes), 40)
        self.assertEqual(self.baraja.naipes[0], 'Ao')
        self.assertEqual(self.baraja.naipes[10], 'Ac')
        self.assertEqual(self.baraja.naipes[20], 'Ae')
        self.assertEqual(self.baraja.naipes[30], 'Ab')

    @patch('baraja.Baraja._Baraja__eligeCarta', lambda self, max, excepted: (excepted + 1) % max )
    def test_Baraja_shuffle(self):

        self.baraja.shuffle()
        self.assertEqual(len(self.baraja.naipes), 40)
        self.assertEqual(self.baraja.naipes[0], 'Ao')
        self.assertEqual(self.baraja.naipes[1], '3o')
        self.assertEqual(self.baraja.naipes[39], '2o')

    def test_Baraja_repartir(self):
        manos = self.baraja.distribute(4, 2)
        self.assertEqual(len(self.baraja.naipes), 32)
        self.assertEqual(len(manos), 2)
        self.assertEqual(len(manos[0]), 4)
        self.assertEqual(len(manos[1]), 4)
        self.assertEqual(manos[0][0], 'Ao')
        self.assertEqual(manos[0][3], '4o')
        self.assertEqual(manos[1][0], '5o')
        self.assertEqual(manos[1][3], 'So')

if __name__ == "__main__":
    unittest.main()