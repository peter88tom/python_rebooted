"""
Tuple is a correction of objects which ordered and immutable
"""
tup1 = ('python', 'Go', 'C++', 50000,)

"""
When writing tuple you need to include , at the end, even if there is one object
"""

"""
Accessing tuple
You can access tuple similar to list
"""
print(tup1[0])
print(tup1[0:2])


"""
Updating tuple,
When updating tuple you have to create a new tuple and concatinate with exist
"""
tup2 = (60,70,90)
updated_tuple = tup1+tup2

print(updated_tuple)
