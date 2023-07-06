# 1012 - 유기농 배추

import sys
sys.setrecursionlimit(10000)  # 재귀함수 한도 제한 해제
input = sys.stdin.readline

T = int(input().rstrip())  # 테스트케이스 개수

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def BFS(x, y):
    queue = [(x, y)]
    matrix[x][y] = 0

    while queue:
        x, y = queue.pop()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny > N or ny < 0:
                continue

            if matrix[nx][ny] == 1:
                queue.append((nx, ny))
                matrix[nx][ny] = 0

for i in range(T):
    M, N, K = list(map(int, input().split()))  # 가로, 세로, 배추 개수
    matrix = [[0] * N for _ in range(M)]
    cnt = 0

    for j in range(K):
        x, y = map(int, input().split())
        matrix[x][y] = 1

    for a in range(M):
        for b in range(N):
            if matrix[a][b] == 1:
                BFS(a, b)
                cnt += 1
    print(cnt)