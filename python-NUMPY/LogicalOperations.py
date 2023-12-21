import numpy as np

arr2 = np.array([
    [1,2,3],
    [3,4,5]
])
arr3 = np.array([
    [2,2,3],
    [1,2,5]
])

print(arr2==arr3)
result = (arr2 == arr3).sum()
print(result)

#indexing in npArrays
arr4 = np.array([
    [[11, 12, 13, 14], 
     [13, 14, 15, 19]], 
    
    [[15, 16, 17, 21], 
     [63, 92, 36, 18]], 
    
    [[98, 32, 81, 23],      
     [17, 18, 19.5, 43]]])

print("\n\n")
print("the shape of arr4 is {} and its valuel is : \n {}".format(arr4.shape, arr4))
print(arr4[1,1,2])
print("\n")
print("print the following ranges [1:, 0:1, :2]")
print(arr4[1:, 0:1, :2])