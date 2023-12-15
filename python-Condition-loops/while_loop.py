"""
    for the while loop it executes a statement as long as the condition is met
    however prevent entering into a loop us

    structure:
    while condition:
        statement

    Factorial System
"""

myNumber = input("Enter any number : \n")
i = 1
result = 1

while i <= int(myNumber):
    result = i * result
    i = i + 1

print("the factorial of {} is {}".format(myNumber, result))