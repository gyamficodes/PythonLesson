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


# Python Booleans
# Booleans represent one of two values: True or False.
print(10 > 9)

voteAge = 18

if  voteAge >= 18:
  print("You can vote")
else:
  print("you cant vote")
  


def myReturn():
  return True
print(myReturn())

c = 200
print(isinstance(c, int))


# The Ternary Operator
num = 5

WKK = "Weekday" if num > 5 else "Weekend"
print(WKK)


# Python Identity Operators

print(10 is not 20)
print((6 + 3) - (6 + 3)) 



# Python Lists
myList = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(type(myList))

# Python - Access List Items
print(myList[0])
print(myList[-1])
print(myList[1:5])


# Python - Change List Items
thislist = ["apple", "banana", "cherry"]
rice = thislist[1] = "Rice"
print(rice)

# add items
laptop = ["Hp", "Dell", "Macbook"]
laptop.append("Asus")
print(laptop)



# Insert Items
# To insert a list item at a specified index, use the insert() method.
# The insert() method inserts an item at the specified index:

laptop.insert(1, "Lenovo")
print(laptop)


tropical = ["mango", "pineapple", "papaya"]

thislist.extend(tropical)
print(thislist)

# Python - Loop Lists

for x in thislist:
  print(x)


# Loop Through the Index Numbers
for i in range(len(thislist)):
  print(thislist[i])


p = 0
while p < len(thislist):
  print(thislist[p])
  p+= 1


  # Looping Using List Comprehension
[print(x) for x in thislist]

# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

for x in fruits:
  if "a" in x:
    print("newlist",x)


    # Python - Sort Lists
    # Sort List Alphanumerically
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1)

thislist2 = [100, 50, 65, 82, 23]
thislist2.sort()
print(thislist2)

# Customize Sort Function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)



# Python - Copy Lists
mylist = thislist;

# Use the slice Operator
# You can also make a copy of a list by using the : (slice) operator.
mylist = thislist1[:]
print(mylist)


# Method 	Description
# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list



# Python Tuples
myTuple = ("apple", "banana", "cherry")


for i in myTuple:
  print(i)

  for i in range(len(myTuple)):
    print(myTuple[i])


    c = 0
while c < len(myTuple):
  print(myTuple[c])
  c+= 1


indi = myTuple.index("banana")
print(indi)

# Create Tuple With One Item
# To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.

thisTuple = ("apple",)
print(thisTuple)


# The tuple() Constructor
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)


# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


# Python - Unpack Tuples
myfruits = ("apple", "banana", "cherry")
(green, yellow, red) = myfruits
print(green)



# Python Sets
theSet = {"apple", "banana", "cherry","banana"}
theSet.add("orange")
print(theSet)


for b in theSet:
  print(b)

# Create and print a dictionary:
  # Dictionaries are written with curly brackets, and have keys and values:

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

