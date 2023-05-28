"""
Dictionary is key value array
"""

student = {"first_name": "Zara", "age": "14", "college": "Zara College"}
print(student)

prin("You access value using keys")
print(student["first_name"])
print("\n")

print("Updating dictionary element")
student["age"] = 15
print(student)
print("\n")

print("Add new dictionary element")
student["last_name"] = "Booker"
print(student)
print("\n")


print("Deleting dictionary element")
del student["last_name"]
print(student)
print("\n")

print("Copying a dictionary(Shallow copy)")
new_student = student.copy()
print(new_student)
print("\n")

print("Return value or default if key not in dictionary")
print(student.get("age"))
print("\n")

print("Return list of dictionary (key, value) tuple pairs ")
print(student.items())
print("\n")

print("Deleting all elements in a dictionary")
student.clear()
print(student)



