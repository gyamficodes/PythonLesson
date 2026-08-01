# What is OOP?
# OOP stands for Object-Oriented Programming.


# Create a Class
# To create a class, use the keyword class:

# class
class MyClass: 
    x = 5

# create object 
# Multiple Objects
# Note: Each object is independent and has its own copy of the class properties.
p1 = MyClass()
p2 = MyClass()
print(p1.x)
print(p2.x)

# delete object
# del p1


# The pass Statement
# class definitions cannot be empty, but if you for some reason have a class definition with no content, put in the pass statement to avoid getting an error.

class Machine:
    pass


# Python __init__() Method
# The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
class Student:
    def __init__(self, name, age, year):
        self.name =  name
        self.age = age 
        self.year = year


S1 = Student("John", 25, 2026)
print(S1.name)
print(S1.age)
print(S1.year)



# Default Values in __init__()
# You can also set default values for parameters in the __init__() method:
class Boosks:
    def  __init__(self, title, author, year = 2026):
        self.title = title
        self.author = author
        self.year = year


B1 = Boosks("Python Programming", "John Doe")
print(B1.title, B1.author, B1.year)
B2 = Boosks("Python Programming", "John Doe", 2025)
print(B2.title, B2.author, B2.year)




