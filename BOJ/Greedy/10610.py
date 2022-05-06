# 10610 - 30

n = list(input())
sum = 0

for i in n:
  sum += int(i)

if '0' not in n or sum%3 != 0:
  print(-1)

else:
    n.sort(reverse = True)
    for i in n:
      print(i, end='')
