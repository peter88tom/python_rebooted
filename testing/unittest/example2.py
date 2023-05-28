"""
  From example.py, you can see there are duplicates of the "Arrange" part of the testing functions. To remove that
  duplicate we use SetUp()

 - The SetUp function will be called before the test

 - The tearDown function will be called after the test

"""

import unittest

def sum_two_number(a, b):
    return a + b



# Test the above function
class SumTwoNumberTest(unittest.TestCase):
    """ Each test must have three stages, Arrange, Act and Assert """

    def setUp(self):
        # Arrange
        # I will be called before each and every test function
        print("SETUP Called...")
        self.a = 10
        self.b = 20


    def tearDown(self):
        print("TearDown Called...")

    def test_sum_two_number_1(self):
        print("Test 1 is called...")
        # Act
        result = sum_two_number(self.a, self.b)

        # Assert
        self.assertEqual(result, self.a + self.b)


    def test_sum_two_number_2(self):
        print("Test 2 is called ...")
        # Act
        result = sum_two_number(self.a, self.b)

        # Assert
        self.assertEqual(result, self.b + self.a)
