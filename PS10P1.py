def computeforcast(month, sales):
  forecastPercent = 0.0

  if month in ("Jan, Feb, Mar"):
    forecastpercent = 0.10
  elif month in ("Apr, May, Jun"):
    forecastpercent = 0.15
  elif month in ("Jul, Aug, Sep"):
    forecastpercent = 0.20
  elif month in ("Oct, Nov, Dec"):
    forecastpercent = 0.25

  NextMonthSales = sales * (1 + forecastpercent)

  return NextMonthSales 
r = input ("Would you like to do the program? (Yes or No): ")

while r == "Yes":
  month = input ("Enter the month: ")
  sales = float(input("Enter the sales: "))
  lastname = input("Enter the last name: ")
  
  NextMonthSales = computeforcast(month, sales)
  print("Next month's sales are: ", NextMonthSales)
  r = input ("Would you like to continue? (Yes or No): ")