# 동전 0 - Greedy Algorithm

n,k = map(int, input().split())
coin = list()
count=0

for i in range(n):
  coin.append(int(input()))

coin.sort(reverse=True)

for i in coin:
  count += k//i
  k %= i
  if k <= 0:
    break

print(count)
