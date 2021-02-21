print("What part do you need?")
part = int(input())
print("What is the quantity of the part?")
quantity = int(input())
if part == 99:
    unitcost = 2
    total = quantity * unitcost
else:
    if part == 10 or part == 55:
        unitcost = 1
        total = quantity * unitcost
    else:
        if part == 80 or part == 70:
                unitcost = 3
                total = quantity * unitcost
        else: 
                unitcost = 5
                total = quantity * unitcost
print("The part number is: " + str(part))
print("The unit cost is:" + str(unitcost))
print("The total is:" + str(total))