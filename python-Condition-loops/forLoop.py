"""
    the for  loop is used to iterate or loop through sth such as list,array,tuple,dictionaries

    for item in sequence:
        statement
    
"""
#list
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for item in week:
    print(item)

#character
favourite = "Partin_Ways"
for item in favourite:
    print(item)

#tuples
mytuple = "HI", "there", "myname", "is", "gard"
# print(type(mytuple)) == tuple 
for item in mytuple:
    print(item)

#dictionary
myDictionary = dict(firstName = "gard", secondName = "alson", age = 23, gender = "male")
#or another way to declare a dictionary can be done
elements =  {"firstname":"Gard","secondName":"Alson","age":23, "maritalStatus":"single"}
print("the type of element is {}".format(type(elements)))
print(type(myDictionary))
for key in myDictionary:
    print("the dictionary's key is {} and it's value is {}".format(key, myDictionary[key]))