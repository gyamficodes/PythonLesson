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

myType = {
  "name": "Jonny",
  "quality": "vrrv",
  "age": 25,
}
print(type(myType))

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

# Python Collections (Arrays)
# There are four collection data types in the Python programming language:

#     List is a collection which is ordered and changeable. Allows duplicate members.
#     Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
#     Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
#     Dictionary is a collection which is ordered** and changeable. No duplicate members.


# Accessing  Items
model = thisdict["model"];

print(model)

if "brand" in thisdict: 
  print("Yes, 'brand' is one of the keys in the thisdict dictionary")


# Change Values
# You can change the value of a specific item by referring to its key name:

thisdict["year"] = 2018

# Adding Items
thisdict["color"] = "red"
# Removing Items
thisdict.pop("model")


print("dict",thisdict)


# loo  dic 
for x in thisdict:
  print(thisdict[x]) 

  # Python - Nested Dictionaries
  # A dictionary can contain dictionaries, this is called nested dictionaries.
  myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
} 
  

# loop through it 
for i, ele in myfamily.items():
  print(i)

  for y in ele:
    print(y + ':', ele[y])


 
    # Python Conditions and If statements
a = 30
b = 200

if(b > a):
  print("b is greater than a");


# Using Variables in Conditions
is_Login_in = True
if is_Login_in:
  print("Welcome back!")
elif is_Login_in == False:
    print("Logout")
else:
  print("create account")


day = 3

if day == 1:
  print("Monday")
elif day == 2:
  print("Tuesday")
elif day == 3:
  print("Wednesday")
elif day == 4:
  print("Thursday")
elif day == 5:
  print("Friday")
elif day == 6:
  print("Saturday")
elif day == 7:
  print("Sunday")
else:
  print("No day")



  # Python Shorthand If

if a > b: print("Come here")

# Short Hand If ... Else
num1 = 10
num2 = 20

print("num1 is greater than num2") if num1 > num2 else print("num2 is greater than num1")


# This is called a conditional expression (sometimes known as a "ternary operator").


# value_if_true if condition else value_if_false
l = 10
result = "yes" if l > 5 else "no"
print(result)

# Python Logical Operators
book1 = 20
book2 = 10

if book1 > book2 and book2 < book1:
  print("Both conditions are True")


if book1 > book2 and book2 > book1:
  print("At least one of the conditions is True")

if not book2 > book1:
    print("book2 is NOT greater than b")


# More Examples
username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

  # Python Nested If
myAge = 25

if myAge > 10:
   print("Above ten,")
   if myAge > 20:
      print("Above twenty,")
   else:
      print("Not above twenty,")



mudician = "blacksherif"

if mudician == "blacksherif":
  print("He is a Ghanaian musician")
  if mudician == " Drake":
    print("He is a Canadian musician")
  else:
    print("He is not a Canadian musician")
else:
  print("He is not a Ghanaian musician")


# Python Pass Statement
# The pass Statement
# if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.
if a > b:
  pass

# Python Match
# The match statement is used to perform different actions based on different conditions.

myDay = 1


match myDay: 
  case 1 | 2 | 3:
    print("Week Day")
  case 2:
    print("Tuesday")
  case 3:
    print("Wednesday")
  case 4:
    print("Thursday")
  case 5:
    print("Friday")
  case 6:
    print("Saturday")
  case 7:
    print("Sunday")
  case _:
    print("Invalid day")


# Python Loops
# Python has two primitive loop commands:
#     while loops
#     for loops


# The while Loop
# With the while loop we can execute a set of statements as long as a condition is true.


i = 1
while i <= 6:
  print(i)
  if i == 3:
    break
  i += 1
   

k = 1
while k < 6:
  k += 1
  if k == 3:
    continue
  print("continue",k)
else:
    print("k is no longer less than 6")


# Python For Loops
# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

fruits = ["apple", "banana", "cherry"]
for x in fruits:
   if x == "banana":
    continue
print(x)

for x in "apple":
  print(x)


# The range() Function
# To loop through a set of code a specified number of times, we can use the range() function,
for x in range(6):
  print(x)

# Nested Loops
# A nested loop is a loop inside a loop.

for i in range(4):
  print(i)
  for y in range(3):
    print("y",y)


# Python Functions
# A function is a block of code which only runs when it is called.
# A function can return data as a result.
# A function helps avoiding code repetition.

def my_function():
  print("Hello from a function")

my_function()


def getGreeting():
   return "Good Morning"

message = getGreeting()
print(message)

# Python Function Arguments
