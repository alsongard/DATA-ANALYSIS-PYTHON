
path = "./myData/loans1.txt"
def open_file(path):
    with open(path, mode='r') as fileObject:
        file_lines = fileObject.readlines()
    return file_lines
all_file_lines = open_file(path)

# print(type(all_file_lines))
# print(all_file_lines)
# for item in all_file_lines:
#     print(item)

def header_obtain():
    header_items = all_file_lines[0].strip().split(",")
    return header_items
file_headers = header_obtain()
def file_values():
    values = []
    for item in all_file_lines[1].strip().split(","):
        if item == " ":
            values.append(0.0)
        else:
            try:
                values.append(float(item))
            except ValueError:
                values.append(item)
    return values
list_values = file_values()
print("list values are : \n")
print(list_values)
print("header values are : \n")
print(file_headers)


def create_dict():
    file_dict = {}
    for value, header in zip(list_values, file_headers):
        file_dict[header] = value
    return file_dict
results = create_dict()
print(results)
