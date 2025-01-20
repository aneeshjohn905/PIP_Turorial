deposit = float(input("Enter the initial deposit amount: "))
interest_rate = float(input("Enter the interest rate: "))
year = int(input("Enter the number of years to be calculated: "))
opening_bal=0
interest_amount=0
deposit_amount=0
print("%-6s %-16s %-10s %-16s" % ("Year","Opening_Balance", "Interest", "Closing_Balance"))
for i in range(1, year + 1):
    opening_bal = deposit
    interest_amount = deposit * (interest_rate/ 100)
    deposit += interest_amount
    deposit_amount = deposit
    print("%-6d %-16.2f %-10.2f %-16.2f" % (i, opening_bal, interest_amount, deposit_amount))
