counter = 10
num = []

while counter > 0:
  x = int(input())
  num.append(x)
  counter -= 1

sum = 0
for l in num:
  sum += l

print(sum)