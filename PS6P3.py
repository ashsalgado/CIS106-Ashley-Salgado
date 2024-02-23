principle = float(input("Enter the principle amount of CD: "))
Maturity = float(input("Enter the year maturity of CD: "))

if principle > 100000 and Maturity == 5:
  interest = 0.06
elif principle >= 50000 and Maturity == 10:
  interest = 0.05
elif principle >= 50000 and Maturity == 5:
  interest = 0.04
else:
  interest = 0.02

firstyearinterest = principle * interest

print("Principle: ", principle)
print("Interest: ", interest)
print("First year interest: ", firstyearinterest)