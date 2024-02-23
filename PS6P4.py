tickets = int(input("Enter number of concert tickets"))

if tickets >= 25:
  price = 50
elif tickets >= 10 and tickets <= 24:
  price = 60
elif tickets >= 5 and tickets <= 9:
  price = 70
else:
  price = 75

total = tickets * price

print("Number of tickets: ", tickets)
print("Price per ticket: $", price)
print("Total cost: $", total)
