import unittest
from romanNF import *


class RomanNumber(unittest.TestCase):
    def test_tradFigureErrors(self):

        with self.assertRaises(ValueError) as context:
            tradFigure(14, 3)
        self.assertIn('ha de estar entre cero y nueve', str(context.exception))   

        with self.assertRaises(ValueError) as context:
            tradFigure(4,7)
        self.assertIn('ha de estar entre cero y tres', str(context.exception))    

        with self.assertRaises(ValueError) as context:
            tradFigure(4,'b')
        self.assertIn('ha de ser entero', str(context.exception))  

    def test_extractFigures(self):
        self.assertTrue(extractFigures(12345), [5,4,3,2,1])

    def test_toRomanErrors(self):
        with self.assertRaises(ValueError) as context:
            toRoman('casa')
        self.assertIn('Valor', str(context.exception))
        self.assertIn('ha de ser entero', str(context.exception))


    def test_algorithm_units(self):
        self.assertEqual(toRoman(1), 'I')
        self.assertEqual(toRoman(3), 'III')
        self.assertEqual(toRoman(4), 'IV')
        self.assertEqual(toRoman(5), 'V')
        self.assertEqual(toRoman(6), 'VI')
        self.assertEqual(toRoman(8), 'VIII')
        self.assertEqual(toRoman(9), 'IX')

    def test_algorithm_decens(self):
        self.assertEqual(toRoman(10), 'X')
        self.assertEqual(toRoman(30), 'XXX')
        self.assertEqual(toRoman(40), 'XL')
        self.assertEqual(toRoman(50), 'L')
        self.assertEqual(toRoman(60), 'LX')
        self.assertEqual(toRoman(80), 'LXXX')
        self.assertEqual(toRoman(90), 'XC')

    def test_algorithm_centens(self):
        self.assertEqual(toRoman(100), 'C')
        self.assertEqual(toRoman(300), 'CCC')
        self.assertEqual(toRoman(400), 'CD')
        self.assertEqual(toRoman(500), 'D')
        self.assertEqual(toRoman(600), 'DC')
        self.assertEqual(toRoman(800), 'DCCC')
        self.assertEqual(toRoman(900), 'CM')

    def test_algorithm_centesn_and_decens_and_units(self):
        self.assertEqual(toRoman(221), 'CCXXI')
        self.assertEqual(toRoman(444), 'CDXLIV')
        self.assertEqual(toRoman(555), 'DLV')
        self.assertEqual(toRoman(878), 'DCCCLXXVIII')
        self.assertEqual(toRoman(999), 'CMXCIX')

    def test_algorithm_until_4000(self):
        self.assertEqual(toRoman(3457), 'MMMCDLVII')

    def test_algoritm_from_4000_to_9999(self):
        self.assertEqual(toRoman(4000), '(IV)')
        self.assertEqual(toRoman(6897), '(VI)DCCCXCVII')

    def test_algorith_greater_than_3999(self):
        self.assertEqual(toRoman(10000), '(X)')
        self.assertEqual(toRoman(27478), '(XXVII)CDLXXVIII')
        self.assertEqual(toRoman(7193291),'((VII))(CXC)MMMCCXCI')

    def test_rompeMiles(self):
        self.assertEqual(rompeMiles(92), [92])
        self.assertEqual(rompeMiles(392), [392])
        self.assertEqual(rompeMiles(3987), [3987])
        self.assertEqual(rompeMiles(4000), [0, 4])
        self.assertEqual(rompeMiles(394197),[197, 394])
        self.assertEqual(rompeMiles(393197),[3197, 390])
        self.assertEqual(rompeMiles(394197245),[245, 197, 394])
        self.assertEqual(rompeMiles(393193245),[3245, 3190, 390])

    def test_digitRoman(self):
        self.assertEqual(digitRoman('I'), 1)
        self.assertEqual(digitRoman('V'), 5)
        self.assertEqual(digitRoman('X'), 10)
        self.assertEqual(digitRoman('L'), 50)
        self.assertEqual(digitRoman('C'), 100)
        self.assertEqual(digitRoman('D'), 500)
        self.assertEqual(digitRoman('M'), 1000)

        with self.assertRaises(ValueError) as context:
            digitRoman('N')
            self.assertTrue('no es un dígito romano' in context.exception)

    def test_to_arabic_only_symbols(self):
        self.assertEqual(toArabic('I'), 1)
        self.assertEqual(toArabic('V'), 5)
        self.assertEqual(toArabic('X'), 10)
        self.assertEqual(toArabic('L'), 50)
        self.assertEqual(toArabic('C'), 100)
        self.assertEqual(toArabic('D'), 500)
        self.assertEqual(toArabic('M'), 1000)

    def test_to_arabic_all(self):
        self.assertEqual(toArabic('III'), 3)
        self.assertEqual(toArabic('IV'), 4)
        self.assertEqual(toArabic('VIII'), 8)
        self.assertEqual(toArabic('((VII))(CXC)MMMCCXCII'), 7193292)

    def test_to_arabic_error(self):
        self.assertRaises(ValueError, toArabic, 'IIII')
        self.assertRaises(ValueError, toArabic, 'VV')
        self.assertRaises(ValueError, toArabic, 'VC')
        self.assertRaises(ValueError, toArabic, 'XM')
        self.assertRaises(ValueError, toArabic, '(XC')
        self.assertRaises(ValueError, toArabic, 'XC)')
        self.assertRaises(ValueError, toArabic, '((XC)')
        self.assertRaises(ValueError, toArabic, ('(CMDC)((CCL))XXX'))
        self.assertRaises(ValueError, toArabic, 'IXC')


    def test_negative_valor(self):
        self.assertEqual(toRoman(-3), '-III')
        self.assertEqual(toArabic('-III'), -3)



