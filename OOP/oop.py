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
    # Properties
    def  __init__(self, title, author, year = 2026):
        self.title = title
        self.author = author
        self.year = year
    # Method
    def displayBook(self):
        print(f"Title: {self.title}, Author: {self.author}, Year: {self.year}")

# Books obJ
B1 = Boosks("Python Programming", "John Doe")
B1.displayBook()
B2 = Boosks("Python Programming", "John Doe", 2025)
B2.displayBook()


# Python self Parameter
# The self parameter is a reference to the current instance of the class.
# It is used to access properties and methods that belong to the class.
# Without self, Python would not know which object's properties you want to access:
class Employer:
    def __init__(self, name, age):
        self.name = name 
        self.age = age 
    def displayEmployer(self):
        print(f"Name: {self.name}, Age: {self.age}")

Em1 = Employer("Alice", 30)
Em1.displayEmployer()


# self Does Not Have to Be Named "self"
# It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class:
class anounceBirhthday():
    def __init__(bithday, name, age, year):
        bithday.name = name
        bithday.age = age 
        bithday.year = year
    def displayBirthday(bithday):
        print(f"my name is {bithday.name} and I am {bithday.age} ,and I was born in {bithday.year}")


B1 = anounceBirhthday("John", 30, 1993)
B1.displayBirthday();


# Python Class Properties
# Properties are variables that belong to a class. They store data for each object created from the class.
# class with properties:

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    def displayCar(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

c1 = Car("Toyota", "Corolla", 2020)
print(c1.make)
c1.displayCar()


# Class Properties vs Object Properties
# Properties defined inside __init__() belong to each object (instance properties).
# Properties defined outside methods belong to the class itself (class properties) and are shared by all objects:

class  Items: 
    














