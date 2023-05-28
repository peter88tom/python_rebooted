"""
Link to video tutorial -> https://www.youtube.com/watch?v=HKTyOUx9Wf4

  Using built-in python unittest.

  In unittest you have to write a class test before a test function,

  All the unittest class should inherit from unittest.TestCase

  In unittest, all your test must start with a "test" when naming them.
"""
import unittest


class LearnTest(unittest.TestCase):

    def test_func_1(self):
        pass

    def test_func_2(self):
        pass

if __name__=="__main__":
    unittest.main()

