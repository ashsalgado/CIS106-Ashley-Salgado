p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
totint = 0.0
print("Year        Begging Balance        Ending Balance")

for x in range(1, 6, 1):
  i = p * r
  totint = totint + i
  endbal = p + i
  print(x, "          ", p, "                ", endbal)
  p = endbal

print("Total interest earned", totint)