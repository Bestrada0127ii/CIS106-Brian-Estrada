n = 20
fnOne = 0
fnTwo = 1
i = 0
print("series")
for i in range(n):
  print(fnOne)
  sum = fnOne + fnTwo
  fnOne = fnTwo
  fnTwo = sum
  i += 1