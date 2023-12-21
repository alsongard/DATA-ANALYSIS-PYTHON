import numpy as np
arr3 = np.array(
    [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 13],
        [13, 14, 15, 16]
    ]
)
print(f"the  arr3 is {arr3} and it's data type is {type(arr3)}")
print("/n/n")

arr2 = np.array(
    [
        [2, 4, 5, 7],
        [11, 13, 17, 19],
        [23, 29, 31, 37],
        [41, 43, 47, 53]
    ]
)
print(f"the  arr2 is {arr2} and it's data type is {type(arr2)}")

#addition to scalar vector
print("\n\n")
print("Addition of arr2 to to scalar vector 3:")
print(arr2 + 3)


print("\n\n")
print("performing array multiplication with scalar quantity")
print(arr2 * 3)

print("\n\n")
print("performing arr3 modulus with scaler")
print(arr3 % 3)

print("\n\n")
print("performing element wise multiplication")
print(arr3 * arr2)

#BROADCASTING
#broadcasting is whereby arithmetic operations can be used between 2 arrays of same shape but different dimensions

arr5 = np.array([2,3,5,7])
#use arr3
#check shape of arr3 and arr5
print("\n\n")
print("shape of arr3 is {}".format(arr3.shape))
print("shape of arr5 is {}".format(arr5.shape))
print(arr3 * arr5)

