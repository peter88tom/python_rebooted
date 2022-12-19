""" The sort() method sorts a list in place. It does changes the order of the elements in the
  original list. To return the new sorted list from the original list, you can use the sorted() function.

  sorted(list).

  sorted() function does not modify the original list. By default it sorts the list from lowest to highest using
  less-than operator( < ).

  If you want to reverse the sort order, you can pass the reverse argument as  True like:

  sorted(list, reverse=True)

"""

""" 
  1. Using python sorted() function to sort a list of strings 
"""
names = ["John", "Richard", "Mary", "Nelly", "Anthony"]
sorted_names = sorted(names)

print(names) # The original list does not change
print(sorted_names) # This return a new sorted list from the original list

