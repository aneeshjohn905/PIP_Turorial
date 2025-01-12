print("Welcome to the Income Tax Calculator")
income = float(input("Enter your income "))

tax_amount = 0

if income <= 300000:
  tax_amount = 0
elif income > 300000 and income <= 700000:
  tax_amount = (income - 300000) * 0.05
elif income > 700000 and income <= 1000000:
  tax_amount = 20000 + (income - 700000) * 0.10
elif income > 1000000 and income <= 1200000:
  tax_amount = 50000 + (income - 1000000) * 0.15
elif income > 1200000 and income <= 1500000:
  tax_amount = 80000 + (income - 1200000) * 0.20
elif income > 1500000:
  tax_amount = 140000 + (income - 1500000) * 0.30

print("\t$€£₹¥₩₿₹¢¤ƒ₹฿₺₴₹₦₱₹")
print("\tTax amount is ₹"+str(tax_amount))
print("\t₹₱₦₹₴₺฿₹ƒ¤¢₹₿₩¥₹£€$")
