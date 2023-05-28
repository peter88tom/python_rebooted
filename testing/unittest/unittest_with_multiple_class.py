"""
  This example will show you how to write unittest with multiple class.

  Classing test depends with how you want to structure you test

  Each test run independently does not matter if it's in same or different class

  If your test function name have the same name one won't be called
"""

import unittest

class LearnTest1(unittest.TestCase):

    def test_func_1(self):
        pass

class LearnTest2(unittest.TestCase):

    def test_func_2(self):
        pass
