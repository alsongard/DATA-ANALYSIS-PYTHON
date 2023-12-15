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
the insert() can be used to data to a list at a given index
the remove() takes in a item word is a list
the  pop() uses an index to remove an item from a list
one can check an item using in "item2bechecked" in mylist

"""
 
print("\n\n")
myFav = ["Polo g", "Wakadinali", "Christian Gates"]
print("His favourites  artist are {}".format(myFav))
result = "Polo g" in myFav
print(result)##return true

newArtist = input("Enter another favoutite artist name :  \n")
myFav.append(newArtist)
newArtist = input("Enter another favoutite artist name :  \n")
myFav.insert(1,newArtist)
print(myFav)

##concatenate lists
students = ["gard", "hello", "earth", "jupiter"]
new_students = ["odin", "thor", "saturn"]
all_students = students + new_students
print("items in new_students are : \n {}".format(new_students))
print("items in students are : \n {}".format(students))

print("Combination of the 2 above lists is done using + sign\n\tall_students: \n {}".format(all_students))

##copy() method
#copy allStudents to newLists
newLists = all_students.copy()
print("item in newlists are : \n {} ".format(newLists))

##reverse a list can be performed in two ways
#reverse() method
myFav.reverse()
print("the reverse of myFav artist is : \n {}".format(myFav))
#providing list with a step -1 mylist["start":"stop":"step"]
print("reverse of the new students is : \n {}".format(myFruits[::-1]))


##sort() method - use to sort a list
myFav.sort()
print(myFav)

##sorted() use this to sort a list
sortedData = sorted(myFav)
print("sorted data in myFav is : \n {}".format(sortedData))


##ascending and descending order
myNumbers = [1,10,9,5,6,2,5,21,13,16,11,19,30]
#to sort the list in ascending order
print("the myNumbers list will be sorted from ascending and descending order\nuse sorted or sort method and then on descending use reverse")
sortedLists = sorted(myNumbers)
print("the sorted list is  in ascending order: \n {}".format(sortedLists))
print("the sorted list in descending order is : \n{}".format(sortedLists[::-1]))