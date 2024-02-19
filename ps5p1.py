itemqty = float(input("Enter the number of items: "))

if itemqty >= 1000:
  unitprice = 3.00
else:
  unitprice = 5.00

extprice = itemqty * unitprice
tax = extprice * 0.07
total = extprice + tax

print("The extended price is: $", extprice)
print("The tax is: $", tax)
print("The total is: $", total)