import unittest
import math


class TestIsEvenMethod(unittest.TestCase):
    '''
    Define the function isEven which returns True,
    if a given number is even and returns False,if the number is odd.
    Define a simple class TestIsEvenMethod derived from unittest.TestCase class.
    Hint : Import unittest module and use TestCase utility of it.
    '''

    def isEven(self, number):
        if(number % 2 == 0):
            return True
        return False
        

    def test_isEven1(self):
        self.assertEqual(self.isEven(5), False, 'Its not even')


    def test_isEven2(self):
        self.assertEqual(self.isEven(10), True, 'Its not even')


    def test_isEven3(self):
        self.assertRaises(TypeError, self.isEven('hello'), 'Cant handle it')

if __name__ == '__main__':
    unittest.main()
        