"""
  Using built-in python unittest.

  In unittest you have to write a class test before a test function,

  All the unittest class should inherit from unittest.TestCase
"""
import unittest


class LearnTest(unittest.TestCase):

    def test_func_1(self):
        pass

    def test_funct_2(self):
        pass

if __name__=="__main__":
    unittest.main()

