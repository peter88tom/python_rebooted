"""
To iterate over a list, you use for loop statement.
for item in list:
  # process the item

In the above syntax, the for loop statement assigns and individual element of the list to the item variable in
each iteration.

Inside the body of the loop you manipulate the item.
"""


"""
1. Example using for loop to iterate over a list
"""
countries = ['Kenya', 'Tanzania', 'South Africa', 'Burundi', 'Rwanda']

# The for loop will assign each countries list to the country variable and print out the country in each iteration.
for country in countries:
    print(country)



"""
2. Using for loop to iterate over a list with index

Sometime you may want to access indexes of elements inside the loop. In these case you can use
the enumerate() function.

enumerate() function return a  tuple that contain the current index and the element of the list

See example below
"""

for country in enumerate(countries):
    print(country)

# To access the index you can unpack the tuple
for index, country in enumerate(countries):
    print(f"{index}: {country}")


"""
The enumerate() function allows you to specify the starting index which defaults to zero
This example uses enumerate() function with the index that start from one.
"""
for index, country in enumerate(countries,1):
    print(f"{index}: {country}")




"""
3. Find the index of an element in a list

To find the index of an element in a list, you can use index() function 

If you attempt to find an element that does not exist in the list you will get an error, to fix
the issue you can use the "in" operator which will return true if exist and false if does not exist
"""

index_of_tz = countries.index('Tanzania')
print(index_of_tz)
