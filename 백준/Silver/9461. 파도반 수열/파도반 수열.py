# BOJ - 9461 파도반 수열

import sys

input = sys.stdin.readline

T = int(input())  # 테스트 케이스 개수

dp = [0] * 101

for _ in range(T):
    N = int(input())  # P(N)

    if N == 1 or N == 2 or N == 3:
        print(1)
        continue

    elif N == 4 or N == 5:
        print(2)
        continue

    else:
        dp[1] = 1
        dp[2] = 1
        dp[3] = 1
        dp[4] = 2
        dp[5] = 2

        for i in range(6, N+1):
            dp[i] = dp[i-1] + dp[i-5]

        print(dp[N])
        