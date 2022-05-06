# 10162 - 전자레인지

t = int(input())

time = [300, 60, 10]
count = []

for i in range(3):
  count.append(t // time[i])
  t -= ((t//time[i]) * time[i])

if t != 0:
  print(-1)

else:
  for i in count:
    print(i, end=' ')
