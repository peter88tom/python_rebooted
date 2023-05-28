# class Parrot:
#     name = ""
#     age = 0
#
# # Create first object
# parrot1 = Parrot()
# parrot1.name = "John"
# parrot1.age = 2
# print(f"My name is {parrot1.name} and my age is {parrot1.age}")


"""
Inheritance:
  Inheritance is a way of creating a new class for using details of an existing class without modifying it.
  
  The newly formed class is a derived(or child class). Similarly, the existing class is a base class(or parent class)
  
  see example below 
"""
# Base class
class Animal:

    def eat(self):
        print("I can eat")

    def sleep(self):
        print("I can sleep")

# Derived class
class Dog(Animal):

  def bark(self):
      print("I can bark! Woof woof")


# Create object of the Dog class
dog1 = Dog()

# Calling member of the base class
dog1.eat()
dog1.sleep()

# Calling member of the derived class
dog1.bark()




"""
Encapsulation:
  -Python encapsulation if one of the key features of object-oriented programming.
  -It refers to the building of attributes and methods inside a single class.  
  - It prevents outer class from accessing and changing the attributes and methods of a class. this can also helps to 
  achieve data hiding                                             
  - In python, we denote private attributes using underscore as the prefix. i.e single _ or double __
  - See example below
"""

class Computer:
    def __init__(self):
        self.__max_price = 900

    def sell(self):
        print(f"Selling Price: {self.__max_price}")

    def set_max_price(self, price):
        self.__max_price = price

c = Computer()
c.sell()

# Change the price
c.__max_price = 1000 # This tried to modify the max price but not allow because it's outside the class
c.sell()

# using setter function
c.set_max_price(1000) # To modify we have to use the setter function which takes price as a parameter
c.sell()


"""
Polymophism:
  - It means more that one form.
  - The same entity(method, operator or object) can perform different operations in difference scenario.
  
  See example below
"""
