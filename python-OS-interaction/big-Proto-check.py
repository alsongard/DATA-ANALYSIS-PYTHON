import os
path = "./myData/loans2.txt"

#open and read file and return a list
def open_file():
    with open(path, mode='r') as file_object:
        file_list = file_object.readlines()
    return file_list

file_data = open_file()#return list
print(type(file_data))
print(file_data)
print("\n\n")
#obtain header statements
def header_obtain():
    header_list = []
    header_list = file_data[0].strip().split(",")
    return header_list

header_data = header_obtain()
print(type(header_data))
print(header_data)
print("\n\n")


#obtain values from file
def file_lines():
    values = []
    for item in file_data[1].strip().split(","):
        if item == " ":
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                value.sappend(item)
    return values
file_values = file_lines()
print(type(file_values))
print(file_values)
print("\n\n")


#create dictionary
def create_dict():
    file_dict = {}
    for key, values in zip(header_data, file_values):
        file_dict[key] = values
    return file_dict
file_data_dict = create_dict()
print(file_data_dict)











# print(os.listdir("./myData"))
# print(path in os.listdir("./myData"))