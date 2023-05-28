class Employee:

  def __init__(self, first_name, last_name, salary):
    self.first_name = first_name
    self.last_name = last_name
    self.salary = salary
    self.email = f"{self.first_name}.{self.last_name}@gmail.com"

  # Function to change salary of employee
  def change_salary(self, salary):
    self.salary = salary


# Class developer will inheriting first_name, last_name and salary from employee class
class Developer(Employee):

  def __init__(self, first_name, last_name, salary, programming_languages):
    super().__init__(first_name, last_name, salary)
    self.prog_langs = programming_languages

  def add_new_language(self,lang):
    self.prog_langs += [lang]

# Accessing employee class
employee1 = Employee("John", "Collins.", 550000)
print(f"{employee1.first_name} this year salary is R {employee1.salary}")

# Use change salary to increase salary for next year
employee1.change_salary(750000)
print(f"{employee1.first_name} next year salary will be R {employee1.salary}")
print("\n")

# Accessing developer class
dev1 = Developer("Devin", "Booker", 450000, ["Python"])
print(f"{dev1.first_name} this year salary is R {dev1.salary}")

# Increase salary
dev1.change_salary(600000)
print(f"{dev1.first_name} next year salary will be R {dev1.salary}")
print("\n")

# Current programming languages
print(f"{dev1.first_name} current programming languages are {dev1.prog_langs}")

# Add new programming language for next year
dev1.add_new_language("Go")
print(f"{dev1.first_name} next year programming languages will be {dev1.prog_langs}")

stin = "Hey there"
print(stin.replace("Hey", "Hello"))

fruits = ["Orange", "Apple", "Pineapple"]

new_f1 = [item for item in fruits if item.endswith('le')]
print(new_f1)




print(range(5))


