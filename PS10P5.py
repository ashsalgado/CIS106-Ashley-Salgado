def compute_assessed_value(county, market_value):
  if county == 'Cook':
      assessed_value_percent = 0.90
  elif county == 'DuPage':
      assessed_value_percent = 0.80
  elif county == 'McHenry':
      assessed_value_percent = 0.75
  elif county == 'Kane':
      assessed_value_percent = 0.60
  else:
      assessed_value_percent = 0.70

  assessed_value = market_value * assessed_value_percent
  return assessed_value


total_market_value = 0
total_assessed_value = 0

r = input("Do you want to compute assessed value of a home? (Yes/No): ")

while r == "yes":
  county = input("Enter the county of the home: ")
  market_value = float(input("Enter the market value of the home: "))

  assessed_value = compute_assessed_value(county, market_value)

  total_market_value = total_market_value + market_value
  total_assessed_value = total_assessed_value + assessed_value

r = input("Do you want to compute assessed value of a home? (Yes/No): ")

print(f"Total market value of all homes $" , total_market_value)
print(f"Total assessed value of all homes $", total_assessed_value) 