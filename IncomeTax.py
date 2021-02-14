print("User's Last Name?")
lastName = str(input())
print("Number of dependents?")
dependents = int(input())
print("What is your gross income?")
grossIncome = int(input())
discount = dependents * 12000
adjustedGrossIncome = grossIncome - discount
if (adjustedGrossIncome > 50000):
    incomeTax = (20 * adjustedGrossIncome) / 100
else:
    incomeTax = (10 * adjustedGrossIncome) / 100
if (incomeTax < 0):
    incomeTax = 100
else:
        incomeTax = (10 * adjustedGrossIncome) / 100
print("Last Name:" + str(lastName))
print("Gross Income: "+ str(grossIncome))
print("Number of Dependents: "+ str(dependents))
print("Adjusted Gross Income: " + str(adjustedGrossIncome))
print("Income Tax: "+ str(incomeTax))