import numpy as np
"""
    in this we will check the shape, data , type, conversion of list to np arrays and perfom multiplication using element bitwise methods
    check shape:
            npArray.shape
    check data:

    to convert:
            np.array()
    to perform multiplication:
            @ method --->> npArray1 @ npArray2
        or
                np.matplot(nparray1, nparray2)
"""

climate_data = [
    [73, 67, 43],
    [91, 88, 64],
    [87, 134, 58],
    [102, 43, 37],
    [69, 96, 70]
]
#convert list to nparray
weights = np.array([0.3, 0.2, 0.5])
print("Weights is {} and it data type is {}".format(weights, type(weights)))
print("the shape of the np array weight is {}".format(weights.shape))

#convert to np Array
climate_np = np.array(climate_data)
print("climate_np is {} and it's data type is {}".format(climate_np, type(climate_np)))
print("The shape of the climate_np array is {}".format(climate_np.shape))

#to check on the data type of the nparray use, .dtype 
print("the data type of the weights np array is {}".format(weights.dtype))
print("the data type of the climate_np array is {}".format(climate_np.dtype))

#to perform matrix multiplication use the method matmul(2args) or @ method
print("the crop yield is {}".format(np.matmul(climate_np, weights)))
print("the cro yield is {}".format(climate_np @ weights))