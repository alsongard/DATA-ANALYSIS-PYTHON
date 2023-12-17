#filter even numbers using function
userNumber = input("enter any the last number of a range : \n")
userList = []
for i in range(int(userNumber)):
    userList.append(i)

print(userList)

def filterEvenNumber(a_list):
    evenNumbers = []
    for number in a_list:
        if number % 2 == 0:
            evenNumbers.append(number)
    return evenNumbers

evenList = []
evenList = filterEvenNumber([1,2,3,4,5,6,7,8,9,10])
print(evenList)