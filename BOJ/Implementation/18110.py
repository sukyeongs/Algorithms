# 18110 - solved.ac

import sys
input = sys.stdin.readline

n = int(input())
opinion = []

def new_round(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if n == 0:
    print(0)

else:
    score = [int(input()) for _ in range(n)]
    exc = new_round(n * 0.15)
    new_score = sorted(score)[exc:n-exc]
    avg = new_round(sum(new_score)/len(new_score))
    print(avg)