import numpy as np
"""
    Another examples of ease and performance of numpy operations
"""
array1 = list(range(1000000))#result in a list of 0 - 999,999
array2 = list(range(1000000))#result in list of 1,000,000 - 1,999,999
#convert to nump array
array1_np = np.array(array1)
array2_np = np.array(array2)

print("the type of array1_np is {} and for the array1 is {}".format(type(array1_np), type(array1)))
print("the type of array2_np is {} and for the array2 is {}".format(type(array2_np), type(array2)))

#check method to give details of the time taken to perform an executable string

def elementWiseMultiplication(arr, ar):
    for x,z in zip(array1, array2):
        result = 0
        result += x * z
    return result
loop_Answer = elementWiseMultiplication(array1,array2)
print(loop_Answer)

np_Answer = np.dot(array1_np, array2_np)
print(np_Answer)

