"""
Recursive function is a function that calls itself until it doesn't

A recursive function needs to have a condition to stop calling itself. So you
need to add an if condition.

See examples below
"""


"""
1. A simple recursive function example in Python
"""

def count_down(start):
  """ Count down from a given number """
  print(start)

  next = start - 1
  if next > 0:
    count_down(next)

count_down(5)



"""
2. Using a recursive function to calculate the sum of a sequence.

Suppose you need to calculate a sum of a sequence from 1 to 1000, A simple 
way to do is to use for loop with range() function
"""
def sum(n):
  total  = 0
  for index in range(n+1):
      total += index
  return  total

result = sum(100)
print(result)


"""
To apply the recursion technique, you can calculate the sum of the sequence from 1 to n as 
 - sum(n) = n + sum(n-1)
 - sum(n-1) = n -1 + sum(n-2)
  ...
  The sum() function keeps calling itself, see below code 
"""

def sum(n):
  print(n)
  if n > 0:
    return n + sum(n-1)
  return 0

result = sum(6)
print(result)

