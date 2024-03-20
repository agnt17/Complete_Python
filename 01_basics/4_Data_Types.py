# Data types in python

# Python data types are dynamic means we need not to declare a variable. The intrepretor automatically assigns the datatype during runtime. 

username = "Aditya"
print(len(username))
# o/p: 6

print(dir(username)) 

# this dir function returns all the methods associated with the particular object.


# O/p: ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__getstate__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'removeprefix', 'removesuffix', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# List in python********************

mylist = [1, "Aditya", 3.14, True] 
print(mylist)

# List and arrays are same in Python 

# In python list can store any type of data

# Dictionaries in Python********************

myDict = {"name": "Aditya", "age": 20, "Course": "B.Tech in Information Technology"}
print(myDict)
print(myDict.keys())
print(myDict.values())


# Tuples in Python*****************
myTuple = (1, 2, 3)
print(myTuple[0])

# There is no as such data type in python... means if u declare a variable then at the time of declaration we don't declare its data type but when its value is assigned inside the memory then the data type is defined.

# The beauty of "is" operator....

# is operator basically tells that if both are on same memory location or not...
# eg:

l1 = [1,2,3,4]
l2 = l1
l3 = l1
l3 = [1,2,3,4]
#  both l1 and l2 points at same location..

print(l1 is l2) # o/p: true
print(l1 is l3) #o/p: false
