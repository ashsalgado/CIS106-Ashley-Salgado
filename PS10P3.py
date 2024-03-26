def compute_out_the_door_price(msrp, make, model, electric_vehicle):
  percentoff = 0.0
  
  if make == 'Honda' and model == 'Accord':
      percent_off = 0.10
  elif make == 'Toyota' and model == 'Rav4':
      percent_off = 0.15
  elif electric_vehicle == 'Y':
      percent_off = 0.30
  else:
      percent_off = 0.05

  discountprice = msrp - (msrp * percent_off)
  tax = discountprice * 0.07
  total = discountprice + tax
  
  return total
total = 0
total_sales = 0


r = input("Do you want to compute the out-the-door price for an automobile? (Yes/No): ")

while r == "Yes":
 make = input("Enter the make of the automobile: ")
 model = input("Enter the model of the automobile: ") 
 electric_vehicle = input("Is it an electric vehicle? (Y/N): ")
 msrp = float(input("Enter the MSRP "))
 
out_door_price = compute_out_the_door_price(msrp, make, model, electric_vehicle)

total = total + msrp
total_sales = total_sales + out_door_price

r = input("Do you want to compute the out-the-door price for an automobile? (Yes/No): ")

print("The out-the-door price is $", out_door_price)
print(f"Total MSRP of all cars: $" ,total)
print(f"Total sales price of all cars: $", total_sales)
