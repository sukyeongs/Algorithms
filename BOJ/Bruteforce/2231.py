# 2231 - 분해합
n = int(input())
gen = 0

for i in range(1, 1000001):
  nList = list(map(int, str(i)))
  total = 0

  total = i + sum(nList)
  if total == n:
    gen = i
    break

print(gen)
