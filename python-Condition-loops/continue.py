#continue statement is used to skip lines of code in a literal

myNumber = input("Enter any number : \n")
result = 1
i = 1
while i <= int(myNumber):
    i = i + 1#why it runs in a loop when 
    if i % 2 == 0:
        print("Even values of i : {}".format(i))
        print("\n")
        continue
    elif i % 3 == 0:
        print("Odd values of i : {}".format(i))
        print("\n")
        continue
    elif i % 5 == 0:
        print("i Values divisible by 5 : {} ".format(i))
        print("\n")
        continue
    
    print("Prime value of i {}".format(i))
    result = result * i 
    


print("Value of result is : {} \n".format(result))