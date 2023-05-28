"""
In this example will show you how to combine two list  using extends
"""

list_a = [1,2,3,4]
list_b = ['a','b','c']

"""
The simple way here you could use for loop
"""
list_a_and_b = []
for l_a in list_a:
    list_b.append(l_a)


print(f"List a and b using for loop: {list_a_and_b}")


""" You can use the + sign to join them too"""
another_list = list_a+list_b
print(f"combine list a and list b using a + sign: {another_list}")


"""Use extend to combine the two list """
list_a.extend(list_b)

print(f"combine the list using extend: {list_a}")
