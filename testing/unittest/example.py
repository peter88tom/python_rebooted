import unittest

def sum_two_number(a, b):
    return a + b


class SumTwoNumberTest(unittest.TestCase):
    """ Each test must have three stages, Arrange, Act and Assert """

    def test_sum_two_number_1(self):
        # Arrange
        a = 10
        b = 20

        # Act
        result = sum_two_number(a, b)

        # Assert
        self.assertEqual(result, a + b)


    def test_sum_two_number_2(self):
        # Arrange
        a = 10
        b = 20

        # Act
        result = sum_two_number(a, b)

        # Assert
        self.assertEqual(result, b + a)
