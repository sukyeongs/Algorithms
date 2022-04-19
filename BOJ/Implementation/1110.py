# 더하기 사이클 - Implementation

n = int(input())

num = n
cnt = 0

while True:
    sum = (num // 10) + (num % 10)
    new = ((num % 10) * 10) + (sum % 10)
    cnt += 1
    if new == n :
        break
    num = new

print(cnt)