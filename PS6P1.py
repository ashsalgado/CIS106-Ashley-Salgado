qty = int(input("Enter the quantity of the item: "))

if qty > 10000:
  price = 10.00
elif qty > 5000:
  price = 20.00
else:
  price = 30.00

extprice = qty * price
tax = extprice * 0.07
total = extprice + tax

print("Extended price $:    ", extprice)
print("Tax $:               ", tax)
print("Total $:             ", total)