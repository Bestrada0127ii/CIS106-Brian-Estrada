def comp():
    global average
    global handicap
    basis = int(input("What is the basis score?\n"))
    percentage = int(input("What is the percentage?\n"))
    average = (gameOne + gameTwo + gameThree)/3
    handicap = basis - average * (percentage /100)

#main
name = str(input("What is the bowlers name?\n"))
gameOne = int(input("Score of the first game?\n"))
gameTwo = int(input("Score of the second game?\n"))
gameThree = int(input("Score of the third game?\n"))
comp()
print("Name: ", name)
print("Average: ", average)
print("Handicap: ", handicap)