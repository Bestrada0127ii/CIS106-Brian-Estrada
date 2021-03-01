def calculate(hits, atBats):
    average = float(hits) / atBats
    return average

#main
print("Last name?")
lastName = string(input())
print("Number of at-bats?")
atBats = int(input())
print("Number of hits?")
hits = int(input())
average = calculate(hits, atBats)
print("Battting average: " + str(average))