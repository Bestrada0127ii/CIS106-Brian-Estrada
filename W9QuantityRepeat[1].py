def comp(price, quantity):
    global extendedPrice
    extendedPrice = float(price) * float(quantity)
#main
f = open("list","r")
item = f.readline()
noofitems = 0
total = 0
while item != "":
  print()
  print("item: ",item)
  price = f.readline()
  print("Price per item: ", price)
  quantity = f.readline()
  print("quantity of item: ", quantity)
  comp(price,quantity)
  print("The total is:$ ", format(extendedPrice,'10,.2f'))
  noofitems = noofitems + 1
  total = extendedPrice + total
  item = f.readline()
else:
    average = float(total) / float(noofitems)
    print("Number of order: ", noofitems)
    print("Total: ", total)
    print("The average is: ", format(average,'10,.2f') )
f.close()
