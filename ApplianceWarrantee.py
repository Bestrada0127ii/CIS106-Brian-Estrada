print("What is the name of the appliance?")
appliance = str(input())
print("What is the price of the appliance")
price = int(input())
if (price > 1000):
    tax = (price * 10) /100
else:
    tax = (price * 5) /100

totalPrice = price + tax
print("Your choosen appliance is: " + str(appliance))
print("The tax is: "+ str(tax))
print("The final price is: " + str(totalPrice))