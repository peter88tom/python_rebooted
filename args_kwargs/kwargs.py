"""
**kwargs is used to pass a keyworded, variable-leght argument dictionary to a function
"""

def print_kwargs(**kwargs):
  print(kwargs)

print_kwargs(kwarg_1="Shark", kwarg_2=3.0, kwarg_3=True)

# How to make user of **kwargs
def print_values(**kwargs):
  for key, value in kwargs.items():
    print(f"The value of {key} is {value}")

print_values(first_name="Sammy", last_name="John", school="DIT")
