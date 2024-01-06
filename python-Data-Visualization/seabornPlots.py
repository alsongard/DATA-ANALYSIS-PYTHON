import matplotlib.pyplot as plt
import seaborn as sns

#one can also plot graphs using the seaborn
#the seaborn.set_style("background/color", "rc")
#style = the style can be a dict or one of the flwing{darkgrid, whitegrid, white, ticks}

#example
sns.set_style("whitegrid")
sns.barplot(x=["A", "B", "C"], y=[1,3,3])
plt.show()

#to add seaborn library
sns.set_style("whitegrid")
# adding orange dataset
years = list(range(2000,2012))
apples = [0.895, 0.91, 0.919, 0.926, 0.929, 0.931, 0.934, 0.936, 0.937, 0.9375, 0.9372, 0.939]
oranges = [0.962, 0.941, 0.930, 0.923, 0.918, 0.908, 0.907, 0.904, 0.901, 0.898, 0.9, 0.896]

#rememberence
plt.figure(figsize=(12,7))
plt.plot(years,oranges, marker="s", ls="--", ms="7", color="red")
plt.plot(years,apples, marker="o", ls="-", ms="8", lw="3", color="k")
plt.legend(["oranges", "apples"])
plt.title("Fruits Production")
plt.xlabel("Fruits Production")
plt.ylabel("Year")
plt.show()

#also one could use the fmt which is the 3rd argument that specifies the marker, linestype and color
# set background to dark grid
sns.set_style("darkgrid")
plt.plot(years,apples, "s-r")
plt.plot(years, oranges, "o--")
plt.xlabel("Year")
plt.ylabel("Fruit Production")
plt.show()
