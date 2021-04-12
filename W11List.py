list = []
listTwo = [500, 600, 700, 800, 900]
grades = ['A', 'B', 'C', 'A', 'A', 'C']
repeat = []
name = ['Rizzo', 'Davis', 'Baez', 'Happ', 'Bryan']
n = int(input("Size of list? "))
for i in range(0, n):
   item = int(input("Integer: "))
   list.append(item)
list.insert(1,99)
list.extend(listTwo)
list.remove(800)
list.pop(2)
for i in grades:
    if(grades.count(i)>1 and i not in repeat):
        repeat.append(i)
print(list)
print(grades)
print('The repeating grades are')
for i in repeat:
    print(i,end=' \n')
print("Index of first B: ", grades.index('B'))
try:
    grades.index('f')
except ValueError:
      print("'F' is not on list")
listTwo.clear()
print('List Two:', listTwo)
name.sort()
print(name)
namer = ['Rizzo', 'Davis', 'Baez', 'Happ', 'Bryan']
namer.reverse()
print('Reverse: ',*namer)