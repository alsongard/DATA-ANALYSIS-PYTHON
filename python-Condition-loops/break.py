myNumber = input("enter any number : \n")
i = 1
result = 1

while i <= int(myNumber):
    result = result * i 
    print("{}\n".format(result))
    if i == 42:
        print("magic number i {} has been reached. Exiting the iteration".format(i))
        break
    i = i + 1
    
print("Value of i is {}".format(i))
print("Value of factorial of {} is {}".format(i, result))
