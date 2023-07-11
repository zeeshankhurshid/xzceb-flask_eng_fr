import unittest
from translator import english2_french,french2_english
class Testtests(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english2_french('Hello'),'Bonjour')
    def french2_english(self):
        self.assertEqual(french2_english('Bonjour'),'Hello')

if __name__ == '__main__':
    unittest.main()