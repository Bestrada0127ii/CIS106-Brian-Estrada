print("Number or tickets")
tickets = int(input())
if tickets >= 25:
    price = 50
    total = ticket + price
else:
    if ticket >= 10 and tickets <= 24:
        price = 60
        total = ticket * price
    else:
        if ticket >= 5 and ticket <= 9:
            price = 70 
            total = price * tickets
        else:
            price = 75
            total = tickets * price
print("Number of tickets: " + str(tickets))
print("Price of a ticket: " + str(price))
print("The total is: " + str(total))