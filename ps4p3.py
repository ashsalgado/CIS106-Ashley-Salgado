#input phase 
meal = float(input("Enter the total of the meal: "))
#process phase
tip15 = meal * 0.15
tip18 = meal * 0.18
tip20 = meal * 0.20
total15 = meal + tip15
total18 = meal + tip18
total20 = meal + tip20
#output phase
print("The total of the meal: ", meal)
print("The tip 15% is: ", tip15)
print("The total of the meal with tip is: ", total15)

print("The total of the meal: ", meal)
print("The tip 18% is: ", tip18)
print("The total of the meal with tip is: ", total18)

print("The total of the meal: ", meal)
print("The tip 20% is: ", tip20)
print("The total of the meal with tip is: ", total20)
