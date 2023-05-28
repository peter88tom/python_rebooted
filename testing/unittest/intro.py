"""
Link to video tutorial -> https://www.youtube.com/watch?v=HKTyOUx9Wf4

  Using built-in python unittest.

  In unittest you have to write a class test before a test function,

  All the unittest class should inherit from unittest.TestCase

  In unittest, all your test must start with a "test" when naming them.

  unittest supports some important concepts in an object-oriented way

  1.text fixture:
        - represents the preparation needed to perform one or more tests, and any
          associated cleanup actions. This may involve, creating temporary or proxy database,
           directories or starting a server process.
  2. test case:
        - A test case is the individual unit of testing. it checks for a specific response to a particular set of
        inputs.
  3. test suite:
        - It's a collection of test cases. it is used to aggregate tests that should be executed together

  4. test runner:
        - It's a component which orchestrates the execution of tests and provide outcome to the user.
"""
import unittest


class LearnTest(unittest.TestCase):

    def test_func_1(self):
        pass

    def test_func_2(self):
        pass

if __name__=="__main__":
    unittest.main()

