def sales_report (sales):
  if sales > 100000.00:
    per = 0.10
    
  elif sales <= 100000.00:
    per = 0.05
  commission = sales * per
  nextyears = sales * 1.05
  return commission,nextyears

salesperson = input("Enter salesperson's name ")
lastname = input("Enter salesperson's last name ")
sales = float(input("Enter sales amount "))
commission,nextyears = sales_report(sales)
print ("This is your commission", commission)
print ("This is your next years report ", nextyears)

