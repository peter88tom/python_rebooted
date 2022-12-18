"""
When the first line in the function body is a string, Python will interpret it as a docstring.

Add you can use help() function to build the documentation of add() function, and you can access
the docstring of a function by help(function_name)

See example below.

Docstring can be single line or multi-line string
"""

def add(a: int, b: int):
  """ Add two arguments
  :param a: an integer
  :param b: an integer
  :return: sum of a and b
  """
  return a + b

addition = add(8, 5)

print(addition)


"""
  Python stores the docstring  in the __doc__ property of the function
  You can access the __doc__ property of a function by add.__doc__
"""
