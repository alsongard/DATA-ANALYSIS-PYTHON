"""
    in a nested for loop, useful for looping in a list of a list or a sequence of a sequence
    brilliance in the following statements
"""

myList = [ {"name": "gard", "age":23, "gender":"male"}, {"name": "alson", "age":23, "gender":"male"}]

for item in myList:
    print("the dictionary is {}".format(item))
    for key in item:
        print("the key is {} and value is {}".format(key, item[key]))


months = ["January", "February", "March"]
for item in months:
    for day in item:
        if item == "January":
            for i in range(32):
                day = i
        elif item == "February":
            for i in range(28):
                day = i 
        else:
            for i in range(31):
                day = i 

    print("the month is {} and days are {}".format(item, day))

print(type(day))
