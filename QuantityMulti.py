print("Quantity?")
quantity = int(input())
if quantity >= 1000 :
    unitPrice = 3
    extendedPrice = quantity * unitPrice
else: 
    unitPrice = 5 
    extendedPrice = quantity * unitPrice
tax = 7 * extendedPrice / 100
total = extendedPrice + tax
print("Your quantity is " + str(quantity))
print("The unit price is "+ str(unitPrice))
print("The extended price is "+ str(extendedPrice))
print("The tax is "+ str(tax))
print("The final price is "+ str(total))