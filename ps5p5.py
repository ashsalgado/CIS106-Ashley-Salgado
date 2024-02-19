qty = int(input("Enter the quantity of the item: "))

if qty >= 1000:
   up = 3.00
else:
   up = 5.00 
  
extprice = qty * up
tax = extprice * 0.07
total = extprice + tax

print ("Quantity ordered", qty)
print ("Unit Price $", up)
print ("Extended Price is $", extprice) 
print ("Tax is $", tax)
print ("Total order $", total)