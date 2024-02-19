item = input("Enter the item name: ")
quantity = input(f"Enter the quantity")

if item == "A":
  Unit_price = 10.00
else:
  Unit_price = 20.00

Total_price = int(quantity) * Unit_price

print("item ", item)
print("unit_price ", Unit_price)
print("extended price: ", Total_price)