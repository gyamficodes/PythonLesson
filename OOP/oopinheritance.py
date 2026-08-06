# # Python Inheritance
# Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.Python Inheritance
# Inheritance allows us to define a class that inherits all the methods and properties from another class.
# Parent class is the class being inherited from, also called base class.
# Child class is the class that inherits from another class, also called derived class.


class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printName(self):
        print(self.firstName, self.lastName)

X = Person("John", "Doe");
X.printName();

# //child class
class Student(Person):
    pass


J = Student("Mike", "Olsen")
J.printName()






