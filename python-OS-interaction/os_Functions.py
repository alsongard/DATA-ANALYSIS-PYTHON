import os
import urllib.request
"""
    the os library is used for interacting with the o.s and creating,deleting files//uses methods that interact
    with files and folders, executing system commands and working with environment variables
    use:
        os.getcwd() to print the current working directory
        os.listdir() to print a list of files in the directory by default if no argument is given
        os.makedirs("filepath&nameofFolder", exist_ok=True)
"""

print("To print the current directory use os.getcwd()")
print(f"The current working directory is {os.getcwd()}")
print("\n")
print("To list the directories in the file use os.listdir()")
print(f"the list of file or directories in this folder is {os.listdir()}")
print("\n")
# os.makedirs("./Data", exist_ok=True)
# print("Data" in os.listdir())

#download files and store them in Data directory
#use urllib.request.retrieve(url)
# urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef","./Data/loans1.txt")
# urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef", "./Data/loans2.txt")
# urllib.request.urlretrieve("https://gist.githubusercontent.com/aakashns/257f6e6c8719c17d0e498ea287d1a386/raw/7def9ef4234ddf0bc82f855ad67dac8b971852ef", "./Data/loans3.txt")

#to read data from file first open
file1 = open("./Data/loans1.txt", mode='r')
#to perfoming the actual reading
file_contents = file1.read()
print("file contents of file1 object")
print(file_contents)
print("\n")
file2 = open("./Data/loans2.txt", mode='r')
file3 = open("./Data/loans3.txt", mode='r')
print("\n")
print("File contents of file2 are: ")
file_contents2 = file2.read()
print(file_contents2)
print("\n")
print("File contents of file3 object are: ")
file_contents3 = file3.read()
print(file_contents3)

#ensure to close the file after opening it
file1.close()
file2.close()
file3.close()

