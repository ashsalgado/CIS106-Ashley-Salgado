def comptuition(credits, dcode):
  
  if dcode == "I":
    tuition = credits * 250
  elif dcode == "O":
    tuition = credits * 550
  else:
    return 0 
  return tuition
tuitiowed = 0 
totaltuitionowed = 0 
r = input("Do you want to enter tuition owed? (Y/N)? ")

while r == "Y":
  lname = input("Enter last name: ")
  credits = float(input("Enter credits taken: "))
  dcode = input("Enter district code (I or O): ")
  tuition = comptuition(credits, dcode)
  tuitiowed = tuition + tuitiowed
  totaltuitionowed = totaltuitionowed + tuition
  print("Student last name: ", lname)
  print("Tuition owed: $", tuition)
  r = input("Do you want to enter tuition owed? (Y/N)? ")
print("Total tuition owed: $", totaltuitionowed)