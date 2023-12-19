import numpy

myArray = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14],
    [15,16,17,18],
    [19,20,21,22]
]
print(type(myArray))
print(len(myArray))
i = 0
j = 0
while i < len(myArray):
    print(myArray[i])
    for item in myArray[i]:
        print(item)
    i = i + 1