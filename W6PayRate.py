def calculate(hours, payRate):
    grossPay = hours * payRate
    return grossPay

def compute(code):
    if code == "J":
        payRate = 50
    else:
        if code == "A":
            payRate = 30
        else:
            payRate = 25
    print("Pay rate is:" + str(payRate))
    return payRate

#main
print("Last name?")
lastName = string(input())
print("Job title?")
jobTitle = string(input())
print("Hours worked?")
hours = float(input())
print("Code: L, A, J")
code= string(input())
payRate = compute(code)
grossPay = calculate(hours, payRate)
print("Last Name: " + str(lastName))
print("Gross pay: " + str(grossPay))