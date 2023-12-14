##this file will be used for all practises 
myFruits = ["banana", "lemon", "apple", "oranges", "waterlemons"]
print("type of var myFruits is {}".format(type(myFruits)))
print("the length of the myFruits variable is {}".format(len(myFruits)))

data = ["james", 23, None, 3.14, ["banana", "lemon", "apple", "oranges", "waterlemons"], "fruits", 3<=5]
#list in python can be used to store different data types
print("\n\n\n")
print("the length of our list is {}".format(len(data)))
print("ELements of a list")
print(myFruits[2:5])
print(data)

#ranges in python end before the last index of the array or list
"""

the append() can be used to add data to a list after the last element
the insert() can bue used to data to a list at a given index

"""

print("\n\n")
myFav = ["Polo g", "Wakadinali", "Christian Gates"]
print("His favourites  artist are {}".format(myFav))

newArtist = input("Enter another favoutite artist name :  \n")
myFav.append(newArtist)
newArtist = input("Enter another favoutite artist name :  \n")
myFav.insert(1,newArtist)
print(myFav)
