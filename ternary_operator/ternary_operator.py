"""
Ternary operator is  value_if_true if condition else value_if_false.

Use ternary operator to make your code more concise.

See example below
"""

age  = input("Enter your age: ")

if int(age) >= 18:
  ticket_price = 20
else:
  ticket_price = 5

print(f"The ticket price is ${ticket_price}")


"""
You can use ternary operator to make the if statement
"""
ticket_price  = 20 if  int(age) >= 18 else 5

print(f"The ticket price is ${ticket_price}")
