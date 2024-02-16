# BOJ - 11279 최대 힙
import sys
import heapq

input = sys.stdin.readline

N = int(input())  # 연산의 개수 (1 이상 100,000 이하)
numbers = []

for _ in range(N):
    x = int(input())
    # 배열이 비어있는데 큰 값을 출력하라고 한 경우
    if x == 0 and not numbers:
        print(0)
        continue
    # 가장 큰 값 출력 후 제거
    elif x == 0:
        print(-heapq.heappop(numbers))
        continue
    # 배열에 x 추가
    else:
        heapq.heappush(numbers, -x)
        continue
