import unittest
from hello import subtract_numbers, divide_numbers

class Test(unittest.TestCase):
    def test_subtract_numbers(self):
        self.assertEqual(subtract_numbers(9, 3), 6)
        self.assertEqual(subtract_numbers(-1, -4), 3)

    def test_divide_numbers(self):
        self.assertEqual(divide_numbers(10, 5), 2)
        self.assertEqual(divide_numbers(-4, 2), -2)

if __name__ == '__main__':
    unittest.main()