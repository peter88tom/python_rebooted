"""
You can user * to unpack values from iterable (tuple, list, dict, etc)
as position function arguments for a function
"""


def unpack_values(first_name, last_name):
    names = f"{first_name} {last_name}"
    return names


some_values = ("John", "Doe")
print(unpack_values(*some_values))

