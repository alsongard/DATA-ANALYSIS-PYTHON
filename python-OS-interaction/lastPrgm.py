#open file
with open("./myData/loans1.txt", mode="r") as fileObject:
    print(fileObject.read())
    #the code above interprets new line characters 
with open("./myData/loans1.txt", mode='r') as file_Object:
    data_list = file_Object.readlines()

    #the code resultin a list of the file's data

#acquire header
print("\n")
def header_Obtain(header_line):
    headers = header_line.strip().split(",")
    return headers
header_data = header_Obtain(data_list[0])
print(header_data)
print("\n")


def values_Obtain(data_lines):
    values = []
    for item in data_lines.strip().split(','):
        if item == " ":
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values
line_data = values_Obtain(data_list[1])
print(line_data)
print("\n")


def create_item_dict(header, values):
    result = {}
    for header,values in zip(header, values):
        result[header] = values
    return result

data_dictionary = create_item_dict(header_data, line_data)
print(data_dictionary)
print("\n")

def readCsv(path):
    result = []
    with open(path, mode='r') as fileObject:
        lines = fileObject.readlines()
        headers = header_Obtain(lines[0])

        for data_line in lines[1:]:
            file_values = values_Obtain(data_line)
            item_dict = create_item_dict(headers, file_values)
            result.append(item_dict)

    return result


filePath = "./myData/loans1.txt"
allFileData = readCsv(filePath)

print(allFileData)



