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