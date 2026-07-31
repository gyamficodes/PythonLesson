import math


# name = input("Please enter your name: ")
# print(f"Hello, {name}! Welcome to the program.")

# age = input("Please enter your age: ")
# if age.isdigit():
#     age = int(age)
#     print(f"You are {age} years old.")
# j

# x = input("Enter a number:")

# #find the square root of the number:
# y = math.sqrt(float(x))

# print(f"The square root of {x} is {y}");

y = True
while y == True:
    x = input("Enter a number:")
    try:
        x = float(x);
        y = False
    except: 
        print("Please enter a valid number.")
    print("Thank You!");









