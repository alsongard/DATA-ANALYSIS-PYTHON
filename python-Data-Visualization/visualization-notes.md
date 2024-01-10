# DATA VISUALIZATION USING MATPLOT & SEABORN

## plot()
Example of Line Graph
the matplotlib module can be used for plotting simple charts such as line  and bar graphs. Import matplotlib module as shown below
``import matplotlib.pyplot as plt``
to plot use the ``plot()`` method which takes in the data set / array
given the data apple_yields = [1,2...] which is a list, draw line graph
``plt.plot(apple_yields)``
``plt.plot(years, apple_yields)``
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

### Line styles 
line styles can be used to edit how line graph appears
ls | linestyle - can be dashed or straight
``plt.plot(years, apples, marker='s' ls="--")``

### color
c | color - used to set the color of the line
``plt.plot(years, apples, c='k',  marker = "9", lw=9, ls="--")``

### figuresize()
the figuresize() can be used to set the size of the figure of the plot
``plt.figuresize(figsize=(width, height))``
plt is an alias of matplotlib

### marker
the markers is used to set the type of marker for the graph
the marker can be set to o,s .e.t.c for more information check [Seaborn markers]("")
``markers="s"`` 

### legend
The legend is used to describe the data represented in the graph.
Example: Can be used whereby a user is plotting 2 different datasets apples and oranges
``plt.legend(["apples","oranges"])

### title
Used to set the title of the graph
``plt.title("title-name")``

### load_dataset()
the load_dataset is a function provided by the seaborn library that can be used to load dataset files
``tips_df = load_dataset("tips)``

### roud()
the round function is used to round of numbers. It takes 2 arguments one the variable name and the other the number of decimal places to round off
`` var_rounded_number = round(var_name, 2)``