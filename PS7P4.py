sumofgrosspay = 0
Numofemplyees = 0

response = input("Do you want to compute the gross pay of an employee? (Yes or No)") 

while response == "Yes":
  lastname = input("Enter employee's last name: ")
  hours = float(input("Enter the number of hours worked: "))
  payrate = float(input("Enter payrate: "))
  if hours > 40:
    grosspay = (40 * payrate) + (hours - 40) * rate * 1.5 * payrate
  else: grosspay = hours * payrate
  
  print("Gross pay: $", grosspay)
  
  sumofgrosspay = sumofgrosspay + grosspay
  Numofemplyees = Numofemplyees + 1
  
  response = input("Do you want to compute the gross pay of an employee? (Yes or No)")

avggrosspay = sumofgrosspay / Numofemplyees

print("Sum of all gross pay: $", sumofgrosspay)
print("Number of employees: ", Numofemplyees)  
print("Average gross pay: $", avggrosspay)