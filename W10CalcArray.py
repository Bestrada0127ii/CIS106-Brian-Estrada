def exam(names,score): 
        for i in range(len(names)):
            print('name: '+ names[i] + ' score: ' + str(score[i]))
def max(score):
    maximum = score[0]
    for i in range(1, len(score)):
        if maximum < score[i]:
            maximum = score[index]
        return maximum
def min(score):
    minimum = score[0]
    for i in range(1, len(score)):
        if minimum > score[i]:
            minimum = score[i]
        return minimum
def comp(score):
    total = 0
    divider = 0
    for index in range(len(score)):
        total += score[index] 
        divider += 1
    average = total / divider
    return average
#main
names = ['smith', 'Johnson', 'Williams','Jones', 'Brown','Davis','Miller', 'Wilson', 'Moore','Walker']
score = [98, 87, 56, 67, 91, 82, 85, 74, 59, 84]
exam(names,score)
maximum = max(score)
minimum = min(score)
average = comp(score)
print('average is: ', str(average))
print('maximum: ' + str(maximum))
print('minimum: ' + str(minimum))