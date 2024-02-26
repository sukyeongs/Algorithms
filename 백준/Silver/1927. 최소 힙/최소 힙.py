# BOJ - 1927 최소 힙

import sys
import heapq
input = sys.stdin.readline

N = int(input())  # N : 연산의 개수
numbers = []

for _ in range(N):
    x = int(input())  # 2^31보다 작은 자연수 or 0

    if x == 0 and len(numbers) == 0:
        print(0)
        continue

    elif x == 0:
        print(heapq.heappop(numbers))
        continue

    else:
        heapq.heappush(numbers, x)
