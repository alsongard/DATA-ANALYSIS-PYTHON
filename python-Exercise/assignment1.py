"""
    ASSIGNMENT 1 FILE
"""

name = input("enter your names : \n")
age = input("Enter your age : \n")
android_Phone = True
#dictionary

person = dict(name = name, age = age, phone = android_Phone)

print("{} is aged {}, and owns an {}\n".format(person["name"], person["age"], "android phone" if person["phone"] else "Iphone"))

##LOOPS TO ITERATE

for key in person:
    print("Key : {} && Value : {}\n".format(key,person[key]))


"""
    assignment 1 problem 2
"""

myList = ["black", "blue", "darkBlue", 5, True]
        # index 0 ,  1,     2,        , 3, 4 total of 5 elements
print("the length of myList is {}".format(len(myList)))
print(myList)

print("My favourite color is {}".format(myList[0:3]))
print("Number of pets i have are {}".format(myList[3]))