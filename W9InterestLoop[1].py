def comp(principle, rate):
  annualInterest = principle * rate /100
  return annualInterest
#main
loop=input("Do you want to do the program? yes/no\n")
year = 0
while loop == "Yes" or loop == "yes":
  principle = float(input("Enter the principle\n"))
  rate = float(input("Enter the rate\n"))
  annualInterest = comp(principle,rate)
  for year in range(1, 5+1,1):
    total = principle + annualInterest
    year = year + 1
    print("Principle: ",principle)
    principle = total
print("Bye")