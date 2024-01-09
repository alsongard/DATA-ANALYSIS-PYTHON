# DATA VISUALIZATION USING MATPLOT & SEABORN

## plot()
Example of Line Graph
the matplotlib module can be used for plotting simple charts such as line  and bar graphs. Import matplotlib module as shown below
``import matplotlib.pyplot as plt``
to plot use the ``plot()`` method which takes in the data set / array
given the data apple_yields = [1,2...] which is a list, draw line graph
``plt.plot(apple_yields)
plt.plot(years, apple_yields)``
In addition, the plot() function can be used to set the type of marker, line style, marker size e.t.c

### Addition of labels to axis
to add respective labels for the data presented use:
the xlabel("name_of_axis") and ylabel("name_of_axis") property
plt.xlabel("Year")
plt.ylabel("apple_yields")

### Plotting Multiples lines
years = list(range(2000,2012))
apple = [1, 23, 31, 51, ....]
oranges = [1, 23, 31, 51, ....]
plt.plot(years, oranges)
plt.plot(years, apple)
plt.xlabel("years")
plt.ylabel("fruit yields")

### Chart Title and Legend
use
plt.title("name_of_title")
plt.legend(["dateset1", "dataset2"])
the legend is used to show which line represent the dataset

### Line styles 
line styles can be used to edit how line graph appears
ls | linestyle - can be dashed or straight
c | color - used to set the color of the line
marker - used to set how the marker points appear can be s=square , c=circle
lw | linewidth - used to set the line thickness

``plt.plot(years, apples, marker = "s", lw=9 ls="dashed")

## figuresize()
the figuresize() can be used to set the size of the figure of the plot
``plt.figuresize(figsize=(width, height))``
plt is an alias of matplotlib

## marker


## legend

## title

