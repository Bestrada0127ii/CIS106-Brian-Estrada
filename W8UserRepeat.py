repeat = str(input("Want to do the program?\n"))
while repeat == "yes" or repeat == "Yes":
    lastName = str(input("last name?\n"))
    examOne = float(input("Exam one score?\n"))
    examTwo = float(input("Exam two score?\n"))
    average = (examOne + examTwo) / 2
    print("Last name: " + lastName)
    print("The average is: " + str(average))
    repeat = str(input("again?\n"))
print("Bye")