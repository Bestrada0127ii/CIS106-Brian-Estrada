def comp(grossIncome):
    global tax, owed
    if grossIncome > 500000:
        tax = 30
    else: 
        if grossIncome > 200000:
            tax = 20
        else:
            tax = 15
    owed = grossIncome * tax /100
#main
repeat = str(input("Do you want to do the program?\n"))
while repeat == "yes" or repeat == "Yes":
    grossIncome = float(input("What is the gross income?"))
    comp(grossIncome)
    print("Gross income: ", grossIncome)
    print("Tax rate: ",tax)
    print("Owed: ", owed)
    repeat = str(input("Again?\n"))
print("bye")