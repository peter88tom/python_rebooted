"""
*args is used as parameter to send a non-keyworded valiable-length argument list to functions
Use this when you does not know how many arguments you're going to pass to a function
"""

def multiply(*args):
  z = 1
  for num in args:
    z *= num
  print(z)

multiply(5,4,7)
