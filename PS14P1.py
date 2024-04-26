class employment:
  def __init__(self, first, last, pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'


  def bonus(self, rate):
    b = float(rate) * float(self.pay)
    return b

emp1 = employment('Corey', 'Schafer', 50000)

print(emp1.email)

print(emp_1.bonus(0.10))
print(emp_1.bonus(0.20))