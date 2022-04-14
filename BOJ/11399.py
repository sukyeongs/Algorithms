# ATM - Greedy Algorithm

n = int(input())
time = list(map(int, input().split()))
time.sort()
result = 0
total = 0

for i in range(n):
  result += time[i]
  total += result

print(total)
