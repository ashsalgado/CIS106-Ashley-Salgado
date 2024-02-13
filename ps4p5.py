#output phase
fixed = float(input("Enter fixed cost: "))
price = float(input("Enter price per unit: "))
cost = float(input("Enter cost per unit: "))
#process phase
break_even = fixed / (price - cost)
#output phase
print("Break-even point: ", break_even)
