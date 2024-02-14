# BOJ - 1764 듣보잡
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 듣도 못한 사람, M: 보도 못한 사람

unheard_list = set(input().rstrip() for _ in range(N))
unseen_list = set(input().rstrip() for _ in range(M))

result = unheard_list.intersection(unseen_list)

print(len(result))
for name in sorted(result):
    print(name)
