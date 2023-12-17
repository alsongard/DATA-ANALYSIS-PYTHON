"""
    range() is used for getting a sequence of characters
    example 1:
    for number in range(20):
        print(number)
    
    example 2:
    startPoint,endPoint
    for number in range(3,20)"
        print()

    example3:
    startPoint,endPoint,interval

    also when knowing the index of a value in our lists
    syntax
    for i in len(sequence/list):
        print()
    using enumare function
    it takes the list as an argument
    for i,val in enumare(listName):

    also the one can use break,continue and pass statement in for loop
    continue - execute code and skip instruction and return to loop
    break - exit loop
    pass - empty loop

    nested and for or while loops, exercise condition

"""

for number in range(20):
    print(number)

print("\n\n")

for number in range(3,10):
    print(number)

#working with sequence/list
a_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
print("\n")
print("Elements or Items in our a_list are : {}".format(len(a_list)))
for i in range(len(a_list)):
    print("The value of the index {} is {}".format(i, a_list[i]))

#enumaration
programmingLanguages = ["Python", "HTML", "PHP", "C", "C++" ]
for i,val in enumerate(programmingLanguages):
    print("value at index {} is {}".format(i,val))

#continue
for i in range(len(programmingLanguages)):
    if programmingLanguages[i] == "C" or programmingLanguages[i] ==  "C++":
        print("the langueage {} is a low level programming langueage".format(programmingLanguages[i]))
        continue
    print("High level programming language : {}".format(programmingLanguages[i]))

#exit
for i in range(len(a_list)):
    if a_list[i] == "Thursday":
        print("I am very busy in {}".format(a_list[i]))
        break
    print("I work on these day {}".format(a_list[i]))