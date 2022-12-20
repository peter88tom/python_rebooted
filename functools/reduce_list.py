"""
reduce() function allows you reduce a list into a single value.

Assume you have a list of numbers and you need to get the total of those numbers, You can use for loop to sum each
element but using reduce() function is much better.

syntax : reduce(fn, list)


reduce has to be imported from python functools module, It is not a built-in function

See example below
"""

from functools import reduce

# Find the sum of this numbers in a list
numbers = [90, 0, 100, 9, 8, 0.4, 300]

def sum(a,b):
    return a + b

numbers = [90, 0, 100, 9, 8, 0.4, 300]
total_of_numbers = reduce(sum,numbers)

print(total_of_numbers)




""" Or using lambda expression """
total_with_lambda = reduce(lambda a,b:a+b, numbers)

print(total_with_lambda)
