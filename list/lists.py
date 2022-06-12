l1 = ["Math", "Physics", "chemistry", 2000, 50000]

print("Original list")
print(l1)
print("\n")

# Accessing values in a list using index
print("Access single value from list")
print(l1[0])
print("\n")

# Access value using index range
print("Access values by index range")
print(l1[0:3])
print("\n")

# Updating list
print("Updating value using index")
l1[0] = 'Geography'
print(l1)
print("\n")

# Deleting value from the list
print("Deleting value from the list")
del l1[0]
print(l1)
print("\n")


print("Indexing, Slicing, Matrixes")
print("Get the last two items in the list")
print(l1[2:])
print("\n")

print("Build-in List Function & methods")
l2 = [1,1,2,3,4,5]

print("Add item in a list")
l2.append(30)
print(l2)
print("\n")

print("Count how times items appeared in a list")
print(l2.count(1))
print("\n")

