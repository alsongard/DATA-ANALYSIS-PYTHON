"""
tuples is an immutable list - it's values cannot be modified or changed
tuples are created with a  ()brackets
conversion of tuples to list and vice versa
use tuples() or list() functions to convert the respective data
"""

print("\t\tTUPLES AND TUPLE'S METHODS")

mytuple = ("j. cole", "polo g", "dreamville", "lil durk", "lil baby")
print(mytuple)

#ONE CANNOT MODIFY A TUPLE
#myLists.remove("polo g") #results in error

#conversion to list and tuples

print("data type of  mytuple is {}".format(type(mytuple)))

print("\t\tCONVERSION")
print("Conversion from tuple to list use list() function and from list to tuples use tuple() method.")

myLists = list(mytuple)
print("data type of below statement is {}".format(type(myLists)))
print("Data in myLists is: \n{}".format(myLists))

ourTuples = tuple(myLists)
print("data type of below statement is {}".format(type(ourTuples)))

print("Data in ourTuples is : \n{}".format(ourTuples))