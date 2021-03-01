def compute(miles, gallons):
    cost = 2.5
    total = cost * gallons
    return total

#main
print("Destination city?")
city = string(input())
print("Miles traveled?")
miles = float(input())
print("Gallons used?")
gallons= float(input())
total = compute(miles, gallons)
print("Destination: " + str(city))
print("Miles: " + str(miles))
print("cost of gallons:" + str(total))