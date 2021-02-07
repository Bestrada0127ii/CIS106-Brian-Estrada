
print("What is your score for exam 1?(60%)")
exam1 = float(input())
print("What is your score for exam 2? (40)")
exam2 = float(input())
finalGrade = ((60 * exam1)+(40*exam2))/(60+40)
print("Your final grade is:" , float(finalGrade))