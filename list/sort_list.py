"""
To sort a list you can use sort()
list.sort()

By default the sort() method sorts elements of a list using less-than operator (<)
in other words it places the lower elements before the higher elements.

To sort elements from higher to lower you must pass reverse=True argument to the sort() method
"""

"""
 1. Using list sort() method to sort a list of strings
"""

names = ["John", "Richard", "Mary", "Nelly", "Anthony"]

# This will sort from low to high
names.sort()

print(names)

# Sort from high to low
names.sort(reverse=True)

print(names)


"""
2. Using sort() method to sort a list of tuples
"""
companies = [('Google', 2019, 124.90),
             ("Apple", 2019, 38.89),
             ("Twitter", 2019, 79.90)]

""" If you want to sort the companies list by revenue from highest to lowest 
    first, specify a sort key and pass it to the sort() method. To define a sort key, 
    you create a function that accepts a tuple and return the element that you want to sort by.
    
    In this example we want the function to return the second key which is a revenue
"""

def sort_key(company):
    return company[2]


companies.sort(key=sort_key, reverse=True)

print(companies)



""" You can use lambda expression to sort """
companies.sort(key=lambda company: company[2])

print(companies)
