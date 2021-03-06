def comp():
    global total
    global tax 
    total = quantity * price
    tax = total * .07
#main
quantity = int(input("What is the quantity?\n"))
price = float(input("What is the unit price?\n"))
comp()
print("The total is: ", total)
print("The tax is: ", tax)