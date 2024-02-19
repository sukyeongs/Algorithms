# BOJ - 1620 나는야 포켓몬 마스터 이다솜
import sys
input = sys.stdin.readline

N, M = map(int, input().split())  # N: 수록된 포켓몬 개수, M: 맞춰야 하는 문제 개수

pocketmon_dict = dict()

for i in range(N):
    pocketmon = input().rstrip()
    pocketmon_dict[i+1] = pocketmon
    pocketmon_dict[pocketmon] = i+1

for _ in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(pocketmon_dict[int(question)])
    else:
        print(pocketmon_dict[question])
