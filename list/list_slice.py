"""
List slice allows you to get a sublist from a list

sub_list = list[begin: end: step]

In this syntax, the begin, end and step arguments must be valid indexes. they are all optional

The begin index default to zero, The end index default to length of the list, and the step index default to 1.

The slice will start from the begin up the the end in the step of step.

The begin, end and step can be  positive or negative. Positive values slice the list
from the first to the last element while negative values slice from last to first element.

You can use the list slice to change the list such as updating, resizing and deleting a part of the list

"""

"""
1. Basic list slice example
"""
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'pink', 'purple']

# This uses slice to get a sublist from the colors list
sub_colors = colors[1:4]
# This example does not use step, therefore it will get values within the range without skipping and elements

print(sub_colors)

"""
2. List slice to get the n-first elements from a list
list[:n]
"""
new_sub_colors = colors[:4]
# Return a list that includes the first 4 elements
print(new_sub_colors)


"""
3. List slice to get the n-last elements from a list
list[-3:]
"""
sub_last_colors = colors[-4:]
# Return the last 4 elements
print(sub_last_colors)


"""
4. List slice to get every nth element from a list
list[::n]

This uses step to return a sublist that include every nth element from a list
"""
sub_every_color = colors[::2]

print(sub_every_color)

"""
5. List slice to reverse a list

  When you use a negative step, the slice includes the list of elements starting from the 
  last element to the first element.
"""
reversed_colors  = colors[::-1]

print(reversed_colors)


"""
6. List slice to substitute part of a list
"""
colors[0:2] = ['Magenta', 'Indigo']
print(colors)


"""
7. List slice to delete elements
"""
del colors[0:2]

print(colors)
