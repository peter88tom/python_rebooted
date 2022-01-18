"""
Dictionary in python is like a hash table in any other language
It is unordered collection of data values, used to store data like a map

Python dictionary uses key:value pair
To access the value we uses key
"""

# Creating a dictionary
Dict = {"Name": "John Doe", 1: [1, 2, 3, 4, 5]}
print(f"Creating Dictionary:  {Dict}")

# Accessing a element using key
print(f"Accessing element using key: {Dict['Name']}")

# Accessing  element using get
print(f"Accessing element using get: {Dict.get(1)}")

# Creation using Dictionary comprehension
myDict = {x: x*2 for x in [1, 2, 3, 4, 5]}
print(myDict)
