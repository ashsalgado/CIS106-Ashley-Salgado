books = input("Enter number of books ordered: ")
cost = input("Enter cost per books $")

Total = int(books) * int(cost)

if Total > 50:
  ship = 0
else:
  ship = 25

Final = Total + ship

print("shipping charges: $", ship)
print("Order total: $", Final)