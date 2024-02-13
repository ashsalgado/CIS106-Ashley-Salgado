#input phase
pricepershare = float(input("Enter price per share: "))
stockprice = float(input("Enter current stock price: "))
quantity = float(input("Enter quantity of stock: "))
#process phase
value = (stockprice - pricepershare) * quantity
#output phase
print("The value of the stock is $", value)
