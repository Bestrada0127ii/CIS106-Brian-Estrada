def comp(quantity, price, discount):
    global discounted
    global newtotal
    total = quantity * price
    newtotal = total * discount / 100
    discounted = total - newtotal
#main
quantity = int(input("What is the quantity?"))
price = float(input("What is the price?"))
discount = float(input("What is the discount rate?"))
comp(quantity, price, discount);
print("Total is", total)
print("The discount is", newtotal)
print("Discounted price is ", discounted)
