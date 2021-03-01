def calculate(quantity, price):
    total = quantity * price
    if total > 10000:
        finalTotal = total - total * 10 /100
    else:
            finalTotal = total
    return finalTotal

#main
print("What is the quantity?")
quantity = int(input())
print("What is the price?")
price = float(input())
finalTotal = calculate(quantity, price)
print(finalTotal)