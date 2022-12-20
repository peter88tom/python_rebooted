"""
When working with list or tuple, you often need to transform the element of a list and
return a new list that contain transformed element


Suppose you are given this list below and you want to double, to do it you can use for loop to iterate over
the element, double each of them, and add it to a new list

bonuses = [100, 200, 300]

doubled_bonuses = []

for bonus in bonuses:
      doubled_bonuses.append(bonus*2)

print(doubled_bonuses)


Python provide a nicer way to do this kind of task by using the map() build-in function

map() function iterate over all elements in a list, or tuple, apply a function to each element and return
a new iterator of the new elements.

See the syntax.
iterator = map(fn, list)

In the above syntax, fn is function that will be called on each element in the list

In fact you can pass any iterable object to the map() function

See example below
"""

def double(bonus):
    return bonus*2

bonuses = [100, 200, 300]

iterator = map(double, bonuses)

# Convert iterator to a list
print(list(iterator))

"""
You can make the code more concise by using lambda expression
"""

iterator_with_lambda = map(lambda bonus: bonus*2, bonuses)

# Convert iterator to a list
print(list(iterator_with_lambda))




"""
See this example using map to return a new list with capitalized first letters
"""
names = ['peter', 'richard', 'paul']

new_names = map(lambda name: name.capitalize(), names)

print(list(new_names))


"""
See this example, using map() function to calculate the tax by 10% for each item in a cart
and you need to add that calculated tax amount as the third element for reach of the item in the cart

The final output should be:
carts  = [['laptop', 700, tax_value],
        ['shirt', 250, tax_value],
        ['t-shirt', 300, tax_value]]
        
      tax_value here is the one calculated
      
 In order to do so, you can use map() function to create a new element of the list and add a new tax amount to
 each 
"""
carts = [['laptop', 700],
        ['shirt', 250],
        ['t-shirt', 300]]

tax = 0.1

carts = map(lambda item: [item[0], item[1], item[1] * tax], carts)

print(list(carts))
