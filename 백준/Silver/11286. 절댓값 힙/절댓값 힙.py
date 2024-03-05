# BOJ - 11286 절댓값 힙
import sys
import heapq
input = sys.stdin.readline

N = int(input())  # 연산의 개수
numbers = []

for _ in range(N):
    x = int(input())
    if x == 0:
        if numbers:
            print(heapq.heappop(numbers)[1])
        else:
            print(0)
    else:
        heapq.heappush(numbers, (abs(x), x))
