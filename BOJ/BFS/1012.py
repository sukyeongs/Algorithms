# 1012 - 유기농 배추

import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline

T = int(input().rstrip())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def BFS(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0

    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue

            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0


for t in range(T):
    M, N, K = map(int, input().split())
    matrix = [[0] * N for _ in range(M)]
    cnt = 0

    for i in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for m in range(M):
        for n in range(N):
            if matrix[m][n] == 1:
                BFS(m, n)
                cnt += 1

    print(cnt)
