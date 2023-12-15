"""
    this is a file to show all tutorials for string methdos
    string methods
    upper(), capitalize(), lower(), split()

    string name or a variable name

    "monday".upper()
    "monday".capitalize()
    "MONDAY".lower()
    "MONDAY".replace("mon", "tues")
    instead of a string use a variable name
    myvar.method()
"""

#capture the day name of the day from the user
print("User the following methods used in string data types\n\tupper()\n\tcapitalizae()\n\tlower()\n\treplace()\n\tsplit()")
print("Use the replace keyword to remove the data in the variable 'day' ")

day = input("Enter the day of the day : \n")
print("day entered by the user is {}".format(day))
print("to replace the day entered we use the replace() method, changed rom {} to {}".format(day, day.replace(day, "wednesday")))
myFruits = "watermelon, lemon, banana, apple, carrot, tomatoes, mangoes"
music = input("Enter your favourite music : \n")
print("favourite music of user is {} and applying upper() methods yields {}".format(music, music.upper()))
print("favourite music of user is {} and applying capitalize() methods yields {}".format(music, music.capitalize()))
print("favourite music of user is {} and applying lower() methods yields {}".format(music, music.lower()))
print("the string will be converted to a list below :\n  {}".format(myFruits))
print("converted : \n {}".format(myFruits.split(",")))


fname = input("Enter full names of user : \n")
age = input("enter age of user : \n")
course = input("enter the course your taking: \n")
print("testing on data concatenation")
print(type(age))
print("His name is " + fname + "and age is " + age + " pursuing " + course) 