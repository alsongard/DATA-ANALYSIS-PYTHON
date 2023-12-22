import os 
from urllib.request import urlretrieve

#create a directory
#already created
# os.makedirs("./myData", exist_ok=True)

#download the required files and open using with function
url1 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans1.txt'
url2 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans2.txt'
url3 = 'https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef/loans3.txt'

# urlretrieve(url1, './myData/loans1.txt')
# urlretrieve(url2, './myData/loans2.txt')
# urlretrieve(url3, './myData/loans3.txt')

print("Verify if file exists in myData")
print(os.listdir("./myData"))
print("\n")

#open the file using with method
with open("./myData/loans2.txt", mode='r') as file2:
    #read a file line by line
    file_contents2 = file2.readlines()
    print(file_contents2)





