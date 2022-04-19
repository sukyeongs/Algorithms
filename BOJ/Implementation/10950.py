# A + B - 3 - Implementation

n = int(input())
result = list()
for _ in range(n):
  a, b = map(int, input().split())
  result.append(a+b)

for i in range(n):
  print(result[i])
