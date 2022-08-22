import unittest
from ejercicio import *
class My_Test(unittest.TestCase):

    def test_1(self):
        self.assertEqual(my_function(7, 4), True)

    def test_2(self):
        self.assertEqual(my_function(4, 4), True)

    def test_3(self):
        self.assertEqual(my_function(2, 6), False)

