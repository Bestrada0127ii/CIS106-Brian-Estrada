print("Enter the number of bookrs order")
quantity = int(input())
print("Enter the cost of a book")
price = int(input())
total = price * quantity
if total <= 50:
    print("shipping is 25$")
    finalTotal = 25 + int(total)
    print("Your total is:" + str(finalTotal))
else:
    print("Shipping is free")
    print("Your total is " + str(total))