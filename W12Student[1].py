class student:
  def __init__(self, first, last, code, credits):
    self.first = first
    self.last = last
    self.code = code
    self.credits = credits
  def calculate(self):
    if self.code == 'I' or self.code == "i":
      return self.credits * 250
    if self.code == 'o' or self.code == 'O':
        return self.credits * 500
    else:
        return ('Wront input. I or O')
#main
first= input("First name?")
last= input("Last name?")
code= input("Code I or O?")
credits = float(input("Number of credits?"))
stud = student(first, last, code, credits)
stud.calculate()
print(student.calculate(stud))