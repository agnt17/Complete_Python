# what is difference b/w repr, str, and print in python?

# repr():
# The repr() function returns a string representation of an object that is more suitable for debugging and development.
# It is meant to provide a clear and unambiguous representation of an object.
# The string returned by repr() should ideally be valid Python code that, when evaluated, would produce an object with the same value.
# Its like good for programmers

# str():
# The str() function returns a string representation of an object that is meant to be readable by humans.
# It is used to convert an object into a human-readable format.
# If a class defines both __str__() and __repr__() methods, str() will use __str__() if available, falling back to __repr__() if not.
#Its good for normal Humans.


# print():
# The print() function is used to display information on the console or standard output.
# It converts objects to strings using str() and displays them.
# It is commonly used for outputting information to the user or for debugging purposes.


# floor and trunc operator in python:
import math
a = 2.7
b = -2.7

print(math.floor(a)) # o/p: 2
print(math.trunc(a)) # o/p: 2

print(math.floor(b)) # o/p: -3
print(math.trunc(b)) # o/p: -2

# trunc basically puts u towards the 0 on number line whereas the floor puts to the smallest integer of that value.