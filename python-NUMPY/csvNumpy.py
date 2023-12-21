import numpy as np
import urllib.request
"""
    working with csv files and using concatenate, reshape and np.matmul()  or @ functions
    comma seperated value files use a comma as a delimiter for fields within the file
    convert file use:
    np.genfromtxt()
"""
urllib.request.urlretrieve('https://gist.github.com/BirajCoder/a4ffcb76fd6fb221d76ac2ee2b8584e9/raw/4054f90adfd361b7aa4255e99c2e874664094cea/climate.csv','climate.txt')

#convert weights into an nparray()
weights = [0.3, 0.2, 0.5]
weights_np = np.array(weights)
print(f"the weights_np is {weights_np}, its data type is {type(weights_np)}, its shape is {weights_np.shape} and using dtype returns {weights_np.dtype}\n")
# print("the weights_np is {} and is date type is {} and it's shape is {} and using dtype returns {}", format(weights_np, type(weights_np),weights_np.shape, weights_np.dtype))


#to convert our file  we use
climate_data = np.genfromtxt("climate.txt", delimiter=",", skip_header=1)
print(f"the type of climate_data is {type(climate_data)}")
print("shape of climate_data  is {}\n".format(climate_data.shape))
print(climate_data)
#to perform the multiplication use @, np.matplot()
yields = climate_data @ weights_np
print("shape of yields is {}\n".format(yields.shape))
#concatenate
climate_result = np.concatenate((climate_data, yields.reshape(10000,1)), axis=1)
print(climate_result)
#to save it
np.savetxt("climateResult.txt",climate_result, fmt='%.2f', delimiter=":", header="temperature, Rainfall, Humidity, CropYields", comments=" ")