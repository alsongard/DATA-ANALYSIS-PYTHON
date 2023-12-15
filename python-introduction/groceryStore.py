"""
bag of  ice = 1.25;
20% profit
500 bags of ice sells

calculate profit
"""
price = 1.25
print("the price of a bag is {}".format(price))
profit_per_Bag = ((20/100) * price)
print("Profit per bag is {}".format(profit_per_Bag))
bags = 500
print("Number of bags sold to day is {}".format(bags))
total = bags * price
print("the total price of {} bags is : {}".format(bags, total))
newProfit = profit_per_Bag * bags
print("total profit made from selling 500 bags is {}".format(newProfit))
print(type(newProfit))
##market system for calculating profits, analysing sells in an organization and draw charts