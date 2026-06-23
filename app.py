import sys 
import random 

print(sys.version);
print("Hello World");


# Python Indentation
# Python uses indentation to indicate a block of code.
if 5 > 2:
  print("Five is greater than two!");
if 5 > 2:
  print("Five is greater than two!");


# Python Variables
x = 10
print(x)


# Python Statements
# A computer program is a list of "instructions" to be "executed" by a computer.
# In a programming language, these programming instructions are called statements.
# The following statement prints the text "Python is fun!" to the screen:

print("Python is fun!")

# Python Output / Print
print("Hello World!")
print('This will also work!')
print("Hello World!", end=" gerdedrg\n")


# Print Numbers
print(111111)
print(10 + 15)
print("I am", 35, "years old.")


"""
This is multi line comment 
"""

#Python Variables
K = "Kwabena"
y = "John"

print(K, y);


# Casting
# If you want to specify the data type of a variable, this can be done with casting.
nim1 = int(50)
stin = str("Hello World")

print(type(nim1))



# Case-Sensitive
a = 4
A = "Salty"

# Python - Variable Names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Multi Words Variable Names
# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"



# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"


# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John" 


# Python Variables - Assign Multiple Values

name, age , year = "John", 25, 2025;
print(name)


# Unpack a Collection
fruit = ["apple", "banana", "cherry"]
x, y, z = fruit
print(x)



# Python - Global Variables
# Global variables can be used by everyone, both inside of functions and outside.

Page = "Awesome"

def myFuncti():
  print("Python is " + Page)

myFuncti();



def myAge():
  age = 30
  print(age)

myAge()

def myLife():
  global lesson
  lesson = "Python is great!"

myLife()

print(lesson)


# Python Data Types
# In programming, data type is an important concept.

# Text Type: 	str
# Numeric Types: 	int, float, complex
# Sequence Types: 	list, tuple, range
# Mapping Type: 	dict
# Set Types: 	set, frozenset
# Boolean Type: 	bool
# Binary Types: 	bytes, bytearray, memoryview
# None Type: 	NoneType



# Python Numbers
# There are three numeric types in Python:

b =  1   #int 
c = 2.8  #float
d = 1j   #complex




# Type Conversion
# You can convert from one type to another with the int(), float(), and complex() methods:
T =  1 
#convert from int to float:
U = float(T)
print(U)
print(random.randrange(1, 10));

# Python Strings
print("Hello")


a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a) 

print(a[0])

# Looping Through a String
for x in "Gyamfi":
  print(x.upper())

  # String Length
print(len(a))

# Check String
print("Lorem" in a)


if("Lorem" in a):
  print("Yes, lorem is present")



# Slicing Strings
Item = "Hello World"
Itemb  =  "Django is great"
print(Item[2:6])
print(Item[2:])

# Negative Indexing
# Use negative indexes to start the slice from the end of the string:
print(Item[-5:-2])


# Python - Modify Strings
print(Item.upper()) #text to upper case
print(Item.lower()) #text to lower case
print(Item.strip()) # removes any whitespace from the beginning or the end
print(Item.replace("H", "J")) # replaces a string with another string
print(Item.split(",")) # returns ['Hello', ' World']
print(Item + Itemb) # concatenates two strings
print('Centered:',Item.center(1)) # returns a centered string
print(Item.casefold())# returns a casefolded string
print(Item.count("o")) # returns the number of times a specified value occurs in a string
print(Item.encode()) # returns an encoded version of the string
print(Item.format_map("{}")) # returns a formatted version of the string
print(Item.index("o")) 
print(Item.isalnum()) #Returns True if all characters in the string are alphanumeric
print(Item.isalpha())  #Returns True if all characters in the string are alphanumeric
print(Item.partition("3"))
print(Item.replace("h", "w"))
# Python - String Concatenation

# String Format
myAge =20
txt = f"My name is John, and I am {myAge} years old"
print(txt)

thePrice = 49
txt = f"The price is {thePrice} dollars"
print(txt)

# Escape Character
myTxt = "We are the so-called \"Vikings\" from the north."
print(myTxt)