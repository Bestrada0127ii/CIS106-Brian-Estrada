def compute(creditHours, districtCode):
    if districtCode == "O":
        price = 250
        tuiton = price * creditHours
    else:
        price = 550
        tuiton = price * creditHours
    return tuiton
#main
print("Last name?")
lastName = string(input())
print("credit hours?")
creditHours= float(input())
print("District code? (I, O)")
districtCode = string(input())
tuiton = compute(creditHours, districtCode)
print("Tuiton: " + str(tuiton))