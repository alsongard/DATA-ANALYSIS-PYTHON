import seaborn as sns
import matplotlib.pyplot as plt
import urllib.request
from IPython.display import display
import pandas as pd


"""
    we will use the iris flower dataset which privides measurement of sepals and perals of 3 species of flowers

"""



#load data to pandas Dataframe

flowers_df = sns.load_dataset("iris")
print(flowers_df)
with pd.option_context("display.max_rows", 150):
    display(flowers_df)

print(f"the type of flowers in the flowers_df dataframe is {flowers_df.species.unique()}")


# visualization of the relationship between the sepal length and sepal width
plt.plot(flowers_df.sepal_length, flowers_df.sepal_width)
plt.show()

#try to acquire only one flower type
setosa_flower_df = flowers_df.species == "setosa"

versicolor_flower_df = flowers_df.species == "versicolor"

virgin_flower_df = flowers_df.species == "virginica"
print(virgin_flower_df)

flower_virgin_df = flowers_df[virgin_flower_df]
flower_versicolor_df = flowers_df[versicolor_flower_df]
flower_setosa_df = flowers_df[setosa_flower_df]

print("The flower species which is virgin is  : ")
print(flower_virgin_df)
print('\n')
plt.plot(flower_setosa_df.sepal_length, flower_setosa_df.sepal_width, c="r")
plt.plot(flower_versicolor_df.sepal_length, flower_versicolor_df.sepal_width, c="b")
plt.plot(flower_virgin_df.sepal_length, flower_virgin_df.sepal_width, c="k")
plt.legend(["setosa", "versicolor", "virgin"])
plt.title("Setosa flower Measurements")
plt.show()

#from the above results it is difficult to determine the relationship between the setosa.sepal_length, setosa.sepal_width
#hence we use the sns.scaterplot() function to use a scatter plot 