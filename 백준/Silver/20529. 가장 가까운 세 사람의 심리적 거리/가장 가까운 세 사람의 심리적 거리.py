# BOJ - 20529 가장 가까운 세 사람의 심리적 거리
import sys
from itertools import combinations
input = sys.stdin.readline

T = int(input())  # 테스트 케이스 수


def calculate_dist(m1, m2):
    distance = 0
    for i, j in zip(m1, m2):
        if i != j:
            distance += 1
    return distance


for _ in range(T):
    N = int(input())  # 학생 수
    mbti = input().rstrip().split()

    # 비둘기집 원리
    if N > 32:
        print(0)

    else:
        result = 12
        case = combinations(mbti, 3)
        for mbti1, mbti2, mbti3 in case:
            dist = 0
            dist += calculate_dist(mbti1, mbti2)
            dist += calculate_dist(mbti2, mbti3)
            dist += calculate_dist(mbti1, mbti3)

            result = min(dist, result)

        print(result)
