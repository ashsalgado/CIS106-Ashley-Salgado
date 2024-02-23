lastname = input("Enter employee last name: ")
salary = float(input("Enter employee salary: "))
joblevel = int(input("Enter employee job level: "))

if joblevel >= 10:
    bonusrate = 0.25
elif joblevel >= 5:
    bonusrate = 0.2
else:
    bonusrate = 0.1

bonus = salary * bonusrate

print("Employee last name:", lastname)
print("Bonus: $", bonus)