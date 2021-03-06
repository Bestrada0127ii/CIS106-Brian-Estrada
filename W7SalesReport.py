def comp():
    global commission
    global nextYear
    nextYear = sales * 5 /100
    if sales > 100000:
        commission = sales * 10 / 100
    else:
        commission = sales * 5 /100
#main
lastName = str(input("Last name?\n"))
sales = float(input("Sales?\n"))
comp()
print("Commission: ", commission)
print("Next year commission: ", nextYear)
