# BOJ - 11403 경로 찾기
import sys
input = sys.stdin.readline

N = int(input())  # 정점의 개수
graph = [list(map(int, input().split())) for _ in range(N)]


for k in range(N):
    for i in range(N):
        for j in range(N):
            if graph[i][k] == 1 and graph[k][j] == 1:
                graph[i][j] = 1

for row in graph:
    print(*row)