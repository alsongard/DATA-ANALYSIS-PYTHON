"""
    the if elif is a short form of if else if statement
    used for checking multiple conditions

    create grade system
"""

grade = input("Enter the your grade : A,B,C,D\n")

if grade == 'A':
    print("Great and Awesome work done, continue performing better!")
elif grade == 'B':
    print("Nice work continue with the hard work you put in")
elif grade == 'C':
    print("Average there is a lot of room for improvement, believe in yourself")
elif grade == 'D':
    print("You can do better, continue with hardwork")


##also it can be combined with the else statement
myNumber = input("enter any number you might think of : \n")
if int(myNumber) % 2 == 0:
    print("the number {} is divisible by 2".format(myNumber))
elif int(myNumber) % 3 == 0:
    print("the number {} is divisible by 3".format(myNumber))
elif int(myNumber) % 5 == 0:
    print("the number {} is divisible by 5".format(myNumber))
else:
    print("the number {} is not divisible by 2,3 or 5".format(myNumber))