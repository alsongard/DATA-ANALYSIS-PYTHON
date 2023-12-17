#our list
tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]
#calculate the number of happy tweets
print("Number of tweets are {}".format(len(tweets)))
happyWords = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sadWords = ['sad', 'bad', 'tragic', 'unhappy', 'worst']

#VALUES & INDEX OF HAPPYWORDS LIST
print("Values and index of happyWords list\n")
for i in range(len(happyWords)):
    print("The value of index {} is {}".format(i, happyWords[i]))
print("\n")
#VALUES & INDEX OF SADWORDS LIST
print("Values and index of sadWords list\n")
for i in range(len(sadWords)):
    print("The value of index {} is {}".format(i, sadWords[i]))

#calculate number of tweets with happy words
#iterate over all statements in tweets
numberHappyTweets = 0

for item in happyWords:
    for userTweets in tweets:
        if item in userTweets:
            numberHappyTweets = numberHappyTweets + 1

print("The number of happy tweets in twitter are {}".format(numberHappyTweets))

#CHECK NUMBER OF TWEETS THAT HAVE WORD HAPPY
happyNumber = 0
for userTweets in tweets:
    if "happy" in userTweets:
        happyNumber = happyNumber + 1
print("the number of happy in all the tweets are : {}".format(happyNumber))
happyFraction = happyNumber / len(tweets)
print(happyFraction)
#CHECK NUMBER OF SAD TWEETS
sadNumber = 0
for item in sadWords:
    for userTweets in tweets:
        if item in userTweets:
            sadNumber = sadNumber + 1

print("the number of sad feedbacks are {}".format(sadNumber))
            

