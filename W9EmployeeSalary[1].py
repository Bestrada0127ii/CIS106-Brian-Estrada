f = open("EmployeeData","r")
tbonus = 0
c = 0
lastname = f.readline()
while lastname != "":
    print()
    salary = f.readline()
    print("Employe last name: ", lastname)
    print("Employee salary: $", format(float(salary),'10,.2f'))
    Bonus = float(salary) * .10
    print("Employee Bonus: $",format((Bonus), '10,.2f'))
    tbonus = tbonus + Bonus
    c = c + 1
    lastname = f.readline()
f.close
