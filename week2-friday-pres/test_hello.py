import unittest
from hello import subtract_numbers, divide_numbers

# test case class is a subclass of unittest.TestCase in order to use methods and attributes in unittest import
class Test(unittest.TestCase):
    # test method for subtract_numbers function
    def test_subtract_numbers(self):
        # check if subtract_numbers(9, 3) equals 6
        self.assertEqual(subtract_numbers(9, 3), 6) # self refers to the instance of the Test class
        # check if subtract_numbers(-1, -4) equals 3
        self.assertEqual(subtract_numbers(-1, -4), 3)

    # test method for divide_numbers function
    def test_divide_numbers(self):
        # check if divide_numbers(10, 5) equals 2
        self.assertEqual(divide_numbers(10, 5), 2)
        # check if divide_numbers(-4, 2) equals -2
        self.assertEqual(divide_numbers(-4, 2), -2)

# ensures test case, unittest.main() runs when the script is run directly, not when it's imported
if __name__ == '__main__':
    unittest.main()