#input phase
fistname = input("Enter your first name: ")
steps = float(input("Enter the number of steps you walked in a day: "))
#process phase
calories = steps * 0.25
#output phase
print("Hello", fistname)
print("You burned", calories, "calories")