name = input("Enter name")
cost = float(input("Enter cost of appliance"))

if cost > 1000:
  warrantee = 0.10
else:
  warrantee = 0.05

warranteeCost = cost * warrantee
total = cost + warranteeCost

print("Name ", name)
print("Cost of appliance is $ ", cost)
print("Warrantee cost ", warranteeCost)
print("Total: ", total)