def compute_square_footage(length, width, height):
  
  floorceling = 2 * length * width
  firsttwall= 2 * length * height
  secoundwalls = 2 * width * height
  totalsquarefootage = floorceiling + firsttwalls + secoundwalls
  return totalsquarefootage

def compute_paint_gallons(square_footage):
  paintgallons= square_footage / 50
  return paintgallons

r = input ("Would you like to compute the squarefootage of a room? Yes or no ")

while r == "Yes":
  length = float(input("Enter the length of the room in feet: "))
  width = float(input("Enter the width of the room in feet: "))
  height = float(input("Enter the height of the room in feet: "))
      
  totalsquarefootage = compute_square_footage(length, width, height)
  paintgal = compute_paint_gallons(squarefootage)
  
  print("The total of gallons of paint needed to paint the room is: ",)