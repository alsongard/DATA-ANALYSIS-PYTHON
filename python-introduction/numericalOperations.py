"""
** - to power
() - specify execution of operations
/ - division
% - return remainder of division
"""


print("Performing mathematical operation")
print(2**3)
print(4%2)#expected value is 0

print("Enter any two numbers that will be perfomed by the following operations and there result displayed")
num1 = input("Enter any number : \n")
num2 = input("Enter any number : \n")
#input method captures user's data as string type hence not adversable to perform numerical operation with it
#also when using format() method ensure to pass in parameter place holder
result = int(num1) * int(num2)
print("result of multiplication  : {}".format(result))
result = int(num1)/int(num2)
print(f"result for division in {result}")
result = int(num1)%int(num2)
print(f"result of the remainder is : {result}")
result = int(num1)**int(num2)
print("result of power is {}".format(result))