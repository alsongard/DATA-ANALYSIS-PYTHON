"""

EXERCISE
A travel company wants to fly a plane to the Bahamas. Flying the plane costs 5000 dollars. So far, 29
people have signed up for the trip. If the company charges 200 dollars per ticket, what is the profit made by the
company? Create variables for each numeric quantity and use appropriate arithmetic operations

"""

planeCost = 5000
ticket = 200
passengers = input("enter the number of passengers to travel : \n")

profit = None

totalCost = int(passengers) * ticket

profit = totalCost - planeCost
print("cost of flying a plane to bahamas is 5000$ and a ticket costs 200$.\nCalculate the amout of profit from {} passangers".format(profit))
print("\tProfit made by the airplane agency is {}".format(profit))