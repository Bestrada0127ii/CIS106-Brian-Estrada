def display(names):
    for i in names:
        print(i)
def reverse(names):
    names.reverse()
    for i in names:
        print(i)

names = ['smith', 'Johnson', 'Williams','Jones', 'Brown','Davis','Miller', 'Wilson', 'Moore','Walker']
print("Names: ")
display(names)
print("Reverse: ")
reverse(names)
