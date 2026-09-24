principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate of interest: "))
time = float(input("Enter time in years: "))
n = int(input("Enter compounds per year: "))

amount = principal * (1 + rate / (100 * n)) ** (n * time)
compound_interest = amount - principal

print("Compound Interest:", compound_interest)
print("Total Amount:", amount)
