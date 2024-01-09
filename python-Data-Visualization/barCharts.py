import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
"""
    using matplotlib to plot bar charts
    to plot a bar we  use the plt.bar() function to plot
    we can also plot several data values by using bottom argument in the plt.bar() function
"""
years = list(range(2000,2006))
apples = [0.35, 0.6, 0.9, 0.8, 0.65, 0.8]
oranges = [0.4, 0.8, 0.9, 0.7, 0.6, 0.8]

print(years)
plt.bar(years, oranges)
plt.title("Oranges Production")
plt.xlabel("Year of Production")
plt.ylabel("Orange Yields")
plt.show()

#to plot several data similar to a histogram
sns.set_style("whitegrid")
plt.bar(years, apples)
plt.bar(years, oranges, bottom=apples)
plt.legend(["apples", "oranges"])
plt.title("Fruit Production")
plt.show()
