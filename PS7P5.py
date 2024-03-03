sumofdiscamt = 0

response = input("Do you want to compute total order with discount? (Yes or No)")
while response == "Yes":
  qty = float(input("Enter quantity"))
  price = float(input("Enter price $" ))
  extprice = qty * price
  if extprice > 10000.00:
    discamt = extprice * 0.25
  else: discamt = extprice * 0.10

  Disctotal = extprice - discamt
  sumofdiscamt = sumofdiscamt + discamt

  print("Extended price is $", extprice)
  print("Discount amount is $", discamt)
  print("Discounted total is $", Disctotal)
  response = input("Do you want to compute another order ?")

print("Sum of all discounts is $", sumofdiscamt)