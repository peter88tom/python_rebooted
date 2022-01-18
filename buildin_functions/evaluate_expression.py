"""
https://www.geeksforgeeks.org/python-evaluate-expression-given-in-string/

Evaluate expression given in string

Sometime while working with python strings, we can have certain computations in string format
and we need to formulate its result.
"""

# Method #1: Using regax + map() + sum()
"""
This method can be used if the string has only + or -
"""
import re

# Initializeing string
test_str = "10+30-3"

# Print original string
print(f"The original string is : {test_str}")

# Expression evaluation in String
# Using regex + map() + sum()
res = sum(map(int, re.findall(r'[+-]?\d+', test_str)))

# Printing result
print(f"The evaluated result is: {res}")



# Method #2: Using eval()
eva_str = eval(test_str)
print(f"Using eval(): {eva_str}")
