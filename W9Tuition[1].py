def comp(credits):
  global tuition
  tuition = float(credits) * 250.00
#main
f = open("tuition.txt","r")
students = 0
total = 0
lastname = f.readline()
print("1 credit = 250 ea")
while lastname != "":
  print()
  credits = f.readline()
  comp(credits)
  print("Student's lastname: ", lastname)
  print("Tuition owed: ", format(float(tuition),'10,.2f'))
  students = students + 1
  total = total + tuition
  lastname = f.readline()
else: 
  print("Number of students:", students)
  print("Total tuiton: ",format(float(total),'10,.2f'))
f.close()