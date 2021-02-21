print("What is the principle:")
principle = int(input())
print("Years?")
years = int(input)
if principle > 100000 and year ==5:
    interest = 6
    total = (principle * interest /100) / years
else:
    if principle >= 50000 and principle <= 100000 and year == 10 :
        interest = 5
        total = (principle * interest /100) / years
    else:
        if year == 5:
            interest = 4 
            total = ( principle * interest / 100) / years
        else: 
            interest = 2
            total = (principle * interest / 100) / years
print("Principle is:" + str(principle))
print("Interest rate is: " + str(interest))
print("Interest of first year is:" + str(total))
