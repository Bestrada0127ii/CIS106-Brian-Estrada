print("What is the orginal price?")
price = float(input())
print("What is the discount percentage?")
discount = float(input())
discounted =  (discount * .01) * price
print("Your discount is: " , float(discounted) , "$")
finalprice = price - discounted
print("Your final price is :" , float(finalprice) , "$")

