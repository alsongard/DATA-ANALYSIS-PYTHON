import matplotlib.pyplot as plt
# import seaborn as sns

#example of data
apple_yields = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931]
plt.plot(apple_yields)
plt.show()

#adding years to the data
years = [2020, 2021, 2022, 2023, 2024, 2026]

#adding labels to the x and y axis
plt.xlabel("years")
plt.ylabel("apple yields")

plt.plot(years, apple_yields)
plt.show()

#adding another data set
years = list(range(2000,2012))#using list mthd frm python introduction
print(years)

# adding orange dataset
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896]
i = 0
while i < len(apples):
    print(f"the index is {i} and the value is {apples[i]}")
    i = i + 1

#plot the data of the 2 datasets
plt.plot(years, apples)
plt.plot(years, oranges)
plt.xlabel("Year of Production")
plt.ylabel("Fruit Production")
plt.show()

#chart title and legend
#for differentiation between the 2 lines of the different data set use legend 
#title for title of graph
plt.plot(years, oranges)
plt.plot(years, apples)
plt.xlabel("Year Production")
plt.ylabel("Fruit Production")
plt.title("Kanto Fruits Yield")
plt.legend(["oranges","apples"])
plt.show()


#line markers
#markers can be used in showing the data points of the data in a line. they are different data markers
plt.plot(years, apples, marker="o" ,c="red", ms=9)
plt.plot(years, oranges, marker="x", ls="dashed", lw=4)
plt.xlabel("Year Production")
plt.ylabel("Fruits of Yield")
plt.title("Kanto Fruit Production")
plt.legend(["apples", "oranges"])
plt.show()

#styling lines and markers
#the plt.plot() function supports many arguments for styling lines and markers
"""
Examples:
color | c - used to set color of line apple line -red
linestyle | ls - used to select type of line e.g dashed oranges - dashed
linewidth | lw - set the width/ thickness
markersize | ms - set size of markers
markerfacecolor | mfc - set color of marker
markeredgecolor | mec - set the edge width of markers
"""

#changing figure size
#use the plt.figure() to change size of figure
plt.figure(figsize=(12, 6))
plt.plot(years, oranges)
plt.show()
