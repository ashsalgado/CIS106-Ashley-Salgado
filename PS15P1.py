class employee:

  def __init__(self,first,last,pay):
    self.first = first
    self.last = last
    self.pay = pay
    self.email = first + '.' + last + '@company.com'

  def bonus(self,rate):
    b = float(rate) * float(self.pay)
    return b


class maneger(employee):
  def longtermbonus(self):
    return 0.4 * float(self.pay)


maneger1 = maneger('jane','doe',5000)
emp1 = employee('corey','schafer',5000)

print(maneger1.first)
print(maneger1.longtermbonus())