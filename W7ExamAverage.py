def comp():
    global totalPoints
    global average
    totalPoints = examOne + examTwo + examThree
    average = totalPoints / 3
lastName = str(input("What is the last name?\n"))
examOne = float(input("What is the score of the first exam?\n"))
examTwo = float(input("What is the score of the second exam?\n"))
examThree = float(input("What is the score of the third exam?\n"))
comp();
print("Last name: ",lastName)
print("total points: ", totalPoints)
print("Average: ",average)