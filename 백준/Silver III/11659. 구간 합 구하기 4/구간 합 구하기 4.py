import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 수의 개수, M: 합을 구해야 하는 횟수
numbers = list(map(int, input().split()))

for i in range(N-1):
    numbers[i+1] += numbers[i]

for _ in range(M):
    start, end = map(int, input().split())
    if start == 1:
        print(numbers[end-1])
    else:
        print(numbers[end-1] - numbers[start-2])
