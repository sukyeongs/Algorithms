# BOJ - 11399 ATM
import sys
sys_input = sys.stdin.readline

N = int(sys_input())
time = list(map(int, sys_input().split()))
time.sort()

for i in range(1, N):
    time[i] += time[i-1]

print(sum(time))
