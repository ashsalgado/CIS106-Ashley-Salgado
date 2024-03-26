def compute_ticket_price(miles):
  if miles >= 30:
      ticket_price = 12
  elif miles <= 20:
      ticket_price = 10
  elif miles <= 10:
      ticket_price = 8
  else:
      ticket_price = 5

  return ticket_price
totalprice = 0

r = input("Do you want to compute train ticket price? (Yes/No): ")

while r == "Yes":
  lastname = input("Enter your last name: ")
  miles = int(input("Enter miles from downtown Chicago: "))

  ticket_price = compute_ticket_price(miles)
  totalprice = totalprice + ticket_price

  print("Ticket price: ", ticket_price)
  r = input("Do you want to compute train ticket price? (Yes/No): ")

print("Sum of all ticket prices: ", totalprice)