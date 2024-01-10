import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display
import pandas as pd

'''
    In this section we shall deal with another data set provided by seaborn called heatmap
    Heatmap - Used to visualize 2 dimensional data
    the flights data set is used to show the number of people in airport
'''

#get the dataset using load_dataset() function

# flight_df = sns.load_dataset("flights").pivot("month", "year", "passengers")
flights_df = sns.load_dataset("flights").pivot("month", "year", "passengers")
print(flights_df)
#using heatmap to visualize the  footfall at the airport
plt.title("No of Passengers (1000s) ")
sns.heatmap(flights_df)
plt.show()
print("\n")

flight_data_df = sns.load_dataset("flights")
print("this is the data in flight_data_df with no pivot function")
print(flight_data_df)
# with pd.option_context("display.max_rows", 147):
#     display(flight_data_df)

print("\n")
#display with actual values for each block in the heatmap
#cmap and annot
plt.title("No of passengers")
sns.heatmap(flights_df, fmt="d", annot=True, cmap="Blues")
plt.show()

