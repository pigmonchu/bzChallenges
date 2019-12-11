from unittest import TestCase, main
from dna import *

class DnaTest(TestCase):
    def test_repes(self):
        self.assertEqual(secuerepe('ctgactga', 'actgagc'), 'actga')
        self.assertEqual(secuerepe('cgtaattgcgat', 'cgtacagtagc'), 'cgta')
        self.assertEqual(secuerepe('ctgggccttgaggaaaactg', 'gtaccagtactgatagt'), 'actg')
        self.assertEqual(secuerepe('ctgactgaa', 'tctgaa'), 'ctgaa')


if __name__ == '__main__':
    main()