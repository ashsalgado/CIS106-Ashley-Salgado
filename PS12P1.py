def displayarrays(lname):
  for i in range(0,10,1):
    print(lname[i])

def rdisplay(lname):
  for i in range(9,-1,-1):
    print(lname[i])

lname = ["Adams", "Baker", "Smith", "Davis", "Jones", "Kelly", "Wilson", "Brown", "Jones", "Miller"]

displayarrays(lname)
print("Reverse order")
rdisplay(lname)