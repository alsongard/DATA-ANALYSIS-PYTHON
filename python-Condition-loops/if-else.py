"""
if (condition):
    statement1
    statement2
else:
    statement1
    statement2
"""
myNumber = input("enter any number that is divisible by 3 : \n")

if int(myNumber) % 3 == 0:
    print("the number {} is divisible by 3".format(myNumber))
else:
    print("the number {} is not divisible by 3".format(myNumber))


print("\n\n")
print("working with strings, tuples and dictionaries using if else statement")
musketeers = ("Athos", "Pothos", "Aramis")
candidate = "D'Artagnan"
if candidate in musketeers:
    print("the candidate {} is in the musketeers".format(candidate))
else:
    print("the candidate {} is not in the musketeers".format(candidate))