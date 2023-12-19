"""
    Radha is buying a house at the cost of 1,260,000
    2 options:
        options 1:
                make a down payment of $300,000 and take an 8 year loan with an interest rate of 10% per annum (Compounded Monthly)
                for the remaining amount
        Option 2:
                take a 10 year loan with an interest rate  of  8% per annum (Compounden monthly) for the entire amount

    EMI = (P*r*(1+r)^n)/(1+r)^n - 1
    EMI monthly installment
    P is the principal amount(loan amount)
    r is the monthly interest rate(annual rate divided by 12 months)
    n is the total number of payments(loan term in months)
"""
amount = input("enter the amount of pay of house : \n")
duration = input("Enter the number of monts for payment : \n")
def calculateMonthlyInstallment(amount, time):
    durationTime = int(duration) * 12
    emi = int(amount) / durationTime
    print("the EMI is ${}".format(emi))

calculateMonthlyInstallment(amount, duration)
