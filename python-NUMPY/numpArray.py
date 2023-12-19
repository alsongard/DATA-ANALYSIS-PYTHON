import numpy as np

#conversion of an arpython list into an array
kanto = np.array([73, 61, 43])
print(kanto)
#check type
print("the type of the array above is {}".format(type(kanto)))
#conversion to numpy array
weight = np.array([0.3, 0.2, 0.5])
print("the array weight has values of {} and is of type {}".format(weight, type(weight)))

#numpy Operations
"""
    numpy arrays can be used in several operations
    bit wise element multiplication in file numpy-Example.py can be easily done if 2 list are np arrays
    Example:
            np.dot(1rst Array, 2nd Array)
            return an array of the result
        or
            np.dot(1rst Array, 2nd Array).sum()
            return a sum of the multiplication of the np arrays
"""

print("\n")
print(np.dot(kanto,weight))

myArray = kanto * weight
print(type(myArray))
print(myArray.sum())

#another example

array1 = np.array([1,2,3,4])
array2 = np.array([5,6,7,8])
print("Another example {}".format(np.dot(array1,array2)))