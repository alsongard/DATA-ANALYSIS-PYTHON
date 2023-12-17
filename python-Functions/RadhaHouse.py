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

totalHouse = 1260000

def solution1():
    downPayment = 300000
    numberOfYears = 8
    interestPerYear = 10/100
    monthly_interest_rate = interestPerYear / 12
    totalMonth = 12 * numberOfYears
    principalAmount = totalHouse - downPayment
    monthlyInstallment = (principalAmount * monthly_interest_rate*(1+monthly_interest_rate)**totalMonth)/((1+monthly_interest_rate)**totalMonth -1)
    return(monthlyInstallment)
answer = solution1()
print(answer)

def solution2():
    monthlyInterestRate = (8/100)/12
    yearNumber = 10
    monthTotal = 12 * yearNumber
    monthlyInstallment = (totalHouse * monthlyInterestRate * (1+monthlyInterestRate)**monthlyInterestRate)/((1+monthlyInterestRate)**monthTotal - 1)
    return monthlyInstallment

answer = solution2()
print(answer)