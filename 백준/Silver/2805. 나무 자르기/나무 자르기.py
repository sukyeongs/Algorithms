# BOJ - 2805 나무 자르기

import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 나무의 수, M: 가져가려고 하는 나무의 길이
heights = list(map(int, input().split()))

start = 0
end = sum(heights)
result = 0

while start <= end:
    cutting_tree = 0
    mid = (start + end) // 2

    for height in heights:
        if height > mid:
            cutting_tree += (height - mid)

    if cutting_tree >= M:
        result = mid
        start = mid + 1

    else:
        end = mid - 1

print(result)
