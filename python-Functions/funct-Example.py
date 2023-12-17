"""
    to define a function use the keyword
    def functionName ():
        statement
    
"""

def sayHello():
    print("Hi there")
    print("Welcome to Python Programming Language \n")

#to run a function call it
sayHello()

##function arguments local scope variables
# def getDetails():
#     name = input("enter user name :\n")
#     age = input("Ente user age : \n")
#     gender = input("Enter user gender : \n")
#     print(type(name))

name = input("enter user name :\n")
age = input("Ente user age : \n")
gender = input("Enter user gender : \n")
def greetUser(name, gender, age):
    if gender ==  "male":
        print("Welcome to the men's club {}".format(gender))
        if int(age) >= 18:
            print("your are an adult and more is expected from you as a young man")
        else:
            print("do the wright thing at the right time")
    elif gender == "female":
        print("Welcome to the female club {}".format(gender))
        if int(age) >= 18:
            print("your are an adult and more is expected from you as a young lady")
        else:
            print("do the wright thing at the right time")



greetUser(name, gender, age)