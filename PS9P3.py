def compMilespergal(miles, gallons):

  if gallons == 0:
    return 0
  else: 
    return miles/gallons

count = 0 

r = input("Do you want to compute miles per gallon? (Y/N)?")

while r == "Y":
  city = input("Enter city name: ")
  miles = float(input("Enter miles driven: "))
  gallons = float(input("Enter gallons used: "))
  mpg = compMilespergal(miles, gallons)
  count = count + 1
  print("City: ", city)
  print("Miles: ", miles)
  print("Gallons per mile: ", mpg)
  r = input("Do you want to compute miles per gallon? (Y/N)?")

print("Number of entries: ", count)