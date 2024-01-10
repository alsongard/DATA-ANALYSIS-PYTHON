import pandas as pd
import seaborn as sns
from IPython.display import display
import matplotlib.pyplot as plt

"""
    Use the tips data set from seaborn
    Use the  seaborn load_dataset() function to laod file data such as csv
    sns.barplot() - used to draw the bar

"""
tips_df = sns.load_dataset("tips")
print(tips_df)
print("\n")

# with pd.option_context("display.max_rows", 245):
#     display(tips_df)
#get data in which customer is smoker

tips_smoker_df = tips_df.smoker == "Yes"
print("Boolean values for smokers")
print(tips_smoker_df)#returned boolen value

print("\n")
print(tips_df[tips_smoker_df])#return only true values
with pd.option_context("display.max_rows", 98):
    print("The data for user who are smokers ")
    display(tips_df[tips_smoker_df])

#try to get the highest bill
result = tips_df.total_bill.max()
print(f"the highest bill paid is {result}")#returned 50.81

#to obtain users who paid 50.81/result
    # highest_user = tips_df.total_bill == result
    # print(highest_user)
    # i = 0
    # for item in highest_user:
    #     if item == "True":
    #         print(item)
    #     i = i + 1

#try to get bar info for total values or totol_bill in each day
saturday_bool_df = tips_df.day == "Sat"
saturday_data_df = tips_df[saturday_bool_df]
saturday_total = saturday_data_df.total_bill.sum()
saturday_total = round(saturday_total, 2)

print(f"the total bill on saturday is {saturday_total}")
print(f"total bills is {tips_df.total_bill.sum()}")

#use the same process and then plot chart for each day
thursday_bool_df = tips_df.day == "Thur"
thursday_data_df  = tips_df[thursday_bool_df]
thursday_total = thursday_data_df['total_bill'].sum()
print(f"The total bill for thursday is {thursday_total}")

#Friday
friday_bool_df = tips_df.day == "Fri"
friday_data_df = tips_df[friday_bool_df]
friday_total = friday_data_df.total_bill.sum()
print(f"the total bill for friday is {friday_total}")

#Sun
sunday_bool_df = tips_df.day == "Sun"
sunday_data_df = tips_df[sunday_bool_df]
sunday_total = sunday_data_df.total_bill.sum()
print(f"the total bill on sunday is {sunday_total}")

days = ["Sunday", "Thursday", "Friday", "Saturday"]
# plt.plot(days, thursday_total)

#check data type of day
print("the data type of day in tip_df is {} and dtype is {}".format(type(tips_df.day), tips_df.day.dtype))
# tips_df["day"] = pd.to_datetime(tips_df.day).day
# print(tips_df) did not work

#draw a bar graph to visualiza the average bill for the days
#one way to do this is to compute the day-wise averages #exercise
saturday_average_bill = saturday_data_df.total_bill.mean()
print(f"the average total_bill of is {saturday_average_bill}")
sns.set_style("darkgrid")
sns.barplot(x='day', y="total_bill", data=tips_df)#the graph represents the average/mean total_bill in each of the days
plt.show()
#the line cutting through each bar represents the amount of variation between the values of total_bill

#try to plot the average total bill for the male and female
#sns.barplot(y="axis-data", x="axis-data", hue="comparison", data=dataframeobject)
sns.barplot(y="total_bill", x="day", hue="sex", data=tips_df)
plt.show()

#acquire data from female only
female_bool = tips_df.sex == "Female"
female_data_df = tips_df[female_bool]
print(female_data_df)
print(f"the average total bill of female is {female_data_df.total_bill.mean()}")

#one can also plot the graph horizontally
sns.barplot(y="day", x="total_bill", hue="sex", data=tips_df)
plt.show()