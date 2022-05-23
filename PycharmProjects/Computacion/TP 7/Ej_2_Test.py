import unittest
from Ej_2 import *

class Testing(unittest.TestCase):
    def test_1(self):
        self.assertEqual(validate_pin("12345"), False)

    def test_2(self):
        self.assertEqual(validate_pin("9765"),True)

    def test_3(self):
        self.assertEqual(validate_pin("a345"),False)