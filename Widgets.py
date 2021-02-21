print("What is the quantity")
quantity = int(input())
if quantity > 100000:
    price = 10
    total = quantity * price
else:
     if quantity >= 50000:
        price = 20
        total = quantity * price
     else:
        price = 30 
        total = quantity * price
tax = 7 * total / 100
extendedPrice = tax + total
print("Your quantity is: " + str(quantity))
print("The cost per item is" + str(price))
print("Your tax total is: " + str(tax))
print("Your final price is: " + str(extendedPrice))