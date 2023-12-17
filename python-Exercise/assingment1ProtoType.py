"""
    ASSIGNMENT 1 FILE
"""
##better system to assignment1.py
name = input("enter your names : \n")
age = input("Enter your age : \n")
android_Phone = input("enter the type of your phone : \n")

if android_Phone == "android":
    phoneType = True
elif android_Phone == "iphone":
    phoneType = False
#create dictionary
person = dict(name = name, age = age, result = phoneType)

print("{} is {} aged, and own a {}".format(person["name"], person["age"], "Android Phone" if person["result"] else "Iphone"))