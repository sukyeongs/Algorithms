# 1026 - 보물
n = int(input())
result = 0

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse=True)

for i in range(n):
  result += (A[i] * B[i])


print(result)
