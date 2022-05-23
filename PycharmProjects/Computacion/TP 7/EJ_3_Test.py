import unittest
from Ej_3 import *

class Testing(unittest.TestCase):
    def test_1(self):
        nums = list(range(0, 101))
        nums.remove(5)
        self.assertEqual(missing_no(nums), 5)

    def test_2(self):
        nums = list(reversed(range(0, 101)))
        nums.remove(10)
        self.assertEqual(missing_no(nums), 10)
