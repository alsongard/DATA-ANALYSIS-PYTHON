# Given values
principal_amount = 1260000 - 300000  # Adjusted principal after down payment
annual_interest_rate = 0.10
loan_term_years = 8

# Convert annual interest rate to monthly and calculate total number of payments
monthly_interest_rate = annual_interest_rate / 12
total_payments = loan_term_years * 12

# Calculate monthly installment (EMI) using the formula
emi = (principal_amount * monthly_interest_rate * (1 + monthly_interest_rate) ** total_payments) / ((1 + monthly_interest_rate) ** total_payments - 1)

# Print the result
print("Monthly Installment (EMI): {}".format(emi))