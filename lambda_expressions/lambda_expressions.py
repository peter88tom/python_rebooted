"""
Lambda expressions allows you to define anonymous function.
Anonymous functions are functions without names, they're useful when you need to use them once.

A lambda expression typically contains one or more arguments, but it can have only one expression.


 See the format:  lambda parameters: expression

 The above format is equivalent to:

 def anonymous(parameters):
        return expression

"""

"""
Function that accept a function example
"""
def get_full_name(first_name, last_name, formatter):
    return formatter(first_name,last_name)

name = get_full_name("John", "Doe", lambda first_name, last_name: f"{first_name}, {last_name}")
print(name)

