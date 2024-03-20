# *************************MUTABLE AND IMMUTABLE TYPES:*******************

#   In Python, the term "MUTABLE" refers to objects whose state or content can be changed after they are created. This means that the memory location (or reference) of the object remains the same, but the internal contents of the object can be modified. Lists, dictionaries, and sets are examples of mutable objects in Python.


# Proof of Mutable nature of Python:

mylistOne = [1,2,3]
mylisttwo = mylistOne
mylisttwo = [1,2,3]

#  although we have assigned 2nd list into same reference of 1st list but later on we changed/ move it to new refernce and due to this now chnages in 1st list wont reflected in 2nd list..

mylistOne[0] = 33 # due to mutable nature of list we can change this...

print(mylistOne[0])
print(mylisttwo[0])

# now you can see that we have already changed the value in first list but that thing is not reflected in the 2nd list..


# slicing of list and how they get transmitted
#  so in basically slicing when u do a slicing a copied part get sliced off..

l1 =  [1,2,3,4]
l2 = l1[:] # this is basically done to slice the complete string and store it to l2 but both have different location as l2 is copy of l1...
