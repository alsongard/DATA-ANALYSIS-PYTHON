#use the keywork type to know the type of data 
fname = input("Enter users name : \n")
print(type(fname))

#multiline strings
a_music_pun = """
Hi there my name is Alexa a new predicting model for "guess"
"what kind of music do you like?"

I like listening to:
"Rnb, Trap, HipHOp"
"""

print(a_music_pun)


#len function is used to check the length of a string
print("the length of the variable a_music_pun is : {}".format(len(a_music_pun)))

#list() function that transform data to a list

music = "Rnb, Trap, HipHOp"
print(len(music))
print(list(music))

##in operator is used to check if a string contains a keyword or a pattern text
today = "Monday"
tommorow = "Tuesday"

print("day" in "Monday")
#return true if it contains data

##string methods
#depending on the data type of the variable each has it's own function
print("the data stored in the variable today is {} and when applied the capitalize method it result into {}".format(today, today.capitalize()))
print(today.upper())
