"""
    to declare a dictionary use curly braces or () method
    myDictionary = {"key":"value", "key":"value2}
    myDictionary = dict(key = "value", key = "value")

"""
#dictionary
myDictionary = dict(firstName = "gard", secondName = "alson", age = 23, gender = "male")
#or another way to declare a dictionary can be done
elements =  {"firstname":"Gard","secondName":"Alson","age":23, "maritalStatus":"single"}
print("the type of element is {}".format(type(elements)))
print(type(myDictionary))
for key in myDictionary:
    print("the dictionary's key is {} and it's value is {}".format(key, myDictionary[key]))

print("to access value only use dictionaryName.values()")

for item in myDictionary.values():
    print("the values of myDictionary are : {}\n".format(item))

cars = {"name":"ferrari", "type":"sports", "speed":220, "year":1997}
#print both key and value using items() method
for item in cars.items():
    print("the key and values of dictionary car is {}".format(item))

#the above method is not preffered
for key, value in cars.items():
    print("key is : {} and Value is {}\n".format(key, value))