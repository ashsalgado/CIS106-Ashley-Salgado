def calculatepayrate(jobcode):

  if jobcode == "L":
    payrate = 25.00
  elif jobcode == "A":
    payrate = 30.00
  elif jobcode == "J":
    payrate = 50.00
  else:
    return "Invalid job code"

  return payrate

def calculategrosspay(hours, payrate):
  if hours > 40:
    grosspay = (40 * payrate) + ((hours - 40) * (payrate * 1.5))
  else:
    grosspay = hours * payrate
  return grosspay

totalgrosspay = 0

r = input("Do you want to calculate pay? (Y/N)? ")
while r == "Y":
  lname = input("Enter last name: ")
  jobcode = input("Enter job code: ")
  hours = float(input("Enter hours worked: "))

  payrate = calculatepayrate(jobcode)
  grosspay = calculategrosspay(hours, payrate)

  totalgrosspay = totalgrosspay + grosspay

  print("Last name: ", lname)
  print("Gross pay: $", grosspay)

  r = input("Do you want to calculate gross pay? (Y/N)? ")

print("Total gross pay: $", totalgrosspay)