class Employee:
  def __init__(self, first, last, pay,rate):
    self.first = first
    self.last = last
    self.pay = pay
    self.rate = rate
    self.email = first + '.' + last + '@company.com'
  def fullname(self):
    return '{} {}'.format(self.first, self.last)
  def bonus(self):
    return self.rate * self.pay
empOne = Employee('Corey', 'Schafer', 50000,.15)
empOne.fullname()
empOne.bonus()
print(Employee.fullname(empOne))
print('Bonus:', Employee.bonus(empOne))