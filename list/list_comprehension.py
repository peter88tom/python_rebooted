"""
List comprehensions allows you create a new list from an existing one

For example you have:
numbers = [1,2,3,4,5]
And you want to get a list of squares from that list, the following are the way you use to do it
"""

numbers = [1,2,3,4,5]

""" 
1. Using for loop
"""
squared_numbers  = []
for number in numbers:
    squared_numbers.append(number**2)

print(f"Using for loop: {squared_numbers}")


"""
2. Using map() function with lambda expression, but it return the iterator, you will have to use list() 
function to convert the iterator to a list
"""

squared_numbers = list(map(lambda number: number**2, numbers))

print(f"Using map: {squared_numbers}")


"""
3. To help create a list based on the transformation python provide a feature called list comprehensions
  - It consist of the following parts
    * An input list (numbers)
    * A variable that represents the element of the list (number)
    * An output expression (number**2) that return the elements of the output list from the
      elements of the input list
"""

squared_numbers = [number**2 for number in numbers]

print(f"Using list comprehensions: {squared_numbers}")



"""
  Python list comprehension with if condition.
  
  There are multiple you can do this

"""

mountains = [
    ['Makalu', 8485],
    ['Lhotse', 8516],
    ['Kilimanjaro', 8586],
    ['K2', 8611],
    ['Everest', 8848]
]


""" 
Assume you want to get the mount where the height is greater that 8600 meters,
You can use fo loop or filter with lambda function like this
"""

highest_mountain = list(filter(lambda m: m[1] > 8600, mountains))

print(f"Highest mountains are: {highest_mountain}")


"""
The list comprehension allows you to replace the filter with lambda function
See below code
"""

highest_mountain = [m for m in mountains if m[1] > 8600]

print(highest_mountain)
