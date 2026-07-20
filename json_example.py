# JSON is a syntax for storing and exchanging data.
# JSON is text, written with JavaScript object notation.
# If you have a JSON string, you can parse it by using the json.loads() method.
import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y) 


# Convert from Python to JSON:

Person = {
    "name": "John",
    "age": 25,
    "city": "New York"
}


Person_json = json.dumps(Person)
print(Person_json)


Me = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
print(json.dumps(Me,  indent=4))