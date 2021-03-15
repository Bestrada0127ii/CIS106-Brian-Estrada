def comp(price, quantity):
    global extendedPrice, discount, discounted, tax
    extendedPrice = price * quantity
    if extendedPrice > 10000:
        discount = .1 * extendedPrice
    else:
        if extendedPrice > 5000:
            discount = .05 * extendedPrice
        else:
            discount = .02 * extendedPrice
    discounted = extendedPrice - discount
    tax = discounted * .07
#main
repeat = str(input("Do you want to do the programm?\n"))
while repeat == "Yes" or repeat == "yes":
    item = str(input("Item name?\n"))
    price = int(input("What is the price of " + item + "?\n"))
    quantity = int(input("What is the quantity of " + item + "?\n"))
    comp(price,quantity)
    print("Extended price:", extendedPrice)
    print("Discount: ", discount)
    print("Discounted: ", discounted)
    print("Tax: ", tax)
    repeat = str(input("Again?\n"))
print("bye")