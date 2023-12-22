import math
path = ("./myData/loans1.txt")
def readCsv(file_path):
    result = []

    def open_file():
        with open(file_path, mode='r') as file_object:
            file_lines = file_object.readlines()
        return file_lines
    file_data = open_file()
    print(file_data)
    print("\n")


    def header_line():
        header_line = []
        header_line= file_data[0].strip().split(",")
        return header_line
    header_data = header_line()
    print(header_data)
    print("\n")


    for lines in file_data[1:]:
        def file_lines(line_data):
            values = []
            for item in line_data.strip().split(','):
                if item == " ":
                    values.append(0.0)
                else:
                    try:
                        values.append(float(item))
                    except ValueError:
                        values.append(item)
            return values

    file_line_values = file_lines(lines)
    print("these are :\n")
    print(file_line_values)
    

    def create_dict():
        file_dict = {}
        for key, values in zip(header_data, file_line_values):
            file_dict[key] = values
        return file_dict
    file_data_dict = create_dict()
    print(file_data_dict)

    result = file_data_dict
    return result

data = readCsv(path)