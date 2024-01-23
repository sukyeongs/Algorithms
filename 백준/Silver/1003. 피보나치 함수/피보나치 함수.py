# BOJ - 1003 피보나치 함수
import sys
sys_input = sys.stdin.readline

T = int(sys_input())    # 테스트케이스 개수

for _ in range(T):
    N = int(sys_input())    # N (40 이하의 자연수 or 0)
    dp = [[0, 0] for _ in range(N + 1)]

    for i in range(N+1):
        if i == 0:
            dp[i] = [1, 0]
        elif i == 1:
            dp[i] = [0, 1]
        else:
            dp[i] = [dp[i-1][0]+dp[i-2][0], dp[i-1][1]+dp[i-2][1]]

    print(*dp[N])

