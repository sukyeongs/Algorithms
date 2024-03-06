# BOJ - 11723 집합
import sys

input = sys.stdin.readline

M = int(input())  # 연산의 수
S = set()


for _ in range(M):
    cmd = input().split()
    if len(cmd) == 1:
        if cmd[0] == 'all':
            S = {i for i in range(1, 21)}
        elif cmd[0] == 'empty':
            S = set()
    else:
        cmd, element = cmd[0], int(cmd[1])
        if cmd == 'add':
            S.add(element)
        elif cmd == 'remove' and element in S:
            S.remove(element)
        elif cmd == 'check':
            print(1 if element in S else 0)
        elif cmd == 'toggle':
            if element in S:
                S.remove(element)
            else:
                S.add(element)
